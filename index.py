from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html") 

@app.route("/shopping_page")
def shopping():
    return render_template("shopping_page.html") 

@app.route("/cart")
def cart():
    return render_template("shopping_cart_page.html") 

@app.route("/login_page")
def login():
    return render_template("login_page.html") 

@app.route("/admin")
def admin():
    return render_template("admin_page.html") 

if __name__ == "__main__":
    app.run(debug=True)