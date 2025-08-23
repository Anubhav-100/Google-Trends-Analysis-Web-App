import streamlit as st
import Home, Dashboard, Contact, About
from navbar import render_navbar
import os

st.set_page_config(page_title="GoogleTrendApp", layout="wide")

def load_css(css_files):
    for css_file in css_files:
        path = os.path.join(os.path.dirname(__file__), css_file)
        if os.path.exists(path):
            with open(path, encoding='utf-8') as f:
                st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
        else:
            st.warning(f"⚠️ File not found: {path}")

load_css(["navbar.css"])

# Render HTML Navbar (header)
navbar_html = render_navbar()
if not navbar_html:
    navbar_html = "<nav><!-- Default navbar --></nav>"
st.markdown(navbar_html, unsafe_allow_html=True)         

# Agar pehle se session_state me page nahi hai → default Home
if "current_page" not in st.session_state:
    st.session_state.current_page = "Home"

# Agar query param aya hai to session_state update karo
raw_page = st.query_params.get("page", st.session_state.current_page)
page = raw_page[0] if isinstance(raw_page, list) else raw_page
page = page.capitalize()

# Update session_state with current page
st.session_state.current_page = page

if page == "Home":
    Home.show()
elif page == "Dashboard":
    Dashboard.show()
elif page == "Contact":
    Contact.show()
elif page == "About":
    About.show()
else:
    st.error("❌ Page not found.")
