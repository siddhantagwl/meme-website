from flask import Flask

# __name__ means that everything that flask needs to run the website is in the current directory
app = Flask(__name__)

# python decorator - adds more functionality to the function just below it
@app.route("/")
def index():
    return "hi sidd"

# this tells flask to run the app on our host and the port specified
app.run(host="0.0.0.0", port=80)