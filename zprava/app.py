# Import a vytvoření instance Flasku
from flask import Flask, render_template, make_response
app = Flask(__name__)

# Naimportování knihovny na vytváření PDF souborů
import pdfkit

@app.route("/")
def make_report():
        return render_template("index.html")

# Export faktury jako PDF
@app.route("/api/pdf/", methods = ['POST'])
def download_pdf():
        html = render_template("report.html")
        options = {
            'page-size': 'A4',
        }
        pdf = pdfkit.from_string(html, False, options=options)
        response = make_response(pdf)
        response.headers["Content-Type"] = "application/pdf"
        response.headers["Content-Disposition"] = "inline; filename=zprava.pdf"
        return response
