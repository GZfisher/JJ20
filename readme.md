本项目为林俊杰歌曲的知识图谱



KGraph内为信息爬取以及知识图谱数据库的构建

QA_app内为简单问答程序



- KGraph

  具体流程如下

  先通过get_songs.ipynb获取网易云音乐中关于林俊杰的歌曲信息，保存在all_songs.csv中

  再通过get_baike.ipynb获取百度百科中关于各歌曲的具体信息，保存在song_infos.csv中

  再通过get_relations.ipynb使用paddlenlp对获取到的百科进行关系提取后保存在song_relations.csv中

  最后使用make_KG.ipynb构建知识图谱

  得到的关系知识图谱如下![graph](C:\Users\10203\Desktop\知识图谱\歌曲\KGraph\graph.png)

- QA_app

  使用flask搭建简单问答页面

![image-20240103144710659](C:\Users\10203\Desktop\知识图谱\歌曲\QA_app\作曲.png)

![image-20240103144812864](C:\Users\10203\Desktop\知识图谱\歌曲\QA_app\专辑.png)

![image-20240103145114629](C:\Users\10203\Desktop\知识图谱\歌曲\QA_app\歌手.png)

![1704265472936](C:\Users\10203\Desktop\知识图谱\歌曲\QA_app\作词.png)