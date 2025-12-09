from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = "super-secret-key"   # REQUIRED for session

menu = [
    {"name": "Pizza", "price": 150, "image": "pizza.jpg"},
    {"name": "Burger", "price": 80, "image": "burger.jpg"},
    {"name": "Pasta", "price": 120, "image": "pasta.jpg"},
    {"name": "Sandwich", "price": 60, "image": "sandwich.jpg"},
    {"name": "French Fries", "price": 70, "image": "fries.jpg"},
    {"name": "Noodles", "price": 110, "image": "noodles.jpg"},
    {"name": "Manchurian", "price": 130, "image": "manchurian.jpg"},
    {"name": "Dosa", "price": 90, "image": "dosa.jpg"},
    {"name": "Ice Cream", "price": 50, "image": "icecream.jpg"},
    {"name": "Cold Drink", "price": 40, "image": "colddrink.jpg"}
]

@app.route("/")
def home():
    if "cart" not in session:
        session["cart"] = []

    total = sum(item["price"] for item in session["cart"])

    return render_template(
        "index.html",
        menu=menu,
        cart=session["cart"],
        total=total
    )

@app.route("/add_to_cart", methods=["POST"])
def add_to_cart():
    item_name = request.form.get("item")

    for item in menu:
        if item["name"] == item_name:
            session["cart"].append(item)
            session.modified = True
            break

    return redirect("/")

@app.route("/checkout")
def checkout():
    cart = session.get("cart", [])
    total = sum(item["price"] for item in cart)

    session["cart"] = []   # clear cart after order

    return render_template("success.html", cart=cart, total=total)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
