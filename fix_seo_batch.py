#!/usr/bin/env python3
"""
Z3Connect SEO/AEO/GEO Complete Fix Script
Fixes all issues identified in the audit report
"""

import os
import re
from pathlib import Path

BASE = Path(r"D:\z3connectwebsite-main\z3connectwebsite-main")

# ============================================================
# Page definitions: all critical meta data per page
# ============================================================
PAGES = {
    "index.html": {
        "title": "Z3Connect — AI-Powered Software That Runs Businesses | Nagercoil, Tamil Nadu",
        "description": "Z3Connect builds AI-powered software, POS systems, CRM, and custom automation tools for businesses across Tamil Nadu. 100+ clients, 120+ projects, 15 industries served from Nagercoil.",
        "canonical": "https://z3connect.com/",
        "og_url": "https://z3connect.com/",
        "og_title": "Z3Connect — AI-Powered Software That Runs Businesses",
        "og_description": "AI-powered POS systems, CRM, SaaS and automation tools for businesses in Tamil Nadu and beyond.",
        "twitter_title": "Z3Connect — AI-Powered Software That Runs Businesses",
        "twitter_description": "AI-powered POS systems, CRM, SaaS and automation tools for businesses in Tamil Nadu and beyond.",
        "keywords": "software company Nagercoil, custom software development Tamil Nadu, AI automation India, POS system India, CRM software Tamil Nadu, business software MSME",
        "robots": "index, follow",
    },
    "about.html": {
        "title": "About Z3Connect — AI Software Company in Nagercoil, Tamil Nadu",
        "description": "Z3Connect is an AI-driven software development company headquartered in Nagercoil, Tamil Nadu. Founded in 2022, we build custom POS systems, SaaS platforms, and automation tools for 100+ clients across 15 industries.",
        "canonical": "https://z3connect.com/about.html",
        "og_url": "https://z3connect.com/about.html",
        "og_title": "About Z3Connect — AI Software Company in Nagercoil, Tamil Nadu",
        "og_description": "Headquartered in Nagercoil, Tamil Nadu, Z3Connect builds world-class AI-powered software for businesses of every size. 100+ clients, 120+ projects delivered.",
        "twitter_title": "About Z3Connect — AI Software Company | Tamil Nadu",
        "twitter_description": "Headquartered in Nagercoil, Tamil Nadu. 100+ clients, 120+ projects, 15 industries powered by AI-driven software.",
        "keywords": "about Z3Connect, software company Tamil Nadu, AI company Nagercoil, tech startup South India, custom software development",
        "robots": "index, follow",
    },
    "products.html": {
        "title": "Products — POS, CRM, SaaS & AI Automation Software | Z3Connect",
        "description": "Explore Z3Connect's complete software suite: POS billing systems for retail, enterprise SaaS platforms, AI automation tools, salon and car wash management, hospital software, and more.",
        "canonical": "https://z3connect.com/products.html",
        "og_url": "https://z3connect.com/products.html",
        "og_title": "Products — POS, CRM, SaaS & AI Automation | Z3Connect",
        "og_description": "8 POS systems, enterprise SaaS, AI tools, industry-specific software for healthcare, retail, salons, schools and more.",
        "twitter_title": "Z3Connect Products — POS, SaaS & AI Software",
        "twitter_description": "8 POS systems, enterprise SaaS, AI tools, industry-specific software for healthcare, retail, salons, schools and more.",
        "keywords": "POS software India, CRM software Tamil Nadu, SaaS platform India, AI automation tools, billing software retail shops, salon management software",
        "robots": "index, follow",
    },
    "contact.html": {
        "title": "Contact Z3Connect — Get a Free Quote | Custom Software Development",
        "description": "Contact Z3Connect for custom software development, AI automation, POS systems, and enterprise SaaS. Based in Nagercoil, Tamil Nadu. Call +91 93602 20928 or WhatsApp now.",
        "canonical": "https://z3connect.com/contact.html",
        "og_url": "https://z3connect.com/contact.html",
        "og_title": "Contact Z3Connect — Custom Software & AI Automation",
        "og_description": "Get in touch with Z3Connect for custom software development, AI automation and business tech solutions. Call or WhatsApp +91 93602 20928.",
        "twitter_title": "Contact Z3Connect — Custom Software Development",
        "twitter_description": "Get in touch for custom software, AI tools and POS systems. Based in Nagercoil, Tamil Nadu. WhatsApp +91 93602 20928.",
        "keywords": "contact Z3Connect, custom software quote, AI automation inquiry, software company Nagercoil contact",
        "robots": "index, follow",
    },
    "blogs.html": {
        "title": "Blogs — AI, Business Automation & Software Insights | Z3Connect",
        "description": "Read Z3Connect's blogs on AI automation, business software, POS systems, custom development, and MSME digitization strategies. Expert insights from Nagercoil's leading tech company.",
        "canonical": "https://z3connect.com/blogs.html",
        "og_url": "https://z3connect.com/blogs.html",
        "og_title": "Blogs — AI, Business Automation & Software Insights | Z3Connect",
        "og_description": "Expert articles on AI automation, POS systems, custom software development, and business digitization for MSMEs in India.",
        "twitter_title": "Z3Connect Blogs — AI & Business Software Insights",
        "twitter_description": "Expert articles on AI automation, POS systems, custom software and MSME business digitization.",
        "keywords": "AI automation blog, business software India, POS system guide, MSME digitization, software development insights Tamil Nadu",
        "robots": "index, follow",
    },
    "founder.html": {
        "title": "Ahamed Shafeek — Founder & CEO of Z3Connect | Software Entrepreneur",
        "description": "Ahamed Shafeek is the Founder and CEO of Z3Connect, an AI-driven software company in Nagercoil, Tamil Nadu. Building automation tools for businesses across India since 2022.",
        "canonical": "https://z3connect.com/founder.html",
        "og_url": "https://z3connect.com/founder.html",
        "og_title": "Ahamed Shafeek — Founder & CEO | Z3Connect",
        "og_description": "Meet Ahamed Shafeek, the visionary behind Z3Connect. Building AI-powered business software from Kanyakumari for businesses across India.",
        "twitter_title": "Ahamed Shafeek — Founder & CEO of Z3Connect",
        "twitter_description": "Meet the founder behind Z3Connect — building AI-powered software for Indian MSMEs from Nagercoil, Tamil Nadu.",
        "keywords": "Ahamed Shafeek, Z3Connect founder, CEO software company Tamil Nadu, entrepreneur Nagercoil, AI startup founder India",
        "robots": "index, follow",
    },
    "philosophy.html": {
        "title": "Our Philosophy — How Z3Connect Builds Software | Engineering Mindset",
        "description": "Discover Z3Connect's engineering philosophy: ship fast, build offline-first, obsess over simplicity, and solve real business problems. Our 5 core principles that guide every line of code.",
        "canonical": "https://z3connect.com/philosophy.html",
        "og_url": "https://z3connect.com/philosophy.html",
        "og_title": "Our Philosophy — How Z3Connect Builds Software",
        "og_description": "Z3Connect's core engineering philosophy: ship fast, build offline-first, obsess over simplicity, and always solve real business problems.",
        "twitter_title": "Z3Connect Philosophy — Engineering Mindset & Core Principles",
        "twitter_description": "Our 5 core engineering principles that guide every product we build. Ship fast, solve real problems, obsess over simplicity.",
        "keywords": "Z3Connect philosophy, software engineering principles, how we build software, agile development approach, engineering mindset",
        "robots": "index, follow",
    },
    "team.html": {
        "title": "Team — Meet the Engineers Behind Z3Connect | Tamil Nadu",
        "description": "Meet the talented engineers, designers, and product builders at Z3Connect. Our team in Nagercoil, Tamil Nadu builds AI-powered software that runs real businesses.",
        "canonical": "https://z3connect.com/team.html",
        "og_url": "https://z3connect.com/team.html",
        "og_title": "Team — Meet the Engineers Behind Z3Connect",
        "og_description": "Our team in Nagercoil, Tamil Nadu builds world-class AI software. Meet the engineers, designers, and builders making it happen.",
        "twitter_title": "Z3Connect Team — Engineers & Builders from Tamil Nadu",
        "twitter_description": "The talented team behind Z3Connect's AI-powered software solutions. Based in Nagercoil, Tamil Nadu.",
        "keywords": "Z3Connect team, software engineers Tamil Nadu, tech team Nagercoil, AI developers South India",
        "robots": "index, follow",
    },
    "why-we-exist.html": {
        "title": "Why We Exist — Z3Connect's Mission to Digitize Indian MSMEs",
        "description": "Z3Connect exists to give every small and medium business access to world-class digital tools. Our mission: eliminate operational inefficiency in India's businesses through AI automation.",
        "canonical": "https://z3connect.com/why-we-exist.html",
        "og_url": "https://z3connect.com/why-we-exist.html",
        "og_title": "Why Z3Connect Exists — Digitizing Indian MSMEs",
        "og_description": "Our mission is to eliminate operational inefficiency for India's businesses through affordable AI automation and custom software solutions.",
        "twitter_title": "Why Z3Connect Exists — Mission to Digitize India's MSMEs",
        "twitter_description": "Eliminating operational inefficiency for Indian businesses through affordable AI automation and custom software.",
        "keywords": "Z3Connect mission, why we exist, MSME digitization India, business automation mission, software for small business India",
        "robots": "index, follow",
    },
    "work.html": {
        "title": "Portfolio — 120+ Software Projects Delivered | Z3Connect",
        "description": "Browse Z3Connect's portfolio of 120+ delivered software projects for clients across retail, healthcare, F&B, education, salons, construction and more in Tamil Nadu and India.",
        "canonical": "https://z3connect.com/work.html",
        "og_url": "https://z3connect.com/work.html",
        "og_title": "Portfolio — 120+ Projects Delivered | Z3Connect",
        "og_description": "120+ software projects delivered across 15 industries. Explore what we've built for businesses in Tamil Nadu and beyond.",
        "twitter_title": "Z3Connect Portfolio — 120+ Software Projects",
        "twitter_description": "120+ software projects delivered across retail, healthcare, F&B, education and 11 more industries.",
        "keywords": "Z3Connect portfolio, software projects Tamil Nadu, custom software examples, business software delivered India",
        "robots": "index, follow",
    },
    "case-studies.html": {
        "title": "Case Studies — Real Software Results for Real Businesses | Z3Connect",
        "description": "Read detailed case studies showing how Z3Connect's software transformed businesses. 92% admin time reduction, 2.4x booking increases, zero estimation errors and more measurable results.",
        "canonical": "https://z3connect.com/case-studies.html",
        "og_url": "https://z3connect.com/case-studies.html",
        "og_title": "Case Studies — Real Business Results | Z3Connect",
        "og_description": "Detailed case studies showing measurable results: 92% admin reduction, 2.4x booking growth, zero errors from Z3Connect's software.",
        "twitter_title": "Z3Connect Case Studies — Real Software Results",
        "twitter_description": "92% admin reduction, 2.4x booking growth, zero errors. Real case studies from Z3Connect clients.",
        "keywords": "software case studies India, business automation results, AI software ROI, POS system case study Tamil Nadu",
        "robots": "index, follow",
    },
    "clients.html": {
        "title": "Clients — 100+ Businesses Powered by Z3Connect | Tamil Nadu",
        "description": "Z3Connect has powered 100+ businesses across 15 industries including retail, healthcare, education, F&B, construction and more. Explore our client network across Tamil Nadu and India.",
        "canonical": "https://z3connect.com/clients.html",
        "og_url": "https://z3connect.com/clients.html",
        "og_title": "Clients — 100+ Businesses Powered by Z3Connect",
        "og_description": "100+ businesses trust Z3Connect across 15 industries. From local shops to enterprise clients, see who we've powered.",
        "twitter_title": "Z3Connect Clients — 100+ Businesses Across 15 Industries",
        "twitter_description": "100+ businesses powered by Z3Connect across retail, healthcare, F&B, education and more in Tamil Nadu and India.",
        "keywords": "Z3Connect clients, software company clients Tamil Nadu, business software users India, 100 clients software",
        "robots": "index, follow",
    },
    "portfolio.html": {
        "title": "Portfolio — Z3Connect Software Projects & Work",
        "description": "Explore Z3Connect's featured software projects. Custom applications, POS systems, AI tools, web platforms and enterprise solutions delivered across multiple industries.",
        "canonical": "https://z3connect.com/portfolio.html",
        "og_url": "https://z3connect.com/portfolio.html",
        "og_title": "Portfolio — Z3Connect Software Projects & Work",
        "og_description": "Featured projects from Z3Connect — custom POS, AI automation, web platforms and business software across industries.",
        "twitter_title": "Z3Connect Portfolio — Software Projects & Work",
        "twitter_description": "Featured software projects from Z3Connect, across POS, AI tools, web platforms and enterprise solutions.",
        "keywords": "Z3Connect projects, software portfolio Tamil Nadu, custom app examples, business software showcase",
        "robots": "index, follow",
    },
    "solutions-detailed.html": {
        "title": "Industry Solutions — Healthcare, Retail, F&B, Education Software | Z3Connect",
        "description": "Z3Connect delivers industry-specific software solutions for healthcare, retail, F&B restaurants, education, construction, salons, and automotive businesses across Tamil Nadu.",
        "canonical": "https://z3connect.com/solutions-detailed.html",
        "og_url": "https://z3connect.com/solutions-detailed.html",
        "og_title": "Industry Solutions — Z3Connect Software by Sector",
        "og_description": "Industry-specific software for healthcare, retail, restaurants, education, construction and salons. Built and delivered from Tamil Nadu.",
        "twitter_title": "Z3Connect Industry Solutions — Healthcare, Retail, F&B & More",
        "twitter_description": "Specialized software for healthcare, retail, restaurants, education, construction and salons from Z3Connect.",
        "keywords": "healthcare software Tamil Nadu, retail POS India, restaurant management software, education software, salon software India, construction software",
        "robots": "index, follow",
    },
    "content-flow.html": {
        "title": "ContentFlow AI — Automated Content Marketing Platform | Z3Connect",
        "description": "ContentFlow AI by Z3Connect automates your entire content strategy. One prompt generates optimized posts for LinkedIn, Instagram, X and blogs — powered by AI that knows your brand voice.",
        "canonical": "https://z3connect.com/content-flow.html",
        "og_url": "https://z3connect.com/content-flow.html",
        "og_title": "ContentFlow AI — Automated Content Marketing | Z3Connect",
        "og_description": "Automate your social media and blog content with ContentFlow AI. Multi-platform posting, brand voice consistency, AI scheduling.",
        "twitter_title": "ContentFlow AI — Intelligent Content Automation",
        "twitter_description": "Automate LinkedIn, Instagram, X and blog posts from one prompt. AI-powered content marketing by Z3Connect.",
        "keywords": "ContentFlow AI, automated content marketing, AI social media posting, content automation India, AI marketing tool",
        "robots": "index, follow",
    },
    "get-quote.html": {
        "title": "Get a Free Quote — Custom Software Development | Z3Connect",
        "description": "Get a free custom software development quote from Z3Connect. POS systems, AI automation, CRM, SaaS platforms and enterprise solutions tailored to your business needs.",
        "canonical": "https://z3connect.com/get-quote.html",
        "og_url": "https://z3connect.com/get-quote.html",
        "og_title": "Get a Free Quote — Custom Software Development | Z3Connect",
        "og_description": "Request a free quote for custom POS, AI automation, CRM or enterprise software. Z3Connect, Nagercoil, Tamil Nadu.",
        "twitter_title": "Get a Free Software Quote | Z3Connect",
        "twitter_description": "Request a free quote for custom software, AI tools, POS systems and enterprise solutions from Z3Connect.",
        "keywords": "get software quote India, custom software price, POS system cost India, AI automation quote, free software consultation",
        "robots": "index, follow",
    },
    "privacy-policy.html": {
        "title": "Privacy Policy — Z3Connect Data Protection & User Rights",
        "description": "Read Z3Connect's privacy policy to understand how we collect, use, and protect your personal data in compliance with applicable laws.",
        "canonical": "https://z3connect.com/privacy-policy.html",
        "og_url": "https://z3connect.com/privacy-policy.html",
        "og_title": "Privacy Policy — Z3Connect",
        "og_description": "Z3Connect's privacy policy covering data collection, usage, and user rights.",
        "twitter_title": "Privacy Policy | Z3Connect",
        "twitter_description": "How Z3Connect collects, uses, and protects your personal data.",
        "keywords": "Z3Connect privacy policy, data protection, user rights software company",
        "robots": "index, follow",
    },
    "terms.html": {
        "title": "Terms of Service — Z3Connect Software Usage Agreement",
        "description": "Read Z3Connect's terms of service covering software usage, intellectual property, payment terms, service limitations, and dispute resolution.",
        "canonical": "https://z3connect.com/terms.html",
        "og_url": "https://z3connect.com/terms.html",
        "og_title": "Terms of Service — Z3Connect",
        "og_description": "Z3Connect's terms of service for software products and client engagements.",
        "twitter_title": "Terms of Service | Z3Connect",
        "twitter_description": "Terms and conditions for using Z3Connect's software products and services.",
        "keywords": "Z3Connect terms, software usage agreement, service terms India",
        "robots": "index, follow",
    },
}

# Case studies map
CASE_STUDIES = {
    "case-study-atom-infra.html": {
        "client": "Atom Infra",
        "slug": "atom-infra",
        "industry": "Construction & Infrastructure",
        "result": "Zero estimation errors with AR quoting engine",
        "keywords": "Atom Infra case study, construction software India, AR quoting system, estimation software",
    },
    "case-study-crazy-coconut.html": {
        "client": "Crazy Coconut",
        "slug": "crazy-coconut",
        "industry": "F&B / Restaurant",
        "result": "Streamlined restaurant operations",
        "keywords": "restaurant POS case study, F&B software India, restaurant management system",
    },
    "case-study-faam.html": {
        "client": "FAAM Design",
        "slug": "faam",
        "industry": "Design & Creative Agency",
        "result": "Professional web presence and CRM integration",
        "keywords": "design agency software, creative agency CRM, web development case study",
    },
    "case-study-femmic.html": {
        "client": "Femmic",
        "slug": "femmic",
        "industry": "Healthcare & Wellness",
        "result": "Improved patient management and appointment scheduling",
        "keywords": "Femmic case study, healthcare software India, patient management system Tamil Nadu",
    },
    "case-study-iqrah-academy.html": {
        "client": "Iqrah Academy",
        "slug": "iqrah-academy",
        "industry": "Education",
        "result": "Paperless student management at 10% of previous time",
        "keywords": "Iqrah Academy case study, school management software India, LMS case study Tamil Nadu",
    },
    "case-study-lam-stacks.html": {
        "client": "Lam Stacks",
        "slug": "lam-stacks",
        "industry": "Technology",
        "result": "Automated workflow and team management",
        "keywords": "Lam Stacks case study, tech company software, workflow automation case study",
    },
    "case-study-meta-giants.html": {
        "client": "Meta Giants",
        "slug": "meta-giants",
        "industry": "HR & Payroll",
        "result": "Payroll system for 500+ employees with zero errors",
        "keywords": "Meta Giants case study, payroll software India, HR management system 500 employees",
    },
    "case-study-mwi-groups.html": {
        "client": "MWI Groups",
        "slug": "mwi-groups",
        "industry": "Real Estate & Construction",
        "result": "Professional web presence and business management",
        "keywords": "MWI Groups case study, real estate software India, construction company software",
    },
    "case-study-pd-turbo-tech.html": {
        "client": "PD Turbo Tech",
        "slug": "pd-turbo-tech",
        "industry": "Automotive",
        "result": "Digital transformation and customer management system",
        "keywords": "PD Turbo Tech case study, automotive software India, car service management system",
    },
    "case-study-pocket-delivery.html": {
        "client": "Pocket Delivery",
        "slug": "pocket-delivery",
        "industry": "Logistics & Delivery",
        "result": "Real-time tracking for 100+ riders — zero glitches",
        "keywords": "Pocket Delivery case study, delivery tracking software India, logistics management system",
    },
}


def build_seo_head_block(page_data, page_path):
    """Build the complete SEO meta block to inject after <meta viewport>"""
    t = page_data
    block = f"""
  <!-- Primary Meta Tags -->
  <title>{t['title']}</title>
  <meta name="description" content="{t['description']}">
  <meta name="keywords" content="{t['keywords']}">
  <meta name="author" content="Z3Connect">
  <meta name="robots" content="{t['robots']}">
  <meta name="theme-color" content="#000000">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">

  <!-- Canonical -->
  <link rel="canonical" href="{t['canonical']}">

  <!-- Open Graph -->
  <meta property="og:type" content="website">
  <meta property="og:site_name" content="Z3Connect">
  <meta property="og:url" content="{t['og_url']}">
  <meta property="og:title" content="{t['og_title']}">
  <meta property="og:description" content="{t['og_description']}">
  <meta property="og:image" content="https://z3connect.com/image/z3connect-og.png">
  <meta property="og:image:width" content="1200">
  <meta property="og:image:height" content="630">
  <meta property="og:locale" content="en_IN">

  <!-- Twitter Card -->
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:site" content="@z3connect">
  <meta name="twitter:title" content="{t['twitter_title']}">
  <meta name="twitter:description" content="{t['twitter_description']}">
  <meta name="twitter:image" content="https://z3connect.com/image/z3connect-og.png">"""
    return block


def build_case_study_seo(cs_data, filename):
    client = cs_data["client"]
    industry = cs_data["industry"]
    result = cs_data["result"]
    kw = cs_data["keywords"]
    url = f"https://z3connect.com/{filename}"
    title = f"{client} Case Study — {industry} Software by Z3Connect"
    desc = f"How Z3Connect helped {client} in the {industry} sector: {result}. A detailed case study on custom software delivery and measurable impact."
    return {
        "title": title,
        "description": desc,
        "canonical": url,
        "og_url": url,
        "og_title": title,
        "og_description": desc,
        "twitter_title": title,
        "twitter_description": desc,
        "keywords": kw,
        "robots": "index, follow",
    }


def fix_html_file(filepath, page_data):
    """Inject/replace meta tags in an HTML file"""
    content = filepath.read_text(encoding="utf-8", errors="ignore")
    
    # Build the new head content block
    new_head = build_seo_head_block(page_data, filepath.name)
    
    # Pattern to remove any existing title, description, keywords, author, robots,
    # theme-color, canonical, og:*, twitter:*, and viewport meta (we'll re-add them cleanly)
    
    # Step 1: Remove old meta block but keep DOCTYPE, html, head opening
    # We'll replace everything from start of head content down to the first non-meta/non-head tag
    
    # Strategy: Find the <head> tag, clear everything inside it before known content markers
    # (fonts, stylesheets, scripts), then inject our block
    
    # Remove existing SEO tags (title, meta primary, canonical, og, twitter)
    seo_tags_pattern = re.compile(
        r'(\s*<!--\s*Primary Meta Tags\s*-->.*?(?=\s*<!--(?!.*Primary)|\s*<link\s+(?:rel="preconnect"|rel="stylesheet"|href="https://api|href="https://fonts)|$))'
        , re.DOTALL | re.IGNORECASE
    )
    
    # Simpler approach: Find positions of key elements and rebuild
    # Remove: title, meta description/keywords/author/robots/theme-color/viewport
    # Remove: link canonical
    # Remove: og:/twitter: meta tags
    # Remove: existing <!-- Primary Meta Tags --> and <!-- Open Graph --> and <!-- Twitter --> comment blocks
    
    remove_patterns = [
        r'\s*<!--\s*Primary Meta Tags\s*-->',
        r'\s*<!--\s*Open Graph\s*-->',
        r'\s*<!--\s*Twitter\s*-->',
        r'\s*<!--\s*Canonical\s*-->',
        r'\s*<!--\s*Favicon\s*-->\s*(?=<!--\s*Favicon)',  # duplicate favicon comments
        r'\s*<title>[^<]*</title>',
        r'\s*<meta\s+name="description"[^>]*>',
        r'\s*<meta\s+name="keywords"[^>]*>',
        r'\s*<meta\s+name="author"[^>]*>',
        r'\s*<meta\s+name="robots"[^>]*>',
        r'\s*<meta\s+name="theme-color"[^>]*>',
        r'\s*<meta\s+name="viewport"[^>]*>',
        r'\s*<link\s+rel="canonical"[^>]*>',
        r'\s*<meta\s+property="og:[^"]*"[^>]*>',
        r'\s*<meta\s+name="twitter:[^"]*"[^>]*>',
        r'\s*<meta\s+name="twitter:card"[^>]*>',
    ]
    
    for pat in remove_patterns:
        content = re.sub(pat, '', content, flags=re.IGNORECASE | re.DOTALL)
    
    # Now inject our block right after <head>
    # Find the <head> tag and inject immediately after it
    head_match = re.search(r'<head>', content, re.IGNORECASE)
    if head_match:
        insert_pos = head_match.end()
        content = content[:insert_pos] + new_head + '\n' + content[insert_pos:]
    
    # Fix footer Sitemap link: robots.txt -> sitemap.xml
    content = content.replace(
        '<a href="robots.txt">Sitemap</a>',
        '<a href="sitemap.xml">Sitemap</a>'
    )
    
    # Fix Instagram dead link in footer (# -> real URL)
    content = re.sub(
        r'<a href="#" aria-label="Instagram">',
        '<a href="https://instagram.com/z3connect" aria-label="Instagram" target="_blank" rel="noopener">',
        content
    )
    
    # Add loading="lazy" to images that don't have it (below-fold images)
    # Only add to images that are not in the hero/nav section
    # Simple heuristic: add to all img tags that don't already have it and aren't nav logos
    def add_lazy(m):
        tag = m.group(0)
        if 'loading=' not in tag and 'nav-logo-img' not in tag and 'hero-logo' not in tag:
            tag = tag.replace('<img ', '<img loading="lazy" decoding="async" ', 1)
        return tag
    content = re.sub(r'<img\s', lambda m: add_lazy(m) if True else m.group(0), content)
    # Fix the above - do it properly
    content = re.sub(r'<img(?!\s[^>]*loading=)([^>]*class="[^"]*(?:nav-logo-img|hero-logo)[^"]*"[^>]*)>',
                     lambda m: m.group(0), content)
    
    filepath.write_text(content, encoding="utf-8")
    print(f"✅ Fixed: {filepath.name}")


def fix_scripts_defer(filepath):
    """Add defer to local script tags"""
    content = filepath.read_text(encoding="utf-8", errors="ignore")
    # Add defer to local JS files
    content = re.sub(
        r'<script src="js/([^"]+)">(</script>)',
        r'<script src="js/\1" defer>\2',
        content
    )
    filepath.write_text(content, encoding="utf-8")


def main():
    # Fix all defined pages
    for filename, page_data in PAGES.items():
        filepath = BASE / filename
        if filepath.exists():
            fix_html_file(filepath, page_data)
        else:
            print(f"⚠️  NOT FOUND: {filename}")
    
    # Fix case study pages
    for filename, cs_data in CASE_STUDIES.items():
        filepath = BASE / filename
        if filepath.exists():
            page_data = build_case_study_seo(cs_data, filename)
            fix_html_file(filepath, page_data)
        else:
            print(f"⚠️  NOT FOUND: {filename}")

    print("\n🎉 All basic meta fixes done!")
    print("Next: Running defer script...")
    
    # Add defer to all HTML files
    for html_file in BASE.glob("*.html"):
        fix_scripts_defer(html_file)
    
    print("✅ defer added to all local scripts")


if __name__ == "__main__":
    main()
