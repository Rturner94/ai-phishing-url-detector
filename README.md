# 🔐 AI Phishing URL Detector

This project is a machine learning-powered phishing URL detector built using Python, scikit-learn, and Streamlit. It analyzes structured URL-based features to determine whether a link is **phishing** or **legitimate** — and offers an easy-to-use web interface for quick testing.


## 📊 Features

- Trained on real-world phishing data  
- Detects phishing vs. legitimate URLs  
- Uses Random Forest for classification  
- Scaled and split data for accuracy  
- Interactive web app built with Streamlit  
- Upload a CSV file to get predictions  


## 🖥️ App Preview

![Phishing App Preview](https://github.com/user-attachments/assets/06972b6b-c236-49e0-82b5-db2d10b66b3d)



## 🚀 Demo

To launch the app locally:

```bash
streamlit run app.py
```

Then open the URL in your browser (usually http://localhost:8501).

Upload a properly formatted CSV file (see below) and view predictions instantly.


## 🧪 Sample Input Format

Upload a CSV that includes the same features used during training.  
You can test with the included:

```
test_input_compatible.csv
```

It contains:
- All required feature columns  
- No "status" column (label is removed)


## ✅ Model Performance

- Accuracy: ~95%  
- Precision: High for both classes  
- Algorithm: Random Forest Classifier  
- Evaluation: Train/test split with classification report


## 📂 Project Structure

```
├── app.py                    # Streamlit web app
├── phishing_detector.py      # ML training and evaluation script
├── phishing_dataset.csv      # Raw dataset
├── requirements.txt          # Dependencies
├── test_input_compatible.csv # Sample input file
├── phishing_app_preview.png  # App preview image
```

---

## 📦 Installation

1. Clone the repo:
```bash
git clone https://github.com/Rturner94/ai-phishing-url-detector.git
cd ai-phishing-url-detector
```

2. Install requirements:
```bash
pip install -r requirements.txt
```

3. Run the app:
```bash
streamlit run app.py
```


## 🧠 Skills Demonstrated

- Python  
- Pandas  
- Scikit-learn  
- Streamlit  
- Data preprocessing  
- Model evaluation  
- Git & GitHub


## 📊 Dataset Source

This project uses the [Phishing Website Detector Dataset](https://www.kaggle.com/datasets/sid321axn/phishing-website-detector) from Kaggle.


## 🛠️ Future Improvements

- Add manual URL entry form for live predictions  
- Deploy on Streamlit Cloud or Hugging Face Spaces  
- Improve feature engineering and feature selection  
- Integrate live URL scanning APIs for real-time detection  


## 🧑‍💼 About Me

Hi, I’m **Ricky Turner** — an aspiring Cybersecurity Analyst passionate about leveraging data and AI to fight online threats. This project highlights my ability to build hands-on tools that solve real-world security problems.


## 🪪 License

This project is licensed under the MIT License.

## 📫 Connect with Me

- GitHub: [@Rturner94](https://github.com/Rturner94) 
