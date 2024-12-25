import os
import datetime

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session, jsonify
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, lookup, usd, check_int

# Configure application
app = Flask(__name__)

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
@login_required
def index():
    """Show portfolio of stocks"""
    USER_ID = session["user_id"]
    buyers = db.execute("SELECT DISTINCT(symbol), price, SUM(shares) AS shares FROM transactions WHERE user_id = ? GROUP BY symbol",USER_ID)
    # symbol = [buyer ["symbol"] for buyer in buyers]
    # shares = [buyer ["shares"] for buyer in buyers]
    # price = [buyer ["price"] for buyer in buyers]
    # total = [buyer ["price"] * buyer ["shares"] for buyer in buyers]
    list = db.execute("SELECT cash FROM users WHERE id = ?", USER_ID)
    cash = list[0]["cash"]
    return render_template("index.html", buyers=buyers, cash=cash)


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""

    if request.method == "GET":
        return render_template("buy.html")

    else:
        symbol = request.form.get("symbol")
        if not symbol:
            return apology("invalid symbol")
        shares = request.form.get("shares")
        item = lookup(symbol.upper())

        if item == None:
            return apology("Stock doesn't exist")
        if shares.isalpha() or shares == "":
            return apology("invalid shares value")
        if not check_int(shares):
            return apology("fractions not supported")
        if int(shares) <= 0:
            return apology("Not valid Shares number")

        user_id = session["user_id"]
        tmp = db.execute("SELECT cash FROM users WHERE id = ?", user_id)
        cash = tmp[0]["cash"]

        transaction_price = item["price"] * int(shares)
        if cash < transaction_price:
            return apology("Not enough Cash")

        # update cash after purchase
        update_cash = cash - transaction_price
        db.execute( "UPDATE users SET cash = :cash WHERE id = :id", cash=update_cash, id=user_id)
        symbols = [ row["symbol"] for row in db.execute("SELECT DISTINCT symbol FROM transactions WHERE user_id = ?", user_id)]
        date= datetime.datetime.now()
        if symbol in symbols:
            cur_shares = db.execute("SELECT SUM(shares) AS shares FROM transactions WHERE user_id= :id AND symbol= :symbol", id= user_id, symbol = symbol)
            new_shares = int(shares) + cur_shares[0]["shares"]
            db.execute("UPDATE transactions SET shares = :shares WHERE user_id = :id AND symbol = :symbol", shares = new_shares, id = user_id, symbol = symbol)
        else:
            db.execute("INSERT INTO transactions (user_id, price, symbol, date, shares) VALUES (?, ?, ?, ?, ?)", user_id, item["price"], item ["name"], date, int(shares))
            row = db.execute("SELECT symbol FROM transactions WHERE user_id = ?", user_id)
            symbols = [stock["symbol"] for stock in row]

        db.execute("INSERT INTO history (user_id, price, symbol, transacted, shares) VALUES (?, ?, ?, ?, ?)", user_id, item["price"], item["name"],date,int(shares))

        flash("Bought!")
        return redirect("/")


@app.route("/history")
@login_required
def history():
    """Show history of transactions"""

    user_id = session["user_id"]

    # transactions info
    list = db.execute("SELECT * FROM history WHERE user_id = ?", user_id)

    return render_template("history.html", transactions=list)


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    """Get stock quote."""

    if request.method == "POST":
        symbol = request.form.get("symbol")
        if not symbol:
            return apology("Invalid Quote")
        else:
            stock = lookup(symbol.upper())
            symbol = stock["symbol"]
            name = stock["name"]
            price = stock["price"]
            if stock == None:
                return apology("Item doesn't exist")
            else:
                return render_template("quoted.html", symbol=symbol, price=price, name=name)
    else:
        return render_template("quote.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""

    if request.method == "POST":
        username = request.form.get("username")
        if not username:
            return apology("invalid username")

        password = request.form.get("password")
        if not password:
            return apology("invalid Password")

        confirmation = request.form.get("confirmation")

        if password != confirmation:
            return apology("invalid confirmation")

        try:
            new_user = db.execute("INSERT INTO users (username, hash) VALUES(?, ?)", username, generate_password_hash(password))
        except:
            return apology("username isn't valid")

    else:
        return render_template("register.html")

    # Remember which user has logged in
    session["user_id"] = new_user

    # Redirect user to home page
    return redirect("/")


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""

    user_id = session["user_id"]
    if request.method == "GET":
            symbols = db.execute("SELECT DISTINCT symbol FROM transactions WHERE user_id = ?", user_id)
            return render_template("sell.html", symbols=symbols)
    else:
        symbol = request.form.get("symbol")
        if not symbol:
            return apology("invalid symbol")

        stock = lookup(symbol)
        if stock == None:
            return apology("Doesn't exist")

        shares = request.form.get("shares")
        if shares.isalpha() or shares == "":
            return apology("invalid shares value")
        if not check_int(shares):
            return apology("fractions not supported")
        if int(shares) <= 0:
            return apology("Not valid Shares number")


        list1 = db.execute("SELECT shares FROM transactions WHERE user_id = :id AND symbol = :symbol GROUP BY symbol", id = user_id, symbol = stock ["symbol"])
        available_shares = list1[0]["shares"]

        if available_shares == 0:
            return apology("not enough shares")
        if int(shares) > available_shares:
            return apology("not enough shares")

        list2 = db.execute("SELECT cash FROM users WHERE id = ?", user_id)
        cash = list2[0]["cash"]

        selling_price = stock["price"] * int(shares)

        # update shares number
        db.execute("UPDATE transactions SET shares = :shares WHERE symbol = :symbol  AND user_id = :id", shares = available_shares-int(shares), symbol = stock ["symbol"], id = user_id)
        date= datetime.datetime.now()
        db.execute("INSERT INTO history (user_id, price, symbol, transacted, shares) VALUES (?, ? , ?, ?, ?)", user_id, stock ["price"], stock ["symbol"], date, -int(shares))

        # update cash
        new_cash = cash + selling_price
        db.execute("UPDATE users SET cash = :cash WHERE id = :id", cash=new_cash, id=user_id)

        flash ("Sold!!")
        return redirect("/")

@app.route("/change", methods=["GET", "POST"])
@login_required
def change():
    """change password"""

    user_id = session["user_id"]

    if request.method == "GET":
        return render_template("change.html")

    else:
        username = request.form.get("username")
        usernames = [row["username"] for row in db.execute("SELECT username FROM users")]
        if not username or username not in usernames:
            return apology("username doesn't exist")

        new_password = request.form.get("new_password")
        if not new_password or new_password.strip() == "":
            return apology("Invalid Password")

        confirmation = request.form.get("confirmation")

        if new_password != confirmation:
            return apology("Invalid Confirmation")

        db.execute("UPDATE users SET hash = :hash WHERE id= :id", hash=generate_password_hash(new_password), id=user_id)

    # Redirect user to home page

    flash("Done!!")
    return redirect("/")
