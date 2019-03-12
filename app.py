from flask import *

app = Flask(__name__)

username = 'fffffffffff'


@app.route('/')
def index():
    return redirect(url_for('login'))


@app.route('/hello')
def hello():
    return render_template('hello.html', username=username)


@app.route('/login', methods=['GET', 'POST'])
def login():
    loginMsg = ''
    if request.method == 'POST':
        global username
        username= request.form['username']
        if request.form['username'] == 'guest' and request.form['password'] == 'guest':
            return redirect(url_for('hello'))
        else:
            loginMsg = 'Invalid username or password, Please try again.'
    return render_template('login.html', loginMsg=loginMsg)


@app.route('/slideshow')
def slideshow():
    return render_template('slideshow.html', username=username)


@app.route('/main')
def main():
    return render_template('main.html', username=username)


if __name__ == '__main__':
    app.run(debug=True)
