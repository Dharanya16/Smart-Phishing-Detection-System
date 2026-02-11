from flask import Flask, render_template, request
import pickle
import re

app = Flask(__name__)

# Load trained model
model = pickle.load(open("phishing_model.pkl", "rb"))

def extract_features(url):
    return [
        len(url),
        1 if url.startswith("https") else 0,
        1 if "@" in url else 0,
        1 if re.search(r"\d+\.\d+\.\d+\.\d+", url) else 0
    ]

@app.route("/", methods=["GET", "POST"])
def index():
    prediction = ""
    if request.method == "POST":
        url = request.form["url"]
        features = [extract_features(url)]
        result = model.predict(features)[0]
        prediction = "⚠️ Phishing Website" if result == 1 else "✅ Safe Website"

    return render_template("index.html", prediction=prediction)

if __name__ == "__main__":
    app.run(debug=True)
