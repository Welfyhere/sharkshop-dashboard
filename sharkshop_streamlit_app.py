
import streamlit as st
import pandas as pd
import altair as alt

st.set_page_config(page_title='🦈 SharkShop Insights', layout='wide')

# Load data
@st.cache_data
def load_data():
    df = pd.read_csv('fixed_ecommerce_data_5_years.csv')
    df['Month'] = pd.to_datetime(df['Month'])
    return df

df = load_data()

# Title and Logo
st.markdown("""<div style='display: flex; align-items: center;'>
<img src='https://upload.wikimedia.org/wikipedia/commons/3/34/Shark_icon.png' width='80'/>
<h1 style='padding-left: 1rem;'>SharkShop Revenue Dashboard</h1>
</div>""", unsafe_allow_html=True)

# Key Metrics
latest = df.iloc[-1]
col1, col2, col3 = st.columns(3)
col1.metric("Latest Revenue", f"${latest['Revenue']:,.0f}")
col2.metric("New Customers", f"{latest['New_Customers']:,}")
col3.metric("Retention Rate", f"{latest['Retention_Rate']}%")

# Revenue over Time
st.subheader("📈 Revenue Over Time")
line_chart = alt.Chart(df).mark_line(point=True).encode(
    x='Month:T',
    y='Revenue:Q',
    tooltip=['Month:T', 'Revenue:Q']
).properties(width=800, height=400)
st.altair_chart(line_chart, use_container_width=True)

# Customer Acquisition Cost over Time
st.subheader("💸 Customer Acquisition Cost Over Time")
cac_chart = alt.Chart(df).mark_line(color='orangered').encode(
    x='Month:T',
    y='Customer_Acquisition_Cost:Q',
    tooltip=['Month:T', 'Customer_Acquisition_Cost:Q']
).properties(width=800, height=300)
st.altair_chart(cac_chart, use_container_width=True)

# Top Product Category Distribution
st.subheader("🏆 Top Product Category Distribution")
category_counts = df['Top_Product_Category'].value_counts().reset_index()
category_counts.columns = ['Category', 'Months']
bar_chart = alt.Chart(category_counts).mark_bar().encode(
    x='Category:N',
    y='Months:Q',
    color='Category:N',
    tooltip=['Category', 'Months']
).properties(width=800, height=300)
st.altair_chart(bar_chart, use_container_width=True)
