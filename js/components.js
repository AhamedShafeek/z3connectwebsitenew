/* ============================================
   Z3Connect — components.js
   WhatsApp button, mobile menu, marquee
   ============================================ */

document.addEventListener('DOMContentLoaded', () => {

    // --- Mobile Menu ---
    const hamburger = document.querySelector('.nav-hamburger');
    const mobileMenu = document.querySelector('.mobile-menu');
    const mobileClose = document.querySelector('.mobile-menu-close');
    const mobileLinks = document.querySelectorAll('.mobile-menu-link, .mobile-menu-cta');

    function openMobileMenu() {
        if (!mobileMenu) return;
        mobileMenu.classList.add('active');
        document.body.style.overflow = 'hidden';
    }

    function closeMobileMenu() {
        if (!mobileMenu) return;
        mobileMenu.classList.remove('active');
        document.body.style.overflow = '';
    }

    if (hamburger) {
        hamburger.addEventListener('click', openMobileMenu);
    }

    if (mobileClose) {
        mobileClose.addEventListener('click', closeMobileMenu);
    }

    mobileLinks.forEach(link => {
        link.addEventListener('click', closeMobileMenu);
    });

    // Close on Escape key
    document.addEventListener('keydown', (e) => {
        if (e.key === 'Escape' && mobileMenu && mobileMenu.classList.contains('active')) {
            closeMobileMenu();
        }
    });

    // --- Marquee Pause on Hover ---
    const marqueeTrack = document.querySelector('.marquee-track');
    if (marqueeTrack) {
        marqueeTrack.addEventListener('mouseenter', () => {
            marqueeTrack.style.animationPlayState = 'paused';
        });
        marqueeTrack.addEventListener('mouseleave', () => {
            marqueeTrack.style.animationPlayState = 'running';
        });
    }

    // --- WhatsApp Button Tooltip ---
    const whatsappBtn = document.querySelector('.whatsapp-float');
    if (whatsappBtn) {
        // Ensure aria-label for accessibility
        whatsappBtn.setAttribute('aria-label', 'Chat on WhatsApp');
        whatsappBtn.setAttribute('role', 'link');
    }

    // --- Project Quote Form Handling ---
    const quoteForm = document.getElementById('projectQuoteForm');
    const successMessage = document.getElementById('formSuccessMessage');

    if (quoteForm && successMessage) {
        quoteForm.addEventListener('submit', function (e) {
            e.preventDefault();

            // Basic animation for transition
            quoteForm.style.opacity = '0';
            setTimeout(() => {
                quoteForm.classList.add('hidden');
                successMessage.classList.remove('hidden');

                // Use Lenis for smooth scroll to success message if available
                if (window.lenis) {
                    window.lenis.scrollTo(successMessage, { offset: -100 });
                } else {
                    successMessage.scrollIntoView({ behavior: 'smooth', block: 'center' });
                }
            }, 400);
        });
    }

    // --- Clients Filter Handling ---
    const filterButtons = document.querySelectorAll('.fb');
    const clientCards = document.querySelectorAll('.cc');

    if (filterButtons.length > 0 && clientCards.length > 0) {
        filterButtons.forEach(btn => {
            btn.addEventListener('click', () => {
                // Update active state
                filterButtons.forEach(b => b.classList.remove('active'));
                btn.classList.add('active');

                // Filter logic
                const category = btn.dataset.filter;
                clientCards.forEach(card => {
                    if (category === 'all' || card.dataset.cat === category) {
                        card.classList.remove('hidden');
                    } else {
                        card.classList.add('hidden');
                    }
                });

                // Refresh Lenis if active because visibility changed
                if (window.lenis) {
                    window.lenis.update();
                }
            });
        });
    }

    // --- Portfolio Filter Handling ---
    const portfolioButtons = document.querySelectorAll('.filter-btn');
    const portfolioCards = document.querySelectorAll('.portfolio-card');

    if (portfolioButtons.length > 0 && portfolioCards.length > 0) {
        portfolioButtons.forEach(btn => {
            btn.addEventListener('click', () => {
                // Update active state
                portfolioButtons.forEach(b => {
                    b.classList.remove('active');
                    // Reset inline styles if present from legacy scripts
                    b.style.background = '';
                    b.style.color = '';
                    b.style.borderColor = '';
                });
                btn.classList.add('active');

                // Filter logic
                const filter = btn.dataset.filter;
                portfolioCards.forEach(card => {
                    if (filter === 'all' || card.dataset.category === filter) {
                        card.style.display = '';
                        setTimeout(() => {
                            card.style.opacity = '1';
                            card.style.transform = 'translateY(0)';
                        }, 10);
                    } else {
                        card.style.opacity = '0';
                        card.style.transform = 'translateY(20px)';
                        setTimeout(() => {
                            card.style.display = 'none';
                        }, 300);
                    }
                });

                // Refresh Lenis if active
                if (window.lenis) {
                    window.lenis.update();
                }
            });
        });
    }

    // --- Mouse Follower ---
    const mouseFollower = document.querySelector('.mouse-follower');
    if (mouseFollower && window.innerWidth > 768) {
        mouseFollower.style.display = 'block';
        document.addEventListener('mousemove', (e) => {
            mouseFollower.style.left = e.clientX + 'px';
            mouseFollower.style.top = e.clientY + 'px';
        });

        const interactiveElements = document.querySelectorAll('a, button, .glass-hover, .group, .portfolio-card, .fb, .filter-btn');
        interactiveElements.forEach(el => {
            el.addEventListener('mouseenter', () => mouseFollower.classList.add('active'));
            el.addEventListener('mouseleave', () => mouseFollower.classList.remove('active'));
        });
    } else if (mouseFollower) {
        mouseFollower.style.display = 'none';
    }
});
