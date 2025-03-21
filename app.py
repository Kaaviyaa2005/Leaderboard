import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="TCE Build Club Leaderboard", layout="wide")

# Elegant Modern Styling
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600&display=swap');

    body {
        background-color: #121212;
        color: #e0e0e0;
        font-family: 'Inter', sans-serif;
    }

    .title-container {
        display: flex;
        justify-content: center;
        align-items: center;
        margin-bottom: 30px;
    }

    .title-container img {
        height: 70px;
        margin: 0 15px;
        border-radius: 10px;
    }

    h1 {
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 2px;
        text-align: center;
        text-align: center;
        color: #ffffff;
    }

    #leaderboardhq {
        margin: 20px auto;
        max-width: 90%;
        border-radius: 10px;
        box-shadow: 0px 4px 12px rgba(255, 255, 255, 0.15);
        transition: all 0.3s ease-in-out;
    }

     .centered-title {
        text-align: center;
        font-weight: 700;
        font-size: 2.5em;
        text-transform: uppercase;
        letter-spacing: 2px;
        color: #ffffff;
    }
    </style>

    </style>
    """,
    unsafe_allow_html=True,
)

# Title with logos
col1, col2 = st.columns([0.5, 5])
with col1:
    st.image("logo1.jpg", width=100)
with col2:
    st.markdown("<h1 class='centered-title'>TCE Build Club Leader Board</h1>", unsafe_allow_html=True)

# **Embed Leaderboard from LeaderboardHQ**
st.write("## 🚀 Live Leaderboard")

leaderboard_html = """
<div id="leaderboardhq" class="cleanslate"></div>
<script src="https://leaderboardhq.com/v1/ndv6bha7"></script>
"""

# Display in Streamlit
components.html(leaderboard_html, height=600, scrolling=True)
