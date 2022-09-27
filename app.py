
from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

# ------------------------- Docs ----------------------------------------


@app.route('/docs')
def docs():
    return render_template('docs.html')

# ------------------------- Docs ----------------------------------------

# ------------------------- Orders ----------------------------------------


@app.route('/orders')
def orders():
    return render_template('orders.html')

# ------------------------- Orders ----------------------------------------


# ------------------------- Pages ---------------------------------------

@app.route('/notifications')
def notifications():
    return render_template('notifications.html')


@app.route('/account')
def account():
    return render_template('account.html')


@app.route('/settings')
def settings():
    return render_template('settings.html')

# ------------------------- Pages ---------------------------------------

# ------------------------- External ------------------------------------


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/signup')
def signup():
    return render_template('signup.html')


@app.route('/reset-password')
def reset_password():
    return render_template('reset-password.html')


@app.route('/404')
def four_not_four():
    return render_template('404.html')

# ------------------------- External ------------------------------------

# ------------------------- Charts --------------------------------------


@app.route('/charts')
def charts():
    return render_template('charts.html')

# ------------------------- Charts --------------------------------------






if __name__ == '__main__':
    app.run()
