# 🚗 **# Used Car Price Prediction**  

## 📌 ## Project Overview  
This project aims to build a "machine learning model to predict the price of used cars based on various attributes such as brand, model, year, mileage, fuel type, and transmission. The model is trained using **RandomForestRegressor** and deployed as an API using **FastAPI**.  

---

## 📂 ## Dataset Description  
- **Source:** Kaggle ([https://www.kaggle.com/datasets/mohitkumar282/used-car-dataset](#))  
- **License:** CC BY 4.0 (Allows reuse with proper attribution)  
- **Structure:** The dataset contains features such as:  
  - 🏎 **Brand & Model** – Car manufacturer and specific model  
  - 📅 **Year** – Year of manufacture  
  - ⏳ **Age** – Age of the car (Current Year - Year)  
  - 🔢 **kmDriven** – Total kilometers driven  
  - ⚙️ **Transmission** – Type of transmission (Manual/Automatic)  
  - 👥 **Owner** – Number of previous owners  
  - ⛽ **FuelType** – Type of fuel (Petrol/Diesel/CNG/Electric)  
  - 💰 **AskPrice** – Listed price of the car (Target Variable)  

---

## 🛠 ## Tech Stack  
✅ **Python** 🐍  
✅ **pandas & numpy** 📊  
✅ **scikit-learn** 🤖  
✅ **matplotlib & seaborn** 📈  
✅ **FastAPI** 🚀 (for API deployment)  
✅ **Joblib** (for model persistence)  

---

## 📊 ## Machine Learning Pipeline  
### **1️⃣ Data Preprocessing**  
   - Handling missing values  
   - Encoding categorical variables  
   - Scaling numerical features  
   - Feature selection  
   
### **2️⃣ Model Training**  
   - Train-test split (80%-20%)  
   - **RandomForestRegressor** used for prediction  
   - Hyperparameter tuning for better accuracy  

### **3️⃣ Model Evaluation**  
   - **Mean Squared Error (MSE)**  
   - **R² Score**  
   - Visualization of Residuals & Predictions  

### **4️⃣ Model Deployment**  
   - Trained model saved as `used_car_price_model.pkl`  
   - API built using **FastAPI**  
   - JSON-based API for real-time predictions  

---

## 🚀 ## How to Use  
### 📥 **Clone the Repository**  
```bash
git clone https://github.com/betel09/used-car-price-prediction.git
cd used-car-price-prediction
