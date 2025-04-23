import streamlit as st

# Page configuration
st.set_page_config(page_title="Govt Health Schemes - India & Northeast", layout="centered")

# Title and subtitle
st.title("Government Health Scheme Assistant🏡")
st.markdown("Explore major **Central** and **Northeast** health schemes offering medical and financial aid.")

st.markdown("---")

# ========== Northeast Schemes ==========
st.subheader("Northeast States Government Schemes🌄")

ner_schemes = {
    "Assam - Atal Amrit Abhiyan": {
        "description": "Free treatment up to ₹2 lakh for BPL and low-income families for major diseases.",
        "link": "https://atalamritabhiyan.assam.gov.in/"
    },
    "Meghalaya - MHIS": {
        "description": "Provides ₹5 lakh insurance to all residents of Meghalaya under Megha Health Insurance Scheme.",
        "link": "https://mhis.org.in/"
    },
    "Manipur - CMHT": {
        "description": "Free cashless treatment for economically vulnerable people under Chief Minister-gi Hakshelgi Tengbang.",
        "link": "https://cmhtmanipur.gov.in/"
    },
    "Mizoram - State Health Scheme": {
        "description": "State-funded healthcare support for tribal population and low-income groups.",
        "link": "https://health.mizoram.gov.in/"
    },
    "Tripura - THAS": {
        "description": "Tripura Health Assurance Scheme for the poor providing free medical care.",
        "link": "https://tripura.gov.in/"
    },
    "Nagaland - CMHIS": {
        "description": "Chief Minister's Health Insurance Scheme offers cashless healthcare up to ₹5 lakh per family per year.",
        "link": "https://cmhis.nagaland.gov.in/"
    },
    "Arunachal Pradesh - CMAAY": {
        "description": "Offers ₹5 lakh coverage under CMAAY, merged with PM-JAY to cover all residents of the state.",
        "link": "https://cmaay.arunachal.gov.in/"
    }
}

for scheme, details in ner_schemes.items():
    with st.expander(f"📗 {scheme}"):
        st.write(details["description"])
        st.markdown(f"[🔗 Visit Official Site]({details['link']})")

st.markdown("---")

# ========== Central Health Schemes ==========
st.subheader("Central Government Schemes🌐")

national_schemes = {
    "Ayushman Bharat (PM-JAY)": {
        "description": "Provides ₹5 lakh coverage per family per year for secondary and tertiary care hospitalization.",
        "link": "https://pmjay.gov.in/"
    },
    "Jan Arogya Yojana": {
        "description": "Covers medical and hospitalization expenses for low-income families in India.",
        "link": "https://mera.pmjay.gov.in/search/login"
    },
    "Rashtriya Swasthya Bima Yojana (RSBY)": {
        "description": "Health insurance scheme for BPL families, now merged into PM-JAY.",
        "link": "https://labour.gov.in/rsby"
    },
    "National Health Mission (NHM)": {
        "description": "A flagship program for universal access to equitable and quality healthcare services.",
        "link": "https://nhm.gov.in/"
    },
    "eSanjeevani Telemedicine": {
        "description": "Free doctor consultations via video calls through the national telemedicine portal.",
        "link": "https://esanjeevani.mohfw.gov.in/"
    },
    "Central Government Health Scheme (CGHS)": {
        "description": "Provides comprehensive medical care to central government employees and pensioners.",
        "link": "https://cghs.nic.in/"
    },
    "Employees' State Insurance (ESI) Scheme": {
        "description": "Health insurance for workers in the organized sector covering medical care, sickness, maternity and disability benefits.",
        "link": "https://www.esic.nic.in/"
    },
    "Ayushman Bharat Digital Mission (ABDM)": {
        "description": "Empowers citizens with a Digital Health ID and secure access to health records online.",
        "link": "https://abdm.gov.in/"
    }
}

for scheme, details in national_schemes.items():
    with st.expander(f"📘 {scheme}"):
        st.write(details["description"])
        st.markdown(f"[🔗 Visit Official Site]({details['link']})")

# ========== Eligibility Checker ==========
st.subheader("Check Your Eligibility✅")

st.markdown("Fill in your details to get suggestions:")

with st.form("eligibility_form"):
    age = st.number_input("Age", 1, 150)
    income = st.number_input("Annual Household Income (₹)", step=1000, min_value=0)
    is_rural = st.selectbox("Do you live in a rural area?", ["Yes", "No"])
    sc_st = st.selectbox("Do you belong to SC/ST category?", ["Yes", "No"])
    occupation = st.selectbox("Occupation", ["Unemployed", "Farmer", "Laborer", "Housewife", "Govt Employee", "Other"])
    region = st.selectbox("Which region do you belong to?", ["Northeast State", "Other"])
    state = st.selectbox("Select your state (for Northeast only)", ["None", "Assam", "Manipur", "Meghalaya", "Arunachal Pradesh", "Mizoram", "Tripura", "Nagaland", "Sikkim"])
    submitted = st.form_submit_button("Check Eligibility🔍")

# ---------------- Results Section ---------------- #
# ---------------- Results Section ---------------- #
if submitted:
    st.markdown("### 🎯 Suggested Schemes Based on Your Inputs")

    eligible_schemes = []

    # Add PM-JAY for low income or SC/ST
    if income <= 200000 or sc_st == "Yes":
        eligible_schemes.append("Ayushman Bharat (PM-JAY)")

    if region == "Northeast State":
        if state == "Manipur":
            eligible_schemes.append("Manipur - CMHT")
        elif state == "Meghalaya":
            eligible_schemes.append("Meghalaya - MHIS")
        elif state == "Arunachal Pradesh":
            eligible_schemes.append("Arunachal Pradesh - CMAAY")
        elif state == "Assam":
            eligible_schemes.append("Assam - Atal Amrit Abhiyan")
        elif state == "Mizoram":
            eligible_schemes.append("Mizoram - State Health Scheme")
        elif state == "Tripura":
            eligible_schemes.append("Tripura - THAS")
        elif state == "Nagaland":
            eligible_schemes.append("Nagaland - CMHIS")

    if eligible_schemes:
        st.success("✅ Based on your inputs, you may be eligible for:")
        for scheme in eligible_schemes:
            if scheme in ner_schemes:
                st.markdown(f"- [{scheme}]({ner_schemes[scheme]['link']})")
            elif scheme in national_schemes:
                st.markdown(f"- [{scheme}]({national_schemes[scheme]['link']})")
            else:
                st.markdown(f"- {scheme} (🔗 link not found)")
    else:
        st.warning("⚠ Based on your details, no direct eligibility matched. You may still explore:")
        st.markdown("[Browse PM-JAY State Info](https://pmjay.gov.in/state-wise-implementation)")

st.markdown("---")
st.caption("⚠️This tool provides an approximate suggestion. Please verify on official health portals for accuracy.")
