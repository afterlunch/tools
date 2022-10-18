from time import sleep
from IPy import IP
import time
import ipaddress
print("-----------------ip tools--------------------------------------------------")
print("|本程序可根据网段批量生成IP详单")
print("|This program can generate IP xDRs in batches based on network segments.")
print("|https://just1982.blogspot.com/")
print("|==========================================================================")
print("|----输入示例：   172.24.0.0/16---------------------------------------------")
# 判断ip地址输入是否符合规范
def check_ip(ipAddr):
  compile_ip = re.compile('^(1\d{2}|2[0-4]\d|25[0-5]|[1-9]\d|[1-9])\.(1\d{2}|2[0-4]\d|25[0-5]|[1-9]\d|\d)\.(1\d{2}|2[0-4]\d|25[0-5]|[1-9]\d|\d)\.(1\d{2}|2[0-4]\d|25[0-5]|[1-9]\d|\d)$')
  if compile_ip.match(ipAddr):
    return True
  else:
    return False

def main():
    p = input("请输入ip网段:")
    q = str(p)
    r = q.replace('/','_Mask_')
    nowtime = time.strftime('%m月%d日%H点%M分%S秒',time.localtime(time.time()))
    file = open(r + '_IP.txt', 'w')
    #p = input("请输入:")
    k = ipaddress.ip_network(q, strict=False)
    t = str(k)
    ip = IP(t) 
    print(ip)
    for x in ip:
        print (x)
        b = str(x)
        file.write(b + '\n')
    file.close()
    print(nowtime + '\n' + p + ' 段IP已生成。\n已写入'+ file.name)
    ttttime = time.strftime('%Y-%m-%d %H:%M:%S')
    print(ttttime)
    #count = len(open(file.name,'rU').readlines())
    main()
if __name__ == '__main__':
    main()
