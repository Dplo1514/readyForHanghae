from flask import Flask, render_template, jsonify, request
from bs4 import BeautifulSoup
import requests

app = Flask(__name__)

from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.dbsparta


## HTML 화면 보여주기
@app.route('/')
def homework():
    return render_template('index.html')


# 주문하기(POST) API
@app.route('/order', methods=['POST'])
def save_order():
    name_recevice = request.form['name_give']
    many_recevice = request.form['many_give']
    address_recevice = request.form['address_give']
    number_recevice = request.form['number_give']


    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
    data = requests.get(name_recevice ,headers=headers)

    soup = BeautifulSoup(data.text, 'html.parser')

    doc = {
        'name' : name_recevice ,
        'many' : many_recevice ,
        'address'  : address_recevice ,
        'number'   : number_recevice
    }

    db.shop.insert_one(doc)

    return jsonify({'msg': '이 요청은 POST!'})


# 주문 목록보기(Read) API
@app.route('/order', methods=['GET'])
def view_orders():
    sample_receive = request.args.get('sample_give')
    print(sample_receive)
    return jsonify({'msg': '이 요청은 GET!'})


if __name__ == '__main__':
    app.run('0.0.0.0', port=8000, debug=True)