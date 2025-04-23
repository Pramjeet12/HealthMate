import streamlit as st

# App title with an improved UI
st.set_page_config(page_title="Compare Hospitals in India", page_icon="🏥", layout="wide")
st.title("Hospitals in Your City🏥")

# Database of hospitals with their websites categorized by type
HOSPITALS_DB = {
    "Delhi": {
        "Government": [
            ("AIIMS", "https://www.aiims.edu"),
            ("Safdarjung Hospital", "https://www.vmmc-sjh.nic.in"),
            ("Lok Nayak Hospital", "http://www.lnh.delhigovt.nic.in"),
            ("GTB Hospital", "http://www.gtbh.delhigovt.nic.in")
        ],
        "Private": [
            ("Medanta Hospital", "https://www.medanta.org"),
            ("Fortis Escorts Hospital", "https://www.fortisescorts.in"),
            ("Max Healthcare", "https://www.maxhealthcare.in"),
            ("BLK-Max Super Specialty Hospital", "https://www.blkhospital.com")
        ]
    },
    "Mumbai": {
        "Government": [
            ("KEM Hospital", "https://www.kem.edu"),
            ("Sion Hospital", "http://www.ltmgh.com"),
            ("JJ Hospital", "https://www.jjhospital.org")
        ],
        "Private": [
            ("Bombay Hospital", "https://www.bombayhospital.com"),
            ("Lilavati Hospital", "https://www.lilavatihospital.com"),
            ("Nanavati Hospital", "https://www.nanavatihospital.org"),
            ("Hiranandani Hospital", "https://www.hiranandanihospital.org")
        ]
    },
    "Bangalore": {
        "Government": [
            ("NIMHANS", "https://www.nimhans.ac.in"),
            ("Victoria Hospital", "http://www.victoriahospital.org"),
            ("Bowring & Lady Curzon Hospital", "http://www.bowringhosp.org")
        ],
        "Private": [
            ("Apollo Hospital", "https://www.apollohospitals.com"),
            ("Manipal Hospital", "https://www.manipalhospitals.com"),
            ("Fortis Hospital", "https://www.fortishealthcare.com")
        ]
    },
    "Patna": {
        "Government": [
            ("PMCH", "http://www.pmch.in"),
            ("IGIMS", "http://www.igims.org"),
            ("NMCH", "http://www.nmch.org")
        ],
        "Private": [
            ("Paras HMRI Hospital", "https://www.parashospitals.com"),
            ("Ruban Memorial Hospital", "https://www.rubanpatna.com"),
            ("Ford Hospital", "https://www.fordhospital.org")
        ]
    },
    "Kolkata": {
        "Government": [
            ("SSKM Hospital", "http://www.sskm.org"),
            ("NRS Medical College", "http://www.nrsmc.edu.in"),
            ("RG Kar Medical College", "https://www.rgkarmch.org")
        ],
        "Private": [
            ("Tata Medical Center", "https://tmckolkata.com"),
            ("AMRI Hospital", "https://www.amrihospitals.in"),
            ("Apollo Gleneagles Hosp.", "https://www.apollohospitals.com")
        ]
    },
    "Hyderabad": {
        "Government": [
            ("Osmania General Hospital", "https://www.oghhyd.org"),
            ("Gandhi Hospital", "http://www.gandhihospital.org")
        ],
        "Private": [
            ("Apollo Hospital", "https://www.apollohospitals.com"),
            ("Yashoda Hospital", "https://www.yashodahospitals.com"),
            ("KIMS Hospitals", "https://www.kimshospitals.com")
        ]
    },
    "Chennai": {
        "Government": [
            ("Rajiv Gandhi Govt. General Hospital", "https://www.rgggh.org"),
            ("Stanley Medical College Hospital", "https://www.stanleyhosp.org")
        ],
        "Private": [
            ("Apollo Hospital", "https://www.apollohospitals.com"),
            ("Fortis Malar Hospital", "https://www.fortishealthcare.com"),
            ("MIOT International", "https://www.miotinternational.com")
        ]
    }
}

# User selection
st.subheader("Select Your City📍")
city = st.selectbox("Select City:", ["Select a City"] + list(HOSPITALS_DB.keys()))

st.subheader("Select Hospital Type🏥")
hospital_type = st.selectbox("Select Type:", ["Select a Type"] + ["Government", "Private"])

# Button to display results
if st.button("Hospitals🔍"):
    if city != "Select a City" and hospital_type != "Select a Type":
        st.subheader(f"🏥 {hospital_type} Hospitals in {city}")
        if hospital_type in HOSPITALS_DB[city]:
            for hospital, website in HOSPITALS_DB[city][hospital_type]:
                st.markdown(f"### **{hospital}**")
                st.markdown(f"🌐 [Visit Website]({website})")
                st.markdown("---")
        else:
            st.warning("No hospitals found for the selected category in this city.")
    else:
        st.warning("Please select a city and hospital type to view hospitals.")

# Footer
st.markdown(
    "⚠️ **Disclaimer:** This app provides information on hospitals but does not endorse any particular hospital. Please visit the websites for more details.")
