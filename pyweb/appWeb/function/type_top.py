import pymysql

host = "tx.pkmgtdz.xyz"
user = "dbuser"
pwd = "dbuser"
db_name = "DoubanData"

connection = pymysql.connect(host=host,
                             port=3306,
                             user=user,
                             password=pwd,
                             db=db_name,
                             charset='utf8')

def getTop(type, n):
    cursor = connection.cursor()
    sql = "select movie_name , AVG(level) , movie_url from user_comment where type LIKE '%%%s%%' GROUP BY movie_url HAVING COUNT(DISTINCT user_id) >= 3  ORDER BY AVG(level) DESC LIMIT %d" % (str(type), n)
    #print(sql)
    cursor.execute(sql)
    #print(cursor.fetchall())
    list = []
    for i in cursor.fetchall():
        # print(i)
        list.append({"name" : i[0] , "val" : float(i[1]) , "url" : i[2]})
    return list

# 剧情分类电影top10

def ret():
    ret = getTop("科幻", 10)
    ret += getTop("喜剧", 10)
    ret += getTop("爱情", 10)
    ret += getTop("动作", 10)
    print(ret)
    return ret

