from flask import Flask,render_template,redirect,request
import joblib

app = Flask(__name__)
model = joblib.load('model.pkl')

@app.route("/")
def beginning():
    return render_template('index.html')

@app.route('/',methods=['POST'])
def predict():
    if request.method=='POST':
        prg = float(request.form['NumPregnancies'])
        glc =float(request.form['glc'])
        bp =float(request.form['bp'])
        skinthickness =float(request.form['skth'])
        insulin =float(request.form['ins'])
        bmi =float(request.form['bm'])
        dpf =float(request.form['dp'])
        age =float(request.form['ag'])
        pred = model.predict([[prg,glc,bp,skinthickness,insulin,bmi,dpf,age]])[0]
        return render_template("index.html",prediction= pred)

if __name__ == "__main__":
    app.run(debug=True)

