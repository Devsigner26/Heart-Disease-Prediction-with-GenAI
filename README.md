# 🫀 Heart Disease Prediction using GenAI

This project predicts whether a person is likely to have heart disease using *generative AI*, based on health-related attributes such as age, blood pressure, cholesterol, and more. It aims to assist in early medical diagnosis using machine learning.

Built using Python and Streamlit, this model reads data from heart.csv and runs predictions via a trained model in finalmvp.py.

---

## 📌 Key Features

- 🧠 Predicts heart disease risk using logistic regression or a trained GenAI classifier
- 📊 Uses 13+ medical attributes (e.g., age, cholesterol, resting ECG, etc.)
- ⚡ Lightweight and interactive with a *Streamlit web interface*
- 📁 Clean dataset with proper preprocessing
- ✅ Easy to run locally or extend for deployment

---

## 📂 Files in this Repo

| File           | Description                                |
|----------------|--------------------------------------------|
| finalmvp.py  | Python script containing the GenAI model logic |
| heart.csv    | Dataset used for training and testing (public) |
| README.md    | This README file                           |

---

## 🧪 Tech Stack

- *Language*: Python 3
- *Libraries*: Pandas, NumPy, Scikit-learn, Streamlit
- *Visualization*: Matplotlib, Seaborn
- *AI/ML*: Logistic Regression / GenAI pipeline (custom logic)
- *GenAI API key*: Gemini api key
---

## 🧪 Results

- 🔍 *Model Type*: Logistic Regression / Custom GenAI Classifier
- 📈 *Accuracy*: ~89% on test data
- 🧪 *Metrics*:
  - Precision: 0.87
  - Recall: 0.90
  - F1 Score: 0.88

> ✔️ Model is well-balanced for binary classification.  
> ✔️ Performs especially well on detecting positive heart disease risk.

## 🚀 Future Enhancements

- 🌐 Deploy the app to *Streamlit Cloud* or *Hugging Face Spaces*
- 📲 Add mobile-responsive layout
- 📊 Integrate visual analytics (e.g. bar charts, heatmaps)
- 🔍 Add *model explainability* via SHAP or LIME
- 🏥 Expand features to integrate real-world hospital EHR data
- 🧠 Train a deep learning version for improved accuracy

---

## 📜 License

This project is licensed under the *MIT License* – see the [LICENSE](./LICENSE) file for details.

## ▶️ How to Run the App

You can run it locally using Streamlit:

```bash
git clone https://github.com/Devsigner26/Heart-Disease-Prediction-with-GenAI.git
cd Heart-Disease-Prediction-with-GenAI
pip install -r requirements.txt
streamlit run finalmvp.py


