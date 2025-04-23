import streamlit as st
import urllib.parse

# App title with an improved UI
st.set_page_config(page_title="Find Top Doctors in India", page_icon="🏥", layout="wide")
st.title("Find Top Doctors in Your City👨‍⚕️")

# Database of top doctors
DOCTORS_DB = {
    "Delhi": {
        "Cardiology": [("Dr. Naresh Trehan", "Medanta", "https://www.medanta.org", "+919876543210"),
                       ("Dr. Ashok Seth", "Fortis Escorts", "https://www.fortisescorts.in", "+919812345678")],
        "Dermatology": [("Dr. Rohit Batra", "Sir Ganga Ram Hospital", "https://www.sgrh.com", "+919845678321"),
                        ("Dr. Niti Khunger", "AIIMS", "https://www.aiims.edu", "+919874563210")]
    },
    "Mumbai": {
        "Neurology": [("Dr. Rajas Deshpande", "Ruby Hall", "https://www.rubyhall.com", "+919823456789"),
                      ("Dr. B.S. Singhal", "Bombay Hospital", "https://www.bombayhospital.com", "+919877654321")],
        "Orthopedics": [("Dr. Sanjay Desai", "Lilavati Hospital", "https://www.lilavatihospital.com", "+919898765432"),
                        ("Dr. Harshavardhan Hegde", "Nanavati Hospital", "https://www.nanavatihospital.org",
                         "+919865432178")]
    },
    "Bangalore": {
        "Gastroenterology": [
            ("Dr. Raj Vigna Venugopal", "Apollo Hospital", "https://www.apollohospitals.com", "+919878765432"),
            ("Dr. Dinesh Kini", "Manipal Hospital", "https://www.manipalhospitals.com", "+919864321789")],
        "Pediatrics": [("Dr. Sharat Babu", "Rainbow Hospital", "https://www.rainbowhospitals.in", "+919854678921"),
                       ("Dr. Swathi Reddy", "Cloudnine Hospital", "https://www.cloudninecare.com", "+919899876543")]
    },
    "Patna": {
        "Cardiology": [("Dr. Rajiv Ranjan", "Paras HMRI Hospital", "https://www.parashospitals.com", "+919911223344"),
                       ("Dr. Manish Kumar", "Ruban Memorial Hospital", "https://www.rubanpatna.com", "+919922334455")],
        "General Physician": [
            ("Dr. Alok Kumar", "Paras HMRI Hospital", "https://www.parashospitals.com", "+919934567890"),
            ("Dr. Ramesh Singh", "IGIMS", "https://www.igims.org", "+919812345676")],
        "Orthopedics": [("Dr. Rajeev Ranjan", "Ruban Memorial Hospital", "https://www.rubanpatna.com", "+919876543219"),
                        ("Dr. Vikash Singh", "Ford Hospital", "https://www.fordhospitalpatna.com", "+919854321098")]
    },
    "Kolkata": {
        "Oncology": [("Dr. Sandeep Ghosh", "Tata Medical Center", "https://tmckolkata.com", "+919876543217"),
                     ("Dr. Priyanka Roy", "AMRI Hospitals", "https://www.amrihospitals.in", "+919843217654")],
        "Pulmonology": [("Dr. Arindam Das", "Apollo Gleneagles", "https://www.apollogleneagles.in", "+919899999999"),
                        ("Dr. Soumitra Ghosh", "Fortis Kolkata", "https://www.fortishealthcare.com", "+919888888888")]
    },
    "Hyderabad": {
        "Endocrinology": [
            ("Dr. Srikanth Reddy", "Yashoda Hospital", "https://www.yashodahospitals.com", "+919812345678"),
            ("Dr. Neelima Yadav", "KIMS", "https://www.kimshospitals.com", "+919887654321")],
        "Nephrology": [("Dr. Suresh Kumar", "NIMS", "https://www.nims.edu.in", "+919834567891"),
                       ("Dr. Anand Kumar", "Apollo Hospitals", "https://www.apollohospitals.com", "+919876543210")]
    }
}

# User selections
st.subheader("Select Your City📍")
city = st.selectbox("Select City:", ["Select a City"] + list(DOCTORS_DB.keys()))

st.subheader("Select Medical Condition🔬")
specialty = st.selectbox("Select Medical Condition:",
                         ["Select a Condition"] + sorted(set(spec for city in DOCTORS_DB.values() for spec in city)))

# Button to display results
if st.button("Find Doctors🔍"):
    if city != "Select a City" and specialty != "Select a Condition":
        if specialty in DOCTORS_DB.get(city, {}):
            st.subheader(f"👨‍⚕️ Top {specialty} Doctors in {city}")
            for doctor in DOCTORS_DB[city][specialty]:
                name, hospital, website, phone = doctor
                st.markdown(f"### **{name}**")
                st.write(f"🏥 {hospital}")
                st.markdown(f"🌐 [Visit Website]({website})")

                # WhatsApp Booking Link
                msg = f"Hello {name}, I would like to book an appointment for {specialty} consultation."
                encoded_msg = urllib.parse.quote(msg)
                whatsapp_url = f"https://api.whatsapp.com/send?phone={phone}&text={encoded_msg}"
                st.markdown(f"[📩 Book Appointment on WhatsApp]({whatsapp_url})")
                st.markdown("---")
        else:
            st.warning("No doctors available for the selected specialty in this city.")

# Footer
st.markdown(
    "⚠️ **Disclaimer:** This app provides information on top doctors but is not a replacement for professional medical advice. Always consult a doctor directly.")