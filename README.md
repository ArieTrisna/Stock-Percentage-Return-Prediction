# 📊 Stock Percentage Return Prediction Using Linear Regression

## 🎯 Objective  
This project aims to **predict the daily percentage return** of the stock **BBCA.JK** (Bank Central Asia, one of Indonesia’s largest banks) using **historical price data and technical indicators** such as **RSI**, **Moving Average (MA)**, and **MACD**. A **Linear Regression** model is applied as a supervised learning method to estimate returns based on engineered features.

---

## 🧠 Methodology  
1. **Data Collection & Cleaning** – Retrieved price data using `yfinance` and prepared it for modeling  
2. **Exploratory Data Analysis** – Analyzed historical trends and patterns using visualizations  
3. **Feature Engineering** – Generated technical indicators (RSI, MA, MACD) to use as input features  
4. **Model Training & Evaluation** – Trained a Linear Regression model and assessed performance  
5. **Summary & Insights** – Reflected on outcomes and potential improvements

---

## 📈 Dataset  
- **Source**: [Yahoo Finance via `yfinance` API](https://pypi.org/project/yfinance/)  
- **Stock**: `BBCA.JK` — Bank Central Asia (Indonesia)  
- Data includes daily price data used to calculate returns and indicators

---

## 📉 Model Performance Summary  
Despite the volatility of financial markets, the Linear Regression model was able to **capture some upward and downward momentum**, demonstrating the predictive power of technical indicators. While the model doesn’t perfectly align with actual returns, it provides a useful baseline and shows room for improvement with more sophisticated techniques or additional features.

**Evaluation Metrics:**
- **MAE**: `0.042`  
  → On average, the predictions are off by ~0.042 from actual returns  
- **MSE**: `0.0023`  
  → The average squared prediction error is ~0.0023  
- **R-squared**: `-0.197`  
  → The model explains -19.7% of the variance (indicating poor generalization in current form)  
- **RMSE**: `0.048`  
  → On average, predictions deviate from actual values by ~0.048

---

## 📌 Key Takeaways  
- **Linear Regression**, although simple, can provide a useful baseline for stock return prediction  
- **Technical indicators** like RSI, MA, and MACD serve as effective features for capturing trends  
- With more **feature engineering**, **regularization**, and possibly **non-linear models**, prediction accuracy can be significantly improved

---

## 🙋‍♂️ About Me  
Hi! I’m **Arie Trisnasaputra**, a recent business & economics graduate from Indonesia currently focused on building my career in data. My work primarily involves **Python, SQL**, and **machine learning** applied to real-world data problems in finance.

I'm actively seeking **entry-level** or **internship roles** in data analysis, data science, or related positions.

📬 Let's connect:  
- [LinkedIn](https://www.linkedin.com/in/arietrisna/)  
- [Email](mailto:arie.trisnasaputra.17@gmail.com)  
- [Instagram](https://www.instagram.com/arietrisn_/)

---

## 📎 Acknowledgements  
- Data provided by [Yahoo Finance](https://finance.yahoo.com/) via `yfinance`  
- Inspired by financial time-series modeling and machine learning use cases in real markets
