from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField,IntegerField

class AddForm(FlaskForm):
    PROD_CODE = StringField('Product Code       :')
    emp_id = StringField('Employee ID       :')
    year = StringField('Year   :')
    week_num = StringField('Week Number: ')
    quantity = StringField('Provide Quantity: ')
    Extended_Service_Plan = StringField('Provide code for extended service plan:')
    submit = SubmitField('Add Order')


class AddRestoreForm(FlaskForm):
    uploaded_file = StringField('attach file here:')
    submit = SubmitField('Add Order')


