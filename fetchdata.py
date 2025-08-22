from pytrends.request import TrendReq
import streamlit as st

def fetch_data():
    keywords = [kw.lower() for kw in st.session_state["keywords"]]  # keywords lowercase
    geo = st.session_state["geo"]
    timeframe = st.session_state["timeframe"]

    pytrends = TrendReq(hl='en-US', tz=330)
    pytrends.build_payload(keywords, timeframe=timeframe, geo=geo, gprop='')

    time_data = pytrends.interest_over_time()
    if 'isPartial' in time_data.columns:
        time_data = time_data.drop(columns=['isPartial'])
    time_data.reset_index(inplace=True)

    region_data = pytrends.interest_by_region(resolution='COUNTRY', inc_low_vol=True, inc_geo_code=False).reset_index()

    time_data.columns = [col.lower() for col in time_data.columns]
    region_data.columns = [col.lower() for col in region_data.columns]

    return time_data, region_data
