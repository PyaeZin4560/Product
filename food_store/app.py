from flask import flask, render_template, request, redirect, url_for

app = flask(__name__)

# Sample food list
foods = [
    {"id": 1, "name": "Fried Rice", "price": 2500},
    {"id": 2, "name": "Chicken Curry", "price": 3000},
    {"id": 3, "name": "Burger", "price": 2000},
]

@app.route('/')
def index():
    return render_template("index.html")
@app.route('/menu')
def menu():
    return render_template("menu.html", foods=foods)
@app.route("/cart")
def cart():
    return render_template("cart.html")
@app.route("/checkout")
def checkout():
    return render_template("checkout.html")
if __name__ == "__main__":
    app.run(debug=True)