from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

html_content = """
<!DOCTYPE html>
<html lang="ar">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>صفحة تسنيم</title>
    <style>
        body {
            background-color: #FFC0CB;
            font-family: Arial, sans-serif;
            text-align: center;
            color: #333;
            margin: 0;
            padding: 50px;
        }
        h1 {
            color: #D63384;
        }
        p {
            font-size: 20px;
        }
    </style>
</head>
<body>
    <h1>مرحبًا بك في صفحتي!</h1>
    <p>هيا بنا نبدأ جولة في معلومات عني:</p>
    <p>✨ اسمي <strong>تسنيم أحمد</strong></p>
    <p>📅 مولودة في سنة <strong>2003</strong></p>
    <p>💻 أحب تعلم <strong>البرمجة</strong></p>
    <p>📖 أحب القراءة جدًا، وأستطيع إنهاء كتاب كامل خلال <strong>ثلاثة أيام</strong></p>
</body>
</html>
"""

@app.get("/", response_class=HTMLResponse)
async def home():
    return html_content
