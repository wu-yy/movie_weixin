'''
require tushare
'''
import time
import  itchat
import  datetime
import tushare as ts
from itchat.content import *


#登录微信
def login():
    itchat.auto_login(hotReload=True)

#获取电影的消息
def movie():
    df = ts.realtime_boxoffice()
    content='排名  电影名字  票房占比  上映时间  累计票房\n'
    for i in range(0,11):
        content=content+str(df['Irank'][i])+' '+df['MovieName'][i]+' '+str(df['boxPer'][i])+'% '+str(df['movieDay'][i])+'天 '+str(df['sumBoxOffice'][i])+'万\n'

    #print(content)
    itchat.send('实时票房：\n'+content,toUserName='filehelper')

#自动回复
@itchat.msg_register(TEXT)
def text_reply(msg):
    if '实时票房' in msg['Text'] or '票房' in msg['Text']:
        movie()
        return ''

#开启定时，循环脚本 30分钟更新一次
def timer():
    while True:
        movie()
        time.sleep(1800)

if __name__=='__main__':
    login()
    timer()
