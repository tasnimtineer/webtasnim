from flask import Flask

app = Flask(_name_)

@app.route("/")
def home():
    return """
    <html>
    <head>
        <title>صفحة تسنيم</title>
        <style>
            body {
                background-color: pink;
                font-family: Arial, sans-serif;
                color: #333;
                text-align: center;
                padding: 50px;
            }
            .content {
                background-color: white;
                padding: 30px;
                border-radius: 20px;
                max-width: 600px;
                margin: auto;
                box-shadow: 0 0 20px rgba(0,0,0,0.1);
            }
            h1 {
                font-size: 2.5em;
                color: #c71585;
            }
            p {
                font-size: 1.2em;
                line-height: 1.6em;
            }
        </style>
    </head>
    <body>
        <div class="content">
            <h1>أهلاً وسهلاً</h1>
            <p>مرحباً بك في صفحة تسنيم</p>
            <p>هيا بنا لنبدأ جولة في معلومات عني:</p>
            <p>1. أحب قراءة الكتب جداً بحيث يمكنني إكمال كتاب كامل خلال ٣ أيام فقط</p>
            <p>2. طموحة جداً ولا أقتنع بالقليل ودائماً أسعى للتطور</p>
            <p>3. شجاعة حتى إذا كنت خائفة ولا أعرف</p>
            <p>4. لدي شغف جديد بالبرمجة</p>
            <br>
            <strong>شكراً لك على زيارتك ❤</strong>
        </div>
    </body>
    </html>
    """

if _name_ == "_main_":
    app.run(debug=True)
