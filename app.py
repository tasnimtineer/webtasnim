from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <html>
    <head><title>صفحتي الشخصية</title></head>
    <body>
        <h1>أهلا وسهلا في صفحتي</h1>
        <p>هيا بنا في جولة ومعلومات حولي.</p>
        <p>اسمي تسنيم وأنا أحب البرمجة وأحب المرحلة الحياتية التي أنا فيها لأن كل يوم شيء جديد!</p>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(debug=True)
