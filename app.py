from flask import Flask, render_template, request
import PyPDF2
import os
from utils import analyze_text

app = Flask(__name__)
UPLOAD_FOLDER = "uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

def extract_text(file):
    reader = PyPDF2.PdfReader(file)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text

@app.route("/", methods=["GET", "POST"])
def index():
    result = None

    if request.method == "POST":
        file = request.files["file"]
        filepath = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
        file.save(filepath)

        with open(filepath, "rb") as f:
            text = extract_text(f)

        result = analyze_text(text[:3000])  # limit text

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)