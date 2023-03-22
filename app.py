from flask import Flask, render_template, jsonify
from database import load_jobs_DB
app = Flask(__name__)

@app.route("/")
def hello_world():
    job = load_jobs_DB()
    return render_template('home.html' , job = job)

@app.route("/api/jobs")
def list_jobs():
  job = load_jobs_DB()
  return jsonify(job)

  


if __name__ == "__main__":
  app.run( host = '0.0.0.0', debug=True)