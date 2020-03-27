# steam=open('aa.txt',encoding='utf8')
# s=steam.read()
# print(s)
# steam.close()
# open命令必须定位到文件，不能是文件夹，涉及文件夹就要用到os模块
with open('aa.txt', 'w') as stream:
    stream.write('在我眼里你就是渣\n')
with open('aa.txt') as dd:
    print(dd.read())

with open('1.jpg', 'rb') as pic:
    contain = pic.read()
    with open('pictures/1.jpg', 'wb') as pic2:
        pic2.write(contain)

print('———————————————os模块部分——————————————————')
import os

print(os.path)
print(os.path.dirname(__file__))

# 将pictures中的1.jpg复制到当前目录
with open(r'pictures\1.jpg', 'rb') as pic:
    contain = pic.read()
    path1 = os.path.join(os.path.dirname(__file__), '2.jpg')
    print(path1)
    with open(path1, 'wb') as pic2:
        pic2.write(contain)

# 如果在实际开发中，经常看不到源文件的文件名，应该如下处理
print('看不到文件名的处理如下*********')
with open(r'pictures\1.jpg', 'rb') as pic:
    contain = pic.read()
    print(pic.name)  # pic的完整路径字符串
    picname = pic.name[pic.name.rfind('\\') + 1:]  # 切片操作，切出最右边的文件名部分
    path1 = os.path.join(os.path.dirname(__file__), picname)
    print(path1)
    with open(path1, 'wb') as pic2:
        pic2.write(contain)

# 一些用法
print('一些用法************')
print(os.path.isabs('images/girl.jpg'))
print(os.path.isabs('c:/images/girl.jpg'))
print(os.path.abspath(__file__))
print(os.path.dirname(__file__))
print(os.getcwd())  #当前文件文件夹的绝对路径

path2=r'pictures\1.jpg'
print(os.path.split(path2))
print(os.path.split(path2)[1])  # split得到绝对路径中的文件名
print(os.path.splitext(path2)[1])  # splitext得到绝对路径中的文件的扩展名，用来得知文件类型
print(os.path.getsize(path2))  # getsize得到文件的大小，单位是字节
print(os.path.join(os.path.split(path2)[0],'aaa','bbb','ccc','1.jpg')) # join函数可以将多个文件夹作为路径


# os.getcwd  os.listdir  os.mkdir  os.rmdir  os.remove  os.chdir
# src_path='c:\p1'
# target_path='c:\p2'
# filelist=os.listdir(src_path)
# if not os.path.exists(target_path):
#     os.mkdir(target_path)
# for file in filelist:
#     with open(os.path.join(src_path,file),'rb') as stre:
#         contain=stre.read()
#         with open(os.path.join(target_path,file),'wb') as stre_w:
#             stre_w.write(contain)

def copy(src_path='c:\p1',target_path='c:\p2'):
    if  not os.path.exists(target_path):
        os.mkdir(target_path)
    filelist = os.listdir(src_path)
    for file in filelist:
        with open(os.path.join(src_path, file), 'rb') as stre:
            contain = stre.read()
            with open(os.path.join(target_path, file), 'wb') as stre_w:
                stre_w.write(contain)
    else:
        print('复制完毕')

copy(target_path='c:\p4')  # 注意，省略第一个参数的方式是直接写target_path='c:\p3'，而不是(,'c:\p3')