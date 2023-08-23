import pymysql
from flask import Flask, render_template, request, redirect, url_for, session
import logging
# from flask_wtf import FlaskForm
# from wtforms import StringField, SubmitField
# from wtforms.validators import DataRequired

app = Flask(__name__)
# Set the SECRET_KEY for your app


@app.route('/index', methods=['GET'])
def view_home():
    return render_template("index.html")


@app.route('/about_us', methods=['GET'])
def view_about():
    return render_template("about_us.html")


@app.route('/our_fleet', methods=['GET'])
def view_fleet():
    return render_template("our_fleet.html")


@app.route('/signup', methods=['GET'])
def view_sign():
    return render_template("signup.html")


@app.route('/login', methods=['GET'])
def view_login():
    return render_template("login.html")


@app.route('/contact_us', methods=['GET'])
def view_contact():
    return render_template("contact_us.html")


@app.route('/faq', methods=['GET'])
def view_faq():
    return render_template("faq.html")


@app.route('/gdpr', methods=['GET'])
def view_gdpr():
    return render_template("gdpr.html")


app.config['SECRET_KEY'] = '0123456789'

app.config['SECRET_KEY'] = '0123456789'


# logging.basicConfig(filename='app.log', level=logging.INFO)


def connection():
    server = 'localhost'
    db = 'heli7'
    uid = 'sky'
    pwd = 'P@$$word'
    conn = pymysql.Connect(host=server, user=uid, password=pwd, database=db)
    conn.autocommit(True)
    return conn


@app.route('/customer/add', methods=['GET', 'POST'])
def add_customer():
    if request.method == 'POST':
        title = request.form["Title"]
        firstname = request.form["FirstName"]
        lastname = request.form["LastName"]
        doornumber = request.form["DoorNumber"]
        streetname = request.form["StreetName"]
        city = request.form["City"]
        postcode = request.form["PostCode"]
        email = request.form["Email"]
        phone = request.form["Phone"]
        dob = request.form["DOB"]
        print(title, firstname, lastname, doornumber,
              streetname, city, postcode, email, dob)
        conn = connection()
        cursor = conn.cursor()
        cursor.execute(
            "insert into customers(Title, FirstName, LastName, DoorNumber, StreetName, City, PostCode, email, phone, DOB) values ('" + title + "','" + firstname + "','" + lastname + "','" + doornumber + "','" + streetname + "','" + city + "','" + postcode + "','" + phone + "','" + email + "','" + dob + "')")
        return "Your Registration Was Successful"
    return render_template("Customer_registration.html")


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        conn = connection()
        with conn.cursor() as cursor:
            sql = "SELECT * FROM login WHERE username = %s AND password = %s"
            cursor.execute(sql, (username, password))
            login = cursor.fetchone()

        if login:
            session['username'] = username
            # redirect(url_for('index'))
            return render_template("index.html", MSG="You are Logged In as " + username)
        else:
            return render_template('Login.html', MSG="Logging Failed")
    return render_template('Login.html', MSG="")


@app.route('/dashboard')
def dashboard():
    if 'username' in session:
        return f"Welcome, {session['username']}!"
    else:
        return redirect(url_for('index.html'))


@app.route('/logout')
def logout():
    if 'username' in session:
        username = session['username']
        logging.info(f"Logged out: {username}")
        session.pop('username', None)
    return redirect(url_for('index'))


@app.route('/user', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')

        conn = connection()
        try:
            with conn.cursor() as cursor:
                sql = "INSERT INTO login (username, email, password) VALUES (%s, %s, %s)"
                cursor.execute(sql, (username, email, password))
            conn.commit()  # Commit the transaction
            return redirect(url_for('success'))
        except Exception as e:
            conn.rollback()  # Roll back changes if an error occurs
            return render_template('signup.html', error=str(e))
        finally:
            conn.close()

    return render_template('signup.html', error=None)


@app.route('/success')
def success():
    return "User registered successfully!"


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
