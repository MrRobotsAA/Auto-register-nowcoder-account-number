"""
:file: validation.py
:description: 从速码获取注册用手机号并获取其验证码

"""

from urllib import request, parse
import sys

username = 'khn64'
passwd = 'chenonly1'
pid = '54672'
province = ''
logIn = 'logIn'; getUserInfos = 'getUserInfos'; getMobilenum='getMobilenum'; getVcodeAndReleaseMobile = 'getVcodeAndReleaseMobile'
token = '556ced690ce5c09c11168cb4cf23282a'
phoneType = 'CMCC'


def get_phone():
    get_phone_url = 'http://api.eobzz.com/httpApi.do?action=%s&pid=%s&uid=%s&token=%s&province=%s&phoneType=%s'\
        % (getMobilenum, pid, username, token, parse.quote(province, encoding='utf-8'), phoneType)
    Req = request.Request(get_phone_url)
    data = request.urlopen(Req).read().decode('utf-8')
    return str(data).split('|')[0]


"""
:param phone: 获取验证码的电话号码
:return: 
"""
def get_validation(phone):
    get_key_url = 'http://api.eobzz.com/httpApi.do?action=%s&mobile=%s&token=%s&uid=%s'\
          % (getVcodeAndReleaseMobile, phone, token, username)
    data = request.urlopen(get_key_url).read().decode('utf-8')
    return data
