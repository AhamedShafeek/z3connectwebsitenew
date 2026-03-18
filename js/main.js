/* ============================================
   Z3Connect — main.js
   Navigation, scroll detection, counters,
   IntersectionObservers
   ============================================ */

document.addEventListener('DOMContentLoaded', () => {
  // --- Scroll Progress Bar ---
  const scrollProgress = document.querySelector('.scroll-progress');

  function updateScrollProgress() {
    if (!scrollProgress) return;
    const scrollTop = window.scrollY;
    const docHeight = document.documentElement.scrollHeight - window.innerHeight;
    const scrollPercent = docHeight > 0 ? (scrollTop / docHeight) * 100 : 0;
    scrollProgress.style.width = scrollPercent + '%';
  }

  // --- Floating Nav: Hide on scroll down, show on scroll up ---
  const floatingNav = document.querySelector('.floating-nav');
  let lastScrollY = 0;
  let ticking = false;

  function updateNav() {
    if (!floatingNav) return;
    const currentScrollY = window.scrollY;

    if (currentScrollY > lastScrollY + 10 && currentScrollY > 200) {
      // Scrolling DOWN fast and past hero — hide nav
      floatingNav.classList.add('nav-scrolled-down');
      floatingNav.classList.remove('nav-scrolled-up');
    } else if (currentScrollY < lastScrollY - 5) {
      // Scrolling UP — show nav
      floatingNav.classList.remove('nav-scrolled-down');
      floatingNav.classList.add('nav-scrolled-up');
    }

    lastScrollY = currentScrollY;
    ticking = false;
  }

  // --- Nav Theme Switching via IntersectionObserver ---
  const lightSections = document.querySelectorAll('.section-light');

  const navObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        // Check if the section at nav position is light
        const rect = entry.boundingClientRect;
        const navHeight = floatingNav ? floatingNav.offsetHeight : 60;

        // Section occupies the nav area
        if (rect.top <= navHeight && rect.bottom >= 0) {
          floatingNav.classList.add('nav-light');
        }
      }
    });
  }, {
    rootMargin: '-1px 0px -90% 0px',
    threshold: 0
  });

  const darkSections = document.querySelectorAll('.section-dark');
  const darkNavObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        const rect = entry.boundingClientRect;
        const navHeight = floatingNav ? floatingNav.offsetHeight : 60;
        if (rect.top <= navHeight && rect.bottom >= 0) {
          floatingNav.classList.remove('nav-light');
        }
      }
    });
  }, {
    rootMargin: '-1px 0px -90% 0px',
    threshold: 0
  });

  lightSections.forEach(section => navObserver.observe(section));
  darkSections.forEach(section => darkNavObserver.observe(section));

  // --- Scroll Handler ---
  function onScroll() {
    if (!ticking) {
      requestAnimationFrame(() => {
        updateNav();
        updateScrollProgress();
      });
      ticking = true;
    }
  }

  window.addEventListener('scroll', onScroll, { passive: true });

  // --- Section Reveal (IntersectionObserver) ---
  const revealElements = document.querySelectorAll('.reveal-element');

  const revealObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('revealed');
        revealObserver.unobserve(entry.target);
      }
    });
  }, {
    threshold: 0.1,
    rootMargin: '0px 0px -50px 0px'
  });

  revealElements.forEach(el => revealObserver.observe(el));

  // --- Stagger Reveal ---
  const staggerElements = document.querySelectorAll('.reveal-stagger');

  const staggerObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('revealed');
        staggerObserver.unobserve(entry.target);
      }
    });
  }, {
    threshold: 0.1,
    rootMargin: '0px 0px -30px 0px'
  });

  staggerElements.forEach(el => staggerObserver.observe(el));

  // --- Counter Animation ---
  const counters = document.querySelectorAll('[data-count]');

  const counterObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        const target = entry.target;
        const end = parseInt(target.getAttribute('data-count'), 10);
        const suffix = target.getAttribute('data-suffix') || '';
        const duration = 2000;
        const startTime = performance.now();

        function animateCount(currentTime) {
          const elapsed = currentTime - startTime;
          const progress = Math.min(elapsed / duration, 1);

          // Ease-out cubic
          const eased = 1 - Math.pow(1 - progress, 3);
          const current = Math.round(eased * end);

          target.textContent = current + suffix;

          if (progress < 1) {
            requestAnimationFrame(animateCount);
          }
        }

        requestAnimationFrame(animateCount);
        counterObserver.unobserve(target);
      }
    });
  }, {
    threshold: 0.5
  });

  counters.forEach(el => counterObserver.observe(el));

  // --- Word-by-Word Reveal (Testimonial) ---
  const wordRevealContainers = document.querySelectorAll('.word-reveal-container');

  if (wordRevealContainers.length > 0) {
    const wordObserver = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          const words = entry.target.querySelectorAll('.word');
          words.forEach((word, i) => {
            setTimeout(() => {
              word.classList.add('revealed');
            }, i * 80);
          });
          wordObserver.unobserve(entry.target);
        }
      });
    }, {
      threshold: 0.3
    });

    wordRevealContainers.forEach(el => wordObserver.observe(el));
  }

  // --- Cyclic Process Auto-Advance ---
  const cycleProcess = document.getElementById('cycle-process');

  if (cycleProcess) {
    const steps = cycleProcess.querySelectorAll('.cycle-step');
    const totalSteps = steps.length;
    let currentStep = 0;
    let cycleInterval = null;
    let isPaused = false;


    function setActiveStep(index) {
      // Remove active from all
      steps.forEach(s => s.classList.remove('active'));
      const activeNodes = cycleProcess.querySelectorAll('.cycle-node');
      activeNodes.forEach(n => n.classList.remove('active'));

      // Set new active
      currentStep = index % totalSteps;
      steps[currentStep].classList.add('active');

      // Update Graphic Nodes
      const curNode = cycleProcess.querySelector(`.node-${currentStep}`);
      if (curNode) curNode.classList.add('active');
    }

    function startCycle() {
      if (cycleInterval) clearInterval(cycleInterval);
      cycleInterval = setInterval(() => {
        if (!isPaused) {
          setActiveStep(currentStep + 1);
        }
      }, 3000);
    }

    // Click to select step
    steps.forEach((step, i) => {
      step.addEventListener('click', () => {
        setActiveStep(i);
        // Reset timer on click
        startCycle();
      });
    });

    // Pause on hover
    cycleProcess.addEventListener('mouseenter', () => { isPaused = true; });
    cycleProcess.addEventListener('mouseleave', () => { isPaused = false; });

    // Start only when visible
    const cycleObserver = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          setActiveStep(0);
          startCycle();
          cycleObserver.unobserve(entry.target);
        }
      });
    }, { threshold: 0.2 });

    cycleObserver.observe(cycleProcess);
  }

  // Initial call
  updateScrollProgress();
  updateNav();

  // --- Dropdown Navigation ---
  const navItems = document.querySelectorAll('.nav-item[data-dropdown]');
  let activeDropdown = null;

  // Close all dropdowns
  function closeAllDropdowns() {
    navItems.forEach(item => {
      item.classList.remove('active');
      const trigger = item.querySelector('.nav-dropdown-trigger');
      if (trigger) trigger.setAttribute('aria-expanded', 'false');
    });
    activeDropdown = null;
  }

  // Toggle dropdown on click (for touch devices)
  navItems.forEach(item => {
    const trigger = item.querySelector('.nav-dropdown-trigger');

    if (trigger) {
      trigger.addEventListener('click', (e) => {
        e.preventDefault();
        e.stopPropagation();

        const isActive = item.classList.contains('active');
        closeAllDropdowns();

        if (!isActive) {
          item.classList.add('active');
          trigger.setAttribute('aria-expanded', 'true');
          activeDropdown = item;
        }
      });
    }
  });

  // Close dropdown when clicking outside
  document.addEventListener('click', (e) => {
    if (activeDropdown && !activeDropdown.contains(e.target)) {
      closeAllDropdowns();
    }
  });

  // Close dropdown on Escape key
  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape') {
      closeAllDropdowns();
    }
  });

  // --- Mobile Menu: Open / Close ---
  const hamburger = document.getElementById('nav-hamburger');
  const mobileMenu = document.getElementById('mobile-menu');
  const mobileClose = document.getElementById('mobile-menu-close');

  if (hamburger && mobileMenu) {
    hamburger.addEventListener('click', () => {
      mobileMenu.classList.add('active');
      hamburger.setAttribute('aria-expanded', 'true');
      document.body.style.overflow = 'hidden';
    });
  }

  if (mobileClose && mobileMenu) {
    mobileClose.addEventListener('click', () => {
      mobileMenu.classList.remove('active');
      if (hamburger) hamburger.setAttribute('aria-expanded', 'false');
      document.body.style.overflow = '';
      // Collapse all mobile groups
      document.querySelectorAll('.mobile-nav-group').forEach(g => g.classList.remove('expanded'));
    });
  }

  // Close mobile menu when clicking a link
  if (mobileMenu) {
    mobileMenu.querySelectorAll('a').forEach(link => {
      link.addEventListener('click', () => {
        mobileMenu.classList.remove('active');
        if (hamburger) hamburger.setAttribute('aria-expanded', 'false');
        document.body.style.overflow = '';
      });
    });
  }

  // --- Mobile Nav Accordion ---
  const mobileNavGroups = document.querySelectorAll('.mobile-nav-group-title');

  mobileNavGroups.forEach(title => {
    title.addEventListener('click', () => {
      const group = title.closest('.mobile-nav-group');
      const isExpanded = group.classList.contains('expanded');

      // Collapse all groups first
      document.querySelectorAll('.mobile-nav-group').forEach(g => g.classList.remove('expanded'));

      // Toggle current
      if (!isExpanded) {
        group.classList.add('expanded');
        title.setAttribute('aria-expanded', 'true');
      } else {
        title.setAttribute('aria-expanded', 'false');
      }
    });
  });

  // --- Active Page Detection ---
  const currentPath = window.location.pathname.split('/').pop() || 'index.html';

  // Map pages to their parent nav groups
  const pageGroups = {
    'about.html': 'company',
    'founder.html': 'company',
    'philosophy.html': 'company',
    'team.html': 'company',
    'why-we-exist.html': 'company',
    'products.html': 'products',
    'solutions-detailed.html': 'products',
    'work.html': 'work',
    'portfolio.html': 'work',
    'case-studies.html': 'work',
    'case-study.html': 'work'
  };

  const parentGroup = pageGroups[currentPath];
  if (parentGroup) {
    const navItem = document.querySelector(`.nav-item[data-dropdown="${parentGroup}"]`);
    if (navItem) {
      const trigger = navItem.querySelector('.nav-dropdown-trigger');
      if (trigger) {
        trigger.style.color = '#fff';
        trigger.style.background = 'rgba(255, 255, 255, 0.1)';
        trigger.style.borderRadius = '9999px';
      }
    }
  }

  // Highlight direct Contact link if on contact page
  if (currentPath === 'contact.html') {
    const contactLink = document.querySelector('.nav-links > a.nav-link[href="contact.html"]');
    if (contactLink) {
      contactLink.style.color = '#fff';
      contactLink.style.background = 'rgba(255, 255, 255, 0.1)';
    }
  }

  // --- Inline Nav SVG Logo: Draw-then-Fill Animation ---
  const navLogoSVGs = document.querySelectorAll('.nav-logo-svg');

  navLogoSVGs.forEach(svg => {
    const paths = svg.querySelectorAll('path');
    let delay = 0;
    let totalDuration = 0;

    paths.forEach(path => {
      const length = path.getTotalLength ? path.getTotalLength() : 100;
      path.style.strokeDasharray = length;
      path.style.strokeDashoffset = length;
      path.style.animation = `navLogoDraw 1.5s ease forwards ${delay}s`;
      delay += 0.12;
      totalDuration = delay + 1.5;
    });

    setTimeout(() => {
      paths.forEach(path => {
        if (!path.classList.contains('nav-logo-no-fill')) {
          path.classList.add('nav-logo-filled');
        }
      });
    }, totalDuration * 1000);
  });

});
