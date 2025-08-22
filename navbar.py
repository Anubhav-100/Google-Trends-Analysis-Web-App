import textwrap

def render_navbar():
    return textwrap.dedent("""
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
                    <form action="" method="get">
                        <input type="hidden" name="page" value="Home">
                        <input class="nav-button" type="submit" value="Home" title="Go to Home Page" aria-label="Go to Home Page">
                    </form>
                </li>
                <li>
                    <form action="" method="get">
                        <input type="hidden" name="page" value="About">
                        <input class="nav-button" type="submit" value="About" title="Learn more About Us" aria-label="Learn more About Us">
                    </form>
                </li>
                <li>
                    <form action="" method="get">
                        <input type="hidden" name="page" value="Contact">
                        <input class="nav-button" type="submit" value="Contact" title="Contact us" aria-label="Contact us">
                    </form>
                </li>
            </ul>
        </nav>
    </header>
    """)
