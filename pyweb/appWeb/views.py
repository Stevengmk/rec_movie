from django.shortcuts import render
import time
from appWeb.function import query
import pymysql as psq
from django.shortcuts import HttpResponse
import json
from appWeb.function import type_top
import random


def index(request):

    return render(request, 'index.html')


def do_filter(request):
    # print("*" * 100)
    if request.is_ajax():
        usr = request.GET['user']
        correct_usr = usr[9:]
        # print(type(usr))
        # print(usr[9:])
        db = psq.connect(host="tx.pkmgtdz.xyz", user="dbuser", password="dbuser", database="DoubanData",charset="utf8")
        # 使用 cursor() 方法创建一个游标对象 cursor
        cursor = db.cursor()
        # 使用 execute()  方法执行 SQL 查询
        cursor.execute("select* from user_comment")
        # 使用 fetchone() 方法获取单条数据.
        datas = cursor.fetchall()
        # user = set()
        ratings = []
        movies = []
        for d in datas:
            line = []
            movie = []
            # 0: user_id. 1:username 2:level 3:movie_url 4:movie_name 5:img_url 6:type
            # user.add(d[0])

            line.append(d[0])
            line.append(d[3])
            line.append(d[2])
            ratings.append(line)

            movie.append(d[3])
            movie.append(d[4])
            movie.append(d[5])
            movie.append(d[6])
            movies.append(movie)
        db.close()

        start = time.perf_counter()
        # list_user = list(user)
        # i = random.randint(0,len(list_user))
        demo = query.CF(movies, ratings)
        # u = user.pop()
        # usr = list_user[i]
        # print(usr)
        # demo.recommendByUser(usr)
        demo.recommendByUser(correct_usr)
        result = demo.showResult()
        print("*"*30)
        # res_json = json.dumps(result[0])
        # print(res_json)  # 按列转换
        print("处理的数据为%d条" % (len(demo.ratings)))
        end = time.perf_counter()
        print("耗费时间： %f s" % (end - start))  # 仅指协同过滤的时间，不包括读取数据库的时间

        print(result)
        # list=[]
        # for i in range(index):
        #     ret = result.iloc[i]
        #     list.append(pd.DataFrame(ret).to_json())
        # print(pd.DataFrame(ret).to_json())
        # print(json.dumps(result))
        # print(result.to_json())
        r = HttpResponse(result.to_json(),content_type='appliaction/json')
        # r = HttpResponse(json.dumps(list), content_type='appliaction/json')
        return r


def do_type_top(request):
    return HttpResponse(json.dumps(type_top.ret()))