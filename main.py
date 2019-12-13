#Created by:  Alexsandro Monteiro
#Date:        19/02/2019
#Site for Tests Python / Flask

from flask import Flask, render_template, url_for, request,send_from_directory

app = Flask(__name__)

@app.route("/")
@app.route("/index")
def index():
  return render_template('index.html')

@app.route("/job")
def job():
  return render_template('job.html')
  
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8080, debug=True)
