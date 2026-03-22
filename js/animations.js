/* ============================================
   Z3Connect — animations.js
   AOS init, Lenis smooth scroll, hero choreography
   ============================================ */

document.addEventListener('DOMContentLoaded', () => {

    // --- Lenis Smooth Scroll ---
    let lenis;

    function initLenis() {
        if (typeof Lenis === 'undefined') return;

        lenis = new Lenis({
            lerp: 0.1, // Smooth interpolation (0.1 is standard for premium feel)
            wheelMultiplier: 1,
            touchMultiplier: 1.5,
            smoothWheel: true,
            orientation: 'vertical',
            gestureOrientation: 'vertical'
        });

        // Expose globally so components.js can use it
        window.lenis = lenis;

        function raf(time) {
            lenis.raf(time);
            requestAnimationFrame(raf);
        }

        requestAnimationFrame(raf);
    }

    initLenis();

    // --- AOS Init ---
    function initAOS() {
        if (typeof AOS === 'undefined') return;

        AOS.init({
            duration: 800,
            easing: 'ease-out-cubic',
            once: true,
            offset: 50,
            disable: window.matchMedia('(prefers-reduced-motion: reduce)').matches
        });
    }

    initAOS();

    // --- Hero Animation Choreography ---
    const prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

    function heroChoreography() {
        const line1 = document.querySelector('.hero-line-1');
        const line2 = document.querySelector('.hero-line-2');
        const subtitle = document.querySelector('.hero-subtitle');
        const ctas = document.querySelector('.hero-ctas');
        const stats = document.querySelector('.hero-stats');
        const scrollArrow = document.querySelector('.hero-scroll');

        if (prefersReducedMotion) {
            // Show everything instantly
            [line1, line2, ctas, stats, scrollArrow].forEach(el => {
                if (el) {
                    el.style.opacity = '1';
                    el.style.transform = 'none';
                    el.style.filter = 'none';
                }
            });
            if (subtitle) {
                const text = subtitle.getAttribute('data-text') || subtitle.textContent;
                subtitle.innerHTML = text;
            }
            return;
        }

        // 0.3s — Line 1 slides up + deblurs
        setTimeout(() => {
            if (line1) line1.classList.add('hero-animate-line');
        }, 300);

        // 0.5s — Line 2 slides up + deblurs
        setTimeout(() => {
            if (line2) line2.classList.add('hero-animate-line');
        }, 500);

        // 0.8s — Subtitle typewriter
        setTimeout(() => {
            if (subtitle) {
                startTypewriter(subtitle);
            }
        }, 800);

        // 1.8s — CTAs fade in
        setTimeout(() => {
            if (ctas) ctas.classList.add('hero-animate-fade-scale');
        }, 1800);

        // 2.4s — Stats fade in (counters handled by IntersectionObserver in main.js)
        setTimeout(() => {
            if (stats) stats.classList.add('hero-animate-fade');
        }, 2400);

        // 3.0s — Scroll indicator
        setTimeout(() => {
            if (scrollArrow) scrollArrow.classList.add('hero-animate-fade');
        }, 3000);
    }

    // --- Typewriter Effect ---
    function startTypewriter(element) {
        const text = element.getAttribute('data-text');
        if (!text) return;

        element.innerHTML = '<span class="cursor"></span>';
        let charIndex = 0;

        function typeChar() {
            if (charIndex < text.length) {
                const cursor = element.querySelector('.cursor');
                if (cursor) {
                    cursor.insertAdjacentText('beforebegin', text[charIndex]);
                }
                charIndex++;
                setTimeout(typeChar, 40 + Math.random() * 30);
            } else {
                // Remove cursor after typing is done (after a brief pause)
                setTimeout(() => {
                    const cursor = element.querySelector('.cursor');
                    if (cursor) cursor.remove();
                }, 2000);
            }
        }

        typeChar();
    }

    // Start hero
    heroChoreography();
});
