---

## README.md

---

# Sales Forecasting for Retail Chain in India

This project aimed to forecast SKU-wise product sales for a retail chain in India across 76 different stores using historical sales data spanning three years on a week-on-week basis.

## Summary of Results

- **Time Series Analysis**: Leveraged ARIMA, a traditional time series forecasting model, to predict the sales for the selected SKU-store combinations. The ARIMA model, while simple, provides a good baseline and captures general trends and seasonality in the data.
  
- **Deep Learning Forecasting**: Built an LSTM model, a type of recurrent neural network, to predict the sales. LSTMs are particularly well-suited for sequence prediction problems and often outperform traditional methods, especially with large datasets.

- **Forecast Period**: Predictions were made for the next 12 weeks for each SKU-store combination.

## Issues Faced

1. **Date Indexing**: The date index in the dataset lacked associated frequency information, resulting in warnings during modeling with ARIMA.
  
2. **ARIMA Parameter Selection**: The ARIMA model parameters (p, d, q) were initially set based on general experience. Finer tuning might yield better results.
  
3. **Data Granularity**: The data is granular, SKU-store-week level, which requires forecasting for numerous combinations, thus demanding significant computational resources.

4. **Deep Learning Dependencies**: The initial environment lacked TensorFlow and Keras libraries, essential for building deep learning models.

## Steps Taken

1. **Data Preprocessing**:
    - Converted the 'week' column to a datetime format for time series analysis.
    - Sorted the data based on store_id, sku_id, and week for consistent sequencing.
    - Normalized the data for the deep learning model since LSTMs are sensitive to input data scale.

2. **Model Building**:
    - For the ARIMA model, we used a sample SKU-store combination to ensure the approach's feasibility. Once verified, the process was scaled to other combinations.
    - For the LSTM model, the time series data was transformed into a supervised learning format. The data was split into training and validation sets. An LSTM architecture was defined and trained on this data.

3. **Forecasting & Visualization**:
    - Used the trained models to forecast sales for the next 12 weeks.
    - Visualized the forecasted values against actual sales for better interpretability.
---
