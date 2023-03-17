from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
  {
    'id':1,
    'title':'Data analyst',
    'location':'addis ababa',
    'salary':'etb. 120,000'
  },
  {
    'id':2,
    'title':'Data scientist',
    'location':'addis ababa',
    'salary':'etb. 130,000'
  },
  {
    'id':3,
    'title':'front end engineer',
    'location':'addis ababa',
    'salary':'etb. 110,000'
  },
  {
    'id':4,
    'title':'back end engineer',
    'location':'addis ababa',
    'salary':'etb. 140,000'
  }
]
@app.route("/")
def hello_world():
    return render_template('home.html' , jobs=JOBS)

@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)

  


if __name__ == "__main__":
  app.run( host = '0.0.0.0', debug=True)