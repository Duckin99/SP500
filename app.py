import streamlit as st
import pandas as pd
import yfinance as yf

def load_df(url = "https://en.wikipedia.org/wiki/List_of_S%26P_500_companies"):
    df = pd.read_html(url)[0]
    return df

st.write("""
### About the S&P 500

The **S&P 500** (Standard & Poor's 500) is a stock market index that tracks the performance of 500 of the largest publicly traded companies in the United States. It is widely regarded as one of the best indicators of the overall health of the U.S. stock market and economy. 

Key features of the S&P 500:
- **Broad Representation**: The index includes companies from various sectors, such as technology, healthcare, financials, and consumer goods.
- **Market Capitalization Weighted**: Companies with larger market capitalizations have a greater impact on the index's performance.
- **Global Influence**: Many companies in the S&P 500 operate internationally, making the index a reflection of global economic trends.

Investors and analysts use the S&P 500 to assess market trends, compare individual stock performance, and benchmark the performance of portfolios. The index is maintained by S&P Dow Jones Indices and is updated periodically to reflect changes in the market.
""")

df_companies_list = load_df()

st.write(df_companies_list)

tickers = list(df_companies_list["Symbol"])

gisc = df_companies_list["GICS Sector"].unique()
st.code(f"GICS Sector: {len(gisc)}\n{gisc}")

selectedGISC = st.selectbox("Select GISC Sector", gisc)

st.write(df_companies_list.groupby("GICS Sector").get_group(selectedGISC))

ticker = st.selectbox("Select a company stock you're interested in", tickers)

df = yf.download(
    ticker,
    period="ytd",
    interval="1d"
)

st.write(df)