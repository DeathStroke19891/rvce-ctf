from flask import Flask, render_template, jsonify, make_response, request, send_from_directory

app = Flask(__name__)

JOBS = [
  {
    'id': 1,
    'title': 'Data Analyst',
    'location': 'Bengaluru, India',
    'salary': 'Rs. 10,00,000'
  },
  {
    'id': 2,
    'title': 'Data Scientist',
    'location': 'Delhi, India',
    'salary': 'Rs. 15,00,000'
  },
  {
    'id': 3,
    'title': 'Frontend Engineer',
    'location': 'Remote'
  },
  {
    'id': 4,
    'title': 'Backend Engineer',
    'location': 'San Francisco, USA',
    'salary': '$150,000'
  }
]


@app.route('/getcookie')
def getcookie():
    auth = request.cookies.get('Auth')
    return auth


@app.route("/", methods=['GET', 'HEAD'])
def hello_rvce():
    if request.method == 'GET':
        if getcookie()=="YWRtaW46MTMzNw==":
            return render_template('admin.html', jobs=JOBS, company_name='RVCE')
        else:
            rendered = render_template('home.html',
                                jobs=JOBS,
                                company_name='RVCE')
            resp = make_response(rendered)
            resp.set_cookie('Auth','YWRtaW46MA==')
            return resp
    elif request.method == 'HEAD':
        print("I am here")
        response.headers['Content-Type'] = 'flag_pwned'
        response.headers['Content-Length'] = '0'
        return response

@app.route('/robots.txt')
def robots():
    return send_from_directory('static', 'robots.txt')

@app.route('/secret_key')
def secret():
    return render_template('secret.html')

@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)


if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
