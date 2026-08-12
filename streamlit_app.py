import streamlit as st

st.set_page_config(
    page_title="Aphrodite Skin Care",
    page_icon="✨",
    layout="wide"
)

st.markdown("""
<style>
    /* ── Global Reset & Base ── */
    @import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@300;400;600;700&family=Lato:wght@300;400;700&display=swap');

    html, body, [class*="css"] {
        font-family: 'Lato', sans-serif;
        background-color: #fdf6f0;
        color: #3a2a2a;
    }
    .block-container { padding: 0 !important; max-width: 100% !important; }
    h1, h2, h3 { font-family: 'Cormorant Garamond', serif; }

    /* ── Header Bar ── */
    .header-bar {
        background: #fff;
        padding: 18px 60px;
        display: flex;
        align-items: center;
        gap: 20px;
        border-bottom: 3px solid #c2185b;
        box-shadow: 0 2px 12px rgba(194,24,91,0.08);
    }
    .header-bar img.logo-img {
        height: 70px;
        width: auto;
    }
    .header-title {
        display: flex;
        flex-direction: column;
    }
    .header-title h1 {
        font-family: 'Cormorant Garamond', serif;
        font-size: 2.4rem;
        color: #9b1a4b;
        margin: 0;
        letter-spacing: 3px;
        text-transform: uppercase;
    }
    .header-title p {
        font-size: 0.95rem;
        color: #c2185b;
        margin: 0;
        font-style: italic;
        letter-spacing: 1px;
    }

    /* ── Hero Section ── */
    .hero-section {
        background: linear-gradient(135deg, #9b1a4b 0%, #c2185b 40%, #e91e8c 100%);
        padding: 80px 60px;
        text-align: center;
        position: relative;
        overflow: hidden;
    }
    .hero-section::before {
        content: '';
        position: absolute;
        top: -50%;
        left: -50%;
        width: 200%;
        height: 200%;
        background: radial-gradient(circle, rgba(255,255,255,0.05) 0%, transparent 60%);
    }
    .hero-section h1 {
        font-family: 'Cormorant Garamond', serif;
        font-size: 3.8rem;
        color: #fff;
        margin-bottom: 10px;
        letter-spacing: 4px;
        text-shadow: 0 2px 20px rgba(0,0,0,0.2);
    }
    .hero-section p {
        font-size: 1.3rem;
        color: rgba(255,255,255,0.9);
        max-width: 700px;
        margin: 0 auto 30px;
        line-height: 1.8;
    }
    .hero-badge {
        display: inline-block;
        background: rgba(255,255,255,0.15);
        border: 1px solid rgba(255,255,255,0.4);
        color: #fff;
        padding: 8px 20px;
        border-radius: 30px;
        font-size: 0.9rem;
        letter-spacing: 2px;
        margin-bottom: 30px;
        backdrop-filter: blur(5px);
    }
    .cta-button {
        display: inline-block;
        background: #fff;
        color: #9b1a4b;
        padding: 16px 45px;
        border-radius: 50px;
        font-size: 1.1rem;
        font-weight: 700;
        text-decoration: none;
        letter-spacing: 1px;
        box-shadow: 0 8px 30px rgba(0,0,0,0.2);
        transition: all 0.3s;
        cursor: pointer;
        border: none;
    }
    .cta-button:hover {
        background: #f8bbd9;
        transform: translateY(-2px);
    }

    /* ── Stats Bar ── */
    .stats-bar {
        background: #fff;
        padding: 30px 60px;
        display: flex;
        justify-content: space-around;
        align-items: center;
        border-bottom: 1px solid #f0d0e0;
        box-shadow: 0 4px 15px rgba(155,26,75,0.07);
    }
    .stat-item {
        text-align: center;
    }
    .stat-number {
        font-family: 'Cormorant Garamond', serif;
        font-size: 2.8rem;
        color: #9b1a4b;
        font-weight: 700;
        line-height: 1;
    }
    .stat-label {
        font-size: 0.85rem;
        color: #888;
        letter-spacing: 1.5px;
        text-transform: uppercase;
        margin-top: 4px;
    }
    .stat-divider {
        width: 1px;
        height: 50px;
        background: #f0d0e0;
    }

    /* ── Section Styles ── */
    .section-wrapper {
        padding: 70px 60px;
    }
    .section-wrapper-alt {
        padding: 70px 60px;
        background: #fff;
    }
    .section-header {
        text-align: center;
        margin-bottom: 50px;
    }
    .section-header h2 {
        font-family: 'Cormorant Garamond', serif;
        font-size: 2.6rem;
        color: #9b1a4b;
        letter-spacing: 2px;
        margin-bottom: 10px;
    }
    .section-header p {
        color: #888;
        font-size: 1rem;
        letter-spacing: 1px;
        text-transform: uppercase;
    }
    .section-divider {
        width: 60px;
        height: 3px;
        background: linear-gradient(90deg, #9b1a4b, #e91e8c);
        margin: 15px auto 0;
        border-radius: 2px;
    }

    /* ── Service Cards ── */
    .service-grid {
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        gap: 25px;
        margin-top: 20px;
    }
    .service-card {
        background: #fff;
        border-radius: 16px;
        padding: 35px 25px;
        text-align: center;
        box-shadow: 0 4px 20px rgba(155,26,75,0.08);
        border-top: 4px solid #c2185b;
        transition: transform 0.3s, box-shadow 0.3s;
    }
    .service-card:hover {
        transform: translateY(-6px);
        box-shadow: 0 12px 35px rgba(155,26,75,0.15);
    }
    .service-icon {
        font-size: 2.5rem;
        margin-bottom: 15px;
    }
    .service-card h3 {
        font-family: 'Cormorant Garamond', serif;
        font-size: 1.4rem;
        color: #9b1a4b;
        margin-bottom: 10px;
    }
    .service-card p {
        color: #666;
        font-size: 0.9rem;
        line-height: 1.7;
    }

    /* ── About Section ── */
    .about-grid {
        display: grid;
        grid-template-columns: 1fr 2fr;
        gap: 60px;
        align-items: center;
    }
    .about-image-wrapper {
        text-align: center;
        position: relative;
    }
    .about-image-wrapper img {
        width: 260px;
        height: 260px;
        border-radius: 50%;
        object-fit: cover;
        border: 6px solid #c2185b;
        box-shadow: 0 10px 40px rgba(155,26,75,0.25);
    }
    .about-badge {
        display: inline-block;
        background: linear-gradient(135deg, #9b1a4b, #c2185b);
        color: #fff;
        padding: 8px 20px;
        border-radius: 20px;
        font-size: 0.8rem;
        letter-spacing: 1px;
        margin-top: 15px;
        text-transform: uppercase;
    }
    .about-content h2 {
        font-family: 'Cormorant Garamond', serif;
        font-size: 2.5rem;
        color: #9b1a4b;
        margin-bottom: 5px;
    }
    .about-content .credentials {
        color: #c2185b;
        font-size: 1rem;
        letter-spacing: 2px;
        margin-bottom: 20px;
        font-weight: 600;
    }
    .about-content p {
        color: #555;
        line-height: 1.9;
        font-size: 1rem;
        margin-bottom: 15px;
    }
    .credential-tags {
        display: flex;
        flex-wrap: wrap;
        gap: 10px;
        margin-top: 20px;
    }
    .cred-tag {
        background: #fce4ec;
        color: #9b1a4b;
        padding: 6px 16px;
        border-radius: 20px;
        font-size: 0.82rem;
        font-weight: 600;
        letter-spacing: 0.5px;
    }

    /* ── Gallery Section ── */
    .gallery-grid {
        display: grid;
        grid-template-columns: 1fr 1fr 1fr;
        gap: 20px;
        margin-top: 20px;
    }
    .gallery-item {
        border-radius: 14px;
        overflow: hidden;
        box-shadow: 0 6px 25px rgba(155,26,75,0.12);
        transition: transform 0.3s;
    }
    .gallery-item:hover {
        transform: scale(1.02);
    }
    .gallery-item img {
        width: 100%;
        height: 250px;
        object-fit: cover;
        display: block;
    }
    .gallery-item.wide {
        grid-column: span 2;
    }
    .gallery-item.wide img {
        height: 280px;
    }
    .gallery-caption {
        background: #fff;
        padding: 12px 16px;
        font-size: 0.85rem;
        color: #9b1a4b;
        font-weight: 600;
        letter-spacing: 0.5px;
        text-align: center;
    }

    /* ── Feature Stripe ── */
    .feature-stripe {
        background: linear-gradient(135deg, #9b1a4b 0%, #c2185b 100%);
        padding: 60px;
        text-align: center;
        color: #fff;
    }
    .feature-stripe h2 {
        font-family: 'Cormorant Garamond', serif;
        font-size: 2.4rem;
        margin-bottom: 15px;
        letter-spacing: 2px;
    }
    .feature-stripe p {
        font-size: 1.1rem;
        opacity: 0.9;
        max-width: 700px;
        margin: 0 auto 30px;
        line-height: 1.8;
    }
    .feature-items {
        display: flex;
        justify-content: center;
        gap: 40px;
        flex-wrap: wrap;
        margin-top: 30px;
    }
    .feature-item {
        background: rgba(255,255,255,0.12);
        border: 1px solid rgba(255,255,255,0.25);
        border-radius: 12px;
        padding: 20px 30px;
        min-width: 160px;
        backdrop-filter: blur(5px);
    }
    .feature-item .fi-icon { font-size: 2rem; margin-bottom: 8px; }
    .feature-item .fi-label {
        font-size: 0.85rem;
        letter-spacing: 1px;
        text-transform: uppercase;
        opacity: 0.9;
    }

    /* ── Conditions Grid ── */
    .conditions-grid {
        display: grid;
        grid-template-columns: repeat(4, 1fr);
        gap: 15px;
    }
    .condition-pill {
        background: linear-gradient(135deg, #fce4ec, #fff);
        border: 1px solid #f8bbd9;
        border-radius: 10px;
        padding: 16px 12px;
        text-align: center;
        font-size: 0.9rem;
        color: #9b1a4b;
        font-weight: 600;
        box-shadow: 0 2px 10px rgba(155,26,75,0.06);
        transition: all 0.3s;
    }
    .condition-pill:hover {
        background: linear-gradient(135deg, #9b1a4b, #c2185b);
        color: #fff;
        transform: translateY(-3px);
    }
    .condition-pill .cp-icon { font-size: 1.4rem; margin-bottom: 6px; }

    /* ── Training Academy ── */
    .academy-box {
        background: linear-gradient(135deg, #1a0a12, #3d0a22);
        border-radius: 20px;
        padding: 60px;
        color: #fff;
        position: relative;
        overflow: hidden;
    }
    .academy-box::before {
        content: '🎓';
        position: absolute;
        font-size: 15rem;
        opacity: 0.04;
        right: -30px;
        top: -30px;
    }
    .academy-box h2 {
        font-family: 'Cormorant Garamond', serif;
        font-size: 2.4rem;
        color: #f8bbd9;
        margin-bottom: 15px;
        letter-spacing: 2px;
    }
    .academy-box p {
        color: rgba(255,255,255,0.8);
        line-height: 1.9;
        font-size: 1rem;
        max-width: 700px;
        margin-bottom: 30px;
    }
    .academy-programs {
        display: flex;
        gap: 20px;
        flex-wrap: wrap;
        margin-top: 10px;
    }
    .program-card {
        background: rgba(255,255,255,0.08);
        border: 1px solid rgba(248,187,217,0.3);
        border-radius: 14px;
        padding: 25px 30px;
        flex: 1;
        min-width: 200px;
    }
    .program-card h4 {
        color: #f8bbd9;
        font-family: 'Cormorant Garamond', serif;
        font-size: 1.3rem;
        margin-bottom: 8px;
    }
    .program-card p {
        font-size: 0.85rem;
        color: rgba(255,255,255,0.7);
        margin: 0;
    }

    /* ── Testimonial ── */
    .testimonial-box {
        background: #fff;
        border-radius: 20px;
        padding: 50px 60px;
        text-align: center;
        box-shadow: 0 8px 40px rgba(155,26,75,0.1);
        border-left: 6px solid #c2185b;
        max-width: 800px;
        margin: 0 auto;
    }
    .testimonial-box .quote {
        font-family: 'Cormorant Garamond', serif;
        font-size: 1.6rem;
        color: #3a2a2a;
        line-height: 1.8;
        font-style: italic;
        margin-bottom: 20px;
    }
    .testimonial-box .quote::before { content: '\\201C'; color: #c2185b; font-size: 2rem; }
    .testimonial-box .quote::after  { content: '\\201D'; color: #c2185b; font-size: 2rem; }
    .testimonial-author {
        color: #9b1a4b;
        font-weight: 700;
        font-size: 0.95rem;
        letter-spacing: 1px;
        text-transform: uppercase;
    }
    .stars { color: #f4c542; font-size: 1.3rem; margin-bottom: 10px; }

    /* ── Contact Box ── */
    .contact-grid {
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 40px;
        align-items: start;
    }
    .contact-info-box {
        background: #fff;
        border-radius: 16px;
        padding: 40px;
        box-shadow: 0 6px 30px rgba(155,26,75,0.1);
    }
    .contact-info-box h3 {
        font-family: 'Cormorant Garamond', serif;
        font-size: 1.8rem;
        color: #9b1a4b;
        margin-bottom: 25px;
    }
    .contact-item {
        display: flex;
        align-items: flex-start;
        gap: 15px;
        margin-bottom: 20px;
        padding-bottom: 20px;
        border-bottom: 1px solid #fce4ec;
    }
    .contact-item:last-child { border-bottom: none; }
    .contact-icon {
        font-size: 1.5rem;
        width: 45px;
        height: 45px;
        background: #fce4ec;
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        flex-shrink: 0;
    }
    .contact-detail strong {
        display: block;
        color: #9b1a4b;
        font-size: 0.8rem;
        letter-spacing: 1.5px;
        text-transform: uppercase;
        margin-bottom: 3px;
    }
    .contact-detail span {
        color: #555;
        font-size: 1rem;
    }
    .building-img-box {
        border-radius: 16px;
        overflow: hidden;
        box-shadow: 0 8px 35px rgba(155,26,75,0.15);
    }
    .building-img-box img {
        width: 100%;
        height: 100%;
        object-fit: cover;
        display: block;
        min-height: 350px;
    }

    /* ── Footer ── */
    .footer {
        background: #1a0a12;
        color: rgba(255,255,255,0.7);
        text-align: center;
        padding: 40px 60px;
    }
    .footer .footer-logo {
        font-family: 'Cormorant Garamond', serif;
        font-size: 1.8rem;
        color: #f8bbd9;
        letter-spacing: 3px;
        margin-bottom: 8px;
    }
    .footer .footer-tagline {
        font-size: 0.85rem;
        color: rgba(255,255,255,0.5);
        letter-spacing: 1px;
        font-style: italic;
        margin-bottom: 20px;
    }
    .footer .footer-copy {
        font-size: 0.8rem;
        color: rgba(255,255,255,0.35);
        border-top: 1px solid rgba(255,255,255,0.1);
        padding-top: 20px;
        margin-top: 15px;
    }
</style>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────────
# HEADER BAR WITH LOGO
# ─────────────────────────────────────────────
col_logo, col_title = st.columns([1, 5])
with col_logo:
    st.image("aphrodite_logo_figure.png", width=80)
with col_title:
    st.markdown("""
    <div class="header-title" style="padding-top:10px;">
        <h1 style="font-family:'Cormorant Garamond',serif;font-size:2.2rem;
                   color:#9b1a4b;letter-spacing:3px;text-transform:uppercase;margin:0;">
            Aphrodite Skin Care LLC
        </h1>
        <p style="color:#c2185b;font-style:italic;margin:0;font-size:0.95rem;">
            Great Skin starts with Great SKIN CARE
        </p>
    </div>
    """, unsafe_allow_html=True)

# ─────────────────────────────────────────────
# HERO
# ─────────────────────────────────────────────
st.markdown("""
<div class="hero-section">
    <div class="hero-badge">✨ Established 2006 · Maryville, Illinois · Greater St. Louis</div>
    <h1>Reveal Your Most<br>Beautiful Skin</h1>
    <p>Advanced skin care, permanent cosmetics, and transformative treatments
       by Master Esthetician Nadiya — over 18 years of expertise.</p>
    <a href="tel:6187918980" class="cta-button">📞 Book Your Appointment</a>
</div>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────────
# STATS BAR
# ─────────────────────────────────────────────
st.markdown("""
<div class="stats-bar">
    <div class="stat-item">
        <div class="stat-number">18+</div>
        <div class="stat-label">Years of Excellence</div>
    </div>
    <div class="stat-divider"></div>
    <div class="stat-item">
        <div class="stat-number">1000s</div>
        <div class="stat-label">Clients Served</div>
    </div>
    <div class="stat-divider"></div>
    <div class="stat-item">
        <div class="stat-number">20+</div>
        <div class="stat-label">Skin Conditions Treated</div>
    </div>
    <div class="stat-divider"></div>
    <div class="stat-item">
        <div class="stat-number">2</div>
        <div class="stat-label">Academy Programs</div>
    </div>
    <div class="stat-divider"></div>
    <div class="stat-item">
        <div class="stat-number">★ 5.0</div>
        <div class="stat-label">Client Rating</div>
    </div>
</div>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────────
# SERVICES
# ─────────────────────────────────────────────
st.markdown("""
<div class="section-wrapper">
    <div class="section-header">
        <p>What We Offer</p>
        <h2>Our Signature Services</h2>
        <div class="section-divider"></div>
    </div>
    <div class="service-grid">
        <div class="service-card">
            <div class="service-icon">💆</div>
            <h3>Advanced Facials</h3>
            <p>Customized facial treatments targeting your unique skin concerns for a radiant, healthy glow.</p>
        </div>
        <div class="service-card">
            <div class="service-icon">💄</div>
            <h3>Permanent Cosmetics</h3>
            <p>Wake up beautiful every day with expertly applied permanent makeup by a certified instructor.</p>
        </div>
        <div class="service-card">
            <div class="service-icon">🎨</div>
            <h3>Scalp Micropigmentation</h3>
            <p>Cutting-edge scalp treatments that restore confidence and create the appearance of fuller hair.</p>
        </div>
        <div class="service-card">
            <div class="service-icon">✨</div>
            <h3>Chemical Peels</h3>
            <p>Professional-grade peels to resurface, brighten, and renew your complexion at every depth.</p>
        </div>
        <div class="service-card">
            <div class="service-icon">🌿</div>
            <h3>Skin Rejuvenation</h3>
            <p>Holistic and clinical approaches to reverse aging signs and restore youthful vitality.</p>
        </div>
        <div class="service-card">
            <div class="service-icon">🔬</div>
            <h3>Medical-Grade Treatments</h3>
            <p>Evidence-based, results-driven protocols for challenging skin conditions and concerns.</p>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────────
# ABOUT NADIYA
# ─────────────────────────────────────────────
st.markdown('<div class="section-wrapper-alt">', unsafe_allow_html=True)
st.markdown("""
<div class="section-header">
    <p>Meet Your Expert</p>
    <h2>About Nadiya</h2>
    <div class="section-divider"></div>
</div>
""", unsafe_allow_html=True)

col_img, col_bio = st.columns([1, 2])
with col_img:
    st.image("nadiya_headshot.png", width=260,
             caption="Nadiya · Master Esthetician & Permanent Cosmetics Instructor")
    st.markdown("""
    <div style="text-align:center;margin-top:10px;">
        <span class="about-badge" style="background:linear-gradient(135deg,#9b1a4b,#c2185b);
              color:#fff;padding:8px 20px;border-radius:20px;font-size:0.8rem;
              letter-spacing:1px;text-transform:uppercase;display:inline-block;">
            Master Esthetician
        </span>
    </div>
    <div style="text-align:center;margin-top:8px;">
        <span style="background:#fce4ec;color:#9b1a4b;padding:6px 16px;border-radius:20px;
              font-size:0.82rem;font-weight:600;display:inline-block;margin:4px;">
            M.A.J
        </span>
        <span style="background:#fce4ec;color:#9b1a4b;padding:6px 16px;border-radius:20px;
              font-size:0.82rem;font-weight:600;display:inline-block;margin:4px;">
            M.B.M
        </span>
        <span style="background:#fce4ec;color:#9b1a4b;padding:6px 16px;border-radius:20px;
              font-size:0.82rem;font-weight:600;display:inline-block;margin:4px;">
            Est. 2006
        </span>
    </div>
    """, unsafe_allow_html=True)

with col_bio:
    st.markdown("""
    <div style="padding-top:20px;">
        <h2 style="font-family:'Cormorant Garamond',serif;font-size:2.4rem;
                   color:#9b1a4b;margin-bottom:5px;">Nadiya</h2>
        <p style="color:#c2185b;font-size:1rem;letter-spacing:2px;
                  font-weight:600;margin-bottom:20px;">
            M.A.J · M.B.M · Master Esthetician & Permanent Cosmetics Instructor
        </p>
        <p style="color:#555;line-height:1.9;font-size:1rem;margin-bottom:15px;">
            With over <strong>18 years of dedicated expertise</strong>, Nadiya is the heart and soul
            of Aphrodite Skin Care. As a <strong>Master Esthetician</strong> and certified
            <strong>Permanent Cosmetics Instructor</strong>, she brings an unmatched depth of
            knowledge to every client interaction.
        </p>
        <p style="color:#555;line-height:1.9;font-size:1rem;margin-bottom:15px;">
            Nadiya founded Aphrodite Skin Care LLC in 2006 with a singular mission:
            to deliver transformative, results-driven skin care in a warm, professional environment.
            Her approach combines the latest clinical techniques with a deeply personal touch,
            ensuring every client feels seen, valued, and cared for.
        </p>
        <p style="color:#555;line-height:1.9;font-size:1rem;">
            Beyond her practice, Nadiya is passionate about education — training the next
            generation of estheticians through her professional academy programs in
            Permanent Cosmetics and Scalp Micropigmentation.
        </p>
        <div style="display:flex;flex-wrap:wrap;gap:10px;margin-top:20px;">
            <span style="background:#fce4ec;color:#9b1a4b;padding:8px 18px;border-radius:20px;
                  font-size:0.85rem;font-weight:600;">🎓 Master Esthetician</span>
            <span style="background:#fce4ec;color:#9b1a4b;padding:8px 18px;border-radius:20px;
                  font-size:0.85rem;font-weight:600;">💄 Permanent Cosmetics Instructor</span>
            <span style="background:#fce4ec;color:#9b1a4b;padding:8px 18px;border-radius:20px;
                  font-size:0.85rem;font-weight:600;">🎨 Scalp Micropigmentation Expert</span>
            <span style="background:#fce4ec;color:#9b1a4b;padding:8px 18px;border-radius:20px;
                  font-size:0.85rem;font-weight:600;">📍 Serving Greater St. Louis</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# ─────────────────────────────────────────────
# OUR SPACE GALLERY
# ─────────────────────────────────────────────
st.markdown("""
<div class="section-wrapper">
    <div class="section-header">
        <p>Come Visit Us</p>
        <h2>Our Beautiful Space</h2>
        <div class="section-divider"></div>
    </div>
</div>
""", unsafe_allow_html=True)

col_g1, col_g2 = st.columns([2, 1])
with col_g1:
    st.image("interior_waiting.png", use_container_width=True,
             caption="🛋️ Our Welcoming Waiting Area & Reception")
with col_g2:
    st.image("building_exterior.png", use_container_width=True,
             caption="🏢 4 Oak Drive, Suite B · Maryville, IL")
    st.image("building_sign.png", use_container_width=True,
             caption="📍 Aphrodite Skin Care · Permanent Cosmetics")

# ─────────────────────────────────────────────
# FEATURE STRIPE
# ─────────────────────────────────────────────
st.markdown("""
<div class="feature-stripe">
    <h2>Why Choose Aphrodite Skin Care?</h2>
    <p>We combine clinical expertise with a luxurious, personalized experience —
       because you deserve both results and comfort.</p>
    <div class="feature-items">
        <div class="feature-item">
            <div class="fi-icon">🏆</div>
            <div class="fi-label">18+ Years Expert Care</div>
        </div>
        <div class="feature-item">
            <div class="fi-icon">🔬</div>
            <div class="fi-label">Medical-Grade Products</div>
        </div>
        <div class="feature-item">
            <div class="fi-icon">💎</div>
            <div class="fi-label">Luxury Experience</div>
        </div>
        <div class="feature-item">
            <div class="fi-icon">🎓</div>
            <div class="fi-label">Certified Instructor</div>
        </div>
        <div class="feature-item">
            <div class="fi-icon">💖</div>
            <div class="fi-label">Personalized Care</div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────────
# CONDITIONS TREATED
# ─────────────────────────────────────────────
st.markdown("""
<div class="section-wrapper-alt">
    <div class="section-header">
        <p>We Specialize In</p>
        <h2>Skin Conditions We Treat</h2>
        <div class="section-divider"></div>
    </div>
    <div class="conditions-grid">
        <div class="condition-pill"><div class="cp-icon">🌸</div>Acne & Breakouts</div>
        <div class="condition-pill"><div class="cp-icon">☀️</div>Sun Damage</div>
        <div class="condition-pill"><div class="cp-icon">🕐</div>Anti-Aging</div>
        <div class="condition-pill"><div class="cp-icon">🔴</div>Rosacea</div>
        <div class="condition-pill"><div class="cp-icon">💧</div>Dry / Dehydrated Skin</div>
        <div class="condition-pill"><div class="cp-icon">🌙</div>Hyperpigmentation</div>
        <div class="condition-pill"><div class="cp-icon">⚡</div>Sensitive Skin</div>
        <div class="condition-pill"><div class="cp-icon">✨</div>Uneven Skin Tone</div>
        <div class="condition-pill"><div class="cp-icon">🌿</div>Oily Skin</div>
        <div class="condition-pill"><div class="cp-icon">💫</div>Fine Lines & Wrinkles</div>
        <div class="condition-pill"><div class="cp-icon">🔵</div>Dark Circles</div>
        <div class="condition-pill"><div class="cp-icon">🌺</div>Enlarged Pores</div>
    </div>
</div>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────────
# TRAINING ACADEMY
# ─────────────────────────────────────────────
st.markdown('<div class="section-wrapper">', unsafe_allow_html=True)
st.markdown("""
<div class="academy-box">
    <h2>🎓 Aphrodite Training Academy</h2>
    <p>
        Nadiya's passion for education extends beyond the treatment room.
        The Aphrodite Training Academy offers professional certification programs
        for aspiring estheticians and beauty professionals looking to master
        the most in-demand techniques in the industry.
    </p>
    <div class="academy-programs">
        <div class="program-card">
            <h4>💄 Permanent Cosmetics</h4>
            <p>Comprehensive training in microblading, permanent eyeliner,
               lip blushing, and more — taught by a certified instructor
               with 18+ years of experience.</p>
        </div>
        <div class="program-card">
            <h4>🎨 Scalp Micropigmentation</h4>
            <p>Master the art and science of SMP — one of the fastest-growing
               services in the beauty industry. Hands-on, certification-ready
               training from an expert practitioner.</p>
        </div>
        <div class="program-card">
            <h4>📋 Professional Certification</h4>
            <p>All programs include hands-on practice, industry-recognized
               certification, and ongoing mentorship support from Nadiya
               and her team.</p>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# ─────────────────────────────────────────────
# TESTIMONIAL
# ─────────────────────────────────────────────
st.markdown("""
<div class="section-wrapper-alt">
    <div class="section-header">
        <p>Client Stories</p>
        <h2>What Our Clients Say</h2>
        <div class="section-divider"></div>
    </div>
    <div class="testimonial-box">
        <div class="stars">★★★★★</div>
        <div class="quote">
            Nadiya is an absolute artist and expert. My skin has never looked better —
            she truly listens to your concerns and creates a treatment plan that delivers
            real results. I wouldn't trust anyone else with my skin!
        </div>
        <div class="testimonial-author">— A Happy Aphrodite Client · Maryville, IL</div>
    </div>
</div>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────────
# CONTACT + BUILDING IMAGE
# ─────────────────────────────────────────────
st.markdown("""
<div class="section-wrapper">
    <div class="section-header">
        <p>We'd Love to See You</p>
        <h2>Visit or Contact Us</h2>
        <div class="section-divider"></div>
    </div>
</div>
""", unsafe_allow_html=True)

col_contact, col_building = st.columns([1, 1])
with col_contact:
    st.markdown("""
    <div class="contact-info-box">
        <h3>📍 Find Us</h3>
        <div class="contact-item">
            <div class="contact-icon">📞</div>
            <div class="contact-detail">
                <strong>Phone</strong>
                <span>618-791-8980</span>
            </div>
        </div>
        <div class="contact-item">
            <div class="contact-icon">📍</div>
            <div class="contact-detail">
                <strong>Address</strong>
                <span>4 Oak Drive, Suite B<br>Maryville, Illinois</span>
            </div>
        </div>
        <div class="contact-item">
            <div class="contact-icon">🌐</div>
            <div class="contact-detail">
                <strong>Website</strong>
                <span>www.AphroditeSC.com</span>
            </div>
        </div>
        <div class="contact-item">
            <div class="contact-icon">🗺️</div>
            <div class="contact-detail">
                <strong>Area Served</strong>
                <span>Maryville, IL & Greater St. Louis</span>
            </div>
        </div>
        <div style="margin-top:25px;text-align:center;">
            <a href="tel:6187918980" style="display:inline-block;background:linear-gradient(135deg,#9b1a4b,#c2185b);
               color:#fff;padding:14px 40px;border-radius:50px;font-size:1rem;font-weight:700;
               text-decoration:none;letter-spacing:1px;box-shadow:0 6px 25px rgba(155,26,75,0.3);">
                📞 Call to Book Now
            </a>
        </div>
    </div>
    """, unsafe_allow_html=True)

with col_building:
    st.image("building_exterior.png", use_container_width=True,
             caption="Aphrodite Skin Care LLC · Maryville, Illinois")

# ─────────────────────────────────────────────
# FOOTER
# ─────────────────────────────────────────────
st.markdown("""
<div class="footer">
    <div class="footer-logo">✨ APHRODITE SKIN CARE LLC ✨</div>
    <div class="footer-tagline">"Great Skin starts with Great SKIN CARE"</div>
    <p style="font-size:0.85rem;color:rgba(255,255,255,0.5);margin:10px 0;">
        4 Oak Drive, Suite B · Maryville, Illinois · 618-791-8980 · www.AphroditeSC.com
    </p>
    <div class="footer-copy">
        © 2006–2025 Aphrodite Skin Care LLC · All Rights Reserved ·
        Inspired by the goddess of beauty herself 🌹
    </div>
</div>
""", unsafe_allow_html=True)
