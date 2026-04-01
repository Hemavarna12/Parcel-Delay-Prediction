# Parcel Delivery Delay Prediction

Predict whether a parcel delivery will be delayed using Python and Machine Learning.

This project simulates real-world logistics data and demonstrates **data analysis, feature engineering, ML modeling, and deployment via a Streamlit app**.

---

## 🚀 Problem Statement

Parcels may be delayed due to traffic, weather, distance, and peak delivery hours.

The goal is to **predict whether a delivery will be delayed** and provide insights for logistics optimization.

**Key Questions:**

- Which deliveries are likely to be late?
- What factors most influence delays?
- How can delivery performance be improved?

---

## 📂 Dataset

- Generated a synthetic dataset of 2,000 deliveries.

**Features include:**

| Feature         | Description                            |
|-----------------|----------------------------------------|
| distance_km     | Distance of delivery in kilometers     |
| traffic         | Traffic condition: Low, Medium, High  |
| weather         | Weather condition: Clear, Rain, Storm |
| vehicle         | Vehicle type: Bike, Van, Truck        |
| hour            | Hour of delivery (0–23)               |
| delivery_time   | Actual delivery time in minutes       |
| expected_time   | Expected delivery time in minutes     |
| delayed         | Target: 0 = On-time, 1 = Delayed     |

---

## 🧠 Approach

1. **Data Preprocessing & Feature Engineering**
   - Handled categorical variables with one-hot encoding
   - Created `is_peak` feature for peak delivery hours

2. **Machine Learning Models**
   - Logistic Regression (baseline)
   - Random Forest Classifier (primary model)

3. **Evaluation Metrics**
   - Accuracy, Precision, Recall, F1-score
   - Confusion Matrix for model performance

4. **Business Insights**
   - Feature importance analysis to identify factors causing delays

5. **Deployment**
   - Streamlit app for live prediction input
   - Users can enter delivery details and get delay prediction instantly

---

## 📊 Results

- Random Forest achieved **~90% accuracy**
- Key factors impacting delivery delays:
  - Traffic condition (high traffic increases delay risk)
  - Weather (storm/rain increases delays)
  - Distance
  - Peak delivery hours

---

## 🖼️ Screenshot

**Example Prediction in Streamlit App:**

![Streamlit App Screenshot](app_screenshot.png)

> Note: JS warnings (fetch errors) may appear in Colab/localtunnel, but the prediction functionality works correctly.

---

## 🖥️ Run Locally

1. Install dependencies:

```bash
pip install pandas numpy scikit-learn matplotlib seaborn streamlit joblib
