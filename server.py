from flask import *

app = Flask(__name__)


@app.route('/')
def signin():
    return render_template("signin.html")

@app.route('/portal')
def portal():
    return render_template("portal.html")


if __name__ == "__main__":
  app.run(debug=True)