#import a lib
import joblib
from flask import Flask,render_template,request


#load a model

model = joblib.load('diabetic_79.pkl')


#create instance of app
app = Flask(__name__)

@app.route('/')
def form():
    return render_template('form.html')



@app.route('/data',methods = ["POST"])
def data():
#names = ['preg','plas','pres','skin','test','mass','pedi','age','class']
    pregnant = request.form.get("preg")
    plasma = request.form.get("plas")
    pressure = request.form.get("pres")
    skin= request.form.get("skin")
    test = request.form.get("test")
    mass = request.form.get("mass")
    pedi = request.form.get("pedi")
    age = request.form.get("age")
    print(pregnant)
    print(plasma)
    print(pressure)
    print(skin)
    print(test)
    print(mass)
    print(pedi)
    print(age)
 
    result = model.predict([[pregnant,plasma,pressure,skin,test,mass,pedi,age]])
    
    if result[0] == 0:
       output =  'Not diabetic'
    else:
        output = 'diabetic'
    
    return render_template('result.html',predict = output)

if __name__=='__main__':
    app.run(debug=True)


#http: hyper test transfer protocol
#html : HyperText Markup Language
