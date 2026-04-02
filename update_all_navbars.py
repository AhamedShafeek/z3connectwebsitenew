import os
import re

html_files = [f for f in os.listdir('.') if f.endswith('.html')]

# The target Navbar HTML to inject (simplified for regex or block replacement)
# We want to replace the entire <nav class="floating-nav" ...> ... </nav> block
# and also the <div class="mobile-menu" ...> ... </div> block.

navbar_template = """  <nav class="floating-nav" id="floating-nav" aria-label="Main navigation">
    <a href="index.html" class="nav-logo">
      <img loading="lazy" decoding="async" src="logo0.png" alt="Z3Connect" class="nav-logo-img">
      <span>Z3Connect</span>
    </a>

    <div class="nav-links">
      <!-- Company Dropdown -->
      <div class="nav-item" data-dropdown="company">
        <button class="nav-link nav-dropdown-trigger" aria-expanded="false" aria-haspopup="true">
          Company
          <svg class="nav-chevron" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"
            stroke-linecap="round">
            <path d="M6 9l6 6 6-6" />
          </svg>
        </button>
        <div class="nav-dropdown" role="menu">
          <a href="about.html" class="nav-dropdown-link" role="menuitem">
            <span class="nav-dropdown-icon">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round">
                <path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2" />
                <circle cx="9" cy="7" r="4" />
                <path d="M23 21v-2a4 4 0 0 0-3-3.87" />
                <path d="M16 3.13a4 4 0 0 1 0 7.75" />
              </svg>
            </span>
            <span>
              <strong>About us</strong>
              <small>Who we are and what drives us</small>
            </span>
          </a>
          <a href="founder.html" class="nav-dropdown-link" role="menuitem">
            <span class="nav-dropdown-icon">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round">
                <path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2" />
                <circle cx="12" cy="7" r="4" />
              </svg>
            </span>
            <span>
              <strong>Founder</strong>
              <small>The mind behind Z3Connect</small>
            </span>
          </a>
          <a href="philosophy.html" class="nav-dropdown-link" role="menuitem">
            <span class="nav-dropdown-icon">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round">
                <path
                  d="M9.663 17h4.673M12 3v1m6.364 1.636l-.707.707M21 12h-1M4 12H3m3.343-5.657l-.707-.707m2.828 9.9a5 5 0 117.072 0l-.548.547A3.374 3.374 0 0014 18.469V19a2 2 0 11-4 0v-.531c0-.895-.356-1.754-.988-2.386l-.548-.547z" />
              </svg>
            </span>
            <span>
              <strong>Philosophy</strong>
              <small>How we think and build</small>
            </span>
          </a>
          <a href="team.html" class="nav-dropdown-link" role="menuitem">
            <span class="nav-dropdown-icon">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round">
                <path
                  d="M12 4.354a4 4 0 110 5.292M15 21H3v-1a6 6 0 0112 0v1zm0 0h6v-1a6 6 0 00-9-5.197M13 7a4 4 0 11-8 0 4 4 0 018 0z" />
              </svg>
            </span>
            <span>
              <strong>Team</strong>
              <small>Meet the people building the future</small>
            </span>
          </a>
          <a href="why-we-exist.html" class="nav-dropdown-link" role="menuitem">
            <span class="nav-dropdown-icon">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round">
                <path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z" />
              </svg>
            </span>
            <span>
              <strong>Why we exist</strong>
              <small>Our purpose and mission</small>
            </span>
          </a>
        </div>
      </div>

      <!-- Products Dropdown -->
      <div class="nav-item" data-dropdown="products">
        <button class="nav-link nav-dropdown-trigger" aria-expanded="false" aria-haspopup="true">
          Products
          <svg class="nav-chevron" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"
            stroke-linecap="round">
            <path d="M6 9l6 6 6-6" />
          </svg>
        </button>
        <div class="nav-dropdown" role="menu">
          <a href="products.html" class="nav-dropdown-link" role="menuitem">
            <span class="nav-dropdown-icon">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round">
                <path d="M20 7l-8-4-8 4m16 0l-8 4m8-4v10l-8 4M4 7l8 4M4 7v10l8 4m0-10v10" />
              </svg>
            </span>
            <span>
              <strong>All products</strong>
              <small>Our complete product suite</small>
            </span>
          </a>
          <a href="solutions-detailed.html" class="nav-dropdown-link" role="menuitem">
            <span class="nav-dropdown-icon">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round">
                <path d="M10 20l4-16m4 4l4 4-4 4M6 16l-4-4 4-4" />
              </svg>
            </span>
            <span>
              <strong>Solutions</strong>
              <small>Industry-specific software</small>
            </span>
          </a>
        </div>
      </div>

      <!-- Work Dropdown -->
      <div class="nav-item" data-dropdown="work">
        <button class="nav-link nav-dropdown-trigger" aria-expanded="false" aria-haspopup="true">
          Work
          <svg class="nav-chevron" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"
            stroke-linecap="round">
            <path d="M6 9l6 6 6-6" />
          </svg>
        </button>
        <div class="nav-dropdown" role="menu">
          <a href="work.html" class="nav-dropdown-link" role="menuitem">
            <span class="nav-dropdown-icon">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round">
                <path d="M12 2v2M12 20v2M4.93 4.93l1.41 1.41M17.66 17.66l1.41 1.41M2 12h2M20 12h2M6.34 17.66l-1.41 1.41M19.07 4.93l-1.41 1.41" />
              </svg>
            </span>
            <span>
              <strong>Our Work</strong>
              <small>Explore our portfolio</small>
            </span>
          </a>
          <a href="case-studies.html" class="nav-dropdown-link" role="menuitem">
            <span class="nav-dropdown-icon">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round">
                <path d="M9 17v-2m3 2v-4m3 4v-6m2 10H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z" />
              </svg>
            </span>
            <span>
              <strong>Case studies</strong>
              <small>Real results, real impact</small>
            </span>
          </a>
          <a href="clients.html" class="nav-dropdown-link" role="menuitem">
            <span class="nav-dropdown-icon">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round">
                <path d="M17 20h5v-2a3 3 0 00-5.356-1.857M17 20H7m10 0v-2c0-.656-.126-1.283-.356-1.857M7 20H2v-2a3 3 0 015.356-1.857M7 20v-2c0-.656.126-1.283.356-1.857m0 0a5.002 5.002 0 019.288 0M15 7a3 3 0 11-6 0 3 3 0 016 0z" />
              </svg>
            </span>
            <span>
              <strong>Clients</strong>
              <small>100+ businesses we've powered</small>
            </span>
          </a>
        </div>
      </div>

      <!-- Blogs and Contact -->
      <a href="http://localhost:5173/blogs" class="nav-link">Blogs</a>
      <a href="http://localhost:5173/contact" class="nav-link">Contact</a>

      <!-- CTA -->
      <a href="get-quote.html" class="nav-cta">Get quote</a>
    </div>

    <!-- Mobile Button -->
    <button class="nav-hamburger" id="nav-hamburger" aria-label="Open menu" aria-expanded="false">
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round">
        <path d="M4 7h16M4 12h16M4 17h16" />
      </svg>
    </button>
  </nav>"""

for html_file in html_files:
    if html_file == 'blogs.html' or html_file == 'contact.html':
        continue # We'll handle these separately or delete them
    
    with open(html_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Use regex to find and replace the floating-nav block
    # This might be tricky if structure varies, but we'll try a common pattern
    new_content = re.sub(r'<nav class="floating-nav".*?</nav>', navbar_template, content, flags=re.DOTALL)
    
    if new_content != content:
        print(f"Updated Navbar in {html_file}")
        with open(html_file, 'w', encoding='utf-8') as f:
            f.write(new_content)
    else:
        print(f"No Navbar found or already updated in {html_file}")
