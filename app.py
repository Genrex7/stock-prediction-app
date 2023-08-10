import streamlit as st
from datetime import date
import yfinance as yf
from prophet import Prophet
from prophet.plot import plot_plotly
from plotly import graph_objs as go

# Set constants
START = "2015-01-01"
TODAY = date.today().strftime("%Y-%m-%d")

# Streamlit app title
st.title("Stock Prediction App")

# Function to load stock data using yfinance
def load_data(ticker):
    data = yf.download(ticker, START, TODAY)
    data.reset_index(inplace=True)
    return data

# Function to plot raw stock data based on selected plot type
def plot_raw_data(data, plot_type):
    fig = go.Figure()

    if plot_type == "line":
        fig.add_trace(go.Scatter(x=data["Date"], y=data["Close"], mode="lines", name="stock_close"))
    elif plot_type == "area":
        fig.add_trace(go.Scatter(x=data["Date"], y=data["Close"], fill='tozeroy', name="stock_area"))
    elif plot_type == "bar":
        fig.add_trace(go.Bar(x=data["Date"], y=data["Volume"], name="stock_volume"))
    elif plot_type == "colored_bar":
        colors = ['green' if close > open_ else 'red' for close, open_ in zip(data["Close"], data["Open"])]
        fig.add_trace(go.Bar(x=data["Date"], y=data["Volume"], marker=dict(color=colors), name="colored_volume"))
    elif plot_type == "candle":
        fig = go.Figure(data=[go.Candlestick(x=data["Date"],
                                               open=data["Open"],
                                               high=data["High"],
                                               low=data["Low"],
                                               close=data["Close"])])
    elif plot_type == "hollow_candle":
        colors = ['green' if close > open_ else 'red' for close, open_ in zip(data["Close"], data["Open"])]
        fig = go.Figure(data=[go.Candlestick(x=data["Date"],
                                               open=data["Open"],
                                               high=data["High"],
                                               low=data["Low"],
                                               close=data["Close"],
                                               increasing_line_color="green",
                                               decreasing_line_color="red")])

    fig.layout.update(title_text=f"Time Series Data ({plot_type.capitalize()})", xaxis_rangeslider_visible=True)
    st.plotly_chart(fig)

# Function to prepare and forecast data using the Prophet model
def forecast_data(data, n_years):
    df_train = data[["Date", "Close"]].rename(columns={"Date": "ds", "Close": "y"})
    
    m = Prophet()
    m.fit(df_train)
    
    future = m.make_future_dataframe(periods=n_years * 365)
    forecast = m.predict(future)
    
    return forecast, m

# Main function to run the Streamlit app
def main():
    # Input fields for stock ticker, prediction years, and plot type
    ticker_input = st.text_input("Enter stock ticker or company name", "AAPL")
    n_years = st.slider("Years of prediction:", 1, 4)
    plot_type = st.selectbox("Select plot type:", ("line", "area", "bar", "colored_bar", "candle", "hollow_candle"))
    
    # Load stock data
    data_load_state = st.text("Loading data...")
    data = load_data(ticker_input)
    
    # Check if data is empty
    if data.empty:
        st.warning(f"No data available for '{ticker_input}'")
        return
    
    data_load_state.text("Loading data...done!")

    # Display raw data and selected plot
    st.subheader("Raw data")
    st.write(data.tail())
    
    plot_raw_data(data, plot_type)
    
    # Generate and display forecast data and components
    forecast, model = forecast_data(data, n_years)
    
    st.subheader("Forecast data")
    st.write(forecast.tail())
    
    st.write("Forecast data")
    fig1 = plot_plotly(model, forecast)
    st.plotly_chart(fig1)
    
    st.write("Forecast components")
    fig2 = model.plot_components(forecast)
    st.write(fig2)

if __name__ == "__main__":
    main()

