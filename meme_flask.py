from flask import Flask, render_template
import requests
# import json

# __name__ means that everything that flask needs to run the website is in the current directory
app = Flask(__name__)

def get_meme():
    url = "https://meme-api.com/gimme"
    print(url)
    resp = requests.get(url)
    data = resp.json()
    meme_large = data['preview'][-1]
    subreddit = data["subreddit"]
    return meme_large, subreddit

# python decorator - adds more functionality to the function just below it
@app.route("/")
def index():
    meme_pic, subreddit = get_meme()
    return render_template("meme_index.html", meme_pic=meme_pic, subreddit=subreddit)


# this tells flask to run the app on our host and the port specified
app.run(host="0.0.0.0", port=80)