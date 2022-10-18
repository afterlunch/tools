from concurrent.futures import thread
import pandas as pd
import time
import datetime
from ast import main
import paramiko
from concurrent.futures import ThreadPoolExecutor,wait
import threading
df = pd.read_excel("data.xlsx")
def printtt(num):
        print(df.values[num,0])
        ip = str(df.values[num,0])
        file = open(ip + 'log.txt', 'w')
        time.sleep(1)
        name = str(df.values[num,1])
        paswd = str(df.values[num,2])
        time.sleep(1)
        npa = str(df.values[num,3])
        ssh=paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(hostname=ip,port=22,username=name,password=paswd)
        print("成功连接"  + ip )
        command=ssh.invoke_shell()
        time.sleep(20)
        command.send("ipmcset -d adduser -v superuser\n")
        time.sleep(5)
        #print(command.recv(2000))
        command.send(paswd + '\n')
        time.sleep(5)
        command.send(npa + '\n')
        time.sleep(5)
        command.send(npa + '\n')
        time.sleep(5)
        command.send('ipmcset -d privilege -v superuser 4')
        time.sleep(5)
        command.send('\n')
        time.sleep(5)
        command.send(paswd)
        time.sleep(5)
        time.sleep(5)
        command.send('\n')
        time.sleep(5)
        time.sleep(5)
        output=command.recv(65535)
        aaaaaa = str(output)
        file.write(aaaaaa + '\n')
        file.close()
        print(output)
        ssh.close() 
def main():
    a_thread =  threading.Thread(target=printtt())
    a_thread.start()
def threpooexe():
    executor = ThreadPoolExecutor(max_workers=65535)
    t = [executor.submit(printtt,num) for num in range(0, 7)]
    if wait(t, return_when='ALL_COMPLETED'):
        end_time = datetime.datetime.now()
        print("完成", end_time)
        #break
if __name__ == '__main__':
    threpooexe()