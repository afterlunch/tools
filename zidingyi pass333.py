import random
import time
m = int(input("【   密码生成器    】\n【已去除易混淆字母 0 数字0 字母l 数字1 等】\n【https://just1982.blogspot.com/】\n请输入开头大写占几位 默认1 生成9位密码  ") or "1")

def ma():
    f = random.sample('ABCDEFGHIJKLMNPQRSTUVWXYZ',m)
    a = random.sample('abcdefghijkmnpqrstuvwxyz',2)
    b = random.sample('ABCDEFGHIJKLMNPQRSTUVWXYZ',2)
    g = random.sample('23456789',3)
    c = random.sample('.+-=',1)
    g = random.sample(c + a + g ,6)
    d = "".join( f + g +  b )
    print(d)
    return d
    
    #file.write(d + '\n')
def xshu():
    i  = int(input('请输入生成的密码条数'))
    nowtime = time.strftime('%m月%d日%H点%M分%S秒',time.localtime(time.time()))
    file = open(nowtime + '_pw.txt', 'w')
    for num in range(0,i):
            file.write(str(ma())  + '\n')           
    file.close()
    print('已成功生成  '+ str(i) + '  条密码\n密码已写入 《'+ nowtime + '_pw.txt 》文件')
if __name__ == '__main__':
    while True:
        xshu()