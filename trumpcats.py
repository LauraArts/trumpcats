
from flask import Flask, render_template, request

app = Flask('MyApp')

#classic front page
@app.route('/')
def hello():
    return render_template("index.html")

#function that will send a person an email to confirm their subscription to our newsletter
def send_simple_message(person_contact):
    return requests.post(
        #maybe we need an API key for our trumpcats mailing list? not sure.
        #took my API key out because mailgun saw I committed this code on github, emailed me, and told me it was concerned for my privacy.
        #for now I"m just using generic link and no api key
        "https://api.mailgun.net/v3/YOUR_DOMAIN_NAME/messages",
        auth=("api", "API KEY"),
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
