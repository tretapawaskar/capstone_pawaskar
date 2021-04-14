import os
from forms import AddForm
from flask import Flask, render_template, url_for, redirect , request
from werkzeug.utils import secure_filename
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import pandas as pd


app = Flask(__name__)

app.config['SECRET_KEY'] = 'SECRET_KEY'

basedir = os.path.abspath(os.path.dirname(__file__))
##app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:Silver@123@localhost/salesordersdb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app,db)


#UPLOAD_FOLDER = 'static/files'
#app.config['UPLOAD_FOLDER'] =  UPLOAD_FOLDER

class UI(db.Model):

    __tablename__ = 'ui'
    sales_index = db.Column(db.Integer, primary_key=True, autoincrement=True)
    PROD_CODE = db.Column(db.Text)
    emp_id = db.Column(db.Text)
    year = db.Column(db.Integer)
    week_num = db.Column(db.Integer)
    quantity = db.Column(db.Integer)
    Extended_Service_Plan = db.Column(db.Text)

    def __init__(self,PROD_CODE, emp_id,year,week_num ,quantity, Extended_Service_Plan ):
        self.PROD_CODE = PROD_CODE
        self.emp_id = emp_id
        self.year = year
        self.week_num = week_num
        self.quantity = quantity
        self.Extended_Service_Plan = Extended_Service_Plan


    def __repr__(self):
        if self.PROD_NAME:
            return f"Production order {self.PROD_NAME} successfully added"
        else:
            return f"Production order {self.PROD_NAME} not added"

######################################################
### Below code is added for restoring EMPLOYEE data from UI
######################################################
class employees(db.Model):

    __tablename__ = 'employees'
    emp_id = db.Column(db.Text, primary_key=True)
    paygrade = db.Column(db.Text)
    region = db.Column(db.Text)
    emp_name = db.Column(db.Text)

    def __init__(self,emp_id,paygrade,region,emp_name):
        self.emp_id = emp_id
        self.paygrade = paygrade
        self.region = region
        self.emp_name = emp_name

    def __repr__(self):
        return f"paygrade :{self.paygrade} emp_id: {self.emp_id} region: {self.region}  emp_name : {emp_name}  "


    #########added class sales

class Sale(db.Model):

    __tablename__ = 'sales'
    sales_index = db.Column(db.Integer, primary_key=True)
    PROD_CODE = db.Column(db.Text, db.ForeignKey('products.PROD_CODE'))
    emp_id = db.Column(db.Text, db.ForeignKey('employees.emp_id'))
    year = db.Column(db.Integer)
    total_sales = db.Column(db.Integer)


    def __init__(self, PROD_CODE, emp_id, year, week_sales, quarter_sales):
        self.PROD_CODE = PROD_CODE
        self.emp_id = emp_id
        self.year = year
        self.total_sales = total_sales


    def __repr__(self):
        if self.PROD_CODE:
            return f"Production order {self.PROD_CODE} successfully added"
        else:
            return f"Production order {self.PROD_CODE} not added"



######################################################
### Below code is added for restoring PRODUCT data from UI
######################################################
class product(db.Model):
    __tablename__ = 'product'
    prod_code = db.Column(db.String(100), primary_key = True)
    prod_name = db.Column(db.String(100))
    url =db.Column(db.String(100))
    link =db.Column(db.String(100))
    manufacturer =db.Column(db.String(100))
    extended_service_plan = db.Column(db.String(100))
    warranty_price = db.Column(db.Integer)


    def __init__(self,prod_code,prod_name,url,link,manufacturer,extended_service_plan,warranty_price):
        self.prod_code = prod_code
        self.prod_name = prod_name
        self.url = url
        self.link = link
        self.manufacturer = manufacturer
        self.extended_service_plan = extended_service_plan
        self.warranty_price= warranty_price


    def __repr__(self):
        return f"prod_code :{self.prod_code} prod_name: {self.prod_name}  url : {self.url}  manufacturer : {self.manufacturer}  extended_service_plan : {self.extended_service_plan}  warranty_price : {self.warranty_price}  "

#############################################################
@app.route('/')
def index():
    return render_template('home.html')

@app.route("/image002.jpg")
def image():
    return render_template("image002.jpg")

@app.route('/success')
def success():
    return render_template('success.html')

@app.route('/success_upload')
def success_upload():
    return render_template('success_upload.html')
################### Code for Adding order ##############
@app.route('/add', methods=['GET', 'POST'])
def add_order():
    form = AddForm()

    if form.validate_on_submit():
        PROD_CODE = form.PROD_CODE.data
        emp_id = form.emp_id.data
        year = form.year.data
        week_num = form.week_num.data
        quantity = form.quantity.data
        Extended_Service_Plan = form.Extended_Service_Plan.data

        if not PROD_CODE or not emp_id or not year or not week_num or not quantity or not Extended_Service_Plan :
            return render_template('add.html', form=form)

        new_order = UI(PROD_CODE,emp_id,year,week_num,quantity,Extended_Service_Plan)
        db.session.add(new_order)
        db.session.commit()

        return redirect(url_for('success'))
    return render_template('add.html', form=form)
############################################
def parseCSV1(file_path):
    # CVS Column Names
    col_names = ['prod_code', 'prod_name', 'url', 'link', 'manufacturer', 'extended_service_plan', 'warranty_price']
    # Use Pandas to parse the CSV file
    csvData = pd.read_csv(file_path, names=col_names, header=None)
    # Loop through the Rows
    for i, row in csvData.iterrows():
        prod_code = (row['prod_code'])
        prod_name = (row['prod_name'])
        url = (row['url'])
        link = (row['link'])
        manufacturer = (row['manufacturer'])
        extended_service_plan = (row['extended_service_plan'])
        warranty_price = (row['warranty_price'])

        Addproduct = product(prod_code, prod_name, url, link, manufacturer, extended_service_plan, warranty_price)
        db.session.add(Addproduct)
        db.session.commit()
######################################################
###############To restore product data ######################
@app.route('/restore_data')
def restore_data():
    return render_template('restore.html')
############################################################
UPLOAD_FOLDER = 'static/files'
app.config['UPLOAD_FOLDER'] =  UPLOAD_FOLDER

@app.route('/uproduct')
def uproduct():
     # Set The upload HTML template '\templates\index.html'
    return render_template('restore.html')

@app.route("/uproduct", methods=['POST'])
def uploadFiles1():
      # get the uploaded file
      uploaded_file = request.files['file']
      if uploaded_file.filename != '':
           file_path = os.path.join(app.config['UPLOAD_FOLDER'], uploaded_file.filename)
          # set the file path
           uploaded_file.save(file_path)
           parseCSV1(file_path)
          # save the file
      return render_template('success_upload.html')

###################################################################
if __name__ == '__main__':
    app.run(debug=True)