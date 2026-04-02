import os
import re

html_files = [f for f in os.listdir('.') if f.endswith('.html')]

footer_template = """  <footer class="section-dark footer" id="footer">
    <div class="container">
      <div class="footer-grid">
        <div class="footer-column">
          <h4>Company</h4>
          <ul>
            <li><a href="about.html">About us</a></li>
            <li><a href="philosophy.html">Philosophy</a></li>
            <li><a href="team.html">Team</a></li>
            <li><a href="founder.html">Founder</a></li>
            <li><a href="why-we-exist.html">Why we exist</a></li>
          </ul>
        </div>
        <div class="footer-column">
          <h4>Products</h4>
          <ul>
            <li><a href="products.html">All products</a></li>
            <li><a href="solutions-detailed.html">ZAssist AI</a></li>
            <li><a href="products.html#zpos">ZPOS</a></li>
            <li><a href="products.html#zcrm">ZCRM</a></li>
            <li><a href="products.html#inventory">ZInventory</a></li>
          </ul>
        </div>
        <div class="footer-column">
          <h4>Solutions</h4>
          <ul>
            <li><a href="solutions-detailed.html#healthcare">Healthcare</a></li>
            <li><a href="solutions-detailed.html#retail">Retail</a></li>
            <li><a href="solutions-detailed.html#fb">F&B</a></li>
            <li><a href="solutions-detailed.html#construction">Construction</a></li>
            <li><a href="solutions-detailed.html#salons">Salons</a></li>
            <li><a href="solutions-detailed.html#education">Education</a></li>
          </ul>
        </div>
        <div class="footer-column">
          <h4>Portfolio</h4>
          <ul>
            <li><a href="work.html">Featured cases</a></li>
            <li><a href="case-studies.html">Case studies</a></li>
            <li><a href="clients.html">Clients</a></li>
            <li><a href="/blogs">Blogs</a></li>
          </ul>
        </div>
        <div class="footer-column">
          <h4>Resources</h4>
          <ul>
            <li><a href="/contact">Contact</a></li>
            <li><a href="get-quote.html">Get quote</a></li>
            <li><a href="mailto:z3connect@gmail.com">Report issue</a></li>
            <li><a href="philosophy.html">How we think</a></li>
          </ul>
        </div>
        <div class="footer-column">
          <h4>Legal</h4>
          <ul>
            <li><a href="privacy-policy.html">Privacy policy</a></li>
            <li><a href="terms.html">Terms of service</a></li>
            <li><a href="sitemap.xml">Sitemap</a></li>
          </ul>
        </div>
      </div>

      <div class="footer-bottom-premium">
        <div class="footer-brand-minimal">
          <div class="nav-logo">
            <img loading="lazy" decoding="async" src="logo0.png" alt="Z3Connect" class="nav-logo-img">
            <span>Z3Connect</span>
          </div>
          <p class="by-line">BY Z3CONNECT — Built in Tamil Nadu</p>
        </div>
        <div class="footer-bottom-row">
          <div class="footer-social-minimal">
            <a href="https://linkedin.com/in/ahamedshafeek" aria-label="LinkedIn"><svg viewBox="0 0 24 24" fill="currentColor"><path d="M19 0h-14c-2.761 0-5 2.239-5 5v14c0 2.761 2.239 5 5 5h14c2.762 0 5-2.239 5-5v-14c0-2.761-2.238-5-5-5zm-11 19h-3v-11h3v11zm-1.5-12.268c-.966 0-1.75-.79-1.75-1.764s.784-1.764 1.75-1.764 1.75.79 1.75 1.764-.783 1.764-1.75 1.764zm13.5 12.268h-3v-5.604c0-3.368-4-3.113-4 0v5.604h-3v-11h3v1.765c1.396-2.586 7-2.777 7 2.476v6.759z"/></svg></a>
            <a href="https://wa.me/919360220928" aria-label="WhatsApp"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M3 21l1.65 -3.8a9 9 0 1 1 3.4 2.9l-5.05 .9" /><path d="M9 10a.5 .5 0 0 0 1 0v-1a.5 .5 0 0 0 -1 0v1a5 5 0 0 0 5 5h1a.5 .5 0 0 0 0 -1h-1a.5 .5 0 0 0 0 1" /></svg></a>
            <a href="https://instagram.com/z3connect" aria-label="Instagram" target="_blank" rel="noopener"><svg viewBox="0 0 24 24" fill="currentColor"><path d="M12 2.163c3.204 0 3.584.012 4.85.07 3.252.148 4.771 1.691 4.919 4.919.058 1.265.069 1.645.069 4.849 0 3.205-.012 3.584-.069 4.849-.149 3.225-1.664 4.771-4.919 4.919-1.266.058-1.644.07-4.85.07-3.204 0-3.584-.012-4.849-.07-3.26-.149-4.771-1.699-4.919-4.92-.058-1.265-.07-1.644-.07-4.849 0-3.204.013-3.583.07-4.849.149-3.227 1.664-4.771 4.919-4.919 1.266-.057 1.645-.069 4.849-.069zM12 0C8.741 0 8.333.014 7.053.072 2.695.272.273 2.69.073 7.052.014 8.333 0 8.741 0 12c0 3.259.014 3.668.072 4.948.2 4.358 2.618 6.78 6.98 6.98C8.333 23.986 8.741 24 12 24c3.259 0 3.668-.014 4.948-.072 4.354-.2 6.782-2.618 6.979-6.98.059-1.28.073-1.689.073-4.948 0-3.259-.014-3.667-.072-4.947-.196-4.354-2.617-6.78-6.979-6.98C15.668.014 15.259 0 12 0zm0 5.838a6.162 6.162 0 100 12.324 6.162 6.162 0 000-12.324zM12 16a4 4 0 110-8 4 4 0 010 8zm6.406-11.845a1.44 1.44 0 100 2.881 1.44 1.44 0 000-2.881z"/></svg></a>
          </div>
          <div class="footer-bottom-links">
            <a href="privacy-policy.html">Privacy policy</a>
            <a href="terms.html">Terms of service</a>
            <a href="/contact">Contact</a>
          </div>
        </div>
      </div>
    </div>
  </footer>"""

for html_file in html_files:
    if html_file in ['server.js', 'package.json', 'node_modules']:
        continue 
    
    try:
        with open(html_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Replace Footer (from footer start to footer end)
        updated = re.sub(r'<footer.*?</footer>', footer_template, content, flags=re.DOTALL)
        
        if updated != content:
            print(f"Updated Footer in {html_file}")
            with open(html_file, 'w', encoding='utf-8') as f:
                f.write(updated)
    except Exception as e:
        print(f"Error updating {html_file}: {e}")
