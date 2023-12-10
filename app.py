from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
  {
    'id':1,
    'title': 'ML engineer',
    'salary': 150000,
    'mode':'online',
    'experience':'2 yrs' 
  },

  {
    'id':2,
    'title': 'Intern MLOps',
    'salary': 60000 ,
    'mode':'hybrid',
    'experience':'6 months' 
  },
  {
    'id':3,
    'title': 'Data Scientist',
    'salary': 120000 ,
    'mode':'office',
    'experience':'2 years' 
  },
  {
    'id':4,
    'title': 'Data Engineer',
    'salary': 120000 ,
    'mode':'remote',
    'experience':'1 years' 
  }

  
]

@app.route("/")
def hello_world():
    return render_template('home.html', jobs=JOBS)

@app.route("/api/jobs")
def joblist():
  return jsonify(JOBS)
     



if __name__=="__main__":
  app.run(host='0.0.0.0', debug=True)
