import pandas as pd
from flask import Flask, render_template
from Titanic_Script import titanic_script
from Finance_Script import finance_script

app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html')


css_header = '''<link rel="stylesheet" type="text/css" href="df_style.css"/>'''


@app.route("/titanic-script")
def titanic():
    titanic_script()
    df1 = pd.read_excel('Reversed_Columns.xlsx').fillna(' ')
    df2 = pd.read_excel('Removed_Every_Other_Column.xlsx').fillna('')
    return render_template('titanic-script.html', tables=[df1.to_html(), df2.to_html()])


@app.route("/finance-script")
def finance():
    finance_script()
    df = pd.read_excel('Finance_Data.xlsx').fillna('')
    return render_template('finance-script.html', tables=[df.to_html()])


if __name__ == '__main__':
    app.run(host='0.0.0.0')
