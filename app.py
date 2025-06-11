from flask import Flask

app = Flask(_name_)

@app.route('/')
def home():
    return "Hello  انا تسنيم احب القراءة والبرمجه!"

if _name_ == 'main':
    app.run()
