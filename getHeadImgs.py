# !/usr/bin/env python3
# _*_ coding:utf-8 _*_
# __author__='阳光流淌007'
# __date__ = '2018-03-06'
"""
https://zhuanlan.zhihu.com/p/34290391
"""
import re
import itchat

itchat.auto_login()

for friend in itchat.get_friends(update=True)[0:]:
    # 可以用此句print查看好友的微信名、备注名、性别、省份、个性签名（1：男 2：女 0：性别不详）
    print(friend['NickName'],
          friend['RemarkName'],
          friend['Sex'],
          friend['Province'],
          friend['Signature'])
    img = itchat.get_head_img(userName=friend["UserName"])

    # 在windows环境下替换非法字符
    rstr = "[\/\\\:\*\?\"\<\>\|]"
    new_NickName = re.sub(rstr, "_", friend['NickName'])

    path = 'avatars/{}({}).jpg'.format(new_NickName, friend['RemarkName'])
    try:
        with open(path, 'wb') as f:
            f.write(img)
    except Exception as e:
        print(repr(e))

itchat.run()
