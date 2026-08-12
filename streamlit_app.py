import streamlit as st

st.set_page_config(
    page_title="Aphrodite Skin Care",
    page_icon="✨",
    layout="wide"
)

st.markdown("""
<style>

.stApp {
    background: linear-gradient(
        180deg,
        #ffffff 0%,
        #eef6fb 100%
    );
}

.hero-title {
    font-size: 4rem;
    font-weight: 700;
    color: #4d6f9a;
}

.hero-subtitle {
    font-size: 1.4rem;
    color: #5b6570;
    margin-bottom: 25px;
}

.cta-box {
    background: white;
    padding: 25px;
    border-radius: 20px;
    border-left: 6px solid #f2c94c;
    box-shadow: 0 8px 20px rgba(0,0,0,.08);
}

.section-title {
    text-align:center;
    color:#4d6f9a;
    font-size:2rem;
    margin-top:40px;
    margin-bottom:20px;
    font-weight:600;
}

.service-card {
    background:white;
    border-radius:20px;
    padding:25px;
    box-shadow:0 8px 18px rgba(0,0,0,.08);
    text-align:center;
    min-height:170px;
}

.stat-card {
    background:white;
    border-radius:18px;
    padding:20px;
    text-align:center;
    box-shadow:0 6px 14px rgba(0,0,0,.06);
}

.stat-number {
    color:#f2c94c;
    font-size:2rem;
    font-weight:700;
}

.about-card {
    background:white;
    border-radius:20px;
    padding:30px;
    box-shadow:0 8px 18px rgba(0,0,0,.07);
}

.footer {
    text-align:center;
    padding:30px;
    color:#777;
}

.stButton button {
    background-color:#f2c94c;
    color:black;
    border:none;
    border-radius:10px;
    font-weight:600;
}

.stButton button:hover {
    background-color:#eaba35;
}

</style>
""", unsafe_allow_html=True)

# HERO

left, right = st.columns([1.5, 1])

with left:

    st.markdown(
        "<div class='hero-title'>Aphrodite Skin Care</div>",
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class='hero-subtitle'>
        Advanced Skin Care • Permanent Cosmetics • Scalp Micropigmentation
        </div>
        """,
        unsafe_allow_html=True
    )

    st.write(
        """
        Helping women and men look and feel their best through
        personalized skin care, permanent cosmetics,
        advanced aesthetic treatments and education.
        """
    )

    st.button("Schedule Consultation")

with right:

    st.markdown(
        """
        <div class='cta-box'>

        <h3>Serving Greater St. Louis</h3>

        📍 Maryville, Illinois

        📞 618-791-8980

        ⏰ By Appointment Only

        ⭐ Award Winning Practice

        </div>
        """,
        unsafe_allow_html=True
    )

# STATS

st.markdown(
    "<div class='section-title'>Why Clients Choose Aphrodite</div>",
    unsafe_allow_html=True
)

c1, c2, c3, c4 = st.columns(4)

stats = [
    ("20+", "Years Experience"),
    ("2006", "Established"),
    ("10+", "Years Awarded"),
    ("IL / MO", "Licensed")
]

for col, stat in zip([c1, c2, c3, c4], stats):

    with col:

        st.markdown(
            f"""
            <div class='stat-card'>
            <div class='stat-number'>{stat[0]}</div>
            <div>{stat[1]}</div>
            </div>
            """,
            unsafe_allow_html=True
        )

# SERVICES

st.markdown(
    "<div class='section-title'>Featured Services</div>",
    unsafe_allow_html=True
)

s1, s2, s3 = st.columns(3)

with s1:
    st.markdown(
        """
        <div class='service-card'>
        <h3>Facials & Skin Care</h3>

        Customized facials,
        anti-aging treatments,
        acne programs,
        chemical peels.
        </div>
        """,
        unsafe_allow_html=True
    )

with s2:
    st.markdown(
        """
        <div class='service-card'>
        <h3>Permanent Cosmetics</h3>

        Eyeliner,
        brows,
        lip procedures,
        cosmetic tattooing.
        </div>
        """,
        unsafe_allow_html=True
    )

with s3:
    st.markdown(
        """
        <div class='service-card'>
        <h3>Scalp Micropigmentation</h3>

        Hairline restoration,
        thinning hair treatment,
        scar camouflage.
        </div>
        """,
        unsafe_allow_html=True
    )


# EXPERIENCE SECTION

st.markdown(
    "<div class='section-title'>Trusted Experience. Proven Results.</div>",
    unsafe_allow_html=True
)

st.write("""
For nearly two decades, Aphrodite Skin Care has helped clients throughout
the Greater St. Louis region improve skin health, restore confidence,
and achieve natural-looking aesthetic results.

Every treatment plan is personalized to your goals, skin condition,
and lifestyle.
""")
# ABOUT

st.markdown(
    "<div class='section-title'>Meet Nadiya</div>",
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class='about-card'>

    <h3>Master Esthetician & Permanent Cosmetics Instructor</h3>

    Nadiya combines European aesthetics, advanced skin care,
    permanent cosmetics, and modern treatment methods
    to help clients look and feel their very best.

    <br><br>

    • Licensed in Illinois, Missouri and Europe

    • Director of Education

    • Permanent Cosmetics Instructor

    • Acne & Anti-Aging Specialist

    • Scalp Micropigmentation Training

    • Serving Greater St. Louis Since 2006

    </div>
    """,
    unsafe_allow_html=True
)

# TESTIMONIAL

st.markdown(
    "<div class='section-title'>Client Experience</div>",
    unsafe_allow_html=True
)

st.success(
    '"I look and feel great every morning. '
    'My permanent makeup turned out natural and beautiful."'
)

# CTA

st.markdown("---")

st.subheader("Ready To Begin Your Skin Care Journey?")

st.write(
    """
    Schedule a personalized consultation and discover
    treatments tailored specifically to your goals.
    """
)

st.button("Book Appointment")

# FOOTER

st.markdown(
    """
    <div class='footer'>

    Aphrodite Skin Care LLC

    Maryville, Illinois

    Inspired by European skin care traditions.

    </div>
    """,
    unsafe_allow_html=True
)
