from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbsparta

#매트릭스의 평점 가져오기
matrix = db.movies.find_one({'title':'매트릭스'})
print(matrix['point'])

#매트릭스와 같은 평점의 영화 제목 가져오기
same_point = list(db.movies.find({'point':'9.39'},{'_id':False}))
for same_points in same_point :
    print(same_points['title'])
ㅇ
#매트릭스 영화 평점을 0으로 만들기
db.movies.update_one({'title':'매트릭스'},{'$set':{'point':'0'}})


