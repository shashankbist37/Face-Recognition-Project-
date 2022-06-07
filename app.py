from flask import Flask

app = Flask(__name__)

@app.route("/")
def welcome():
    return "welcome"

if __name__=='__main_':
            app.run()

