import streamlit as st

# ── PAGE CONFIG ───────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Aphrodite Skin Care",
    page_icon="✨",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ── GLOBAL CSS ────────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;600;700&family=Lato:wght@300;400;700&display=swap');

* { box-sizing: border-box; margin: 0; padding: 0; }

html, body, [data-testid="stAppViewContainer"] {
    background: #fff8f9;
    font-family: 'Lato', sans-serif;
    color: #2d2d2d;
}

[data-testid="stAppViewContainer"] > .main > div {
    padding: 0 !important;
    max-width: 100% !important;
}

[data-testid="stHeader"] { background: transparent; }
[data-testid="stSidebar"] { display: none; }

h1, h2, h3 {
    font-family: 'Playfair Display', serif;
}

.block-container {
    padding: 0 !important;
    max-width: 100% !important;
}

/* ── NAV ── */
.navbar {
    background: rgba(255,255,255,0.97);
    backdrop-filter: blur(10px);
    padding: 18px 60px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    border-bottom: 2px solid #f8bbd0;
    position: sticky;
    top: 0;
    z-index: 999;
    box-shadow: 0 2px 20px rgba(155,26,75,0.08);
}
.navbar-brand {
    font-family: 'Playfair Display', serif;
    font-size: 1.7rem;
    font-weight: 700;
    color: #9b1a4b;
    letter-spacing: 1px;
}
.navbar-brand span {
    color: #c2185b;
}
.navbar-tagline {
    font-size: 0.75rem;
    color: #ad6383;
    letter-spacing: 2px;
    text-transform: uppercase;
    margin-top: 2px;
}
.nav-links {
    display: flex;
    gap: 32px;
    list-style: none;
}
.nav-links a {
    text-decoration: none;
    color: #6d2b45;
    font-size: 0.9rem;
    font-weight: 600;
    letter-spacing: 1px;
    text-transform: uppercase;
    transition: color 0.3s;
}
.nav-links a:hover { color: #c2185b; }

/* ── HERO ── */
.hero {
    background: linear-gradient(135deg, #9b1a4b 0%, #c2185b 40%, #e91e8c 100%);
    padding: 110px 60px;
    text-align: center;
    position: relative;
    overflow: hidden;
}
.hero::before {
    content: '';
    position: absolute;
    top: -60px; right: -60px;
    width: 400px; height: 400px;
    background: rgba(255,255,255,0.05);
    border-radius: 50%;
}
.hero::after {
    content: '';
    position: absolute;
    bottom: -80px; left: -80px;
    width: 500px; height: 500px;
    background: rgba(255,255,255,0.04);
    border-radius: 50%;
}
.hero-eyebrow {
    font-size: 0.85rem;
    letter-spacing: 4px;
    text-transform: uppercase;
    color: #f8bbd0;
    margin-bottom: 16px;
}
.hero h1 {
    font-size: 4rem;
    font-weight: 700;
    color: #fff;
    line-height: 1.15;
    margin-bottom: 16px;
    text-shadow: 0 2px 20px rgba(0,0,0,0.15);
}
.hero h1 span {
    color: #ffd6e7;
    font-style: italic;
}
.hero-sub {
    font-size: 1.25rem;
    color: rgba(255,255,255,0.88);
    max-width: 600px;
    margin: 0 auto 36px;
    line-height: 1.7;
    font-weight: 300;
}
.hero-btns {
    display: flex;
    gap: 16px;
    justify-content: center;
    flex-wrap: wrap;
}
.btn-primary {
    background: #fff;
    color: #9b1a4b;
    padding: 16px 40px;
    border-radius: 50px;
    font-weight: 700;
    font-size: 1rem;
    text-decoration: none;
    letter-spacing: 1px;
    box-shadow: 0 8px 30px rgba(0,0,0,0.15);
    transition: transform 0.2s, box-shadow 0.2s;
    display: inline-block;
}
.btn-primary:hover {
    transform: translateY(-3px);
    box-shadow: 0 12px 40px rgba(0,0,0,0.2);
}
.btn-secondary {
    background: transparent;
    color: #fff;
    padding: 16px 40px;
    border-radius: 50px;
    font-weight: 600;
    font-size: 1rem;
    text-decoration: none;
    letter-spacing: 1px;
    border: 2px solid rgba(255,255,255,0.7);
    transition: background 0.3s, border-color 0.3s;
    display: inline-block;
}
.btn-secondary:hover {
    background: rgba(255,255,255,0.15);
    border-color: #fff;
}

/* ── STATS ── */
.stats-bar {
    background: #fff;
    padding: 50px 60px;
    display: flex;
    justify-content: center;
    gap: 60px;
    flex-wrap: wrap;
    border-bottom: 1px solid #fce4ec;
    box-shadow: 0 4px 20px rgba(155,26,75,0.06);
}
.stat-item { text-align: center; }
.stat-number {
    font-family: 'Playfair Display', serif;
    font-size: 2.8rem;
    font-weight: 700;
    color: #9b1a4b;
    line-height: 1;
}
.stat-label {
    font-size: 0.85rem;
    color: #ad6383;
    letter-spacing: 2px;
    text-transform: uppercase;
    margin-top: 6px;
}

/* ── SECTION HEADERS ── */
.section-header {
    text-align: center;
    margin-bottom: 50px;
}
.section-eyebrow {
    font-size: 0.8rem;
    letter-spacing: 4px;
    text-transform: uppercase;
    color: #c2185b;
    margin-bottom: 12px;
}
.section-title {
    font-family: 'Playfair Display', serif;
    font-size: 2.4rem;
    color: #6d2b45;
    margin-bottom: 14px;
}
.section-divider {
    width: 60px;
    height: 3px;
    background: linear-gradient(90deg, #c2185b, #e91e8c);
    margin: 0 auto 18px;
    border-radius: 2px;
}
.section-subtitle {
    font-size: 1.05rem;
    color: #7a4060;
    max-width: 580px;
    margin: 0 auto;
    line-height: 1.7;
}

/* ── SERVICES ── */
.services-section {
    background: #fff8f9;
    padding: 80px 60px;
}
.services-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
    gap: 28px;
    max-width: 1200px;
    margin: 0 auto;
}
.service-card {
    background: #fff;
    border-radius: 20px;
    padding: 36px 28px;
    border: 1px solid #fce4ec;
    box-shadow: 0 4px 20px rgba(155,26,75,0.06);
    transition: transform 0.3s, box-shadow 0.3s;
    position: relative;
    overflow: hidden;
}
.service-card::before {
    content: '';
    position: absolute;
    top: 0; left: 0; right: 0;
    height: 4px;
    background: linear-gradient(90deg, #c2185b, #e91e8c);
}
.service-card:hover {
    transform: translateY(-6px);
    box-shadow: 0 16px 50px rgba(155,26,75,0.14);
}
.service-icon {
    font-size: 2.5rem;
    margin-bottom: 16px;
    display: block;
}
.service-card h3 {
    font-size: 1.2rem;
    color: #6d2b45;
    margin-bottom: 10px;
}
.service-card p {
    font-size: 0.92rem;
    color: #7a4060;
    line-height: 1.65;
}
.service-price {
    margin-top: 16px;
    font-size: 0.85rem;
    color: #c2185b;
    font-weight: 700;
    letter-spacing: 1px;
}

/* ── ABOUT ── */
.about-section {
    background: linear-gradient(135deg, #fce4ec 0%, #fff8f9 100%);
    padding: 90px 60px;
}
.about-inner {
    max-width: 1100px;
    margin: 0 auto;
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 70px;
    align-items: center;
}
.about-badge {
    display: inline-block;
    background: linear-gradient(135deg, #9b1a4b, #c2185b);
    color: #fff;
    font-size: 0.78rem;
    letter-spacing: 2px;
    text-transform: uppercase;
    padding: 8px 20px;
    border-radius: 50px;
    margin-bottom: 20px;
}
.about-text h2 {
    font-size: 2.4rem;
    color: #6d2b45;
    line-height: 1.25;
    margin-bottom: 20px;
}
.about-text p {
    font-size: 1rem;
    color: #5a3048;
    line-height: 1.8;
    margin-bottom: 16px;
}
.about-credentials {
    display: flex;
    flex-direction: column;
    gap: 14px;
    margin-top: 28px;
}
.credential-item {
    display: flex;
    align-items: center;
    gap: 14px;
    background: #fff;
    padding: 14px 20px;
    border-radius: 12px;
    border-left: 4px solid #c2185b;
    box-shadow: 0 2px 10px rgba(155,26,75,0.07);
}
.credential-icon { font-size: 1.4rem; }
.credential-text {
    font-size: 0.92rem;
    color: #5a3048;
    font-weight: 500;
}
.about-visual {
    display: flex;
    flex-direction: column;
    gap: 20px;
}
.about-stat-card {
    background: #fff;
    border-radius: 16px;
    padding: 28px;
    text-align: center;
    box-shadow: 0 4px 20px rgba(155,26,75,0.08);
    border: 1px solid #fce4ec;
}
.about-stat-card .big-number {
    font-family: 'Playfair Display', serif;
    font-size: 3rem;
    font-weight: 700;
    color: #9b1a4b;
}
.about-stat-card .big-label {
    font-size: 0.85rem;
    color: #ad6383;
    letter-spacing: 2px;
    text-transform: uppercase;
    margin-top: 4px;
}
.about-quote {
    background: linear-gradient(135deg, #9b1a4b, #c2185b);
    border-radius: 16px;
    padding: 28px;
    color: #fff;
    font-style: italic;
    font-size: 1.05rem;
    line-height: 1.7;
    text-align: center;
}

/* ── FEATURE STRIPE ── */
.feature-stripe {
    background: linear-gradient(135deg, #9b1a4b 0%, #c2185b 50%, #e91e8c 100%);
    padding: 70px 60px;
    text-align: center;
}
.feature-stripe h2 {
    font-size: 2.2rem;
    color: #fff;
    margin-bottom: 16px;
}
.feature-stripe p {
    color: rgba(255,255,255,0.88);
    font-size: 1.1rem;
    max-width: 600px;
    margin: 0 auto 36px;
    line-height: 1.7;
}
.feature-pills {
    display: flex;
    flex-wrap: wrap;
    gap: 12px;
    justify-content: center;
    margin-bottom: 36px;
}
.feature-pill {
    background: rgba(255,255,255,0.15);
    border: 1px solid rgba(255,255,255,0.3);
    color: #fff;
    padding: 10px 22px;
    border-radius: 50px;
    font-size: 0.88rem;
    letter-spacing: 0.5px;
}

/* ── CONDITIONS ── */
.conditions-section {
    background: #fff;
    padding: 80px 60px;
}
.conditions-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
    gap: 20px;
    max-width: 1100px;
    margin: 0 auto;
}
.condition-card {
    background: linear-gradient(135deg, #fff8f9, #fce4ec);
    border-radius: 14px;
    padding: 24px 20px;
    text-align: center;
    border: 1px solid #f8bbd0;
    transition: transform 0.2s, box-shadow 0.2s;
}
.condition-card:hover {
    transform: translateY(-4px);
    box-shadow: 0 10px 30px rgba(155,26,75,0.12);
}
.condition-icon { font-size: 2rem; margin-bottom: 10px; }
.condition-card h4 {
    font-size: 1rem;
    color: #6d2b45;
    margin-bottom: 6px;
}
.condition-card p {
    font-size: 0.82rem;
    color: #9b6070;
    line-height: 1.5;
}

/* ── TRAINING ── */
.training-section {
    background: linear-gradient(135deg, #fff0f3 0%, #fff8f9 100%);
    padding: 80px 60px;
}
.training-inner {
    max-width: 1100px;
    margin: 0 auto;
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 60px;
    align-items: start;
}
.training-text h2 {
    font-size: 2.2rem;
    color: #6d2b45;
    margin-bottom: 18px;
}
.training-text p {
    font-size: 0.97rem;
    color: #5a3048;
    line-height: 1.8;
    margin-bottom: 14px;
}
.training-list {
    list-style: none;
    display: flex;
    flex-direction: column;
    gap: 12px;
    margin-top: 10px;
}
.training-list li {
    display: flex;
    align-items: flex-start;
    gap: 12px;
    font-size: 0.93rem;
    color: #5a3048;
    line-height: 1.6;
}
.training-list li::before {
    content: '✦';
    color: #c2185b;
    font-size: 0.9rem;
    margin-top: 2px;
    flex-shrink: 0;
}
.training-cards {
    display: flex;
    flex-direction: column;
    gap: 18px;
}
.training-card {
    background: #fff;
    border-radius: 14px;
    padding: 24px;
    border: 1px solid #fce4ec;
    box-shadow: 0 3px 15px rgba(155,26,75,0.07);
    border-left: 4px solid #c2185b;
}
.training-card h4 {
    font-size: 1rem;
    color: #6d2b45;
    margin-bottom: 8px;
}
.training-card p {
    font-size: 0.87rem;
    color: #7a4060;
    line-height: 1.6;
}

/* ── TESTIMONIALS ── */
.testimonials-section {
    background: #fff8f9;
    padding: 80px 60px;
}
.testimonials-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    gap: 28px;
    max-width: 1100px;
    margin: 0 auto;
}
.testimonial-card {
    background: #fff;
    border-radius: 20px;
    padding: 36px 28px;
    border: 1px solid #fce4ec;
    box-shadow: 0 4px 20px rgba(155,26,75,0.06);
    position: relative;
}
.testimonial-card::before {
    content: '"';
    position: absolute;
    top: 16px; left: 24px;
    font-size: 5rem;
    color: #fce4ec;
    font-family: 'Playfair Display', serif;
    line-height: 1;
}
.stars {
    color: #e91e8c;
    font-size: 1rem;
    margin-bottom: 14px;
}
.testimonial-text {
    font-size: 0.95rem;
    color: #5a3048;
    line-height: 1.75;
    font-style: italic;
    margin-bottom: 20px;
    position: relative;
    z-index: 1;
}
.testimonial-author {
    font-weight: 700;
    color: #9b1a4b;
    font-size: 0.9rem;
}
.testimonial-detail {
    font-size: 0.8rem;
    color: #ad6383;
    margin-top: 2px;
}

/* ── CONTACT ── */
.contact-section {
    background: linear-gradient(135deg, #fce4ec 0%, #fff0f3 100%);
    padding: 90px 60px;
}
.contact-inner {
    max-width: 1000px;
    margin: 0 auto;
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 60px;
    align-items: start;
}
.contact-info h2 {
    font-size: 2.2rem;
    color: #6d2b45;
    margin-bottom: 18px;
}
.contact-info p {
    font-size: 0.97rem;
    color: #5a3048;
    line-height: 1.8;
    margin-bottom: 28px;
}
.contact-items {
    display: flex;
    flex-direction: column;
    gap: 16px;
}
.contact-item {
    display: flex;
    align-items: flex-start;
    gap: 16px;
    background: #fff;
    padding: 18px 20px;
    border-radius: 14px;
    box-shadow: 0 3px 12px rgba(155,26,75,0.07);
}
.contact-item-icon {
    font-size: 1.5rem;
    flex-shrink: 0;
}
.contact-item-label {
    font-size: 0.75rem;
    letter-spacing: 2px;
    text-transform: uppercase;
    color: #c2185b;
    font-weight: 700;
    margin-bottom: 3px;
}
.contact-item-value {
    font-size: 0.97rem;
    color: #4a2035;
    font-weight: 500;
}
.contact-cta {
    background: #fff;
    border-radius: 20px;
    padding: 40px 36px;
    box-shadow: 0 8px 40px rgba(155,26,75,0.1);
    text-align: center;
}
.contact-cta h3 {
    font-size: 1.6rem;
    color: #6d2b45;
    margin-bottom: 12px;
}
.contact-cta p {
    font-size: 0.95rem;
    color: #7a4060;
    line-height: 1.7;
    margin-bottom: 28px;
}
.cta-phone {
    font-family: 'Playfair Display', serif;
    font-size: 2rem;
    color: #9b1a4b;
    font-weight: 700;
    display: block;
    margin-bottom: 8px;
    text-decoration: none;
}
.cta-hours {
    font-size: 0.85rem;
    color: #ad6383;
    letter-spacing: 1px;
    margin-bottom: 24px;
}
.btn-cta {
    display: inline-block;
    background: linear-gradient(135deg, #9b1a4b, #c2185b);
    color: #fff;
    padding: 16px 44px;
    border-radius: 50px;
    font-weight: 700;
    font-size: 1rem;
    text-decoration: none;
    letter-spacing: 1px;
    box-shadow: 0 8px 30px rgba(155,26,75,0.3);
    transition: transform 0.2s, box-shadow 0.2s;
}
.btn-cta:hover {
    transform: translateY(-3px);
    box-shadow: 0 14px 40px rgba(155,26,75,0.4);
}

/* ── FOOTER ── */
.footer {
    background: #2d0a1a;
    padding: 60px 60px 30px;
    color: #d4889e;
}
.footer-inner {
    max-width: 1100px;
    margin: 0 auto;
    display: grid;
    grid-template-columns: 2fr 1fr 1fr;
    gap: 50px;
    margin-bottom: 40px;
}
.footer-brand h3 {
    font-family: 'Playfair Display', serif;
    font-size: 1.5rem;
    color: #f8bbd0;
    margin-bottom: 10px;
}
.footer-brand p {
    font-size: 0.88rem;
    line-height: 1.7;
    color: #b07080;
}
.footer-col h4 {
    font-size: 0.8rem;
    letter-spacing: 3px;
    text-transform: uppercase;
    color: #f8bbd0;
    margin-bottom: 16px;
}
.footer-col ul {
    list-style: none;
    display: flex;
    flex-direction: column;
    gap: 8px;
}
.footer-col ul li {
    font-size: 0.88rem;
    color: #b07080;
}
.footer-bottom {
    border-top: 1px solid #4a1428;
    padding-top: 24px;
    text-align: center;
    font-size: 0.82rem;
    color: #7a3a50;
}
</style>
""", unsafe_allow_html=True)

# ── NAVBAR ────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="navbar">
    <div>
        <div class="navbar-brand">✨ Aphrodite <span>Skin Care</span></div>
        <div class="navbar-tagline">Maryville, Illinois · Est. 2006</div>
    </div>
    <ul class="nav-links">
        <li><a href="#services">Services</a></li>
        <li><a href="#about">About</a></li>
        <li><a href="#conditions">Conditions</a></li>
        <li><a href="#training">Training</a></li>
        <li><a href="#contact">Contact</a></li>
    </ul>
</div>
""", unsafe_allow_html=True)

# ── HERO ──────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="hero">
    <div class="hero-eyebrow">✦ Greater St. Louis Area · Maryville, Illinois ✦</div>
    <h1>Reveal Your Most<br><span>Radiant Skin</span></h1>
    <p class="hero-sub">
        Expert skin care by Nadiya — Master Aesthetician with over 18 years of experience
        transforming skin and building confidence.
    </p>
    <div class="hero-btns">
        <a href="tel:6187918980" class="btn-primary">📞 Book Appointment</a>
        <a href="#services" class="btn-secondary">Explore Services</a>
    </div>
</div>
""", unsafe_allow_html=True)

# ── STATS ─────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="stats-bar">
    <div class="stat-item">
        <div class="stat-number">18+</div>
        <div class="stat-label">Years Experience</div>
    </div>
    <div class="stat-item">
        <div class="stat-number">5,000+</div>
        <div class="stat-label">Clients Served</div>
    </div>
    <div class="stat-item">
        <div class="stat-number">20+</div>
        <div class="stat-label">Treatments Offered</div>
    </div>
    <div class="stat-item">
        <div class="stat-number">2006</div>
        <div class="stat-label">Established</div>
    </div>
    <div class="stat-item">
        <div class="stat-number">100%</div>
        <div class="stat-label">Dedicated to You</div>
    </div>
</div>
""", unsafe_allow_html=True)

# ── SERVICES ──────────────────────────────────────────────────────────────────
st.markdown("""
<div class="services-section" id="services">
    <div class="section-header">
        <div class="section-eyebrow">✦ What We Offer ✦</div>
        <div class="section-title">Our Signature Services</div>
        <div class="section-divider"></div>
        <div class="section-subtitle">
            From corrective treatments to luxurious relaxation, every service is
            customized to your unique skin needs.
        </div>
    </div>
    <div class="services-grid">
        <div class="service-card">
            <span class="service-icon">🌿</span>
            <h3>Custom Facials</h3>
            <p>Personalized facial treatments designed for your specific skin type and concerns — from deep cleansing to anti-aging.</p>
            <div class="service-price">Starting from $75</div>
        </div>
        <div class="service-card">
            <span class="service-icon">💎</span>
            <h3>Microdermabrasion</h3>
            <p>Advanced exfoliation that resurfaces skin, reduces fine lines, and restores a youthful, glowing complexion.</p>
            <div class="service-price">Starting from $95</div>
        </div>
        <div class="service-card">
            <span class="service-icon">⚗️</span>
            <h3>Chemical Peels</h3>
            <p>Medical-grade peels targeting hyperpigmentation, acne scars, sun damage, and uneven skin texture.</p>
            <div class="service-price">Starting from $110</div>
        </div>
        <div class="service-card">
            <span class="service-icon">✨</span>
            <h3>LED Light Therapy</h3>
            <p>Non-invasive light therapy that stimulates collagen, reduces inflammation, and accelerates skin healing.</p>
            <div class="service-price">Starting from $65</div>
        </div>
        <div class="service-card">
            <span class="service-icon">🌸</span>
            <h3>Waxing Services</h3>
            <p>Precise, gentle hair removal for face and body using premium waxes suited for sensitive skin.</p>
            <div class="service-price">Starting from $20</div>
        </div>
        <div class="service-card">
            <span class="service-icon">💆</span>
            <h3>Dermaplaning</h3>
            <p>Manual exfoliation technique that removes dead skin cells and vellus hair for a silky-smooth finish.</p>
            <div class="service-price">Starting from $85</div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# ── ABOUT ─────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="about-section" id="about">
    <div class="about-inner">
        <div class="about-text">
            <div class="about-badge">✦ Meet Your Aesthetician ✦</div>
            <h2>Nadiya — Master Aesthetician & Founder</h2>
            <p>
                With credentials as a <strong>Master Aesthetician (M.A.J)</strong> and
                <strong>Master Body Masseuse (M.B.M)</strong>, Nadiya brings an unmatched
                depth of expertise to every treatment. Since founding Aphrodite Skin Care
                in 2006, she has dedicated her career to helping clients achieve their
                healthiest, most radiant skin.
            </p>
            <p>
                Nadiya's approach blends the science of skin biology with the art of
                personalized care. She continuously advances her knowledge through
                ongoing education, ensuring her clients always receive the most
                effective, up-to-date treatments available.
            </p>
            <p>
                Located in Maryville, Illinois, Aphrodite Skin Care proudly serves
                clients throughout the Greater St. Louis area in a serene, welcoming
                environment designed for total relaxation and transformation.
            </p>
            <div class="about-credentials">
                <div class="credential-item">
                    <span class="credential-icon">🎓</span>
                    <span class="credential-text">Master Aesthetician — M.A.J Certified</span>
                </div>
                <div class="credential-item">
                    <span class="credential-icon">💆</span>
                    <span class="credential-text">Master Body Masseuse — M.B.M Certified</span>
                </div>
                <div class="credential-item">
                    <span class="credential-icon">📅</span>
                    <span class="credential-text">18+ Years in Practice — Est. 2006</span>
                </div>
                <div class="credential-item">
                    <span class="credential-icon">📍</span>
                    <span class="credential-text">Serving Greater St. Louis from Maryville, IL</span>
                </div>
            </div>
        </div>
        <div class="about-visual">
            <div class="about-stat-card">
                <div class="big-number">18+</div>
                <div class="big-label">Years of Expertise</div>
            </div>
            <div class="about-stat-card">
                <div class="big-number">M.A.J</div>
                <div class="big-label">Master Aesthetician</div>
            </div>
            <div class="about-stat-card">
                <div class="big-number">M.B.M</div>
                <div class="big-label">Master Body Masseuse</div>
            </div>
            <div class="about-quote">
                "My passion is helping every client feel confident and beautiful
                in their own skin. Skin care is not just a treatment — it's
                a journey we take together."
                <br><br>— Nadiya, Founder
            </div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# ── FEATURE STRIPE ────────────────────────────────────────────────────────────
st.markdown("""
<div class="feature-stripe">
    <h2>✨ Why Choose Aphrodite Skin Care?</h2>
    <p>
        We combine advanced techniques with a deeply personal approach —
        because your skin deserves nothing less than expert, compassionate care.
    </p>
    <div class="feature-pills">
        <span class="feature-pill">🏆 18+ Years Experience</span>
        <span class="feature-pill">🔬 Medical-Grade Treatments</span>
        <span class="feature-pill">💖 Personalized Consultations</span>
        <span class="feature-pill">🌿 Clean, Safe Products</span>
        <span class="feature-pill">📍 Convenient Location</span>
        <span class="feature-pill">✦ Ongoing Education</span>
        <span class="feature-pill">😌 Relaxing Environment</span>
        <span class="feature-pill">⭐ 5-Star Client Reviews</span>
    </div>
    <a href="tel:6187918980" class="btn-primary">Call Now: 618-791-8980</a>
</div>
""", unsafe_allow_html=True)

# ── CONDITIONS ────────────────────────────────────────────────────────────────
st.markdown("""
<div class="conditions-section" id="conditions">
    <div class="section-header">
        <div class="section-eyebrow">✦ Skin Concerns We Address ✦</div>
        <div class="section-title">Conditions We Treat</div>
        <div class="section-divider"></div>
        <div class="section-subtitle">
            Nadiya specializes in a wide range of skin conditions, providing
            targeted, effective solutions for every concern.
        </div>
    </div>
    <div class="conditions-grid">
        <div class="condition-card">
            <div class="condition-icon">🔴</div>
            <h4>Acne & Breakouts</h4>
            <p>Targeted treatments to clear, calm, and prevent acne at every stage.</p>
        </div>
        <div class="condition-card">
            <div class="condition-icon">🌙</div>
            <h4>Hyperpigmentation</h4>
            <p>Brightening protocols to fade dark spots, melasma, and uneven tone.</p>
        </div>
        <div class="condition-card">
            <div class="condition-icon">⏳</div>
            <h4>Aging & Fine Lines</h4>
            <p>Anti-aging therapies to smooth wrinkles and restore youthful firmness.</p>
        </div>
        <div class="condition-card">
            <div class="condition-icon">🌊</div>
            <h4>Dehydrated Skin</h4>
            <p>Deep hydration treatments that restore moisture balance and glow.</p>
        </div>
        <div class="condition-card">
            <div class="condition-icon">🌸</div>
            <h4>Rosacea & Redness</h4>
            <p>Gentle, calming therapies to reduce redness and soothe sensitive skin.</p>
        </div>
        <div class="condition-card">
            <div class="condition-icon">☀️</div>
            <h4>Sun Damage</h4>
            <p>Corrective treatments to reverse UV damage and restore skin clarity.</p>
        </div>
        <div class="condition-card">
            <div class="condition-icon">💧</div>
            <h4>Oily & Congested Skin</h4>
            <p>Deep cleansing and balancing treatments to control oil and minimize pores.</p>
        </div>
        <div class="condition-card">
            <div class="condition-icon">🌿</div>
            <h4>Sensitive Skin</h4>
            <p>Soothing, hypoallergenic treatments tailored for reactive skin types.</p>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# ── TRAINING ──────────────────────────────────────────────────────────────────
st.markdown("""
<div class="training-section" id="training">
    <div class="training-inner">
        <div class="training-text">
            <div class="section-eyebrow">✦ Education & Mentorship ✦</div>
            <h2>Professional Training Programs</h2>
            <p>
                Nadiya is passionate about elevating the next generation of skin care
                professionals. Through personalized mentorship and hands-on training,
                she shares 18+ years of knowledge and expertise.
            </p>
            <p>
                Whether you're a newly licensed aesthetician or an experienced
                professional looking to expand your skills, Aphrodite Skin Care
                offers training programs designed to accelerate your growth.
            </p>
            <ul class="training-list">
                <li>One-on-one mentorship with a Master Aesthetician</li>
                <li>Hands-on training with real clients and live demonstrations</li>
                <li>Advanced chemical peel and microdermabrasion techniques</li>
                <li>Business development and client consultation skills</li>
                <li>Product knowledge and skin analysis training</li>
                <li>Flexible scheduling to fit your professional goals</li>
            </ul>
        </div>
        <div class="training-cards">
            <div class="training-card">
                <h4>🎓 Aesthetician Mentorship</h4>
                <p>Personalized one-on-one mentorship program for licensed aestheticians seeking to deepen their skills and confidence.</p>
            </div>
            <div class="training-card">
                <h4>⚗️ Advanced Peel Training</h4>
                <p>Comprehensive training in medical-grade chemical peels, contraindications, and client aftercare protocols.</p>
            </div>
            <div class="training-card">
                <h4>💎 Microdermabrasion Certification</h4>
                <p>Hands-on training in professional microdermabrasion techniques for optimal skin resurfacing results.</p>
            </div>
            <div class="training-card">
                <h4>💼 Business & Client Skills</h4>
                <p>Learn how to build a loyal client base, conduct thorough consultations, and grow your aesthetic practice.</p>
            </div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# ── TESTIMONIALS ──────────────────────────────────────────────────────────────
st.markdown("""
<div class="testimonials-section" id="testimonials">
    <div class="section-header">
        <div class="section-eyebrow">✦ Client Stories ✦</div>
        <div class="section-title">What Our Clients Say</div>
        <div class="section-divider"></div>
    </div>
    <div class="testimonials-grid">
        <div class="testimonial-card">
            <div class="stars">★★★★★</div>
            <div class="testimonial-text">
                "Nadiya is absolutely incredible. My skin has never looked better.
                After just three sessions, my hyperpigmentation has faded dramatically.
                She truly cares about her clients and it shows in every treatment."
            </div>
            <div class="testimonial-author">Sarah M.</div>
            <div class="testimonial-detail">Client since 2019 · Chemical Peel Series</div>
        </div>
        <div class="testimonial-card">
            <div class="stars">★★★★★</div>
            <div class="testimonial-text">
                "I drove from St. Louis just to see Nadiya and it was 100% worth it.
                Her expertise is unmatched. My acne-prone skin has completely
                transformed. I won't trust anyone else with my skin."
            </div>
            <div class="testimonial-author">Jessica T.</div>
            <div class="testimonial-detail">Client since 2021 · Custom Facial Program</div>
        </div>
        <div class="testimonial-card">
            <div class="stars">★★★★★</div>
            <div class="testimonial-text">
                "As a fellow aesthetician, I sought out Nadiya for her training
                program. Her knowledge is extraordinary and her teaching style
                is warm and thorough. Highly recommend for any professional."
            </div>
            <div class="testimonial-author">Amanda R.</div>
            <div class="testimonial-detail">Licensed Aesthetician · Training Graduate</div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# ── CONTACT ───────────────────────────────────────────────────────────────────
st.markdown("""
<div class="contact-section" id="contact">
    <div class="contact-inner">
        <div class="contact-info">
            <div class="section-eyebrow">✦ Get In Touch ✦</div>
            <h2>Visit Aphrodite Skin Care</h2>
            <p>
                Ready to begin your skin transformation? We'd love to welcome you
                to our studio. Call to schedule your personalized consultation today.
            </p>
            <div class="contact-items">
                <div class="contact-item">
                    <span class="contact-item-icon">📞</span>
                    <div>
                        <div class="contact-item-label">Phone</div>
                        <div class="contact-item-value">618-791-8980</div>
                    </div>
                </div>
                <div class="contact-item">
                    <span class="contact-item-icon">📍</span>
                    <div>
                        <div class="contact-item-label">Address</div>
                        <div class="contact-item-value">4 Oak Drive, Suite B<br>Maryville, Illinois</div>
                    </div>
                </div>
                <div class="contact-item">
                    <span class="contact-item-icon">🌐</span>
                    <div>
                        <div class="contact-item-label">Website</div>
                        <div class="contact-item-value">aphroditesc.com</div>
                    </div>
                </div>
                <div class="contact-item">
                    <span class="contact-item-icon">🗺️</span>
                    <div>
                        <div class="contact-item-label">Area Served</div>
                        <div class="contact-item-value">Greater St. Louis Metropolitan Area</div>
                    </div>
                </div>
            </div>
        </div>
        <div class="contact-cta">
            <h3>Book Your Appointment</h3>
            <p>
                Call us today to schedule your personalized skin care consultation
                with Nadiya. New clients are always welcome!
            </p>
            <a href="tel:6187918980" class="cta-phone">618-791-8980</a>
            <div class="cta-hours">Call or Text · By Appointment</div>
            <a href="tel:6187918980" class="btn-cta">📞 Call Now</a>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# ── FOOTER ────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="footer">
    <div class="footer-inner">
        <div class="footer-brand">
            <h3>✨ Aphrodite Skin Care</h3>
            <p>
                Expert skin care by Nadiya, Master Aesthetician (M.A.J, M.B.M).
                Serving the Greater St. Louis area from Maryville, Illinois since 2006.
            </p>
        </div>
        <div class="footer-col">
            <h4>Services</h4>
            <ul>
                <li>Custom Facials</li>
                <li>Microdermabrasion</li>
                <li>Chemical Peels</li>
                <li>LED Light Therapy</li>
                <li>Dermaplaning</li>
                <li>Waxing</li>
            </ul>
        </div>
        <div class="footer-col">
            <h4>Contact</h4>
            <ul>
                <li>618-791-8980</li>
                <li>4 Oak Drive, Suite B</li>
                <li>Maryville, Illinois</li>
                <li>aphroditesc.com</li>
            </ul>
        </div>
    </div>
    <div class="footer-bottom">
        © 2024 Aphrodite Skin Care · Maryville, Illinois · All Rights Reserved
        · Designed with ✨ for radiant skin
    </div>
</div>
""", unsafe_allow_html=True)
