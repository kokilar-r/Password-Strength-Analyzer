import streamlit as st
import re
import random
import string

# =========================================================
# PAGE SETTINGS
# =========================================================

st.set_page_config(
    page_title="Password Strength Analyzer",
    page_icon="🔐",
    layout="centered"
)

# =========================================================
# CUSTOM CSS
# =========================================================

st.markdown("""
<style>

.stApp {
    background: linear-gradient(135deg, #0f2027, #203a43, #2c5364);
}

.main-title {
    text-align: center;
    color: #00ffcc;
    font-size: 42px;
    font-weight: bold;
    margin-top: 20px;
}

.subtitle {
    text-align: center;
    color: #ffffff;
    font-size: 18px;
    margin-bottom: 30px;
}

.card {
    background-color: rgba(255, 255, 255, 0.10);
    padding: 25px;
    border-radius: 15px;
    margin-top: 20px;
    color: white;
}

.section-title {
    color: #00ffcc;
    font-size: 24px;
    font-weight: bold;
    margin-top: 20px;
    margin-bottom: 15px;
}

</style>
""", unsafe_allow_html=True)


# =========================================================
# TITLE
# =========================================================

st.markdown(
    '<div class="main-title">🔐 Password Strength Analyzer</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'Check your password security and generate strong passwords'
    '</div>',
    unsafe_allow_html=True
)


# =========================================================
# COMMON PASSWORDS
# =========================================================

common_passwords = [
    "123456",
    "password",
    "12345678",
    "qwerty",
    "admin",
    "letmein",
    "welcome",
    "abc123"
]


# =========================================================
# PASSWORD GENERATOR
# =========================================================

def generate_password(length):

    characters = (
        string.ascii_uppercase +
        string.ascii_lowercase +
        string.digits +
        "!@#$%^&*"
    )

    return "".join(
        random.choice(characters)
        for _ in range(length)
    )


# =========================================================
# PASSWORD INPUT
# =========================================================

password = st.text_input(
    "🔑 Enter your password",
    type="password",
    placeholder="Enter password here..."
)


# =========================================================
# ANALYZE PASSWORD
# =========================================================

if password:

    score = 0
    suggestions = []

    # -----------------------------------------------------
    # LENGTH CHECK
    # -----------------------------------------------------

    if len(password) >= 8:
        score += 1
    else:
        suggestions.append(
            "Use at least 8 characters"
        )

    # -----------------------------------------------------
    # UPPERCASE CHECK
    # -----------------------------------------------------

    if re.search(r"[A-Z]", password):
        score += 1
    else:
        suggestions.append(
            "Add at least one uppercase letter"
        )

    # -----------------------------------------------------
    # LOWERCASE CHECK
    # -----------------------------------------------------

    if re.search(r"[a-z]", password):
        score += 1
    else:
        suggestions.append(
            "Add at least one lowercase letter"
        )

    # -----------------------------------------------------
    # NUMBER CHECK
    # -----------------------------------------------------

    if re.search(r"[0-9]", password):
        score += 1
    else:
        suggestions.append(
            "Add at least one number"
        )

    # -----------------------------------------------------
    # SPECIAL CHARACTER CHECK
    # -----------------------------------------------------

    if re.search(r"[^A-Za-z0-9]", password):
        score += 1
    else:
        suggestions.append(
            "Add at least one special character"
        )


    # =====================================================
    # COMMON PASSWORD WARNING
    # =====================================================

    if password.lower() in common_passwords:

        st.warning(
            "⚠️ This is a commonly used password. "
            "Please choose a different password."
        )


    # =====================================================
    # PASSWORD CRITERIA
    # =====================================================

    st.markdown(
        '<div class="section-title">🔎 Password Criteria</div>',
        unsafe_allow_html=True
    )

    col1, col2 = st.columns(2)

    with col1:

        if len(password) >= 8:
            st.success("✅ 8+ Characters")
        else:
            st.error("❌ 8+ Characters")

        if re.search(r"[A-Z]", password):
            st.success("✅ Uppercase")
        else:
            st.error("❌ Uppercase")

        if re.search(r"[a-z]", password):
            st.success("✅ Lowercase")
        else:
            st.error("❌ Lowercase")

    with col2:

        if re.search(r"[0-9]", password):
            st.success("✅ Number")
        else:
            st.error("❌ Number")

        if re.search(r"[^A-Za-z0-9]", password):
            st.success("✅ Special Character")
        else:
            st.error("❌ Special Character")


    # =====================================================
    # PASSWORD STRENGTH
    # =====================================================

    st.markdown(
        '<div class="section-title">💪 Password Strength</div>',
        unsafe_allow_html=True
    )

    if score <= 2:

        st.error("🔴 WEAK")

    elif score <= 4:

        st.warning("🟡 MEDIUM")

    else:

        st.success("🟢 STRONG")


    # =====================================================
    # SECURITY SCORE
    # =====================================================

    st.write(
        f"### Security Score: {score}/5"
    )

    st.progress(score / 5)


    # =====================================================
    # SUGGESTIONS
    # =====================================================

    if suggestions:

        st.markdown(
            '<div class="section-title">💡 Suggestions</div>',
            unsafe_allow_html=True
        )

        for suggestion in suggestions:

            st.write(
                "➡️ " + suggestion
            )

    else:

        st.success(
            "🎉 Excellent! Your password meets all basic requirements."
        )


# =========================================================
# DIVIDER
# =========================================================

st.divider()


# =========================================================
# STRONG PASSWORD GENERATOR
# =========================================================

st.markdown(
    '<div class="section-title">🎲 Strong Password Generator</div>',
    unsafe_allow_html=True
)

st.write(
    "Generate a random password with uppercase, "
    "lowercase, numbers and special characters."
)


# =========================================================
# PASSWORD LENGTH
# =========================================================

length = st.slider(
    "📏 Password Length",
    min_value=8,
    max_value=32,
    value=12
)


# =========================================================
# GENERATE BUTTON
# =========================================================

if st.button("🎲 Generate Strong Password"):

    generated = generate_password(length)

    st.code(generated)

    st.success(
        "✅ Strong password generated successfully!"
    )


# =========================================================
# DEVELOPER DETAILS
# =========================================================

st.divider()

st.markdown(
    '<div class="section-title">👨‍💻 Developer Details</div>',
    unsafe_allow_html=True
)

st.markdown("""
<div class="card">

<b>Name:</b> R. Kokila<br><br>

<b>Course:</b> Computer Science Engineering<br><br>

<b>Specialization:</b> Cyber Security<br><br>

<b>College:</b> EASA College of Engineering and Technology<br><br>

<b>Technologies:</b><br><br>

🐍 Python &nbsp; | &nbsp;
🎈 Streamlit &nbsp; | &nbsp;
🔎 Regular Expressions (Regex) &nbsp; | &nbsp;
🎨 HTML/CSS

<br><br>

<b>Project:</b> 🔐 Password Strength Analyzer

<br><br>

<b>Project Description:</b><br><br>

A Python-based cybersecurity application that analyzes
password strength, detects commonly used passwords,
provides security recommendations, and generates
strong random passwords.

</div>
""", unsafe_allow_html=True)