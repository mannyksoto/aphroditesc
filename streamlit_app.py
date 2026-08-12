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

/* ================================================= */
/* BACKGROUND */
/* ================================================= */

.stApp {
    background: linear-gradient(
        180deg,
        #c7d6e6 0%,
        #b8cada 45%,
        #afc4db 100%
    );
}

/* ================================================= */
/* GLOBAL TEXT */
/* ================================================= */

html,
body,
p,
span,
li,
label,
div,
h1,
h2,
h3,
h4,
h5,
h6 {
    color: #22334D !important;
}

/* ================================================= */
/* HERO */
/* ================================================= */

.hero-section {
    background: linear-gradient(
        135deg,
        #355885,
        #4d74a5
    );

    padding: 70px;
    border-radius: 32px;

    box-shadow:
    0 20px 45px rgba(0,0,0,.15);

    margin-bottom: 40px;
}

.hero-title {

    color: white !important;

    font-size: 5rem;
    font-weight: 800;

    margin-bottom: 15px;
}

.hero-subtitle {

    color: rgba(255,255,255,.9) !important;

    font-size: 1.5rem;
}

.hero-description {

    color: rgba(255,255,255,.85) !important;

    margin-top: 25px;

    font-size: 1.1rem;
}

/* ================================================= */
/* SECTION HEADER */
/* ================================================= */

.section-title {

    text-align:center;

    color:#243B5A !important;

    font-size:2.6rem;

    font-weight:800;

    margin-top:60px;

    margin-bottom:40px;
}

/* ================================================= */
/* CARDS */
/* ================================================= */

.card {

    background:white;

    padding:30px;

    border-radius:24px;

    box-shadow:
    0 12px 25px rgba(0,0,0,.08);

    color:#22334D !important;
}

.card h3 {
    color:#355885 !important;
}

/* ================================================= */
/* STATS */
/* ================================================= */

.stat-card {

    background:white;

    border-radius:22px;

    padding:25px;

    text-align:center;

    box-shadow:
    0 12px 25px rgba(0,0,0,.08);
}

.stat-number {

    color:#E7BE47 !important;

    font-size:2.5rem;

    font-weight:800;
}

/* ================================================= */
/* FEATURE STRIPE */
/* ================================================= */

.feature-stripe {

    background:
    linear-gradient(
        135deg,
        #243B5A,
        #355885
    );

    padding:50px;

    border-radius:30px;

    text-align:center;

    margin-top:50px;
}

.feature-stripe h2 {

    color:white !important;
}

.feature-stripe p {

    color:rgba(255,255,255,.9) !important;
}

/* ================================================= */
/* CTA BOX */
/* ================================================= */

.cta-box {

    background:white;

    border-top:8px solid #E7BE47;

    border-radius:24px;

    padding:30px;

    box-shadow:
    0 12px 25px rgba(0,0,0,.08);
}

.cta-box * {

    color:#22334D !important;
}

/* ================================================= */
/* BUTTONS */
/* ================================================= */

.stButton button {

    background:#E7BE47;

    color:#22334D;

    font-weight:700;

    border:none;

    border-radius:12px;

    padding:0.75rem 1.5rem;
}

.stButton button:hover {

    background:#d4ac3d;
}

/* ================================================= */
/* CONTACT BOX */
/* ================================================= */

.contact-box {

    background:white;

    padding:35px;

    border-radius:24px;

    box-shadow:
    0 12px 25px rgba(0,0,0,.08);
}

/* ================================================= */
/* FOOTER */
/* ================================================= */

.footer {

    text-align:center;

    color:#243B5A !important;

    padding:40px;

    font-size:1rem;
}

</style>
""", unsafe_allow_html=True)


# =====================================================
# HERO
# =====================================================

st.markdown("""
<div class="hero-section">

<div class="hero-title">
Aphrodite Skin Care
</div>

<div class="hero-subtitle">
Advanced Skin Care • Permanent Cosmetics • Scalp Micropigmentation
</div>

<div class="hero-description">

Helping women and men look and feel their very best through
personalized skin care treatments, permanent cosmetics,
advanced aesthetic services, and professional training.

</div>

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

with s1:
    st.markdown("""
    <div class="card">

    <h3>Facials & Clinical Skin Care</h3>

    Customized facials

    Chemical peels

    Acne treatments

    Anti-aging programs

    Clinical skincare therapies

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

st.markdown("""
<div class="contact-box">

<h3>Contact Us</h3>

📍 4 Oak Drive, Suite B

Maryville, Illinois

# =====================================================
# FOOTER
# =====================================================
st.markdown("""
<div class="footer">

Aphrodite Skin Care LLC

Inspired by European skincare traditions.

Copyright 2006-2026

</div>
""", unsafe_allow_html=True)
