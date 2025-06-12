from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <html>
    <head>
        <title>صفحتي الشخصية</title>
        <style>
            body {
                font-family: 'Arial', sans-serif;
                background-color: #f4f4f4;
                color: #333;
                text-align: center;
                margin: 50px;
                padding: 20px;
            }
            h1 {
                color: #007bff;
                font-size: 2.5em;
            }
            p {
                font-size: 1.2em;
                line-height: 1.6;
                max-width: 700px;
                margin: auto;
            }
            .container {
                background-color: #fff;
                padding: 20px;
                border-radius: 10px;
                box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1);
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>مرحبًا بكم في صفحتي الشخصية!</h1>
            <p>أنا شخص مليء بالطموح والفضول، لدي شغف عميق بالتكنولوجيا، خاصة الذكاء الاصطناعي والبرمجة.</p>
            <p>رحلتي في الذكاء الاصطناعي مدفوعة برغبة قوية لفهم الأنظمة الذكية وإنشاء حلول مؤثرة باستخدام البيانات والتعلم الآلي.</p>
            <p>لقد أكملت العديد من الدورات التدريبية عبر منصات مثل AI Academy، إدراك، ALX، LinkedIn Learning، ومبادرة Million Engineers.</p>
            <p>إلى جانب اهتماماتي التقنية، أنا قارئة نهمة يمكنني إنهاء كتاب كامل في ثلاثة أيام فقط! القراءة تعزز إبداعي وتفكيري النقدي.</p>
            <p>أواجه التحديات بشجاعة وفضول، وأسعى دائمًا إلى التطور واستكشاف تجارب جديدة.</p>
            <p>مع أساس قوي في الذكاء الاصطناعي والبرمجة وعقلية نمو، أتطلع للمساهمة في مشاريع مبتكرة والتعاون مع محترفين لديهم نفس الشغف لتشكيل المستقبل!</p>
        </div>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(debug=True)
