from flask import Flask

app = Flask(__name__)

app.config["ENV"] = "development" 

from app import views

if __name__ == "__main__":
    app.run()