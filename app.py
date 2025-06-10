from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello  انا تسنيم احب القراءة والبرمجه!"

if __name__ == '_main_':
    app.run()
