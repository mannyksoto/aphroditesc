import streamlit as st

st.set_page_config(
    page_title="Aphrodite Skin Care",
    page_icon="✨",
    layout="wide"
)

# =====================================================
# STYLING
# =====================================================

st.markdown("""
<style>

.stApp {
    background: linear-gradient(
        180deg,
        #f5f9fc 0%,
        #dde8f1 100%
    );
}

/* GENERAL TEXT */

html, body, [class*="css"] {
    color: #2f4058;
}

/* HERO */

.hero-title {
    font-size: 4.2rem;
    font-weight: 800;
    color: #466a99;
    margin-bottom: 10px;
}

.hero-subtitle {
    font-size: 1.3rem;
    color: #4c5664;
    margin-bottom: 25px;
}

.hero-box {
    background:white;
    padding:35px;
    border-radius:28px;
    box-shadow:0 12px 35px rgba(0,0,0,.08);
}

/* CTA */

.cta-box {
    background:white;
    padding:30px;
    border-radius:24px;
    border-top:5px solid #f2c94c;
    box-shadow:0 12px 35px rgba(0,0,0,.08);
}

/* HEADINGS */

.section-title {
    text-align:center;
    font-size:2.2rem;
    font-weight:700;
    color:#466a99;
    margin-top:60px;
    margin-bottom:30px;
}

/* STATS */

.stat-card {
    background:white;
    color:#2f4058;
    text-align:center;
    padding:25px;
    border-radius:20px;
    box-shadow:0 8px 24px rgba(0,0,0,.08);
}

.stat-number {
    color:#f2c94c;
    font-size:2.4rem;
    font-weight:800;
}

/* SERVICES */

.service-card {
    background:white;
    color:#2f4058;
    padding:28px;
    border-radius:22px;
    text-align:center;
    box-shadow:0 8px 24px rgba(0,0,0,.08);
    min-height:220px;
}

.service-card h3 {
    color:#466a99;
    margin-bottom:15px;
}

/* ABOUT */

.about-card {
    background:white;
    color:#2f4058;
    padding:35px;
    border-radius:24px;
    box-shadow:0 10px 30px rgba(0,0,0,.08);
}

.about-card h2,
.about-card h3 {
    color:#466a99;
}

/* FEATURE BAND */

.feature-band {
    background:#466a99;
    color:white;
    padding:45px;
    text-align:center;
    border-radius:25px;
    margin-top:50px;
    margin-bottom:40px;
}

/* BUTTON */

.stButton button {
    background:#f2c94c;
    color:black;
    font-weight:700;
    border:none;
    border-radius:12px;
    padding:12px 24px;
}

.stButton button:hover {
    background:#e2bb44;
}

/* FOOTER */

.footer {
    text-align:center;
    color:#5f6672;
    padding:40px;
}

</style>
""", unsafe_allow_html=True)

# =====================================================
# HERO
# =====================================================

left, right = st.columns([1.6, 1])

with left:

    st.markdown("""
    <div class="hero-box">

    <div class="hero-title">
    Aphrodite Skin Care
    </div>

    <div class="hero-subtitle">
    Advanced Skin Care • Permanent Cosmetics • Scalp Micropigmentation
    </div>

    Helping women and men look and feel their very best through
    personalized skin care treatments, permanent cosmetic services,
    and professional aesthetic education.

    </div>
    """, unsafe_allow_html=True)

    st.button("Schedule Consultation")

with right:

    st.markdown("""
    <div class="cta-box">

    <h3>Serving Greater St. Louis</h3>

    📍 Maryville, Illinois

    <br><br>

    📞 618-791-8980

    <br><br>

    ⭐ Award Winning Practice

    <br><br>

    ⏰ By Appointment Only

    </div>
    """, unsafe_allow_html=True)

# =====================================================
# STATS
# =====================================================

st.markdown(
    "<div class='section-title'>Why Clients Choose Aphrodite</div>",
    unsafe_allow_html=True
)

c1,c2,c3,c4 = st.columns(4)

stats = [
    ("20+","Years Experience"),
    ("2006","Established"),
    ("10+","Award Years"),
    ("IL / MO","Licensed")
]

for col, item in zip([c1,c2,c3,c4], stats):

    with col:

        st.markdown(f"""
        <div class="stat-card">
            <div class="stat-number">{item[0]}</div>
            <br>
            {item[1]}
        </div>
        """, unsafe_allow_html=True)

# =====================================================
# SERVICES
# =====================================================

st.markdown(
    "<div class='section-title'>Featured Services</div>",
    unsafe_allow_html=True
)

s1,s2,s3 = st.columns(3)

with s1:
    st.markdown("""
    <div class="service-card">
    <h3>Facials & Skin Care</h3>

    Customized facials

    Chemical peels

    Acne treatment

    Anti-aging programs

    Clinical skincare
    </div>
    """, unsafe_allow_html=True)

with s2:
    st.markdown("""
    <div class="service-card">
    <h3>Permanent Cosmetics</h3>

    Eyeliner

    Brows

    Lip procedures

    Cosmetic tattooing

    Enhancement services
    </div>
    """, unsafe_allow_html=True)

with s3:
    st.markdown("""
    <div class="service-card">
    <h3>Scalp Micropigmentation</h3>

    Hair thinning

    Alopecia

    Hairline restoration

    Scar camouflage

    SMP training
    </div>
    """, unsafe_allow_html=True)

# =====================================================
# EXPERIENCE
# =====================================================

st.markdown(
    "<div class='section-title'>Trusted Experience. Proven Results.</div>",
    unsafe_allow_html=True
)

st.write("""
For nearly two decades, Aphrodite Skin Care has helped clients throughout
the Greater St. Louis region improve skin health, restore confidence,
and achieve natural-looking aesthetic results.

Every treatment plan is customized to individual goals,
skin conditions, and lifestyle.
""")

# =====================================================
# CONDITIONS
# =====================================================

st.markdown(
    "<div class='section-title'>Conditions We Commonly Treat</div>",
    unsafe_allow_html=True
)

left,right = st.columns(2)

with left:

    st.markdown("""
    ✅ Acne

    ✅ Rosacea

    ✅ Hyperpigmentation

    ✅ Sun Damage

    ✅ Uneven Skin Tone

    ✅ Aging Skin
    """)

with right:

    st.markdown("""
    ✅ Alopecia

    ✅ Hair Thinning

    ✅ Male Pattern Baldness

    ✅ Female Pattern Baldness

    ✅ Scar Camouflage

    ✅ Cosmetic Corrections
    """)

# =====================================================
# ABOUT
# =====================================================

st.markdown(
    "<div class='section-title'>Meet Nadiya</div>",
    unsafe_allow_html=True
)

st.markdown("""
<div class="about-card">

<h2>Master Esthetician & Permanent Cosmetics Instructor</h2>

Nadiya combines European aesthetic traditions with modern
skin care science to provide personalized treatments designed
to deliver real results.

<br><br>

• Licensed in Illinois, Missouri, and Europe

• Director of Education

• Permanent Cosmetics Instructor

• Acne & Anti-Aging Specialist

• Scalp Micropigmentation Training

• Serving Greater St. Louis Since 2006

</div>
""", unsafe_allow_html=True)

# =====================================================
# TRAINING ACADEMY
# =====================================================

st.markdown(
    "<div class='section-title'>Aphrodite Academy</div>",
    unsafe_allow_html=True
)

st.info("""
Professional education programs in Permanent Cosmetics
and Scalp Micropigmentation featuring hands-on instruction,
small class sizes, certification, starter kits,
and post-graduation support.
""")

# =====================================================
# BLUE FEATURE SECTION
# =====================================================

st.markdown("""
<div class="feature-band">

<h2>
Great Skin Starts With Great Skin Care
</h2>

Helping clients achieve confidence through advanced skin care,
permanent cosmetics, and personalized treatment plans.

</div>
""", unsafe_allow_html=True)

# =====================================================
# TESTIMONIAL
# =====================================================

st.markdown(
    "<div class='section-title'>Client Experience</div>",
    unsafe_allow_html=True
)

st.success("""
★★★★★

'I look and feel great every morning.
My permanent makeup turned out natural and beautiful.'
""")

# =====================================================
# CONTACT
# =====================================================

st.markdown(
    "<div class='section-title'>Contact Us</div>",
    unsafe_allow_html=True
)

st.markdown("""
📍 4 Oak Drive, Suite B

Maryville, Illinois 62062

📞 618-791-8980

⏰ By Appointment Only

Serving the Greater St. Louis Bi‑State Area
""")

st.button("Book Appointment")

# =====================================================
# FOOTER
# =====================================================

st.markdown("""
<div class="footer">

Aphrodite Skin Care LLC

Inspired by European skincare traditions.

© 2006–2026

</div>
""", unsafe_allow_html=True)
