from flask import Flask, render_template
app = Flask(__name__)


@app.route('/bmi/<weight>/<height>')
def calBMI(weight,height):
    BMI = float(weight)/(float(height)*float(height))
    result = ''
    if BMI < 16:
        result= "You are underweight!"
    elif BMI < 18.5:
        result= "You are underweight!"
    elif BMI < 25:
        result= "You are normal!"
    elif BMI < 30:
        result= "You are overweight!"
    elif BMI >= 30:
        result= "You are obese!"
    else:
        result= "Please input weight and height accurately!"

    return "Your BMI=" + str(BMI) + "    " + result 
if __name__ == '__main__':
  app.run(debug=True)
