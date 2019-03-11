from flask import *

app = Flask(__name__)


@app.route('/')
def index():
    return redirect(url_for('login'))


@app.route('/hello')
def hello():
    return render_template('hello.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    loginMsg = ''
    if request.method == 'POST':
        if request.form['username'] == 'guest' and request.form['password'] == 'guest':
            return render_template('hello.html')
        else:
            loginMsg = 'Invalid username or password, Please try again.'
    return render_template('login.html', loginMsg=loginMsg)


@app.route('/slideshow')
def slideshow():
    return render_template('slideshow.html')


@app.route('/main')
def main():
    return render_template('main.html')

if __name__ == '__main__':
    app.run(debug=True)
