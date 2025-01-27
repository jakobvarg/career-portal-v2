from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS =  [
  {
    'id': 1,
    'title': 'UI/UX Designer',
    'location': 'Kochi, Panampally Nagar',
    'salary': '30,000'
  },
  {
    'id': 2,
    'title': 'Jr. Frontend Developer',
    'location': 'Kochi, Edapally',
    'salary': '20,000'
  },
  {
    'id': 3,
    'title': 'React JS Developer',
    'location': 'Kochi, Infopark',
    'salary': '40,000'
  },
  {
    'id': 4,
    'title': 'SEO Manager',
    'location': 'Hybrid',
  },
  {
    'id': 5,
    'title': 'Python Flask Developer',
    'location': 'Remote',
    'salary': '50,000'
  }
]

@app.route("/")
def hellow():
  return render_template('home.html', jobs=JOBS, company_name="Jakob's IT Jobs")

@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)

if __name__ == "__main__":
  app.run(host='0.0.0.0',debug=True)
 