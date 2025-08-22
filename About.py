import streamlit as st
import os

def show():
    def load_css(css_files):
        for css_file in css_files:
            path = os.path.join(os.path.dirname(__file__), css_file)
            if os.path.exists(path):
                with open(path, encoding='utf-8') as f:
                    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

    load_css(["about_lay.css", "about.css"])

    st.markdown("""
    <div class="about-header">
        <h1>About Google Trends Analysis Web App</h1>
    </div>
    """, unsafe_allow_html=True)

    # Layout with two columns
    col1, col2 = st.columns([1, 1])

    with col1:
        st.markdown("""
        <div class="about-card">
            <h3> Project Overview</h3>
            <p>
            This project is a web application that visualizes data from Google Trends.
            The main objective is to analyze the popularity of keywords over time and across different geographic regions, providing clean UI, interactive insights.  
            </p>
        </div>

        <div class="about-card">
            <h3> Key Features</h3>
            <ul>
                <li><b>Keyword Analysis:</b> One primary keyword with multiple comparison keywords.</li>
                <li><b>Timeframe Selection:</b> Flexible options (last 12 months, last 5 years, or custom ranges).</li>
                <li><b>Geographic Insights:</b> Global or country-level analysis.</li>
                <li><b>Interactive Visualizations:</b> Built with Plotly/Altair, including:
                    <ul>
                        <li>Line charts (keyword popularity over time)</li>
                        <li>Bar charts (top regions by search interest)</li>
                        <li>Donut charts (percentage share of keywords)</li>
                        <li>Scatter plots (keyword comparisons)</li>
                        <li>Choropleth maps (region-wise search interest)</li>
                    </ul>
                </li>
                <li><b>Responsive Design:</b> Custom CSS for a modern, user-friendly interface.</li>
                <li><b>Automated Pipeline:</b> Pytrends → cleaned <code>time_data.csv</code> & <code>region_data.csv</code>.</li>
                <li><b>Dynamic Dashboard:</b> Built on Streamlit with custom responsive styling.</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="about-card">
            <h3>Tech Stack</h3>
            <ul>
                <li><b>Python –</b> Core development</li>
                <li><b>Pytrends API –</b> Google Trends data extraction</li>
                <li><b>Pandas –</b> Data processing & transformation</li>
                <li><b>Plotly/Matplotlib –</b> Interactive charting</li>
                <li><b>Streamlit –</b> Web app and dashboard</li>
                <li><b>Custom CSS –</b> UI/UX design and responsiveness</li>
            </ul>
        </div>

        <div class="about-card">
            <h3> Learning Outcomes</h3>
            <ul>
                <li>API integration and robust error handling.</li>
                <li>End-to-end data pipeline (fetch → clean → visualize).</li>
                <li>Interactive dashboards with user-driven inputs.</li>
                <li>Responsive UI/UX with modern CSS in Streamlit.</li>
            </ul>
        </div>

        <div class="about-card">
            <h3> Impact</h3>
            <p>
            This project demonstrates the ability to <b>transform real-world data into actionable insights.</b> 
            It can be applied in areas such as <b>market research, digital marketing, and audience analysis,</b>
            helping identify search trends and regional interests for better decision-making.
            </p>
        </div>
        """, unsafe_allow_html=True)