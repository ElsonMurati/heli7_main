from flask import Flask, render_template, Blueprint

heli7_app = Blueprint('heli7_app', __name__)
app = Flask(__name__)


@heli7_app.route('/home')
def home():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True, port=5002)

# def connection():
#     server = 'localhost'
#     db = 'skallia'
#     uid = 'sky'
#     pwd = 'P@$$word'
#     conn = pymysql.connect(host=server, user=uid, password=pwd, database=db)
#     conn.autocommit(True)
#     return conn


# @app.route('/language/add/<lang>')
# def add_language(lang):
#     conn = connection()
#     cursor = conn.cursor()
#     cursor.execute("insert into language(name) values('" + lang + "')")
#     return "Successfully added " + lang


# @app.route('/customer')
# def main():
#     customer = []
#     conn = connection()
#     cursor = conn.cursor()
#     cursor.execute("select * from customer")
#     for row in cursor.fetchall():
#         customer.append({"customer_id": row[0], "first_name": row[2], "last_name": row[3], "email": row[4]})
#     conn.close()
#     return render_template("customer.html", customer=customer)


# @app.route('/', methods=['GET', 'POST'])
# @app.route('/home', methods=['GET', 'POST'])
# def register():
#     errormessage = ""

#     form = BasicForm()

#     if request.method == 'POST':
#         name = form.name.data
#         age = form.age.data

#         if len(name) == 0:
#             errormessage = "Please enter your name"
#         else:
#             return "Thank you for Submitting the form"

#     return render_template('home.html', form=form, errormessage=errormessage)
