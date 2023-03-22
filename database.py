from sqlalchemy import create_engine, text

DB_connection_string = os.environ['DB_CONNECTION_STRING']
engine = create_engine(DB_connection_string,connect_args={"ssl":{
  "ssl_ca": "/etc/ssl/cert.pem"
}})


def load_jobs_DB():
  
  with engine.connect() as conn:
    result = conn.execute(text("select * from job"))
    job = []
    for row in result.all():
    
      row_as_dict = row._mapping
      job.append(dict(row_as_dict))
    
  return job
    
    
  
  
    
my_secret = os.environ['DB_CONNECTION_STRING']
