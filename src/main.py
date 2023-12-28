from flask import Flask, render_template_string, render_template
import pandas as pd

from app.generate_html import generate_html

app = Flask(__name__)

@app.route("/")
def home():
   return render_template("home.html")

@app.route('/refund')
def refund():
   return render_template("refund.html")


@app.route('/handle_refund/<string:refund_date>')
def handle_refund(refund_date):
   if refund_date=="Nov_2023":
      df = pd.read_csv('medicine_management/src/static/csvs/ex_army_ex_nov_2023.csv')
   elif refund_date=="Dec_2023":
      df = pd.read_csv('medicine_management/src/static/csvs/ex_army_ex_dec_2023.csv')
   
   html = generate_html(df)

   return render_template_string(html)

if __name__ == '__main__':
    app.run(debug=False, port=8080)
