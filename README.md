#  Smart Phishing Detection System

A Machine Learning based web application that detects whether a given URL is **Phishing** or **Legitimate**.

---

##  Project Overview

Phishing websites are fraudulent sites designed to steal sensitive information like passwords, credit card numbers, and personal data.

This project uses **Machine Learning (Logistic Regression)** to analyze URL features and predict whether a website is phishing or safe.

---

##  Features

*  URL-based phishing detection
*  Machine Learning model (Scikit-learn)
*  Web interface using Flask
*  Simple and clean UI
*  Instant prediction result

---

##  Technologies Used

* Python 3.11
* Flask
* Scikit-learn
* Pandas
* HTML & CSS

---

##  Project Structure

```
Smart-Phishing-Detection-System/
│
├── app.py
├── model.py
├── dataset.csv
├── phishing_model.pkl
│
├── static/
│     └── style.css
│
└── templates/
      └── index.html
```

---

## ⚙️ How It Works

1. The user enters a URL.
2. The system extracts important features like:

   * URL length
   * Presence of IP address
   * Special characters
3. The trained ML model analyzes these features.
4. The system predicts:

   *  Legitimate Website
   *  Phishing Website

---

##  How to Run the Project

### 1️. Install Python 3.11

### 2️. Install required libraries

```bash
pip install flask pandas scikit-learn
```

### 3️. Train the model (if not trained)

```bash
python model.py
```

### 4️. Run the application

```bash
python app.py
```

Open browser and go to:

```
http://127.0.0.1:5000
```

---

##  Sample Test URLs

* http://paypal-login-security-update.com
* http://192.168.1.1/login
* http://verify-your-bank-account-now.com

---

##  Future Improvements

* Deep learning model
* Real-time website scanning
* Database logging
* Deployment on cloud (Heroku / Render)

---

