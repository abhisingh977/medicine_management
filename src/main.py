from flask import Flask, render_template_string, render_template, request
from werkzeug.utils import secure_filename
import pandas as pd

from app.generate_html import generate_html

app = Flask(__name__)

@app.route("/")
def home():
   return render_template("home.html")

@app.route('/refund')
def refund():
   refund_data = {
    'Nov_2023': {
        'loss': 1000,
        'recovery': 800,
        'profit': 200
    },
    'Dec_2023': {
        'loss': 1200,
        'recovery': 1000,
        'profit': 200
    },
    'Jan_2024': {
        'loss': 800,
        'recovery': 900,
        'profit': 100
    },
    'Feb_2024': {
        'loss': 1500,
        'recovery': 1300,
        'profit': 200
    }
}
   return render_template("refund.html", refund_data=refund_data)

@app.route('/handle_refund/<string:refund_date>')
def handle_refund(refund_date):
   df = None
   if refund_date=="Nov_2023":
      df = pd.read_csv('static/csvs/ex_army_ex_nov_2023.csv')
   elif refund_date=="Dec_2023":
      df = pd.read_csv('static/csvs/ex_army_ex_dec_2023.csv')


   if df is None:
      html = """<p>No data available for the selected refund date.</p>
         <form action="{{ url_for('handle_file_upload') }}" method="post" enctype="multipart/form-data">
         <label for="nearExpiryMedicine">Upload Near Expiry Medicine File for this month:</label>
         <input type="file" id="nearExpiryMedicine" name="nearExpiryMedicine" accept=".xls, .xlsx, .csv, .txt, application/vnd.ms-excel, application/vnd.openxmlformats-officedocument.spreadsheetml.sheet, text/plain">
         <input type="submit" value="Upload">
        </form>

      """
   else:
      html = generate_html(df)

   return render_template_string(html)


@app.route('/handle_file_upload', methods=['POST'])
def handle_file_upload():
    if 'nearExpiryMedicine' not in request.files:
        # No file part in the request
        return 'No file part'

    file = request.files['nearExpiryMedicine']

    if file.filename == '':
        # No selected file
        return 'No selected file'

    if file:
        # Secure the filename and save the file to a specific directory
        filename = secure_filename(file.filename)
        file.save(f'uploads/{filename}')  # Save to the 'uploads' directory, create it if not exists

        # Perform additional processing or redirect as needed
        return 'File uploaded successfully'

    return 'Error uploading file'


if __name__ == '__main__':
    app.run(debug=False, port=8080)

