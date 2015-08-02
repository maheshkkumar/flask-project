from flask import Flask, request, url_for, render_template, redirect

app = Flask(__name__)


@app.route('/')
def index():
	return render_template("index.html")



if __name__ == "__main__":
    app.run(debug=True)
