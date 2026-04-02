"""
Add missing Schema JSON-LD markup to pages that lack it.
Pages targeted: philosophy.html, why-we-exist.html, work.html,
content-flow.html, and all 10 case-study-*.html files.
"""

import re
import os

BASE = r"d:\z3connectwebsite-main\z3connectwebsite-main"

# ─── Schema blocks per page type ────────────────────────────────────────────

PHILOSOPHY_SCHEMA = '''
  <!-- Structured Data (Schema.org) -->
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@graph": [
      {
        "@type": "BreadcrumbList",
        "itemListElement": [
          {"@type": "ListItem", "position": 1, "name": "Home", "item": "https://z3connect.com"},
          {"@type": "ListItem", "position": 2, "name": "Philosophy", "item": "https://z3connect.com/philosophy.html"}
        ]
      },
      {
        "@type": "WebPage",
        "@id": "https://z3connect.com/philosophy.html",
        "url": "https://z3connect.com/philosophy.html",
        "name": "Our Philosophy — How Z3Connect Builds Software",
        "description": "Z3Connect's core engineering philosophy: ship fast, build offline-first, obsess over simplicity, and solve real business problems.",
        "publisher": {"@id": "https://z3connect.com/#organization"},
        "about": {
          "@type": "Organization",
          "@id": "https://z3connect.com/#organization"
        }
      },
      {
        "@type": "ItemList",
        "name": "Z3Connect Core Engineering Principles",
        "description": "The 5 guiding principles that shape every product Z3Connect builds.",
        "numberOfItems": 5,
        "itemListElement": [
          {"@type": "ListItem", "position": 1, "name": "Solve Real Problems", "description": "Every line of code must trace back to removing operational friction for real businesses."},
          {"@type": "ListItem", "position": 2, "name": "Ship, Then Improve", "description": "Deploy functional v1s rapidly, gather real-world data, and iterate relentlessly."},
          {"@type": "ListItem", "position": 3, "name": "Obsess Over Simplicity", "description": "Strip away the unnecessary, ensuring systems are intuitive for anyone to master."},
          {"@type": "ListItem", "position": 4, "name": "Speed Is A Feature", "description": "Deploy in weeks, iterate daily, and compound speed into reliability for partners."},
          {"@type": "ListItem", "position": 5, "name": "Built to Scale", "description": "Clean code, strong architecture — systems that handle 1 user or 1 million without breaking."}
        ]
      }
    ]
  }
  </script>
'''

WHY_WE_EXIST_SCHEMA = '''
  <!-- Structured Data (Schema.org) -->
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@graph": [
      {
        "@type": "BreadcrumbList",
        "itemListElement": [
          {"@type": "ListItem", "position": 1, "name": "Home", "item": "https://z3connect.com"},
          {"@type": "ListItem", "position": 2, "name": "Why We Exist", "item": "https://z3connect.com/why-we-exist.html"}
        ]
      },
      {
        "@type": "WebPage",
        "@id": "https://z3connect.com/why-we-exist.html",
        "url": "https://z3connect.com/why-we-exist.html",
        "name": "Why Z3Connect Exists — Mission to Digitize Indian MSMEs",
        "description": "Z3Connect exists to give every small and medium business access to world-class digital tools. Our mission: eliminate operational inefficiency through AI automation.",
        "publisher": {"@id": "https://z3connect.com/#organization"}
      },
      {
        "@type": "FAQPage",
        "mainEntity": [
          {
            "@type": "Question",
            "name": "Why was Z3Connect founded?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Z3Connect was founded because small and medium businesses in India were losing 3-5 hours daily on repetitive manual tasks. We exist to give that time back through affordable AI automation and custom software tailored to each business's workflow."
            }
          },
          {
            "@type": "Question",
            "name": "What problem does Z3Connect solve?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Z3Connect solves the digital divide for India's MSMEs. We replace paper logs, spreadsheets, and manual processes with AI-powered POS systems, CRM tools, and custom automation that make businesses more efficient and scalable."
            }
          },
          {
            "@type": "Question",
            "name": "Is Z3Connect affordable for small businesses?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Yes. Z3Connect is purpose-built for MSME pricing — enterprise-grade automation at costs small businesses can afford. We design our products to be accessible, not exclusive to large corporations."
            }
          }
        ]
      }
    ]
  }
  </script>
'''

WORK_SCHEMA = '''
  <!-- Structured Data (Schema.org) -->
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@graph": [
      {
        "@type": "BreadcrumbList",
        "itemListElement": [
          {"@type": "ListItem", "position": 1, "name": "Home", "item": "https://z3connect.com"},
          {"@type": "ListItem", "position": 2, "name": "Portfolio", "item": "https://z3connect.com/work.html"}
        ]
      },
      {
        "@type": "CollectionPage",
        "@id": "https://z3connect.com/work.html",
        "url": "https://z3connect.com/work.html",
        "name": "Portfolio — 120+ Software Projects Delivered | Z3Connect",
        "description": "Browse Z3Connect's portfolio of 120+ delivered software projects for clients across retail, healthcare, F&B, education, salons, construction and more.",
        "publisher": {"@id": "https://z3connect.com/#organization"},
        "about": {"@id": "https://z3connect.com/#organization"}
      },
      {
        "@type": "ItemList",
        "name": "Z3Connect Featured Client Projects",
        "description": "A selection of flagship software projects delivered by Z3Connect.",
        "numberOfItems": 10,
        "itemListElement": [
          {"@type": "ListItem", "position": 1, "name": "Atom Infra — 3D/AR Construction Visualization Portal", "url": "https://z3connect.com/case-study-atom-infra.html"},
          {"@type": "ListItem", "position": 2, "name": "MWI Groups — Enterprise Multi-Brand Management System", "url": "https://z3connect.com/case-study-mwi-groups.html"},
          {"@type": "ListItem", "position": 3, "name": "PD Turbo Tech — Automotive Service Platform", "url": "https://z3connect.com/case-study-pd-turbo-tech.html"},
          {"@type": "ListItem", "position": 4, "name": "Crazy Coconut — F&B Restaurant POS & Ordering System", "url": "https://z3connect.com/case-study-crazy-coconut.html"},
          {"@type": "ListItem", "position": 5, "name": "Pocket Delivery — Last-Mile Logistics Platform", "url": "https://z3connect.com/case-study-pocket-delivery.html"}
        ]
      }
    ]
  }
  </script>
'''

CONTENT_FLOW_SCHEMA = '''
  <!-- Structured Data (Schema.org) -->
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@graph": [
      {
        "@type": "BreadcrumbList",
        "itemListElement": [
          {"@type": "ListItem", "position": 1, "name": "Home", "item": "https://z3connect.com"},
          {"@type": "ListItem", "position": 2, "name": "ContentFlow AI", "item": "https://z3connect.com/content-flow.html"}
        ]
      },
      {
        "@type": "SoftwareApplication",
        "name": "ContentFlow AI",
        "alternateName": "Content Flow",
        "applicationCategory": "BusinessApplication",
        "operatingSystem": "Web",
        "url": "https://z3connect.com/content-flow.html",
        "description": "ContentFlow AI automates your entire content strategy. One prompt generates optimized posts for LinkedIn, Instagram, X and blogs — powered by AI that knows your brand voice.",
        "offers": {
          "@type": "Offer",
          "priceCurrency": "INR",
          "availability": "https://schema.org/InStock"
        },
        "publisher": {"@id": "https://z3connect.com/#organization"},
        "featureList": [
          "Multi-platform content generation",
          "AI-powered scheduling",
          "Brand voice consistency",
          "LinkedIn, Instagram, X, and Blog posting",
          "Unified analytics dashboard"
        ]
      },
      {
        "@type": "FAQPage",
        "mainEntity": [
          {
            "@type": "Question",
            "name": "What is ContentFlow AI?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "ContentFlow AI is a content marketing automation platform by Z3Connect. You provide one prompt or idea, and AI agents generate optimized posts tailored for LinkedIn, Instagram, X, and your blog — consistent with your brand voice."
            }
          },
          {
            "@type": "Question",
            "name": "How does ContentFlow AI work?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "ContentFlow works in 3 steps: (1) Drop a voice note, rough draft, or link as input. (2) AI agents generate platform-specific versions for each social channel. (3) Content flows automatically to your scheduled queue for hands-free publishing."
            }
          },
          {
            "@type": "Question",
            "name": "Which social platforms does ContentFlow AI support?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "ContentFlow AI supports LinkedIn, Instagram, X (Twitter), and personal or business blogs. Each platform gets content optimized specifically for its format and audience."
            }
          }
        ]
      }
    ]
  }
  </script>
'''

# Case study schema template
def make_case_study_schema(page_slug, client_name, industry, headline, description, url, results):
    return f'''
  <!-- Structured Data (Schema.org) -->
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@graph": [
      {{
        "@type": "BreadcrumbList",
        "itemListElement": [
          {{"@type": "ListItem", "position": 1, "name": "Home", "item": "https://z3connect.com"}},
          {{"@type": "ListItem", "position": 2, "name": "Case Studies", "item": "https://z3connect.com/case-studies.html"}},
          {{"@type": "ListItem", "position": 3, "name": "{client_name}", "item": "https://z3connect.com/{page_slug}"}}
        ]
      }},
      {{
        "@type": "Article",
        "@id": "https://z3connect.com/{page_slug}",
        "headline": "{headline}",
        "description": "{description}",
        "url": "https://z3connect.com/{page_slug}",
        "datePublished": "2026-03-28",
        "dateModified": "2026-04-02",
        "author": {{
          "@type": "Organization",
          "@id": "https://z3connect.com/#organization",
          "name": "Z3Connect"
        }},
        "publisher": {{
          "@id": "https://z3connect.com/#organization"
        }},
        "about": {{
          "@type": "Thing",
          "name": "{client_name}",
          "description": "Client in the {industry} industry served by Z3Connect"
        }},
        "keywords": ["case study", "{client_name.lower()}", "{industry.lower()}", "Z3Connect", "custom software India"],
        "articleBody": "{description} {results}"
      }}
    ]
  }}
  </script>
'''

CASE_STUDIES = {
    "case-study-atom-infra.html": {
        "client_name": "Atom Infra",
        "industry": "Construction & Infrastructure",
        "headline": "Atom Infra Case Study — 3D/AR Construction Visualization Portal by Z3Connect",
        "description": "How Z3Connect built a 3D/AR visualization portal for Atom Infra, cutting client approval times by 50% and reducing revision cycles by 3x.",
        "results": "50% faster approvals, 100% web-accessible, 3x fewer revision cycles achieved."
    },
    "case-study-crazy-coconut.html": {
        "client_name": "Crazy Coconut",
        "industry": "Food & Beverage",
        "headline": "Crazy Coconut Case Study — Restaurant Management System by Z3Connect",
        "description": "How Z3Connect delivered a comprehensive restaurant management and POS system for Crazy Coconut, streamlining orders, billing, and kitchen operations.",
        "results": "Faster order processing, reduced billing errors, and improved kitchen coordination achieved."
    },
    "case-study-faam.html": {
        "client_name": "FAAM",
        "industry": "Fashion & Retail",
        "headline": "FAAM Case Study — Fashion Retail Platform by Z3Connect",
        "description": "How Z3Connect built a fashion retail management platform for FAAM with inventory tracking, billing, and customer management.",
        "results": "Streamlined retail operations, reduced manual inventory work, and improved customer data management."
    },
    "case-study-femmic.html": {
        "client_name": "Femmic",
        "industry": "Healthcare & Wellness",
        "headline": "Femmic Case Study — Healthcare Management System by Z3Connect",
        "description": "How Z3Connect built a clinic and patient management system for Femmic, digitizing appointment booking, patient records, and billing.",
        "results": "Digitized patient records, reduced appointment no-shows, and automated billing workflows."
    },
    "case-study-iqrah-academy.html": {
        "client_name": "IQRAH Academy",
        "industry": "Education",
        "headline": "IQRAH Academy Case Study — Learning Management System by Z3Connect",
        "description": "How Z3Connect built a learning management system for IQRAH Academy, enabling online course delivery, student tracking, and certification management.",
        "results": "2.4x increase in student enrollment, streamlined course delivery, and automated certification workflow."
    },
    "case-study-lam-stacks.html": {
        "client_name": "Lam Stacks",
        "industry": "Technology & SaaS",
        "headline": "Lam Stacks Case Study — SaaS Platform Development by Z3Connect",
        "description": "How Z3Connect partnered with Lam Stacks to build a full-stack SaaS platform with multi-tenant architecture and real-time analytics.",
        "results": "Production-ready SaaS platform delivered, multi-tenant architecture, real-time dashboards operational."
    },
    "case-study-meta-giants.html": {
        "client_name": "Meta Giants",
        "industry": "Digital & DeFi",
        "headline": "Meta Giants Case Study — DeFi Ecosystem Platform by Z3Connect",
        "description": "How Z3Connect built a DeFi ecosystem platform for Meta Giants, including smart contract integration, wallet connectivity, and real-time asset tracking.",
        "results": "Full DeFi platform delivered with smart contract integration, real-time transaction tracking, and secure wallet management."
    },
    "case-study-mwi-groups.html": {
        "client_name": "MWI Groups",
        "industry": "Multi-Brand Enterprise",
        "headline": "MWI Groups Case Study — Enterprise Multi-Brand Management System by Z3Connect",
        "description": "How Z3Connect built a unified enterprise management system for MWI Groups, consolidating operations across multiple business verticals.",
        "results": "Unified multi-brand dashboard, cross-vertical reporting, and centralized inventory management delivered."
    },
    "case-study-pd-turbo-tech.html": {
        "client_name": "PD Turbo Tech",
        "industry": "Automotive Services",
        "headline": "PD Turbo Tech Case Study — Automotive Service Management by Z3Connect",
        "description": "How Z3Connect built an automotive service management platform for PD Turbo Tech, covering vehicle tracking, service history, billing, and appointments.",
        "results": "Streamlined service workflow, digital job cards, automated invoicing, and improved vehicle turnaround time."
    },
    "case-study-pocket-delivery.html": {
        "client_name": "Pocket Delivery",
        "industry": "Logistics & Last-Mile Delivery",
        "headline": "Pocket Delivery Case Study — Last-Mile Logistics Platform by Z3Connect",
        "description": "How Z3Connect built a last-mile delivery management platform for Pocket Delivery with real-time tracking, route optimization, and driver management.",
        "results": "Real-time delivery tracking, optimized routes, reduced delivery times, and improved driver coordination achieved."
    }
}

# ─── Helpers ─────────────────────────────────────────────────────────────────

def inject_schema(filepath, schema_block):
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    if "application/ld+json" in content:
        print(f"  SKIP (already has schema): {os.path.basename(filepath)}")
        return
    # Inject before </head>
    if "</head>" not in content:
        print(f"  WARN: No </head> found in {os.path.basename(filepath)}")
        return
    new_content = content.replace("</head>", schema_block.rstrip() + "\n\n</head>", 1)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(new_content)
    print(f"  INJECTED schema into: {os.path.basename(filepath)}")


# ─── Main ────────────────────────────────────────────────────────────────────

print("=== Adding missing Schema JSON-LD ===\n")

# Philosophy
inject_schema(os.path.join(BASE, "philosophy.html"), PHILOSOPHY_SCHEMA)

# Why We Exist
inject_schema(os.path.join(BASE, "why-we-exist.html"), WHY_WE_EXIST_SCHEMA)

# Work
inject_schema(os.path.join(BASE, "work.html"), WORK_SCHEMA)

# ContentFlow
inject_schema(os.path.join(BASE, "content-flow.html"), CONTENT_FLOW_SCHEMA)

# All case studies
for filename, data in CASE_STUDIES.items():
    schema = make_case_study_schema(
        page_slug=filename,
        client_name=data["client_name"],
        industry=data["industry"],
        headline=data["headline"],
        description=data["description"],
        url=f"https://z3connect.com/{filename}",
        results=data["results"]
    )
    inject_schema(os.path.join(BASE, filename), schema)

print("\n=== Done! ===")
