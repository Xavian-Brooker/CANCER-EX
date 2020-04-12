from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, DecimalField, SelectField
from wtforms.validators import DataRequired, Length, Email, EqualTo

'''
p_map = {'name':'Robert Downey',
 'age':51,
 'sex':'M',
 'height':1.81,
 'weight':74,
 'diet_type':'NV',
 'country':'United States of America',
 'diet':{'red_meat':1,
  'processed_meat':1,
  'liquor_alcohol':1,
  'smoking':1}}
'''

# 1. Red Meat Nearly 120 Grams a Day   
# 2. Processed Meat nearly 50 grams a day 
# 3. Liquor/Spirit nearly 60 grams/L daily
# 4. Smoking nearly 3-5 cigarettes a day 
# 5. Body Mass Index > 25


class UserForm(FlaskForm):
	
	name = StringField('Full Name',
		validators=[DataRequired()])

	country = StringField('Country of Residence', 
		validators=[DataRequired()])

	age = IntegerField('Age',
		validators=[DataRequired()])
	
	weight = IntegerField('Weight in Kilograms',
		validators=[DataRequired()])
	
	height = DecimalField('Height in meters',
		validators=[DataRequired()])

	sex = SelectField('Sex', 
		choices=[('M','Male'), ('F', 'Female')],
		validators=[DataRequired()])

	diet_type = SelectField('Diet Type',
		choices=[('V','Vegetarian'),('NV','Non Vegetarian')],
		validators=[DataRequired()])

	nuts = SelectField('Do you consume 1 ounce (28 grams) nuts (almonds, hazelnuts etc.) more than or twice a week?',
		choices=[('0','No'), ('1','Yes')],
		validators=[DataRequired()])

	red_meat = SelectField('Do you eat red meat nearly 120 grams a day?',
		choices=[('0','No'),('1','Yes')],
		validators=[DataRequired()])
	
	processed_meat = SelectField('Do you eat processed_meat nearly 50 grams a day?',
		choices=[('0','No'),('1','Yes')],
		validators=[DataRequired()])

	liquor_alcohol = SelectField('Do you consume Liquor/Spirit nearly 60 grams/L a day?',
		choices=[('0','No'),('1','Yes')],
		validators=[DataRequired()])	

	smoking = SelectField('Do you smoke nearly 3-5 cigarettes a day?',
		choices=[('0','No'),('1','Yes')],
		validators=[DataRequired()])
	
	f_smoking = SelectField('Were you a former smoker?',
		choices=[('0','No'),('1','Yes')],
		validators=[DataRequired()])

	diabetes = SelectField('Do you have Type 1/ Type 2 Diabetes?',
		choices=[('0','No'),('1','Yes')],
		validators=[DataRequired()])

	pancreatitis = SelectField('Do you have Acute/ Chronic Pancreatitis?',
		choices=[('0','No'),('1','Yes')],
		validators=[DataRequired()])

	familial = SelectField('Do you two or more first-order relatives with Pancreatic Cancer?',
		choices=[('0','No'),('1','Yes')],
		validators=[DataRequired()])


	submit = SubmitField('Submit')
