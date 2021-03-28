import socket
import os
import whois
import time

#识别目标是否存在cdn
def cdn_check(url):
    cdn_data=os.popen('nslookup + url') #调用系统命令执行
    print (cdn_data)
    cdn_datas=cdn_data.read()
    x=cdn_datas.count('.')
    if x>8:  #如果不存在CDN 那么nslookup只会解析处一条ip ip连同域名一共八个.
        print("该域名存在CDN")
    else:
        print("该域名不存在CDN")

#端口扫描
#1.原生态 自己写socket协议进行tcp，udp扫描
#2.调用第三方masscan和nmap等扫描
#3.调用系统工具基本执行  
#这里使用socket协议进行
def portscan(url,port=80):
    server=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    ports=range(1,65535)
    for port in ports:
        if server.connect((url,port)):
            print(port+"端口处于开放状态")
        else:
            continue

#whois查询 ,这里引入了第三方whois库直接查    
def whois_check(url):
    data=whois.whois(url)
    print (data)

#子域名查询,这里是利用字典查询
def zym_check(url):
    for zym_data in open('dict.txt'):
        zym_data=zym_data.replace('\n','')
        url=zym_data+'.xueersi.com'  #生成子域名
        try:
            ip=socket.gethostname(url)
            print(url+'-->'+ip)
            time.sleep(0.1)
        except:
            pass

url=input("请输入您的url地址：")
port=input("请输入您要检测的端口号，默认为80端口")
if url:
    cdn_check(url)
    portscan(url,port)
    whois_check(url)
    zym_check(url)
