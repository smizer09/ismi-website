from flask import Flask, render_template, jsonify
from database import load_jobs_DB, load_job_DB
app = Flask(__name__)

@app.route("/")
def hello_world():
    jobs = load_jobs_DB()
    return render_template('home.html' , jobs = jobs)

@app.route("/job/<id>")
def show_jobs(id):
    job = load_job_DB(id)
     
    return render_template('jobpage.html' , job = job)
    

@app.route("/api/jobs")
def list_jobs():
  job = load_jobs_DB()
  return jsonify(jobs)

  


if __name__ == "__main__":
  app.run( host = '0.0.0.0', debug=True)