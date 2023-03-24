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
    
  
  
   
my_secret = os.environ['DB_CONNECTION_STRING']
