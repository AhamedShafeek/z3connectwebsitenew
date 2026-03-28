import os
import re

template_file = "d:/z3connectwebsite-main/z3connectwebsite-main/case-study.html"

with open(template_file, "r", encoding="utf-8") as f:
    template_content = f.read()

case_studies = [
    {
        "id": "pd-turbo-tech",
        "tag": "Automotive",
        "title": "Automated Billing & Inventory System",
        "logo": "image/portfolio_logo/pdturbotech_logo.jpg",
        "subtitle": "Cut invoicing time by 80% and eliminated manual stock errors with a unified digital ecosystem.",
        "context": "<p>PD Turbo Tech is a specialized automotive service center handling 50+ vehicles daily. They managed hundreds of distinct spare parts manually, generating invoices and tracking inventory primarily on paper and basic spreadsheets.</p>",
        "problems": [
            ("Time-Consuming Invoicing", "Service advisors spent up to 15 minutes manually writing invoices and cross-referencing part prices."),
            ("Stock Discrepancies", "Without real-time inventory tracking, staff often committed parts to customers that were out of stock."),
            ("Missing Analytics", "The owner had no immediate visibility into daily revenue, top-selling services, or inventory costs.")
        ],
        "solution_intro": "<p>We deployed a comprehensive digital ecosystem using a React Native tablet app for advisors and a Node.js web dashboard for management, backed by a robust PostgreSQL database.</p>",
        "solution_features": [
            ("Digital Job Cards", "Advisors can create job cards directly on tablets, instantly syncing with the parts department."),
            ("Live Inventory Sync", "Stock levels update automatically as parts are assigned to jobs. Low-stock alerts are sent instantly."),
            ("1-Click Invoicing", "Invoices are generated instantly from completed job cards containing accurate parts and labor costs."),
            ("Executive Dashboard", "Real-time analytics for revenue, parts consumption, and mechanic performance trackable from anywhere.")
        ],
        "implementation": "<p><strong>Week 1:</strong> System architecture and database design. Audited their existing parts spreadsheet to prepare for migration.</p><p><strong>Week 2-3:</strong> Front-end app development and back-end inventory logic construction. Conducted pilot testing with senior advisors.</p><p><strong>Week 4:</strong> Full deployment and staff training. Migrated all previous service records into the new system.</p>",
        "results_stats": [
            ("80%", "Faster Invoicing"),
            ("100%", "Digital Records"),
            ("Zero", "Inventory Errors")
        ],
        "results_text": "<p>The entire workflow—from vehicle intake to final billing—is now entirely paperless and lightning fast. Service advisors handle 30% more customers per day without feeling rushed.</p><p>The business owner now has absolute control and visibility over operations, receiving automated daily digest reports.</p>",
        "technologies": ["React Native", "Node.js", "PostgreSQL", "Tablet App", "Digital Billing"]
    },
    {
        "id": "mwi-groups",
        "tag": "Multi-Brand",
        "title": "Multi-branch Operational ERP",
        "logo": "image/portfolio_logo/mwilogo.svg",
        "subtitle": "Centralized data across divisions, yielding a 40% efficiency boost in financial reporting and team operations.",
        "context": "<p>MWI Groups operates multiple business divisions including retail and contracting. Their varied operations meant each branch used disparate systems, making consolidated reporting and cross-branch visibility practically impossible.</p>",
        "problems": [
            ("Fragmented Data", "Each division used different tools (Excel, Tally, paper), making it difficult to gauge overall company health."),
            ("Slow Reporting", "Consolidating end-of-month financial reports took the accounting team entirely too long."),
            ("Communication Silos", "Teams across different branches struggled to coordinate shared resources effectively.")
        ],
        "solution_intro": "<p>We built a unified Enterprise Resource Planning (ERP) platform tailored strictly for their operational workflows, unifying data streams into a single source of truth.</p>",
        "solution_features": [
            ("Central Dashboard", "A unified control hub showing real-time KPIs across all business divisions simultaneously."),
            ("Automated Consolidation", "Financial tools that automatically sync daily sales and expenses across branches."),
            ("Resource Allocation", "A module to track and allocate shared assets, staff, and inventory between divisions dynamically."),
            ("Role-based Access", "Granular permissions ensuring staff only see data relevant to their specific branch and role.")
        ],
        "implementation": "<p><strong>Phase 1:</strong> Workflow mapping for all 3 major divisions. Designed the unified data schema.</p><p><strong>Phase 2:</strong> Developed the core financial consolidation engine and the central dashboard.</p><p><strong>Phase 3:</strong> Branch-by-branch rollout to ensure smooth transitions without disrupting daily operations.</p>",
        "results_stats": [
            ("40%", "Efficiency Boost"),
            ("1", "Unified System"),
            ("Live", "Branch Analytics")
        ],
        "results_text": "<p>MWI Groups achieved total operational clarity. The executive team can instantly check the vital signs of any division at any moment, and month-end reporting now takes hours instead of days.</p><p>Cross-branch resource sharing has become fluid, significantly reducing redundant operational costs.</p>",
        "technologies": ["React", "Express.js", "MongoDB", "ERP", "Data Visualizations"]
    },
    {
        "id": "iqrah-academy",
        "tag": "Education",
        "title": "Custom Learning Management System",
        "logo": "image/portfolio_logo/iqralogo.svg",
        "subtitle": "Scaled to 1000+ simultaneous students without performance drops, automating quizzes and grading.",
        "context": "<p>IQRAH Academy is a rapidly growing educational institution. As their student base expanded, their reliance on generic, off-the-shelf LMS tools created massive admin overhead and limited their ability to track specific student progress metrics.</p>",
        "problems": [
            ("Admin Overhead", "Manually enrolling students, assigning courses, and grading basic quizzes consumed too much faculty time."),
            ("Limited Tracking", "Off-the-shelf software failed to provide deep analytical insights into where students were struggling."),
            ("System Crashes", "During peak exam times, their previous system suffered severe slowdowns and crashes.")
        ],
        "solution_intro": "<p>We completely engineered a proprietary Learning Management System focused entirely on high concurrency, automated grading, and deep analytics.</p>",
        "solution_features": [
            ("Auto-Grading Engine", "Quizzes and assessments are instantly graded, with immediate feedback delivered to the student."),
            ("Deep Analytics Map", "Instructors see heatmaps of quiz results, instantly highlighting topics the class is failing to grasp."),
            ("Elastic Infrastructure", "Cloud-native architecture designed to scale automatically during high-traffic exam periods."),
            ("Parent Portal", "A dedicated access point for parents to track their child's attendance and academic progress.")
        ],
        "implementation": "<p><strong>Month 1:</strong> Cloud architectural design and database optimization for high-read/write exam scenarios.</p><p><strong>Month 2:</strong> Core LMS features, instructor dashboards, and the quiz engine.</p><p><strong>Month 3:</strong> Beta launch with one class, followed by a full migration of 1000+ students and historic records.</p>",
        "results_stats": [
            ("1000+", "Active Users"),
            ("99.9%", "Uptime"),
            ("Autoscaled", "Infrastructure")
        ],
        "results_text": "<p>IQRAH Academy successfully transitioned completely to the new digital platform. Faculty save an average of 10 hours a week on grading and admin tasks, allowing them to focus entirely on instruction.</p><p>The system handled their biggest exam season flawlessly without a single latency spike.</p>",
        "technologies": ["AWS", "Node.js", "React", "Serverless", "Analytics"]
    },
    {
        "id": "pocket-delivery",
        "tag": "Logistics",
        "title": "Fleet Tracking & Mobile App",
        "logo": "image/portfolio_logo/pocketdeliverywordlogo.svg",
        "subtitle": "Reduced late deliveries by 35% through real-time route optimization and automated dispatching.",
        "context": "<p>Pocket Delivery is an agile urban logistics startup. Managing a growing fleet of riders with basic chat apps and spreadsheets was causing massive inefficiencies, missed delivery windows, and poor customer communication.</p>",
        "problems": [
            ("Inefficient Dispatch", "Dispatchers manually assigned orders to riders based on guesswork, resulting in overlapping routes."),
            ("No Live Tracking", "Customers called headquarters constantly to ask where their packages were."),
            ("Payment Disputes", "Cash-on-delivery tracking was manual, leading to complex reconciliation at the end of shifts.")
        ],
        "solution_intro": "<p>We created a powerful dual-interface platform: a live operational dashboard for dispatchers and a streamlined mobile app for the delivery fleet.</p>",
        "solution_features": [
            ("Smart Routing", "Algorithms automatically compute and assign the most efficient delivery sequence for riders."),
            ("Live GPS Tracking", "Real-time rider locations are visible to dispatch and optionally shared via SMS links with customers."),
            ("Digital Proof of Delivery", "Riders capture signatures and photos in-app, instantly syncing to the central database."),
            ("Automated COD Reconciliation", "The app tracks exact cash collected versus expected, making end-of-day balances trivial.")
        ],
        "implementation": "<p><strong>Sprint 1:</strong> GPS integration and algorithmic routing design.</p><p><strong>Sprint 2:</strong> Rider app development and central dispatcher dashboard construction.</p><p><strong>Sprint 3:</strong> Field testing with 5 riders to calibrate routing algorithms, then full rollout.</p>",
        "results_stats": [
            ("35%", "Fewer Late Deliveries"),
            ("100%", "Route Optimization"),
            ("Zero", "Reconciliation Errors")
        ],
        "results_text": "<p>Delivery efficiency skyrocketed. Riders complete more deliveries per shift because routes are mathematically optimized, and customer support calls dropped by 60% due to the live tracking links.</p><p>The end-of-day cash reconciliation, which previously took hours, is now done in minutes.</p>",
        "technologies": ["Flutter", "Google Maps API", "Node.js", "WebSockets", "GPS Sync"]
    },
    {
        "id": "crazy-coconut",
        "tag": "F&B",
        "title": "POS & Digital Menu Management",
        "logo": "image/portfolio_logo/crazycoconut_logo.webp",
        "subtitle": "Sped up table turnover by 15% with seamless kitchen ticketing and a unified digital POS.",
        "context": "<p>Crazy Coconut is a bustling, high-volume restaurant. The disconnect between the front-of-house ordering and the kitchen led to delayed orders, incorrect dishes, and frustrated staff during peak hours.</p>",
        "problems": [
            ("Lost Kitchen Tickets", "Paper tickets generated at the register were frequently delayed or lost before reaching the kitchen."),
            ("Menu Update Lag", "Changing prices or 86'ing out-of-stock items took too long to propagate across all systems."),
            ("Slow Checkout", "Splitting bills and managing complex orders bogged down the cashier during rushes.")
        ],
        "solution_intro": "<p>We replaced their legacy setup with a cloud-synced Point of Sale (POS) system combined with a robust Kitchen Display System (KDS).</p>",
        "solution_features": [
            ("Kitchen Display System", "Orders are fired instantly to digital screens in the kitchen the second payment is processed."),
            ("Cloud Menu Manager", "Managers can update items, prices, and stock status from their phone, syncing everywhere globally."),
            ("Advanced Billing", "Features to easily split checks, apply dynamic discounts, and process rapid payments."),
            ("Inventory Link", "Ingredients deplete automatically based on recipe mapping as dishes are sold.")
        ],
        "implementation": "<p><strong>Phase 1:</strong> Recipe mapping and menu ingestion into the new database.</p><p><strong>Phase 2:</strong> Software configuration and hardware setup (tablets for POS, screens for kitchen).</p><p><strong>Phase 3:</strong> After-hours mock service to train the staff, followed by an aggressive overnight live switch.</p>",
        "results_stats": [
            ("15%", "Faster Table Turnover"),
            ("100%", "Digital Kitchen Sync"),
            ("Zero", "Lost Tickets")
        ],
        "results_text": "<p>The chaos of peak service is dramatically reduced. The kitchen operates in a quiet, organized manner using digital queues instead of shouting and paper tickets.</p><p>Faster table turnover has directly increased their daily revenue without altering the physical restaurant space.</p>",
        "technologies": ["React", "Express Hub", "WebSockets", "KDS UI", "Automated Inventory"]
    },
    {
        "id": "meta-giants",
        "tag": "Agency / ERP",
        "title": "Custom Production ERP",
        "logo": "image/portfolio_logo/Metagiants_logo.png",
        "subtitle": "Streamined production management and financial tracking for a growing media agency.",
        "context": "<p>Meta Giants needed a more robust way to track complex production schedules and financial inflows across multiple high-budget projects.</p>",
        "problems": [
            ("Schedule Conflicts", "Multiple projects sharing resources led to bottlenecks."),
            ("Financial Blindspots", "Project-wise profitability was difficult to calculate in real-time."),
            ("Communication Gaps", "Project files and updates were scattered.")
        ],
        "solution_intro": "<p>We built a central Production ERP that unifies scheduling, resource allocation, and project-based accounting.</p>",
        "solution_features": [
            ("Resource Scheduler", "Visual calendar for gear and talent allocation."),
            ("Profitability Tracker", "Real-time spend vs budget dashboards for every project."),
            ("Asset Management", "Centralized repository for project deliverables and assets."),
            ("Automated Invoicing", "Generate milestones-based invoices automatically.")
        ],
        "implementation": "<p><strong>Month 1:</strong> Workflow audit and database architecture.</p><p><strong>Month 2:</strong> Front-end development and accounting integration.</p><p><strong>Month 3:</strong> Deployment and team onboarding.</p>",
        "results_stats": [
            ("30%", "Better Resource Use"),
            ("Live", "Project P&L"),
            ("100%", "Digital Workflow")
        ],
        "results_text": "<p>Meta Giants now manages twice the project volume with the same staff. Visibility into project profitability allows them to make smarter bidding decisions.</p>",
        "technologies": ["React", "Node.js", "MySQL", "ERP", "Project Mgmt"]
    },
    {
        "id": "femmic",
        "tag": "Healthcare",
        "logo": "image/portfolio_logo/femmiclogo.svg",
        "title": "Clinic Appointment & Record Management",
        "subtitle": "Achieved zero double bookings, digitized patient histories, and drastically reduced waiting room time.",
        "context": "<p>Femmic is a specialized healthcare clinic. Their reliance on phone-based booking and paper patient files created massive front-desk bottlenecks and inefficient doctor consultations.</p>",
        "problems": [
            ("Overbooked Slots", "Receptionists occasionally double-booked doctors, leading to unhappy waiting patients."),
            ("Inaccessible Histories", "Retrieving physical patient files for repeat visits was slow and prone to filing errors."),
            ("No Reminders", "A high rate of patient no-shows because no automated reminder system was in place.")
        ],
        "solution_intro": "<p>We deployed a comprehensive Clinic Management System handling everything from online scheduling to digital prescriptions.</p>",
        "solution_features": [
            ("Online Patient Portal", "Patients can book available slots online and fill out pre-consultation intake forms digitally."),
            ("Electronic Health Records", "Doctors instantly view complete medical histories on tablets during the consultation."),
            ("Automated Reminders", "WhatsApp and SMS reminders sent 24 hours and 2 hours before the appointment."),
            ("Digital Prescriptions", "Prescriptions are generated dynamically and can be sent directly to affiliated pharmacies.")
        ],
        "implementation": "<p><strong>Phase 1:</strong> System design focusing strictly on data security and privacy compliance.</p><p><strong>Phase 2:</strong> Building the calendar locking mechanisms and EHR database schemas.</p><p><strong>Phase 3:</strong> Digitizing recent paper records and launching the online portal to the public.</p>",
        "results_stats": [
            ("Zero", "Double Bookings"),
            ("40%", "Drop in No-Shows"),
            ("100%", "Digital Patient Flow")
        ],
        "results_text": "<p>The clinic's waiting room transformed from chaotic to calm. Doctors are better prepared for consultations because they read digital intake forms beforehand.</p><p>No-shows have dropped dramatically thanks to the automated WhatsApp reminders, directly increasing clinic revenue.</p>",
        "technologies": ["React", "Express.js", "Secure Database", "WhatsApp API", "EHR System"]
    },
    {
        "id": "atom-infra",
        "tag": "Construction Tech",
        "logo": "image/portfolio_logo/atominfra_logo.png",
        "title": "3D/AR Visualization Portal",
        "subtitle": "Shortened client approval times by letting stakeholders 'walk through' architectural models securely on the web.",
        "context": "<p>Atom Infra is an innovative construction firm. They realized that sending flat 2D renders and CAD files to clients was leading to miscommunications, delayed approvals, and costly revisions post-construction.</p>",
        "problems": [
            ("Visualization Gap", "Clients frequently struggled to understand spatial dimensions from 2D architectural plans."),
            ("Lengthy Approvals", "Iterating on designs required endless emails and in-person meetings."),
            ("Software Limits", "Clients didn't have heavy CAD software installed to view the actual 3D files.")
        ],
        "solution_intro": "<p>We built a secure, web-based 3D visualization portal utilizing WebGL, allowing clients to interact with complex architectural models directly in their browsers.</p>",
        "solution_features": [
            ("Browser WebGL Engine", "Heavy architectural models render smoothly on standard laptops and tablets without plugins."),
            ("Annotation Tools", "Clients can pin comments and feedback directly onto specific elements in the 3D space."),
            ("Version Control", "A clear history of model versions so clients can see exactly what changed after their feedback."),
            ("AR Mode", "Mobile users can project the 3D models onto their physical environment using Augmented Reality.")
        ],
        "implementation": "<p><strong>Sprint 1:</strong> Three.js and WebGL optimization to compress and render large model files efficiently in-browser.</p><p><strong>Sprint 2:</strong> Building the secure client portal and the 3D annotation interactive layer.</p><p><strong>Sprint 3:</strong> Beta testing with a live client project, refining the lighting and interaction controls.</p>",
        "results_stats": [
            ("50%", "Faster Approvals"),
            ("100%", "Web Accessible"),
            ("3x", "Less Revision Cycles")
        ],
        "results_text": "<p>The platform completely modernized Atom Infra's client presentation process. Clients engage deeply with the models, pinning exact feedback which eliminates ambiguity.</p><p>The overall lifecycle from initial design pitch to final sign-off has been cut in half.</p>",
        "technologies": ["Three.js", "WebGL", "React", "Node.js", "AWS S3 Integration"]
    },
    {
        "id": "faam",
        "tag": "Sports & Fitness",
        "logo": "image/portfolio_logo/faam_logo.png",
        "title": "Gym Membership & Access Control",
        "subtitle": "Automated billing recovery and saw a 20% increase in active memberships through streamlined self-service.",
        "context": "<p>FAAM is a premium sports and fitness facility. Tracking member expiration dates, managing renewals, and controlling facility access was largely a manual effort causing massive revenue leakage.</p>",
        "problems": [
            ("Revenue Leakage", "Members whose subscriptions had expired were still occasionally gaining entry to the facility."),
            ("Manual Follow-ups", "The reception desk wasted hours making phone calls to chase late payments."),
            ("No Class Booking", "Members had to call in to reserve spots in popular fitness classes, leading to frustration.")
        ],
        "solution_intro": "<p>We engineered a complete Club Management System featuring automated recurring billing, member app, and hardware gate integration.</p>",
        "solution_features": [
            ("Hardware Access Integration", "The system connects directly to the gym's turnstiles; expired accounts are automatically denied entry."),
            ("Automated Auto-Pay", "Members securely link cards for automated monthly renewals, drastically reducing churn."),
            ("Member App Booking", "A mobile portal where members can instantly book classes and manage their plans."),
            ("Dunning Management", "Automated system that retries failed payments and sends dynamic SMS alerts.")
        ],
        "implementation": "<p><strong>Week 1-2:</strong> Core membership logic and payment gateway integration containing the recurring billing engine.</p><p><strong>Week 3:</strong> Hardware integration with the local biometric/RFID turnstile systems via local bridge software.</p><p><strong>Week 4:</strong> Launching the member-facing web app and migrating all active members.</p>",
        "results_stats": [
            ("20%", "More Active Members"),
            ("100%", "Automated Access"),
            ("Minimal", "Revenue Leakage")
        ],
        "results_text": "<p>FAAM saw an immediate increase in recognized revenue simply by stopping unauthorized access at the gate.</p><p>The automated billing system collects payments quietly in the background, freeing the reception staff to actually serve members instead of acting as debt collectors.</p>",
        "technologies": ["Hardware Bridge", "Stripe Connect", "Node.js", "React", "Access Control"]
    },
    {
        "id": "lam-stacks",
        "tag": "Tech / SaaS",
        "logo": "image/portfolio_logo/Lamstacks-logo.svg",
        "title": "Scalable Cloud Architecture",
        "subtitle": "Reduced server costs by 50% while designing infrastructure capable of handling 3x sudden traffic spikes.",
        "context": "<p>Lam Stacks runs a high-demand tech SaaS product. As they acquired enterprise clients, their monolithic server architecture started crumbling under the load, resulting in downtime and sky-high AWS bills.</p>",
        "problems": [
            ("System Outages", "Unexpected traffic spikes caused out-of-memory errors and database deadlocks."),
            ("Bloated Costs", "They were severely over-provisioning servers just to handle the 'worst-case scenario'."),
            ("Slow Deployments", "Pushing updates to production took hours and frequently required scheduled downtime.")
        ],
        "solution_intro": "<p>We architected a complete migration from a monolithic structure to a highly optimized, auto-scaling containerized cloud environment.</p>",
        "solution_features": [
            ("Docker Containerization", "Separated their massive application into specialized, lightweight microservices."),
            ("Kubernetes Orchestration", "Implemented k8s to automatically scale individual services up or down based on exact CPU/Memory demands."),
            ("Database Sharding", "Restructured their primary database to distribute connection loads evenly across multiple nodes."),
            ("CI/CD Pipeline", "Automated the testing and deployment process so code goes from GitHub to production in minutes with zero downtime.")
        ],
        "implementation": "<p><strong>Phase 1:</strong> Deep auditing of the existing codebase to identify boundaries for microservices.</p><p><strong>Phase 2:</strong> Containerizing the services and establishing the new AWS Kubernetes clusters.</p><p><strong>Phase 3:</strong> A highly choreographed overnight database migration and DNS switch to the new infrastructure.</p>",
        "results_stats": [
            ("99.99%", "Uptime Achieved"),
            ("50%", "Cost Reduction"),
            ("Minutes", "Deploy Times")
        ],
        "results_text": "<p>Lam Stacks now operates with enterprise-grade reliability. Their infrastructure automatically scales up during marketing pushes and scales down at night, saving them thousands in hosting costs.</p><p>Their engineering team now deploys updates 5x faster, completely eliminating terrifying 'deployment nights'.</p>",
        "technologies": ["AWS", "Kubernetes", "Docker", "CI/CD", "PostgreSQL Sharding"]
    }
]

for study in case_studies:
    # We will regex replace the target blocks.
    # Block 1: Logo & Nav Injection (Template already has floating-nav, but let's re-inject logo correctly)
    logo_html = f'<div class="flex items-center gap-6 mb-8 flex-wrap"><img src="{study["logo"]}" alt="{study["title"]} Logo" class="h-16 w-auto object-contain glass p-2 rounded-xl"><span class="px-3 py-1 glass rounded-full text-xs uppercase tracking-wider">{study["tag"]}</span></div>'
    new_html = re.sub(
        r'<div class="flex items-center gap-6 mb-8 flex-wrap">.*?</div>',
        logo_html,
        template_content,
        count=1,
        flags=re.DOTALL
    )

    # Fallback for if the first regex didn't find the exact flex container (e.g. if I updated template slightly differently)
    if new_html == template_content:
        new_html = re.sub(
            r'<div class="mb-8">\s*<span class="px-3 py-1 glass rounded-full text-xs uppercase tracking-wider">.*?</span>\s*</div>',
            logo_html,
            template_content,
            count=1,
            flags=re.DOTALL
        )

    # Block 2: Title
    new_html = re.sub(
        r'<h1 class="font-display text-4xl sm-text-5xl md-text-6xl font-bold mb-6 leading-tight">\s*.*?\s*</h1>',
        f'<h1 class="font-display text-4xl sm-text-5xl md-text-6xl font-bold mb-6 leading-tight">\n        {study["title"]}\n      </h1>',
        new_html,
        count=1,
        flags=re.DOTALL
    )
    
    # Block 3: Subtitle
    new_html = re.sub(
        r'<p class="text-xl md-text-2xl opacity-80 leading-relaxed">\s*.*?\s*</p>',
        f'<p class="text-xl md-text-2xl opacity-80 leading-relaxed">\n        {study["subtitle"]}\n      </p>',
        new_html,
        count=1,
        flags=re.DOTALL
    )
    
    # Block 4: Context
    new_html = re.sub(
        r'<h2 class="font-display text-2xl md-text-3xl font-semibold mb-6">Client Context</h2>\s*<div class="space-y-4 text-lg leading-relaxed opacity-90">.*?</div>',
        f'<h2 class="font-display text-2xl md-text-3xl font-semibold mb-6">Client Context</h2>\n        <div class="space-y-4 text-lg leading-relaxed opacity-90">\n          {study["context"]}\n        </div>',
        new_html,
        count=1,
        flags=re.DOTALL
    )
    
    # Block 5: The Problem
    problems_html = ""
    for prob in study["problems"]:
        problems_html += f"""
          <div class="flex items-start">
            <div class="w-8 h-8 glass rounded-lg flex items-center justify-center mr-4 flex-shrink-0 mt-1">
              <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4 text-red-400" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
              </svg>
            </div>
            <div>
              <h3 class="text-xl font-semibold mb-2">{prob[0]}</h3>
              <p class="opacity-80">{prob[1]}</p>
            </div>
          </div>
"""
    new_html = re.sub(
        r'<h2 class="font-display text-2xl md-text-3xl font-semibold mb-6">The Problem</h2>\s*<div class="space-y-6">.*?</div>\s*</div>\s*<div class="glass rounded-2xl p-8 md-p-12 mb-12">\s*<h2 class="font-display text-2xl md-text-3xl font-semibold mb-6">Our Solution</h2>',
        f'<h2 class="font-display text-2xl md-text-3xl font-semibold mb-6">The Problem</h2>\n        <div class="space-y-6">\n{problems_html}        </div>\n      </div>\n\n      <div class="glass rounded-2xl p-8 md-p-12 mb-12">\n        <h2 class="font-display text-2xl md-text-3xl font-semibold mb-6">Our Solution</h2>',
        new_html,
        count=1,
        flags=re.DOTALL
    )
    
    # Block 6: Our Solution
    solution_features_html = ""
    for feat in study["solution_features"]:
        solution_features_html += f"""
            <div class="glass rounded-xl p-6">
              <h3 class="text-lg font-semibold mb-3">{feat[0]}</h3>
              <p class="text-sm opacity-80">{feat[1]}</p>
            </div>
"""
    solution_html = f"""<div class="space-y-6">
          <div class="text-lg opacity-90 leading-relaxed">{study["solution_intro"]}</div>

          <div class="grid grid-cols-1 md-grid-cols-2 gap-6 mt-8">
{solution_features_html}          </div>
        </div>"""
        
    new_html = re.sub(
        r'<h2 class="font-display text-2xl md-text-3xl font-semibold mb-6">Our Solution</h2>\s*<div class="space-y-6">.*?</div>\s*</div>\s*<div class="glass rounded-2xl p-8 md-p-12 mb-12">\s*<h2 class="font-display text-2xl md-text-3xl font-semibold mb-6">Implementation</h2>',
        f'<h2 class="font-display text-2xl md-text-3xl font-semibold mb-6">Our Solution</h2>\n        {solution_html}\n      </div>\n\n      <div class="glass rounded-2xl p-8 md-p-12 mb-12">\n        <h2 class="font-display text-2xl md-text-3xl font-semibold mb-6">Implementation</h2>',
        new_html,
        count=1,
        flags=re.DOTALL
    )
    
    # Block 7: Implementation
    new_html = re.sub(
        r'<h2 class="font-display text-2xl md-text-3xl font-semibold mb-6">Implementation</h2>\s*<div class="space-y-4 text-lg leading-relaxed opacity-90">.*?</div>',
        f'<h2 class="font-display text-2xl md-text-3xl font-semibold mb-6">Implementation</h2>\n        <div class="space-y-4 text-lg leading-relaxed opacity-90">\n          {study["implementation"]}\n        </div>',
        new_html,
        count=1,
        flags=re.DOTALL
    )
    
    # Block 8: Results stats and text
    results_stats_html = ""
    for stat in study["results_stats"]:
        results_stats_html += f"""          <div class="text-center">
            <div class="text-4xl font-display font-bold text-gradient mb-2">{stat[0]}</div>
            <div class="text-sm uppercase tracking-wider opacity-70">{stat[1]}</div>
          </div>\n"""
          
    new_html = re.sub(
        r'<div class="grid grid-cols-1 md-grid-cols-3 gap-6 mb-8">.*?</div>\s*<div class="space-y-4 text-lg leading-relaxed opacity-90">.*?</div>',
        f'<div class="grid grid-cols-1 md-grid-cols-3 gap-6 mb-8">\n{results_stats_html}        </div>\n\n        <div class="space-y-4 text-lg leading-relaxed opacity-90">\n          {study["results_text"]}\n        </div>',
        new_html,
        count=1,
        flags=re.DOTALL
    )
    
    # Block 9: Technologies
    tech_html = ""
    for tech in study["technologies"]:
        tech_html += f'<span class="px-4 py-2 glass rounded-full text-sm">{tech}</span>\n          '
    new_html = re.sub(
        r'<div class="flex flex-wrap gap-3">\s*<span class="px-4 py-2 glass rounded-full text-sm">React Native.*?</div>',
        f'<div class="flex flex-wrap gap-3">\n          {tech_html}</div>',
        new_html,
        count=1,
        flags=re.DOTALL
    )
    
    # Title tag
    new_html = new_html.replace("<title>Case Study - Z3Connect</title>", f"<title>{study['title']} Case Study | Z3Connect</title>")

    with open(f"d:/z3connectwebsite-main/z3connectwebsite-main/case-study-{study['id']}.html", "w", encoding="utf-8") as f:
        f.write(new_html)

print("Generated 10 case study files with logos and common navbar.")
