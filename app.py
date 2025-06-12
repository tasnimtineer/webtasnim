from flask import Flask

app = Flask(__name__)

@app.route("/")
def about():
    return """
    <html>
    <head>
        <title>Spark Group</title>
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
            .container {
                background-color: #fff;
                padding: 20px;
                border-radius: 10px;
                box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1);
                max-width: 800px;
                margin: auto;
            }
            .section {
                margin-top: 20px;
                padding: 15px;
                border-left: 5px solid #007bff;
                background-color: #f9f9f9;
                text-align: left;
            }
            .section h2 {
                color: #007bff;
            }
            p {
                font-size: 1.2em;
                line-height: 1.6;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>👩‍💻 من نحن</h1>
            <div class="section">
                <h2>من نحن</h2>
                <p>نحن مجموعة من الطموحات، جمعنا الشغف بالتكنولوجيا والرغبة في التعلم والتطور. نؤمن أن المستقبل يعتمد على من يمتلك المهارات الرقمية، ونسعى لأن نكون جزءًا من هذا المستقبل المتسارع.</p>
            </div>

            <div class="section">
                <h2>🌟 رؤيتنا</h2>
                <p>نطمح إلى بناء مستقبل رقمي أفضل من خلال التعلم المستمر، والتعاون، وابتكار حلول تكنولوجية تساهم في تحسين حياتنا وحياة من حولنا.</p>
            </div>

            <div class="section">
                <h2>🎯 هدف المشروع</h2>
                <p>هدف مشروعنا هو تطوير مهاراتنا العملية في مجال التكنولوجيا، والعمل الجماعي، واستكشاف مجالات جديدة في عالم البرمجة، الذكاء الاصطناعي، أو أي مجال تقني يخدم المجتمع ويواكب العصر.</p>
            </div>

            <div class="section">
                <h2>💡 مجال اهتمامنا</h2>
                <p>نهتم بالتكنولوجيا، التحول الرقمي، البرمجة، الذكاء الاصطناعي، تصميم المواقع، وتعلم كل ما هو جديد في هذا العالم المتغير. نحب مشاركة المعرفة ونستمتع بتجربة أشياء جديدة.</p>
            </div>

            <div class="section">
                <h2>✨ معاً نحو المستقبل</h2>
                <p>نؤمن أن التعاون يصنع الفرق، وأن كل فكرة يمكن أن تكون بداية لشيء عظيم. شكرًا لاهتمامكم، ونتمنى أن يكون مشروعنا مصدر إلهام وتحفيز لكل من يسعى للتطور.</p>
            </div>
        </div>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(debug=True)
