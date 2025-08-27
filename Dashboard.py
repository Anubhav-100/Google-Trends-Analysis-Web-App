import streamlit as st
import os
from charts import *

def show():

    def load_css(css_files):
        for css_file in css_files:
            path = os.path.join(os.path.dirname(__file__), css_file)
            if os.path.exists(path):
                with open(path, encoding='utf-8') as f:
                    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

    load_css(["dashboard.css", "dash_layout.css"])

    # --- Load data from session_state ---
    try:
        time_data = st.session_state["time_data"]
        region_data = st.session_state["region_data"]
        keywords = st.session_state["keywords"]
        geo = st.session_state["geo"]
    except KeyError:
        st.error("❌ Data not found. Please submit from Home page.")
        return
    
    if st.session_state['screen_width'] < 680:
        with st.container():
            st.markdown('<div class="btn-grid-sentinel" aria-hidden="true"></div>', unsafe_allow_html=True)
            st.markdown("<h1>Google Trends Analysis Dashboard</h1>", unsafe_allow_html=True)

            # Buttons arranged in 2 rows × 3 cols
            button_keys = ["bar", "line", "donut", "map", "scatter", "compare"]
            button_labels = ["Bar Chart", "Line Chart", "Donut", "Map Chart", "Scatter", "Compare"]

            for i in range(0, len(button_keys), 3):
                col1, col2, col3 = st.columns(3, gap="small", vertical_alignment="top")

                with col1:
                    if st.button(button_labels[i], key=button_keys[i]):
                        st.session_state["selected_chart"] = button_keys[i]
                
                if i + 1 < len(button_keys):
                    with col2:
                        if st.button(button_labels[i+1], key=button_keys[i+1]):
                            st.session_state["selected_chart"] = button_keys[i+1]
                
                if i + 2 < len(button_keys):
                    with col3:
                        if st.button(button_labels[i+2], key=button_keys[i+2]):
                            st.session_state["selected_chart"] = button_keys[i+2]

            selected_keyword = st.selectbox("Keywords", options=[col.upper() for col in keywords], key="keyword_select_mobile")
            selected_keyword = selected_keyword.lower()

    else:
        with st.container():
            header_col, buttons_col, keyword_col = st.columns([2.38, 3, 0.62])
            with header_col:
                st.markdown("<h1>Google Trends Analysis Dashboard</h1>", unsafe_allow_html=True)
            with buttons_col:
                cols = st.columns(6, gap="small")
                button_keys = ["bar", "line", "donut", "map", "scatter", "compare"]
                button_labels = ["Bar Chart", "Line Chart", "Donut Chart", "Map Chart", "Scatter Plot", "Compare"]
                for col, key, label in zip(cols, button_keys, button_labels):
                    with col:
                        if st.button(label, key=key):
                            st.session_state["selected_chart"] = key
            with keyword_col:
                selected_keyword = st.selectbox("Keywords", options=[col.upper() for col in keywords], key="keyword_select_desktop")
                selected_keyword = selected_keyword.lower()

# --- Display selected chart ---
    chart = st.session_state.get("selected_chart", "bar")
    if chart == "bar":
        fig = plot_bar(region_data, selected_keyword)
        st.plotly_chart(fig, use_container_width=True, config={
            "displayModeBar": True,
            "modeBarButtonsToRemove": ["zoom2d", "pan2d", "select2d", "lasso2d", "zoomIn2d", "zoomOut2d", "autoScale2d", "hoverCompareCartesian", "hoverClosestCartesian", "toggleSpikelines"],
            "displaylogo": False
        })
    elif chart == "line":
        fig = plot_line(time_data, selected_keyword)
        st.plotly_chart(fig, use_container_width=True, config={
            "displayModeBar": True,
            "modeBarButtonsToRemove": ["zoom2d", "pan2d", "select2d", "lasso2d", "zoomIn2d", "zoomOut2d", "autoScale2d", "hoverCompareCartesian", "hoverClosestCartesian", "toggleSpikelines"],
            "displayogo": False
        })
    elif chart == "donut":
        fig = plot_donut(time_data, keywords)
        st.plotly_chart(fig, use_container_width=True, config={
            "displayModeBar": True,
            "modeBarButtonsToRemove": ["zoom2d", "pan2d", "select2d", "lasso2d", "zoomIn2d", "zoomOut2d", "autoScale2d", "hoverCompareCartesian", "hoverClosestCartesian", "toggleSpikelines"],
            "showLogo": False
        })
    elif chart == "map":
        fig = plot_map(region_data, selected_keyword, geo)
        st.plotly_chart(fig, use_container_width=True, config={
            "displayModeBar": True,
            "modeBarButtonsToRemove": ["zoom2d", "pan2d", "select2d", "lasso2d", "zoomIn2d", "zoomOut2d", "autoScale2d", "hoverCompareCartesian", "hoverClosestCartesian", "toggleSpikelines"],
            "displaylogo": False
        })
    elif chart == "scatter":
        fig = plot_scatter(region_data, keywords)
        st.plotly_chart(fig, use_container_width=True, config={
            "displayModeBar": True,
            "modeBarButtonsToRemove": ["zoom2d", "pan2d", "select2d", "lasso2d", "zoomIn2d", "zoomOut2d", "autoScale2d", "hoverCompareCartesian", "hoverClosestCartesian", "toggleSpikelines"],
            "displaylogo": False
        })
    elif chart == "compare":
        fig = plot_allline(time_data, keywords)
        st.plotly_chart(fig, use_container_width=True, config={
            "displayModeBar": True,
            "modeBarButtonsToRemove": ["zoom2d", "pan2d", "select2d", "lasso2d", "zoomIn2d", "zoomOut2d", "autoScale2d",  "hoverCompareCartesian", "hoverClosestCartesian", "toggleSpikelines"],
            "displaylogo": False
        })