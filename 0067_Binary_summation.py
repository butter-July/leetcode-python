class Solution(object):
    def addBinary(self, a, b):
        A=0
        B=0
        for i in range(len(a)):
            A+=int(a[i])*(2**(len(a)-1-i))
        for j in range(len(b)):
            B+=int(b[j])*(2**(len(b)-1-j))                  #注意这因为ab都是字符串所以要把他们都转化成int才能进行进制的转换而不是直接ij的运算!!/
        C=A+B
        if C==0:
            return '0'
        c=''                   #记得对c进行初始化''或者""无所谓
        while C>0:
            c=str(C%2)+c             #因为c是字符串了所以+代表连接的意思而不是数值的相加并且这里的C是int取余后要换成str
            C=C//2                      #C进行整除慢慢的进行二进制的转换
        return c        
