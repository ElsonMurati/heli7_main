from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/index', methods=['GET'])
def view_home():
    return render_template("index.html")


# added route for booking
booked_trips = []


@app.route("/book", methods=["GET", "POST"])
def book_trip():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        destination = request.form.get("destination")
        departure_date = request.form.get("departure_date")

        booked_trips.append({
            "name": name,
            "email": email,
            "destination": destination,
            "departure_date": departure_date
        })

        return "Trip booked successfully!"

    return render_template("book.html")


if __name__ == "__main__":
    app.run(port=5002)
