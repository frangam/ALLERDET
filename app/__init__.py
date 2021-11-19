from flask import Flask

app = Flask(__name__)
app.config.from_object('config')

from app import views

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000) #host visible desde internet