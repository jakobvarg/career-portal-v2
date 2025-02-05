from flask import Flask, render_template, jsonify, request
from database import load_jobs_from_db, load_job_by_id, add_application_to_db

app = Flask(__name__)

@app.route("/")
def home():
  JOBS = load_jobs_from_db()
  return render_template('home.html', jobs=JOBS, company_name="Jakob's IT Jobs")

@app.route("/api/jobs")
def list_jobs():
  JOBS = load_jobs_from_db()
  return jsonify(JOBS)

@app.route("/job/<id>")
def show_jobs_by_id(id):
  JOB = load_job_by_id(id)
  if JOB:
    return render_template('jobpage.html', job=JOB, company_name="Jakob's IT Jobs")
  else:
    return render_template('404.html')

@app.route("/job/<id>/apply", methods=['POST'])
def apply_for_job(id):
  DATA = request.form
  JOB = load_job_by_id(id)
  add_application_to_db(id, DATA)
  if JOB:
    return render_template('applyjob.html', application=DATA, job=JOB, company_name="Jakob's IT Portal")
  else:
    return render_template('404.html')
    
if __name__ == "__main__":
  app.run(host='0.0.0.0',debug=True)
 