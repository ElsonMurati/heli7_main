import pymysql

from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/index', methods=['GET'])
def view_home():
    return render_template("index.html")

# Connection to SQL


def connection():
    server = 'localhost'
    db = 'heli7'
    uid = 'sky'
    pwd = 'P@$$word'
    conn = pymysql.Connect(host=server, user=uid, password=pwd, database=db)
    conn.autocommit(True)
    return conn

# To book trips


@app.route('/book', methods=["GET", "POST"])
def book_trip():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        destination = request.form.get("destination")
        departure_date = request.form.get("departure_date")

# To store in Database
        insert_query = """
            INSERT INTO bookings (name, email, destination, departure_date)
            VALUES (%s, %s, %s, %s)
        """
        data = (name, email, destination, departure_date)
        conn = connection()
        cursor = conn.cursor()
        cursor.execute(insert_query, data)

        return render_template("thank_you.html")

    return render_template("book.html")


if __name__ == "__main__":
    app.run(port=5002)
