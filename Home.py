import streamlit as st
import os
import subprocess
from fetchdata import fetch_data
from streamlit_javascript import st_javascript

def show():

    def load_css(css_files):
        for css_file in css_files:
            path = os.path.join(os.path.dirname(__file__), css_file)
            if os.path.exists(path):
                with open(path, encoding='utf-8') as f:
                    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
            else:
                st.warning(f"⚠️ File not found: {path}")

    load_css(["home.css", "home_layout.css"])


    st.markdown('<h1>Google Trends Analysis</h1>', unsafe_allow_html=True)

    # Inputs
    primary = st.text_input("Primary Keyword", placeholder="Enter main keyword....")
    comp_raw = st.text_input("Comparison Keywords", placeholder="Enter comparison keywords (comma-separated)...")
    timeframe = st.text_input("Timeframe", value="today 12-m")

    country_map = {
        "Global": "",
        "India 🇮🇳": "IN", "USA 🇺🇸": "US", "United Kingdom 🇬🇧": "GB",
        "Canada 🇨🇦": "CA", "Australia 🇦🇺": "AU", "Germany 🇩🇪": "DE",
        "France 🇫🇷": "FR", "Italy 🇮🇹": "IT", "Spain 🇪🇸": "ES",
        "Brazil 🇧🇷": "BR", "Mexico 🇲🇽": "MX", "Russia 🇷🇺": "RU",
        "Japan 🇯🇵": "JP", "South Korea 🇰🇷": "KR", "China 🇨🇳": "CN",
        "South Africa 🇿🇦": "ZA", "Saudi Arabia 🇸🇦": "SA", "United Arab Emirates 🇦🇪": "AE",
        "Bangladesh 🇧🇩": "BD", "Pakistan 🇵🇰": "PK", "Nepal 🇳🇵": "NP",
        "Indonesia 🇮🇩": "ID", "Thailand 🇹🇭": "TH", "Malaysia 🇲🇾": "MY",
        "Philippines 🇵🇭": "PH", "Vietnam 🇻🇳": "VN", "Singapore 🇸🇬": "SG",
        "Argentina 🇦🇷": "AR", "Netherlands 🇳🇱": "NL", "Sweden 🇸🇪": "SE",
        "Switzerland 🇨🇭": "CH", "Turkey 🇹🇷": "TR"
    }

    country_label = st.selectbox("Select Country", options=list(country_map.keys()))
    geo = country_map[country_label]

    comparison_keywords = [k.strip() for k in comp_raw.split(',') if k.strip()]

    if st.button("Submit"):
        if primary and comparison_keywords and timeframe:
            all_keywords = [primary] + comparison_keywords
            all_keywords = [col.lower() for col in all_keywords]

            st.session_state["keywords"] = all_keywords
            st.session_state["primary"] = primary.lower()
            st.session_state["timeframe"] = timeframe
            st.session_state["geo"] = geo
            
            try:
                st.info("⚙️ Fetching Google Trends data...")
                time_data, region_data = fetch_data()
                st.session_state["region_data"] = region_data
                st.session_state["time_data"] = time_data
                st.success("✅ Data fetched and saved successfully!")
                
            except subprocess.CalledProcessError as e:
                st.error("❌ Failed to fetch data. Please check your setup.")
                st.code(e.stderr)

            with st.spinner("Redirecting to Dashboard..."):
                st.query_params.update({"page": "Dashboard"})
                st.rerun()

        else:
            st.warning("⚠️ Please fill all the fields.")
            
    # JavaScript to get screen width      
    if "screen_width" not in st.session_state:
        st.session_state["screen_width"] = None

    js_width = st_javascript("window.innerWidth")
    if js_width is not None:
        st.session_state["screen_width"] = int(js_width)
        