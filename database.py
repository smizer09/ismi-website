from sqlalchemy import create_engine, text
import os

DB_connection_string = os.environ['DB_CONNECTION_STRING']
engine = create_engine(DB_connection_string,connect_args={"ssl":{
  "ssl_ca": "/etc/ssl/cert.pem"
}})


def load_jobs_DB():
  
  with engine.connect() as conn:
    result = conn.execute(text("select * from job"))
    jobs = []
    for row in result.all():
    
      row_as_dict = row._mapping
      jobs.append(dict(row_as_dict))
    
  return jobs


def load_job_DB(id):
  
  with engine.connect() as conn:
    result = conn.execute(text("SELECT * FROM job WHERE id = {} ".format(id) ))
    job = []
    

    for row in result.all():
      a = row._mapping
      job.append(dict(a))
  return job

def add_app_DB(job_id , data ):
  with engine.connect() as conn:
    
    
    conn.execute(text("INSERT INTO applications(job_id, full_name, email, linkedin_url, education, work_experience, resume_url)  Values ('{}', '{}','{}','{}', '{}' , '{}' , '{}')" .format(job_id , data['full_name'], data['email'], data['linkedin_url'], data['education'], data['work_experience'], data['resume_url']) ))
    
    
    
    

  
              
  
    
  
  
   

