\# Parcel Delivery Delay Prediction



Predict whether a parcel delivery will be delayed using Python and Machine Learning.  

This project simulates real-world logistics data and demonstrates data analysis, feature engineering, ML modeling, and deployment via a Streamlit app.



\---



\## 🚀 Problem Statement



Parcels may be delayed due to traffic, weather, distance, and peak delivery hours.  

The goal is to \*\*predict whether a delivery will be delayed\*\* and provide insights for logistics optimization.



\*\*Key Questions:\*\*



\- Which deliveries are likely to be late?  

\- What factors most influence delays?  

\- How can delivery performance be improved?



\---



\## 📂 Dataset



\- Generated a synthetic dataset of 2000 deliveries.  

\- Features include:



| Feature | Description |

|---------|-------------|

| `distance\_km` | Distance of delivery in kilometers |

| `traffic` | Traffic condition: Low, Medium, High |

| `weather` | Weather condition: Clear, Rain, Storm |

| `vehicle` | Vehicle type: Bike, Van, Truck |

| `hour` | Hour of delivery (0–23) |

| `delivery\_time` | Actual delivery time in minutes |

| `expected\_time` | Expected delivery time in minutes |

| `delayed` | Target: 0 = On-time, 1 = Delayed |



\---



\## 🧠 Approach



1\. \*\*Data Preprocessing \& Feature Engineering\*\*

&#x20;  - Handled categorical variables with \*\*one-hot encoding\*\*  

&#x20;  - Created `is\_peak` feature for peak delivery hours



2\. \*\*Machine Learning Models\*\*

&#x20;  - Logistic Regression (baseline)  

&#x20;  - Random Forest Classifier (primary model)



3\. \*\*Evaluation Metrics\*\*

&#x20;  - Accuracy, Precision, Recall, F1-score  

&#x20;  - Confusion Matrix for model performance



4\. \*\*Business Insights\*\*

&#x20;  - Feature importance analysis to identify factors causing delays  



5\. \*\*Deployment\*\*

&#x20;  - Streamlit app for live prediction input  

&#x20;  - Users can input delivery details and get delay prediction instantly  



\---



\## 📊 Results



\- Random Forest achieved \*\*\~90% accuracy\*\*  

\- Key features impacting delivery delays:

&#x20; - Traffic condition (High traffic increases delay risk)  

&#x20; - Weather (Storm/Rain increases delays)  

&#x20; - Distance  

&#x20; - Peak delivery hours  



\---



\## 🖼️ Screenshot



\*\*Example Prediction in Streamlit App:\*\*  



!\[Streamlit App Screenshot](app\_screenshot.png)



> Note: JS warnings (fetch errors) may appear in Colab/localtunnel. The prediction functionality works correctly.



\---



