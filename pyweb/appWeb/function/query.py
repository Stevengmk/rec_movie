from numpy import *
import pandas as pd

class CF:
    def __init__(self, movies, ratings, k=10, n=5):
        self.movies = movies
        self.ratings = ratings  # 评分
        self.k = k  # 邻居个数
        self.n = n  # 推荐个数
        self.userDict = {}  # 用户对电影的评分，数据格式{'UserID':[(MovieID,Rating)]}
        self.ItemUser = {}  # 对某电影评分的用户，数据格式：{'MovieID',[UserID1]}
        # {'1',[1,2,3..],...}
        self.neighbors = []  # 邻居的信息
        self.recommandList = []  # 推荐列表
        self.cost = 0.0

    # 基于用户的推荐
    # 根据对电影的评分计算用户之间的相似度
    def recommendByUser(self, userId):
        self.formatRate()  # 将ratings转换为userDict和ItemUser
        self.getNearestNeighbor(userId)  # 找到某用户的相邻用户
        self.getrecommandList(userId)  # 获取推荐列表

    # 将ratings转换为userDict和ItemUser
    def formatRate(self):
        self.userDict = {}
        self.ItemUser = {}
        for i in self.ratings:
            # 评分最高为5 除以5 进行数据归一化
            temp = (i[1], float(i[2]) / 5)  # i[0]:userID,i[1]:movieID,i[2]:rating
            # 计算userDict {'1':[(1,5),(2,5)...],'2':[...]...}
            if (i[0] in self.userDict):
                self.userDict[i[0]].append(temp)
            else:
                self.userDict[i[0]] = [temp]
            # 计算ItemUser {'1',[1,2,3..],...}
            if (i[1] in self.ItemUser):
                self.ItemUser[i[1]].append(i[0])
            else:
                self.ItemUser[i[1]] = [i[0]]

    # 找到某用户的相邻用户
    def getNearestNeighbor(self, userId):
        neighbors = []
        self.neighbors = []
        # 获取userId评分的电影都有那些用户也评过分
        for i in self.userDict[userId]:  # 该用户评分的每个电影
            for j in self.ItemUser[i[0]]:  # 遍历对同个电影有评分的用户
                if (j != userId and j not in neighbors):  # 找到所有符合的用户
                    neighbors.append(j)
                    # 计算这些用户与userId的相似度并排序
        for i in neighbors:
            dist = self.getCost(userId, i)  # 只要有交集的用户就计算二者的余弦相似度
            self.neighbors.append([dist, i])  # 填入self.neighbors
        # 排序默认是升序，reverse=True表示降序
        self.neighbors.sort(reverse=True)
        self.neighbors = self.neighbors[:self.k]  # 取相似度最高的k个相邻用户

        # 获取推荐列表

    def getrecommandList(self, userId):
        self.recommandList = []
        # 建立推荐字典
        recommandDict = {}  # {'MovieID':dist}
        for neighbor in self.neighbors:
            movies = self.userDict[neighbor[1]]  # 找到每个邻居的评论的所有电影
            for movie in movies:
                if (movie[0] in recommandDict):  # movie[0]就是电影ID movie[1]是评分，如果该电影已加入推荐列表，就增加相似度
                    recommandDict[movie[0]] += neighbor[0]  # neighboe[0]是相似度，neighbor[1]是用户ID
                else:
                    recommandDict[movie[0]] = neighbor[0]
        # 建立推荐列表
        for key in recommandDict:
            self.recommandList.append([recommandDict[key], key])  # {[dist,MovieID]...}
        self.recommandList.sort(reverse=True)
        self.recommandList = self.recommandList[:self.n]  # 选取前n个

    # 计算余弦距离
    def getCost(self, userId, l):  # l是邻居用户
        # 获取用户userId和l评分电影的并集
        # {'电影ID'：[userId的评分，l的评分]} 没有评分为0
        user = self.formatuserDict(userId, l)
        x = 0.0
        y = 0.0
        z = 0.0
        for k, v in user.items():
            x += float(v[0]) * float(v[0])
            y += float(v[1]) * float(v[1])
            z += float(v[0]) * float(v[1])
        if (z == 0.0):
            return 0
        return z / sqrt(x * y)

        # 格式化userDict数据

    def formatuserDict(self, userId, l):
        user = {}  # {'电影ID'：[userId的评分，l的评分]} 没有评分为0
        for i in self.userDict[userId]:
            user[i[0]] = [i[1], 0]
        for j in self.userDict[l]:
            if (j[0] not in user):
                user[j[0]] = [0, j[1]]
            else:
                user[j[0]][1] = j[1]
        return user

    def showResult(self):
        neighbors_id = [i[1] for i in self.neighbors]
        line = []
        movie = []
        for item in self.recommandList:
            fromID = []
            for i in self.movies:
                if i[0] == item[1]:
                    movie = i
                    break
            # for i in self.ItemUser[item[1]]:
            #     if i in neighbors_id:
            #         fromID.append(i)
            # movie.append(fromID)
            line.append(movie)
        # result = pd.DataFrame(line, columns=['movieURL', 'Name', 'img_url', 'type', 'from userID'])
        result = pd.DataFrame(line, columns=['movieURL', 'Name', 'img_url', 'type'])
        return result