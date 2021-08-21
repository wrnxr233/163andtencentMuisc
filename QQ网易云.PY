#!/usr/bin/python3

'''
欢迎访问仙人小站https://www.wrnxr.cc/
更多干货等着你
'''

import requests
import json
import urllib.request
import os

#到二仙桥
print('欢迎访问仙人小站https://www.wrnxr.cc/\n更多干货等着你!\n')
print('正在检测服务器链接是否可用...')
#走成华大道
testurl='(你的url)'

try:
    status = urllib.request.urlopen(testurl).code
    print(status,'服务器连接成功\n')
except Exception as err:
    print(err,'服务器连接失败\n')
    input('按enter退出')
    os._exit(0)

#保熟
c0=(input('请选择音乐平台：\n1.QQ音乐\n2网易云音乐\n请选择：'))
if c0 == ('1'):
    url='(你的url）'
elif c0 == ('2'):
    url='(你的url）'
else:
    input('请输入正确的选项')

#蚌埠住了
c1=(input('请选择接下来您要进行的操作：\n1.搜索歌曲进行解析\n2.使用歌曲ID解析\n3.解析歌单内的歌曲\n请选择：'))
if c1 == ('1'):
    #准备吟唱
    songid=(input('请输入需要搜索的歌曲或歌手:'))

    #开始吟唱

    if len(songid)>0:
        pass
    else:
        print('请输入要搜索的歌曲或歌手')
        input('按enter退出')
    payload={'id':(songid),'type':'search'}
    headers={'content-type':'application/x-www-form-urlencoded'}
    jr=requests.get(url,params=payload,headers=headers)
    songs_json_list=json.loads(jr.text)
    print('\n搜索结果：')
    for song in songs_json_list:
        if len(song['url'])>0:
            pass
        else:
            song['url']=('mp3直链获取失败！该歌曲可能为会员歌曲或暂无版权')
        print ('\n\n曲目:'+song['name']+'\n\n作者：'+song['author']+'\n\n歌曲ID:'+str(song['song_id'])+'\n\nmp3直链：'+song['url']
           )
    surl=(input('想立即试听？请粘贴mp3地址到此处：'))
    file=(surl)
    os.system(file)
    input('\n\n按enter退出')
elif c1 == ('2'):
    #准备吟唱
    songid=(input('请输入需要解析的歌曲ID:'))

    #开始吟唱

    if len(songid)>0:
        pass
    else:
        print('快回去输入歌曲ID')
        input('按enter退出')
    payload={'id':(songid),'type':'song'}
    headers={'content-type':'application/x-www-form-urlencoded'}
    jr=requests.get(url,params=payload,headers=headers)
    jrr=json.loads(jr.text)
    mp3name=jrr['name']
    mp3author=jrr['author']
    mp3url=jrr['url']
    if len(mp3url)>0:
        pass
    else:
        mp3url=('mp3直链获取失败！该歌曲可能为会员歌曲或暂无版权')
    mp3lrc=jrr['lrc_data']

    print('\n歌曲名：',mp3name,
          '\n歌手：',mp3author,
          '\n下载链接：',mp3url,
          '\n本曲歌词：\n',mp3lrc)
    input('\n\n按enter退出')
elif c1 == ('3'):
    #准备吟唱
    songid=(input('请输入需要解析的歌单ID:'))

    #开始吟唱

    if len(songid)>0:
        pass
    else:
        print('快回去输入歌曲ID')
        input('按enter退出')
    payload={'id':(songid),'type':'playlist'}
    headers={'content-type':'application/x-www-form-urlencoded'}
    jr=requests.get(url,params=payload,headers=headers)
    jrr=json.loads(jr.text)
    mp3name=jrr['name']
    mp3author=jrr['author']
    mp3url=jrr['url']
    if len(mp3url)>0:
        pass
    else:
        mp3url=('mp3直链获取失败！该歌曲可能为会员歌曲或暂无版权')

    print('\n歌曲名：',mp3name,
          '\n歌手：',mp3author,
          '\n下载链接：',mp3url)
    input('\n\n按enter退出')

else:
    input('请输入正确的选项')
