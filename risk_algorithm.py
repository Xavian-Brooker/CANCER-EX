
# Importing Pandas for csv processing
import pandas as pd

# p_map is a dictionary containing the basic retrospective & dietary information of the patient
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
  'smoking':1,
  'nuts':0},
  'disease':{'diabetes':0,
  'pancreatitis':0,
  'familial':0,
  'f_smoking':0}}
'''

# Risk reducing factor:
# 1. Vegetarian Diet

# Risk increasing factors: 
# 1. Red Meat Nearly 120 Grams a Day   
# 2. Processed Meat nearly 50 grams a day 
# 3. Liquor/Spirit nearly 60 grams/L daily
# 4. Smoking nearly 3-5 cigarettes a day 
# 5. Body Mass Index > 25

# rr_map contains the relative risk increases due to these factors
# Data obtained from https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6396775/

'''
rr_map = {'vegetarian':0.9,
'red_meat':1.3,
'processed_meat':1.15,
'liquor_alcohol':1.3,
'smoking':2.0,
'nuts':0.65}
'''
rr_map = {'diet':{'vegetarian':0.9,
'red_meat':1.3,
'processed_meat':1.15,
'liquor_alcohol':1.3,
'smoking':2.0,
'nuts':0.65},
'disease':{'diabetes':1.8,
'pancreatitis':2.1,
'familial':2.08,
'f_smoking':1.2}}

# Importing the dataset into the dataframe according to Age, Sex & Region
# All datasets obtained from http://gco.iarc.fr/today/

def get_datasets(p_map):
	if int (p_map['age'])>=50:
	    if p_map['sex']=='M':
	        dataset = pd.read_csv('datasets/a_50_male.csv', engine='python')
	    else :
	        dataset = pd.read_csv('datasets/a_50_fem.csv', engine='python')

	elif int (p_map['age'])<50:
	    if p_map['sex']=='M':
	        dataset = pd.read_csv('datasets/b_50_male.csv', engine='python')
	    else :
	        dataset = pd.read_csv('datasets/b_50_fem.csv', engine='python')
	return dataset
        
def calculate_risk(dataset,p_map):
	# 1. Calculate the Initial Risk depending upon Location and age
	init_risk = (dataset.loc[dataset['Population'] == p_map['country']]).values[0][5]
	print('Initial Risk of developing Pancreatic Cancer due to your region of stay, age and sex is', init_risk)
	regional_risk = init_risk

	# 2. Decrease the Initial Risk by 10% if the diet is vegetarian
	if p_map['diet_type'] == 'V':
	    init_risk = rr_map['diet']['vegetarian']*init_risk

	# Calculate the increased risk due to diseases
	for d in p_map['disease']:
	    if(p_map['disease'][d]==1):
	        init_risk += init_risk*(rr_map['disease'][d]-1)
	    
	# Initialize a variable increase
	increase = 0

	# 3. Calculate Risk Increase due to obesity (BMI>25)
	p_bmi = float (p_map['weight'])/(float (p_map['height'])**2)
	if p_bmi >= 25:
	    increase += init_risk

	# 4. Calculate the Ris Increase due to Dietary Factors using Relative Risks from rr_map
	for j in p_map['diet']:
	    if(p_map['diet'][j]==1):
	        increase += init_risk*(rr_map['diet'][j]-1)

	r_type = 0
	p_increase = (increase+init_risk)/init_risk 
	if p_increase >= 3:
		r_type = 'substantially high risk increase'
	elif p_increase >=1.1:
		r_type = 'moderately/mildly high risk increase'
	else:
		r_type = 'no such risk increase' 


	# Finally print the total risk and risk increase
	# print('Your final Risk According the above mentioned details is', init_risk+increase, 'Increase in risk due to your diet is', increase)
	return init_risk, increase, regional_risk, r_type


def return_results(init_risk, regional_risk, increase, r_type, p_map):
	p1 = 'You rinitial (unchangable) risk of developing pancreatic cancer in your lifetime due to your age, sex, country of Incidence or any family relative suffering from pancreatic cancer is:'+ str(init_risk) + '%. It is already ' + str((init_risk-regional_risk)) + '% more than the national average of ' + p_map['country'] + ' which is ' + str(regional_risk) + '%'
	p2 = 'You have a ' + r_type + ' for Pancreatic Cancer due to your dietary preferences and alcohol/smoking (if). Your increase in risk due to these factors are ' + str(increase) +'%. Your (%) risk increase is ' + str((init_risk+increase)/init_risk)
	p4 = 'If you\'d like to reduce your risk than try switching to a vegan/vegetarian lifestyle, reduce meat consumption & avoid smoking/liquor (if). Try eating almonds and hazelhuts too!'
	
	if r_type == 'substantially high risk increase':
		p3 = 'If you are observing Pancreatic Cancer symptoms such as gastric pain, sudden onset of diabetes etc. than you should definitely consider taking the Spermine Lateral Flow Test.'
	else :
		p3 = 'As you don\'t have a Substantially high risk for Pancreatic Cancer, you may or may not chose to take the Spermine test depending on the signs & symptoms you are observing'
	
	return p1,p2,p3,p4, r_type
