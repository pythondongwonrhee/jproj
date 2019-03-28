# from flask import *
# from datetime import datetime
# from dbModel import *

# app = Flask(__name__)

# username = ''


# @app.route('/')
# def index():
#     return redirect(url_for('comment'))


# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     loginMsg = ''
#     if request.method == 'POST':
#         global username
#         username= request.form['username']
#         if request.form['username'] == 'guest' and request.form['password'] == 'guest':
#             return redirect(url_for('hello'))
#         else:
#             loginMsg = 'Invalid username or password, Please try again.'
#     return render_template('login.html', loginMsg=loginMsg)

# @app.route('/hello')
# def hello():
#     return render_template('hello.html', username=username)

# @app.route('/slideshow')
# def slideshow():
#     return render_template('slideshow.html', username=username)


# @app.route('/main')
# def main():
#     return render_template('main.html', username=username)


# # @app.route('/comment')
# # def comment():
# #     return render_template('comment.html', username=username)

# @app.route('/comment')
# def comment():
#     data = username
#     data_UserData = UserData.query.all()
#     history_dic = {}
#     history_list = []
#     for _data in data_UserData:
#         history_dic['Name'] = _data.Name
#         history_dic['Id'] = _data.Id
#         history_dic['Description'] = _data.Description
#         history_dic['CreateDate'] = _data.CreateDate.strftime('%Y/%m/%d %H:%M')
#         history_list.append(history_dic)
#         history_dic = {}
#     return render_template('comment.html', **locals())


# @app.route('/API/add_data', methods=['POST'])
# def add_data():
#     name = request.form['name']
#     description = request.form['description']
#     if name != "" and description != "":
#         add_data = UserData(
#             Name=name,
#             Description=description,
#             CreateDate=datetime.now()
#         )
#         db.session.add(add_data)
#         db.session.commit()
#     return redirect('comment')


# if __name__ == '__main__':
#     app.run(debug=True)






from flask import *
from datetime import datetime
from dbModel import *

app = Flask(__name__)

username = 'fffffffffff'


@app.route('/')
def index():
    return redirect(url_for('comment'))


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


# @app.route('/comment')
# def comment():
#     return render_template('comment.html', username=username)

@app.route('/comment')
def comment():
    data = "Deploying a Flask App To Heroku"
    # data_UserData = UserData.query.all()
    data_UserData = UserData.query.order_by(desc(UserData.CreateDate)).all()
    # find_userData = UserData.query.select().where(UserData.Name == 'ffff')
    # data_UserData = UserData.query.filter_by(Name='ffff').all()
    history_dic = {}
    history_list = []
    for _data in data_UserData:
        history_dic['Name'] = _data.Name
        history_dic['Id'] = _data.Id
        history_dic['Description'] = _data.Description
        history_dic['CreateDate'] = _data.CreateDate.strftime('%Y/%m/%d %H:%M:%S')
        history_list.append(history_dic)
        history_dic = {}
    return render_template('comment.html', **locals())


@app.route('/API/add_data', methods=['POST'])
def add_data():
    name = request.form['name']
    description = request.form['comment']
    if name != "" and description != "":
        add_data = UserData(
            Name=name,
            Description=description,
            CreateDate=datetime.now()
        )
        db.session.add(add_data)
        db.session.commit()
    return redirect('comment')


@app.route('/API/search', methods=['POST'])
def search_data():
    searchh = request.form['searchh']
    data_UserData = UserData.query.filter_by(Name=searchh).all()
    history_dic = {}
    history_list = []
    for _data in data_UserData:
        history_dic['Name'] = _data.Name
        history_dic['Id'] = _data.Id
        history_dic['Description'] = _data.Description
        history_dic['CreateDate'] = _data.CreateDate.strftime('%Y/%m/%d %H:%M:%S')
        history_list.append(history_dic)
        history_dic = {}
    return render_template('comment.html', **locals())

if __name__ == '__main__':
    app.run(debug=True)