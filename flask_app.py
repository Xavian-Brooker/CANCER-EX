from flask import Flask, render_template, url_for, flash, redirect, request
from forms import UserForm
import risk_algorithm

app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'

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

p_info={}

@app.route("/", methods=['GET','POST'])
@app.route("/home", methods=['GET', 'POST'])
def home():
    form = UserForm()
    
    if form.validate_on_submit():
        # a.append(form.username.data)

        p_info.update({'name':form.name.data,
            'age':form.age.data,
            'sex':form.sex.data,
            'height':form.height.data,
            'weight':form.weight.data,
            'country':form.country.data,
            'diet_type':form.diet_type.data,
            'diet':{'red_meat':int(form.red_meat.data),
                        'processed_meat':int(form.processed_meat.data),
                        'liquor_alcohol':int(form.liquor_alcohol.data),
                        'smoking':int(form.smoking.data),
                        'nuts':int(form.nuts.data)},
            'disease':{'diabetes':int(form.diabetes.data),
                        'pancreatitis':int(form.pancreatitis.data),
                        'f_smoking':int(form.f_smoking.data),
                        'familial':int(form.familial.data)}})
        
        flash(f'Information submitted for {form.name.data}!', 'success')
        return redirect(url_for('results'))
    
    return render_template('home.html', form=form)

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/results", methods=['GET', 'POST'])
def results():
    dataset = risk_algorithm.get_datasets(p_info)
    init_risk, increase, regional_risk, r_type = risk_algorithm.calculate_risk(dataset=dataset, p_map=p_info)
    # print(p_info, init_risk, increase)
    p1,p2,p3,p4, r_type = risk_algorithm.return_results(init_risk=init_risk, regional_risk=regional_risk, increase=increase, r_type=r_type, p_map=p_info)
    
    if r_type=='substantially high risk increase':
        color = 'p-3 mb-2 bg-danger text-white'
    elif r_type=='moderately/mildly high risk increase':
        color = 'p-3 mb-2 bg-warning text-dark'
    else:
        color = 'p-3 mb-2 bg-success text-white'

    return render_template('results.html', name=p_info['name'], p1=p1, p2=p2, p3=p3,p4=p4, color=color)

if __name__ == '__main__':
    app.run(debug=True)