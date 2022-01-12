from flask import Flask, render_template, request, jsonify
app = Flask(__name__)
from pymongo import MongoClient
import certifi

ca = certifi.where()
client = MongoClient('mongodb+srv://test:sparta@cluster0.9fupx.mongodb.net/Cluster0?retryWrites=true&w=majority',tlsCAFile=ca)
db = client.dbsparta


@app.route('/')
def home():
    return render_template('index.html')

@app.route("/homework", methods=["POST"])
def homework_post():
    name_receive = request.form['name_give']
    comment_receive = request.form['comment_give']

    doc = {
        "name" : name_receive ,
        "comment" : comment_receive
    }
    db.fancomment.insert_one(doc)
    return jsonify({'msg': '저장 완료!'})


@app.route("/homework", methods=["GET"])
def homework_get():
    fan_list = list(db.fancomment.find({},{'_id':False}))
    return jsonify({'fan': fan_list})


if __name__ == '__main__':
    app.run('0.0.0.0', port=8000, debug=True)