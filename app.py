from flask import *
from datetime import datetime
from dbModel import *
import requests

app = Flask(__name__)

username = None

@app.route('/')
def index():
    return redirect(url_for('hello'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    loginMsg = ''
    if request.method == 'POST':
        global username
        username= request.form['username']
        if request.form['password'] == 'Guest':
            print(username)
            resp = make_response(render_template('hello.html', username=username))
            print (resp)
            resp.set_cookie('username', username)
            return resp
        else:
            loginMsg = 'Invalid password, Please try again.'
    return render_template('login.html', loginMsg=loginMsg)

@app.route('/weather', methods=['GET', 'POST'])
def weather():
    print('gggggggggggggggggg')
    city = request.form['cityy']
    city2 = city.encode("utf-8")
    print('citu2', city2)
    print('city', city)
    payload = {'q': city + ',CA', 'APPID' : '796f194a3c3999feb3fcba072372a256'}

    w = requests.get('http://api.openweathermap.org/data/2.5/weather', params=payload)
    print(w.url)
    # w = requests.get('http://api.openweathermap.org/data/2.5/weather?q=city2,US&APPID=796f194a3c3999feb3fcba072372a256')
    w_json = w.json()
    print (w_json)

    for xx in w_json:
        print("Number of people in space:", xx)

    x1 = w_json['weather'][0]['description']
    x2 = w_json['main']['temp']

    return render_template('hello.html', x1=x1, city=city, x2= x2-273.15)
    # if request.method == 'POST':
    #     print('weahterrrrrrrrrrrrr')
    #     city = request.form['city']
    #     print(city)
    # return render_template('hello.html')

@app.route('/hello')
def hello():
    return render_template('hello.html', username=username)


@app.route('/slideshow')
def slideshow():
    return render_template('slideshow.html', username=username)


@app.route('/assignment_temp_convert')
def assignment_temp_convert():
    return render_template('assignment_temp_convert.html', username=username)


@app.route('/assignment_first')
def assignment_first():
    return render_template('assignment_first.html', username=username)

@app.route('/assignment_store')
def assignment_store():
    return render_template('assignment_store.html', username=username)


@app.route('/main')
def main():
    username = request.cookies.get('username')
    print('username_main', username)
    return render_template('main.html', username=username)


@app.route('/comment')
def comment():
    username = request.cookies.get('username')
    data_CommentDb = CommentDb.query.order_by(desc(CommentDb.CreateDate)).all()
    Comment_dic = {}
    Comment_list = []
    for dataa in data_CommentDb:
        Comment_dic['Name'] = dataa.Name
        Comment_dic['Id'] = dataa.Id
        Comment_dic['Comment'] = dataa.Comment
        Comment_dic['CreateDate'] = dataa.CreateDate.strftime('%Y/%m/%d %H:%M:%S')
        Comment_list.append(Comment_dic)
        Comment_dic = {}
    return render_template('comment.html', **locals())


@app.route('/API/add_data', methods=['POST'])
def add_data():
    name = request.form['name']
    comment = request.form['comment']
    if name != "" and comment != "":
        add_data = CommentDb(
            Name=name,
            Comment=comment,
            CreateDate=datetime.now()
        )
        try:
            db.session.add(add_data)
            db.session.commit()
                
        except:
            db.session.rollback()
    return redirect('comment')


@app.route('/API/search', methods=['POST'])
def search_data():
    searchh = request.form['searchh']
    data_CommentDb = CommentDb.query.filter_by(Name=searchh).all()
    Comment_dic = {}
    Comment_list = []
    for dataa in data_CommentDb:
        Comment_dic['Name'] = dataa.Name
        Comment_dic['Id'] = dataa.Id
        Comment_dic['Comment'] = dataa.Comment
        Comment_dic['CreateDate'] = dataa.CreateDate.strftime('%Y/%m/%d %H:%M:%S')
        Comment_list.append(Comment_dic)
        Comment_dic = {}
    return render_template('comment.html', **locals())

if __name__ == '__main__':
    app.run(debug=True)
