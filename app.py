from flask import *

app = Flask(__name__)


@app.route('/')
def index():
    return redirect(url_for('login'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    loginMsg = ''
    if request.method == 'POST':
        if request.form['username'] == 'guest' and request.form['password'] == 'guest':
            return 'hello '
        else:
            loginMsg = 'Invalid username or password, Please try again.'
    return render_template('login.html', loginMsg=loginMsg)


if __name__ == '__main__':
    app.run(debug=True)
