from flask import Flask, render_template

app = Flask(__name__)


@app.route('/index', methods=['GET'])
def view_home():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(port=5002)
