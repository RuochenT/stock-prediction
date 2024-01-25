This project encompasses various stages, including data collection, exploratory data analysis, data preprocessing, and the three kind of models: time series, machine learning, and deep learning models. The final step involves comparing the results of each model using the Root Mean Squared Error (RMSE) metric.
## Data 
I retrieved stock data using WebSocket due to the nature of the data being presented in a chart. Unfortunately, conventional methods such as requests or BeautifulSoup are not applicable in this scenario. The data fetched pertains to Adanc stock, representing Advanced Info Service Public Company Limited, Thailand's largest GSM mobile phone operator. For more details on the source of the data, you can visit the following website: [Link](https://www.settrade.com/th/technical-chart?symbol=ADVANC&type=stock) 

The data includes closing, opening,highest, lowest, and date which covers the period from 2018-12-21 to 2023-12-20. 
<img width="327" alt="Screenshot 2567-01-25 at 22 10 45" src="https://github.com/RuochenT/Classify-loan/assets/119982930/662f9699-83ab-4732-a18c-ce5065026030">

## EDA 
![1](https://github.com/RuochenT/Classify-loan/assets/119982930/466ab13b-b0b2-4a8f-9ebb-7591113408a3)
![2](https://github.com/RuochenT/Classify-loan/assets/119982930/ce4d91c3-2c84-4ebf-bc6f-e5c3890c8c02)

## Methods 
1. Time series methods: ARIMA (done), EWMA
2. Machine learning methods: Random forests, XGBoost, MARS
3. Deep learning methods: RNN and LSTM (next)

## Model diagnostics for time series methods 
![3](https://github.com/RuochenT/Classify-loan/assets/119982930/a9118371-a9c2-4aac-b89f-7574f0aacc7a)
![4](https://github.com/RuochenT/Classify-loan/assets/119982930/d66ae322-b84e-4a75-816f-46daf975546c)

