# Stock Prediction App

This is a Streamlit web application that allows users to predict and visualize stock prices using the Prophet forecasting model. The app provides options to select a stock ticker or company name, choose the number of years for prediction, and visualize the stock data in various plot types.

## Features

-   Enter a stock ticker or company name to load historical stock data.
-   Choose the number of years for prediction using a slider.
-   Select different types of plots for visualizing stock data, including line, area, bar, colored bar, candle, and hollow candle plots.
-   Display raw data, forecast data, and forecast components.
-   Built-in caching for efficient data loading and processing.

## Getting Started

1.  Clone the repository to your local machine:

    ```bash
    git clone
    ```

2.  Install the required packages:

    ```bash
    pip install streamlit yfinance prophet plotly
    ```

3.  Run the streamlit app:

    ```bash
    streamlit run app.py
    ```

## Usage

1. Enter a stock ticker or company name in the input field.
2. Adjust the slider to select the number of years for prediction.
3. Choose a plot type from the dropdown menu (line, area, bar, colored bar, candle, hollow candle).
4. Explore the raw data, selected plot visualization, forecast data, and forecast components.

## Dependencies / Requirements

-   [![Streamlit][streamlit]][streamlitURL]
-   [![yfinance][yfinance]][yfinanceURL]
-   [![prophet][prophet]][prophetURL]
-   [![plotly][plotly]][plotlyURL]

[streamlit]: https://img.shields.io/badge/streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white
[streamlitURL]: https://streamlit.io/
[yfinance]: https://img.shields.io/badge/yfinance-4B00C8?style=for-the-badge&logo=yahoo&logoColor=white
[yfinanceURL]: https://pypi.org/project/yfinance/
[prophet]: https://img.shields.io/badge/prophet-2D4485?style=for-the-badge&logo=prophet&logoColor=white
[prophetURL]: https://facebook.github.io/prophet/
[plotly]: https://img.shields.io/badge/plotly-0C0D0D?style=for-the-badge&logo=plotly&logoColor=white
[plotlyURL]: https://plotly.com/

## Roadmap

### The following things can be done to improve the project:

-   [ ] Show data of a day also in the graph
-   [ ] Show data like this [yahoo page](https://finance.yahoo.com/quote/AAPL?p=AAPL&.tsrc=fin-srch)

