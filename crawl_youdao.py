

'''
"你好","src":"hello"}]],"errorCode":0,"type":"en2zh-CHS","smartResult":{"entries":["","n. 表示问候， 惊奇或唤起注意时的用语\r\n","int. 喂；哈罗\r\n","n. (Hello)人名；(法)埃洛\r\n"],"type":1}}

http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule
'''

import requests
import json
import time
import hashlib
import random

word = input("please enter the word")
url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'

'''
var
r = function(e)
{
    var
t = n.md5(navigator.appVersion),
    r = "" + (new Date).getTime(),
        i = r + parseInt(10 * Math.random(), 10);
return {
    ts: r,
    bv: t,
    salt: i,
    sign: n.md5("fanyideskweb" + e + i + "n%A-rKaT5fb[Gy?;N5@Tj")
}
};
'''

header = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36',
    'Referer': 'http://fanyi.youdao.com/',
    'Cookie': 'OUTFOX_SEARCH_USER_ID=1885494528@10.169.0.83; JSESSIONID=aaa7WLoy3p1LU9FO4hc9w; OUTFOX_SEARCH_USER_ID_NCOO=792147090.3028487; ___rl__test__cookies=1577362530605'
}

# reformat coat
data = {
    'i': word,
    'from': 'AUTO',
    'to': 'AUTO',
    'smartresult': 'dict',
    'client': 'fanyideskweb',
    # 盐 时间戳 + 4位随机数
    'salt': '15773625306098',
    # JS  加密
    'sign': 'c14b7e838dd531e85b981387e806f47a',
    # 毫秒的时间戳
    'ts': '1577362530609',
    'bv': '10695818032b95bf045a585ae8c1ebaa',
    'doctype': 'json',
    'version': '2.1',
    'keyfrom': 'fanyi.web',
    'action': 'FY_BY_CLICKBUTTION',
}

ts = int(time.time()*10000)

salt = ts + int(random.random()*10)

sign = "fanyideskweb" + word + str(salt) + "n%A-rKaT5fb[Gy?;N5@Tj"
sign = hashlib.md5(sign.encode('utf-8')).hexdigest()


data['ts'] = ts
data['salt'] = salt
data['sign'] = sign


# 为什么用post发送请求 查看源网站

r = requests.post(url,headers=header,data=data)
print(r)

# 200 请求成功 404 未找到 500  301

print(r.json())

# {'errorCode': 50} 反爬
# user-agent
# ip代理池
# Referer 从哪里访问网站
# cookie 用户信息 本地 session      cookie和session 的区别

