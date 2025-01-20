import streamlit as st
import pandas as pd
import yfinance as yf

@st.cache_data
def load_df(url = "https://en.wikipedia.org/wiki/List_of_S%26P_500_companies"):
    df = pd.read_html(url)[0]
    return df

st.title("S&P500")

st.write("""
The **S&P 500** (Standard & Poor's 500) is a stock market index that tracks the performance of 500 of the largest publicly traded companies in the United States. It is widely regarded as one of the best indicators of the overall health of the U.S. stock market and economy. 

""")

df_companies_list = load_df()

st.write(df_companies_list)

tickers = list(df_companies_list["Symbol"])

gisc = df_companies_list["GICS Sector"].unique()
st.code(f"GICS Sector: {len(gisc)}\n{gisc}")

selectedGISC = st.multiselect("Select GISC Sector", gisc)

st.write(df_companies_list[df_companies_list["GICS Sector"].isin(selectedGISC)])

ticker = st.multiselect("Select a company stock you're interested in", tickers)

if len(ticker) > 0:
    df = yf.download(
        ticker,
        period="1y",
        interval="1d"
    )

    st.line_chart(df["Close"])
else:
    st.write("Please select at least one stock to display data.")