# -*- coding: utf-8 -*-
'''2018 - 3 - 15 - 22 -19'''
from PIL import Image
import time

codeLib = '''@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?- _+~<>i!lI;:,"^`'. '''#生成字符画所需的字符集
count = len(codeLib)

def transform1(image_file):
    image_file = image_file.convert("L")#转换为黑白图片，参数"L"表示黑白模式
    codePic = ''
    for h in range(0,image_file.size[1]):  #size属性表示图片的分辨率，'0'为横向大小，'1'为纵向
        for w in range(0,image_file.size[0]):
            gray = image_file.getpixel((w,h)) #返回指定位置的像素，如果所打开的图像是多层次的图片，那这个方法就返回一个元组
            codePic = codePic + codeLib[int(((count-1)*gray)/256)]#建立灰度与字符集的映射
        codePic = codePic+'\r\n'
    return codePic

def main():
    name = input("请确保无误后，将文件拖入cmd中，删掉双引号：")
    start = time.clock()
    fp = open('%s'%name,'rb')
    image_file = Image.open(fp)

    temp = image_file.size[1]*image_file.size[0]
    #######################################
    #设置图片比例 
    #根据需要 ，自行设置
    x = 0.18
    y = 0.1
    ######################################

    image_file=image_file.resize((int(image_file.size[0]*x), int(image_file.size[1]*y)))#调整图片大小
    print ('Info:',image_file.size[0],' ',image_file.size[1],' ',count)


    tmp = open('%s.txt'%name,'w')
    tmp.write(transform1(image_file))
    tmp.close()

    end = time.clock()
    print("用时：",end-start,"s")
    time.sleep(3)#睡3秒


if __name__ == '__main__':
    main()