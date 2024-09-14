from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello from Flask on EC2!"

if __name__ == '__main__':
    app.run(debug=True, port=80)