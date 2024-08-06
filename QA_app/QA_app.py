from flask import Flask, render_template, request
from py2neo import Graph
import re
app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        question = request.form['question']
        return render_template("index.html", data=QA(question=question))
    else:
        return render_template("index.html", data="")

# 问答函数
def QA(question):
    # 先链接到数据库
    graph = Graph("neo4j://localhost:7687", auth=("neo4j", "jj20jj20"))
    # 拆分问题
    # 问题格式如    歌名 的 属性
    song_name = question[:question.rfind("的")]
    # 问题有
    # 专辑
    # 歌手
    # 作曲
    # 作词
    if re.search(pattern=r"专辑", string=question):
        # 专辑问题
        res = graph.run("match (a:`歌曲`{`name`:'"+song_name+"'}) RETURN a.`专辑`")
        return res.data()[0]['a.`专辑`']
    elif re.search(pattern=r"歌手", string=question):
        # 歌手问题
        res = graph.run("match (a:`歌曲`{`name`:'"+song_name+"'})-[:`歌手`]->(b:`人物`) RETURN b.name")
        ans = ""
        t = res.data()
        for i in range(0, len(t)):
            if i == 0:
                ans = t[i]['b.name']
            else:
                ans = ans + ', ' + t[i]['b.name']
        return ans
    elif re.search(pattern=r"作曲", string=question):
        # 作曲问题
        res = graph.run("match (a:`歌曲`{`name`:'"+song_name+"'})-[:`作曲`]->(b:`人物`) RETURN b.name")
        ans = ""
        t = res.data()
        for i in range(0, len(t)):
            if i == 0:
                ans = t[i]['b.name']
            else:
                ans = ans + ', ' + t[i]['b.name']
        return ans
    elif re.search(pattern=r"作词", string=question):
        # 作词问题
        res = graph.run("match (a:`歌曲`{`name`:'"+song_name+"'})-[:`作词`]->(b:`人物`) RETURN b.name")
        ans = ""
        t = res.data()
        for i in range(0, len(t)):
            if i == 0:
                ans = t[i]['b.name']
            else:
                ans = ans + ', ' + t[i]['b.name']
        return ans
    else:
        # 无法解答
        return "无法解答"

if __name__ == '__main__':
    app.run(port=8080,host="127.0.0.1",debug=True)