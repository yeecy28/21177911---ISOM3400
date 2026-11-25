import streamlit as st
import pandas as pd

st.set_page_config(page_title="Submission Template", layout="wide")

st.title("📝 Assignment Submission")

# ==========================================
# Task 1
# ==========================================
st.header("Task 1: Build a stock dashboard with sidebar controls")


# Starter code
ticker_info = pd.read_csv("https://raw.githubusercontent.com/justinjiajia/datafiles/refs/heads/main/ticker_info.csv")

# extract S&P 100 tickers from ticker_info
ticker_list = list(ticker_info.Ticker.unique())

# Load the stock data
stock_data = pd.read_csv(
    "https://github.com/justinjiajia/datafiles/raw/refs/heads/main/stock_data_yf.csv", 
    parse_dates=['Date']
)

 
 

st.info("Write your Task 1 code below ...")

# --- STUDENT CODE AREA START ---

st.title("S&P 100 Stock Dashboard 📊")

show_market_cap = st.sidebar.checkbox("Show Market Cap by Sector", value=True)

selected_tickers = st.sidebar.multiselect(
    "Select Stocks", 
    options=ticker_list, 
    default=['TSLA', 'NVDA', 'AAPL']
)

selected_years = st.sidebar.slider(
    "Select Year Range", 
    min_value=2020, 
    max_value=2025, 
    value=(2024, 2025)
)

#market cap chart
if show_market_cap:
    st.subheader("Market Cap by Sector")
    st.bar_chart(
        ticker_info, 
        x="Sector", 
        y="Market Cap (B)", 
        color="Ticker", 
        horizontal=True
    )

#stock trend analysis
if len(selected_tickers) == 0:
    st.error("Please select at least one stock!")
else:
    filtered_data = stock_data.query(
        f"Date <= '{selected_years[1]}-12-31' and Date >= '{selected_years[0]}-01-01' and Ticker in {selected_tickers}"
    )

    
    st.subheader(f"Stock Trend Analysis ({selected_years[0]} - {selected_years[1]})")
    
    #line chart
    st.subheader("Closing Prices")
    st.line_chart(
        filtered_data, 
        x="Date", 
        y="Close", 
        color="Ticker"
    )

 # bar chart
    st.subheader("Trading Volume")
    st.bar_chart(
        filtered_data, 
        x="Date", 
        y="Volume", 
        color="Ticker"
    )
    
# --- STUDENT CODE AREA ---

st.divider()

# ==========================================
# Task 2
# ==========================================

st.header("Task 2: Display a video based on user input")

st.info("Write your Task 2 code below ...")

# --- STUDENT CODE AREA START ---
if "video_url" not in st.session_state:
    st.session_state.video_url = ""
if "clicked" not in st.session_state:
    st.session_state.clicked = False

col1, col2 = st.columns([2, 1], vertical_alignment="bottom")

with col1:
     url_input = st.text_input(
        "Enter the URL of a video", 
        value="https://interactive-examples.mdn.mozilla.net/media/cc0-videos/flower.mp4"
    )
    
with col2:
    # Submit button
    if st.button("Submit"):
        st.session_state.video_url = url_input
        st.session_state.clicked = True

with st.container(border=True, width=640, height=400, horizontal_alignment="center"):
    if not st.session_state.clicked:
        # Before submission message
        st.info("Please enter a video URL and click Submit to display the video.")
    else:
        # Try to load the video, catch exceptions for invalid URLs
        try:
            st.video(st.session_state.video_url)
        except Exception:
            st.error("Error: The video could not be loaded. Please check the URL and try again.")




# --- STUDENT CODE AREA END ---
