from flask import Flask, render_template, jsonify, request
from bs4 import BeautifulSoup
import requests

app = Flask(__name__)

from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.dbsparta

from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.dbhomework


## HTML 화면 보여주기
@app.route('/')
def homework():
    return render_template('index.html')


# 주문하기(POST) API
@app.route('/order', methods=['POST'])
def save_order():
    name_receive = request.form['name_give']
    amount_receive = request.form['amount_give']
    address_receive = request.form['address_give']
    phone_receive = request.form['phone_give']

    doc = {
        'name': name_receive,
        'amount': amount_receive,
        'address': address_receive,
        'phone': phone_receive,
    }

    db.shop.insert_one(doc)

    return jsonify({'msg': '주문정보 저장이 완료되었습니다.'})



# 주문 목록보기(Read) API
@app.route('/order', methods=['GET'])
def view_orders():
    orderer = list(db.homework.find({}, {'_id': False}))
    return jsonify({'all_orderer': orderer})



if __name__ == '__main__':
    app.run('0.0.0.0', port=8000, debug=True)