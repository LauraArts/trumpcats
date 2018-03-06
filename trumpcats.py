
from flask import Flask, render_template, request

app = Flask('MyApp')

#classic front page
@app.route('/')
def hello():
    return render_template("index.html")

#function that will send a person an email to confirm their subscription to our newsletter
def send_simple_message(person_contact):
    return requests.post(
        "https://api.mailgun.net/v3/sandbox300587fa18d34f74bc4b86c6a553b208.mailgun.org/messages",
        auth=("api", "key-c822d5f589dc282e4ef647920e646a78"),
        data={"from": "Your trumpcats pham",
              "to": [person_contact],
              "subject": "Hello",
              "text": "This is to confirm your subscription to trumpcats!"})

#the decorator for our signup page
@app.route("/signup", methods =["POST"])
def signup():
    form_data = request.form
    recipient = form_data["email"]
    send_simple_message(recipient)
    return render_template('thankyou.html', data=form_data)

if __name__ == "__main__":
	app.run(debug=True)
