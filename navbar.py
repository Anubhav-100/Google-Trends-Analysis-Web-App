# navbar.py
import textwrap
import streamlit as st

def render_navbar():
    current_page = st.session_state.get("current_page", "Home")
    return textwrap.dedent(f"""
    <header class="header">
        <nav class="navbar" role="navigation" aria-label="Main Navigation">
            <input type="checkbox" id="menu-toggle" style="display: none;">
            <label class="hamburger" for="menu-toggle" role="button" aria-label="Toggle navigation menu" title="Toggle Menu">
                <span></span>
                <span></span>
                <span></span>
            </label>
            <ul class="navbar-list">
                <li>
                    <a class="nav-button {'active' if current_page == 'Home' else ''}" href="?page=Home" target="_self" title="Go to Home Page" aria-label="Go to Home Page">Home</a>
                </li>
                <li>
                    <a class="nav-button {'active' if current_page == 'About' else ''}" href="?page=About" target="_self" title="Learn more About Us" aria-label="Learn more About Us">About</a>
                </li>
                <li>
                    <a class="nav-button {'active' if current_page == 'Contact' else ''}" href="?page=Contact" target="_self" title="Contact us" aria-label="Contact us">Contact</a>
                </li>
            </ul>
        </nav>
    </header>
    """)