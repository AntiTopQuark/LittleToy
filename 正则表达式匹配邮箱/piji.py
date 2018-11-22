import re

re_email = re.compile(r'^[0-9a-zA-Z\.\-\_\#\$\%\^\&\*\!]+@[a-zA-z0-9]+(\.com)$')
re_time = re.compile(r'^(0[0-9]|1[0-9]|2[0-3]|[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])$')
re_date = re.compile(r'^(0[1-9]|1[0-2]|[0-9])(-|/|:)(0[1-9]|1[0-9]|2[0-9]|3[0-1]|[0-9])$')


def judge(string):
    if re_email.match(string):
        print("OK,It`s a email")
    else:
        print("NO\n")
while(1):
    try:
        string = input("输入字符串:")
        judge(string)
    except:
        break
    
