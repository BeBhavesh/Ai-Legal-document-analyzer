# ⚖️ AI Legal Document Analyzer

A simple AI/NLP-based web application that analyzes legal documents (PDF) and provides:
- 📄 Summary
- 📌 Key Clauses
- ⚠️ Risk Factors

---

## 🚀 Features

- Upload legal PDF documents
- Extract text using PyPDF2
- Generate summary automatically
- Detect key clauses (payment, termination, liability)
- Identify potential risks using keyword-based NLP

---

## 🧠 Tech Stack

- Python (Flask)
- PyPDF2 (PDF processing)
- HTML + Bootstrap (Frontend)
- NLP Logic (Keyword-based analysis)

---

## 📁 Project Structure

legal-analyzer/
│── app.py
│── utils.py
│── requirements.txt
│── templates/
│ └── index.html
│── static/
│ └── style.css
│── uploads/
│── README.md


---

## ⚙️ Setup & Run

### 1️⃣ Clone repo
```bash
git clone https://github.com/yourusername/legal-analyzer.git
cd legal-analyzer

2️⃣ Create virtual environment
python3 -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
3️⃣ Install dependencies
pip install -r requirements.txt
4️⃣ Run app
python3 app.py
5️⃣ Open browser
http://127.0.0.1:5000
