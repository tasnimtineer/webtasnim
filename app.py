from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello to my world Let's go on a little tour and learn more about me!
I love reading books and can finish a whole book in just three days.
I'm passionate about programming and enjoy growth and trying new things.
I'm brave and always try to face challenges, even when I'm afraid.!"

if __name__ == '_main_':
    app.run()
