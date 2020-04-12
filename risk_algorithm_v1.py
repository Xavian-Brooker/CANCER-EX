
# Importing Pandas for csv processing
import pandas as pd

# p_map is a dictionary containing the basic retrospective & dietary information of the patient
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
rr_map = {'vegetarian':0.9,
'red_meat':1.3,
'processed_meat':1.15,
'liquor_alcohol':1.3,
'smoking':2.0,}

# Importing the dataset into the dataframe according to Age, Sex & Region
# All datasets obtained from http://gco.iarc.fr/today/

def get_datasets(p_map):
	if int (p_map['age'])>=50:
	    if p_map['sex']=='M':
	        dataset = pd.read_csv('datasets/a_50_male.csv')
	    else :
	        dataset = pd.read_csv('datasets/a_50_fem.csv')

	elif int (p_map['age'])<50:
	    if p_map['sex']=='M':
	        dataset = pd.read_csv('datasets/b_50_male.csv')
	    else :
	        dataset = pd.read_csv('datasets/b_50_fem.csv')
	return dataset
        
def calculate_risk(dataset,p_map):
	# 1. Calculate the Initial Risk depending upon Location and age
	init_risk = (dataset.loc[dataset['Population'] == p_map['country']]).values[0][5]
	print('Initial Risk of developing Pancreatic Cancer due to your region of stay, age and sex is', init_risk)

	# 2. Decrease the Initial Risk by 10% if the diet is vegetarian
	if p_map['diet_type'] == 'V':
	    init_risk = rr_map['vegetarian']*init_risk
	    
	# Initialize a variable increase
	increase = 0

	# 3. Calculate Risk Increase due to obesity (BMI>25)
	p_bmi = float (p_map['weight'])/(float (p_map['height'])**2)
	if p_bmi >= 25:
	    increase += init_risk

	# 4. Calculate the Ris Increase due to Dietary Factors using Relative Risks from rr_map
	for j in p_map['diet']:
	    if(p_map['diet'][j]==1):
	        increase += init_risk*(rr_map[j]-1)

	return init_risk, increase
	# Finally print the total risk and risk increase
	# print('Your final Risk According the above mentioned details is', init_risk+increase, 'Increase in risk due to your diet is', increase)

'''
dataset=get_datasets(p_map)
calculate_risk(dataset,p_map)
'''