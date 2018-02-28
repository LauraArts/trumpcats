
from flask import Flask, render_template, request

app = Flask('MyApp')


@app.route('/')
def hello():
    return "hello kittykat"

if __name__ == "__main__"
	app.run(debug=True)

