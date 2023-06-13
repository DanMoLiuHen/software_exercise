import oracledb
import json
import requests
import uvicorn
from random import choice

import numpy as np
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# 2、声明一个 源 列表；重点：要包含跨域的客户端 源
# 3、配置 CORSMiddleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 允许访问的源
    allow_credentials=True,  # 支持 cookie
    allow_methods=["*"],  # 允许使用的请求方法
    allow_headers=["*"]  # 允许携带的 Headers
)


def cosine_similarity(u, v):
    """计算余弦相似度"""
    return np.dot(u, v) / (np.linalg.norm(u) * np.linalg.norm(v))

class recommendation():
    def __init__(self) -> None:
        self.dishes_map={}# 菜品映射表(id->编号)
        self.dish_id_name={}# 菜品映射表(id->名称)
        self.users_map={}# 用户映射表(name->编号)
        self.prepareData()
        self.buildRatingMatrix()

    def prepareData(self):
        database=oracledb.connect(user='DBKS01', password='jiaojiaodb', dsn='192.168.193.163:1521/xe')
        cur = database.cursor()
        cur.execute("select DISTINCT DISH_ID from DISHES")
        res=cur.fetchall()
        self.dishes_map={tup[0]:i for i,tup in enumerate(res)}
        cur.execute("select DISTINCT DISH_ID,DISH_NAME from DISHES")
        res=cur.fetchall()
        self.dish_id_name={tup[0]:tup[1] for tup in res}
        cur.execute("select DISTINCT USER_NAME from VIP")
        res=cur.fetchall()
        self.users_map={tup[0]:i for i,tup in enumerate(res)}
        cur.execute("SELECT USER_NAME,DISH_ID,STARS FROM COMMENT_ON_DISH")
        self.res2=cur.fetchall()
        database.close() 

    def buildRatingMatrix(self):
        # 提取行数(用户名)、列数（菜品id）和值（评分）到不同的列表
        rows = [self.users_map[x[0]] for x in self.res2]
        cols = [self.dishes_map[x[1]] for x in self.res2]

        num_rows = len(self.users_map)
        num_cols = len(self.dishes_map)

        # 构建用户评分矩阵
        # 创建一个全为零的矩阵
        self.matrix = np.zeros((num_rows, num_cols))
        # 将元素放入矩阵，并计算行列重合元组的平均值
        for i in range(len(self.res2)):
            row = rows[i]
            col = cols[i]
            value = self.res2[i][2]
            if self.matrix[row, col] != value:
                self.matrix[row, col] = (self.matrix[row, col] + value) / 2
        # 初始化用户相似度矩阵
        self.user_similarity = np.zeros((num_rows, num_rows))
        # 计算用户之间的相似度
        for i in range(num_rows):
            for j in range(i, num_rows):
                if i == j:
                    # 用户与自身的相似度为1
                    self.user_similarity[i][j] = 1
                else:
                    self.user_similarity[i][j] = cosine_similarity(self.matrix[i], self.matrix[j])
                    self.user_similarity[j][i] = self.user_similarity[i][j]

    def predict(self,user_id):
        """预测用户对未评分物品的兴趣程度"""
        mean_user_rating = self.matrix.mean(axis=1)
        ratings_diff = self.matrix - mean_user_rating[:, np.newaxis]
        pred = mean_user_rating[user_id] + self.user_similarity[user_id].dot(ratings_diff) / np.array([np.abs(self.user_similarity[user_id]).sum(axis=0)])
        return pred
    
    '''
    dish_description: string;
    dish_discount:    number;
    dish_id:          number;
    dish_name:        string;
    dish_picture:     string;http://192.168.193.163:81/dishes/dish_{dish_id}.png
    dish_price:       number;
    dish_rate:        number;
    dish_tag:         string;
    '''
    def solver(self,user_id):
        """解决方案"""
        user_id=self.users_map[user_id]
        predictions = self.predict(user_id)
        # 获取用户未评分的物品索引
        unrated_items = np.where(self.matrix[user_id] == 0)[0]
        # 根据预测评分生成推荐列表
        recommendations = unrated_items[np.argsort(-predictions[unrated_items])]
        # 构建返回数据
        return_data=[]

        result=[]
        for key,val in self.dishes_map.items():
            if val in recommendations:
                result.append(key)
        all_dishes=self.getAllDishes()
        for dish in all_dishes:
            if dish['dish_id'] in result:
                return_data.append(dish)
        return return_data
 
    def getAllDishes(self):
        url = 'http://192.168.193.163:5000/api/OrderDish/GetAllDishes'
        headers = {
            'Content-Type': 'application/json',
        }
        response = requests.get(url, headers=headers)
        ans = response.json()['dish_all']
        return ans

@app.get("/recommendation/{user_name}")
def readItem(user_name: str):
    a=recommendation()
    ret = a.solver(user_name)
    print(len(ret))
    return {"recommendation": ret}

@app.get("/comment/{dish_name}")
def getComment(dish_name: str):
    # 指定JSON文件路径
    file_path = "comments_reviewed.json"
    # 打开JSON文件并读取内容
    with open(file_path, "r",encoding='utf-8') as file:
        json_data = file.read()
    # 解析JSON数据为Python对象
    data = json.loads(json_data)
    return {k:choice(v) for k, v in data[dish_name].items()}

if __name__ == "__main__":
    # Use this for debugging purposes only
    uvicorn.run(app, host="0.0.0.0", port=8001, log_level="debug")
