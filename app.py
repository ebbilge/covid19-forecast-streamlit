import streamlit as st
import pandas as pd
from prophet import Prophet
import plotly.graph_objects as go

@st.cache_data
def load_data():
    url = "https://catalog.ourworldindata.org/garden/covid/latest/compact/compact.csv"
    df = pd.read_csv(url)
    df = df[['country', 'date', 'new_cases']]
    df['date'] = pd.to_datetime(df['date'])
    df['new_cases'] = df['new_cases'].fillna(0)
    df = df[df['new_cases'] >= 0]
    return df

df = load_data()
countries = df['country'].unique()

@st.cache_resource
def train_model(country):
    df_country = df[df['country'] == country][['date', 'new_cases']]
    df_country = df_country.rename(columns={'date': 'ds', 'new_cases': 'y'})
    
    if len(df_country) < 30:  # çok az veri varsa modelleme yapma
        return None, None

    model = Prophet(
        changepoint_prior_scale=0.05,
        seasonality_prior_scale=5,
        yearly_seasonality=True,
        weekly_seasonality=True
    )
    model.fit(df_country)
    
    future = model.make_future_dataframe(periods=30)
    forecast = model.predict(future)
    
    return df_country, forecast

st.title("🌍 COVID-19 Forecast using Prophet (Country-based)")
country = st.selectbox("Select a Country", countries)

df_country, forecast = train_model(country)

if df_country is None:
    st.warning("⚠️ Bu ülke için yeterli veri yok.")
else:
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df_country['ds'], y=df_country['y'],
                             mode='lines', name='Actual'))
    fig.add_trace(go.Scatter(x=forecast['ds'], y=forecast['yhat'],
                             mode='lines', name='Predicted'))
    fig.update_layout(title=f"{country} - COVID-19 Forecast (Prophet)",
                      xaxis_title="Date", yaxis_title="New Cases")

    st.plotly_chart(fig, use_container_width=True)
