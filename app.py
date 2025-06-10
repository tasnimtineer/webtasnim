from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello from Azure Web App!"

if __name__ == '_main_':
    app.run()
