from flask import Flask, render_template, jsonify, request
from database import load_jobs_DB, load_job_DB, add_app_DB
app = Flask(__name__)

@app.route("/")
def hello_world():
    applications = load_jobs_DB()
    return render_template('home.html' , applications = applications)

@app.route("/job/<id>")
def show_jobs(id):
    jobs = load_job_DB(id)
     
    return render_template('jobpage.html' , jobs=jobs)
    

@app.route("/job/<id>/apply", methods=['post'])
def apply_to_jobs(id):
  data = request.form
  job = load_job_DB(id)
  add_app_DB(id, data)

  return render_template('application_sub.html', applications=data ) 
  
@app.route("/api/jobs")
def list_jobs():
  job = load_jobs_DB()
  return jsonify(jobs)

  


if __name__ == "__main__":
  app.run( host = '0.0.0.0', debug=True)