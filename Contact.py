import streamlit as st
import os

def show():
    # Include Font Awesome CDN for social icons that overerrides italics default CSSS
    st.markdown("""
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css" integrity="sha512-DTOQO9RWCH3ppGqcWaEA1BIZOC6xxalwEsw9c2QQeAIftl+Vegovlnee1c9QX4TctnWMn13TZye+giMm8e2LwA==" crossorigin="anonymous" referrerpolicy="no-referrer" />
    """, unsafe_allow_html=True)

    st.markdown('''
        <h1 style="text-align:center; color:black; padding-top: clamp(2.5rem, 3vw, 6rem); margin-bottom: 0.5rem;
               padding-bottom: 0rem; padding-left: 2rem; 
               font-size: clamp(2rem, 3vw, 4rem); font-family: 'Segoe UI', sans-serif;">
        <b>Connect With Me</b>
        </h1>
        <p style="text-align:center; color:black; font-size: clamp(0.8rem, 2vw, 1.5rem); margin-bottom: 0rem;
            line-height: 1.4;">
            <b><i>Have a project in mind or just want to say hello? Let’s create something amazing together</i></b>
        </p>
    ''', unsafe_allow_html=True)

    def load_css(css_files):
        for css_file in css_files:
            path = os.path.join(os.path.dirname(__file__), css_file)
            if os.path.exists(path):
                with open(path, encoding='utf-8') as f:
                    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

    load_css(["cont_lay.css", "contact.css"])

    contact_html = """
    <div class="contact-section">
        <div class="profile-row">
            <div class="profile-left">
                <img src="https://i.postimg.cc/vmn34Vy9/mee-1.jpg" alt="Anubhav Photo" class="profile-img">
            </div>
            <div class="profile-details">
                <h2>Anubhav Kumar Kesharwani</h2>
                <p class="role"><b><i>Data Analyst | UI/UX Integrator</i></b></p>
                <p>
                    “This Google Trends Analysis webApp is a project I built to visualize keyword popularity over time and across regions. 
                    I worked on data fetching using Pytrends, automated CSV pipelines, and interactive visualizations with Streamlit and Plotly. 
                    Feel free to connect if you’d like to explore or collaborate!”
                </p>
            </div>
        </div>
        <div class="contact-info">
            <p> <a href="tel:+916387399625" style="text-decoration: none; color: inherit;">
                <i class="fas fa-phone fa-lg" style="color: #333333; margin-right: 8px;"></i><u>+91-6387399625</u></p>
            <p> <i class="fas fa-envelope fa-lg" style="color: #EA4335; margin-right: 8px;"></i>
                <a href="mailto:anubhavkesharwani38@gmail.com">anubhavkesharwani38@gmail.com</a></p>
            <p>
                <a href="https://www.linkedin.com/in/anubhav-kesharwani-1a1267312" target="_blank"><i class="fab fa-linkedin fa-lg" style="color: #0A66C2; margin-right: 8px;"></i>LinkedIn</a> | 
                <a href="https://github.com/Anubhav-100" target="_blank"><i class="fab fa-github fa-lg" style="color: #181717; margin-right: 8px;"></i>GitHub</a> | 
                <a href="https://www.instagram.com/anubhav_k_47" target="_blank"><i class="fab fa-instagram fa-lg" style="color: #C13584; margin-right: 8px;"></i>Instagram</a>
            </p>
        </div>
    </div>
    """

    # Render directly without iframe
    st.markdown(contact_html, unsafe_allow_html=True)