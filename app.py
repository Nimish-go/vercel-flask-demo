from flask import Flask, render_template, jsonify, make_response
import pdfkit
import os

app = Flask(__name__)

# Path to wkhtmltopdf binary inside bin/
wkhtmltopdfpath = os.path.join(os.path.dirname(__file__), 'bin', 'wkhtmltopdf')
config = pdfkit.configuration(wkhtmltopdf=wkhtmltopdfpath)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/downloadpdf')
def downloadPdf():
    html = render_template('index.html')
    pdf = pdfkit.from_string(html, False, configuration=config)

    response = make_response(pdf)
    response.headers['Content-Type'] = 'application/pdf'
    response.headers['Content-Disposition'] = 'attachment; filename=output.pdf'
    return response

if __name__ == '__main__':
    app.run(debug=True, port=5002)
