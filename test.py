def write114514():
    name=input('please input target file\'s name:')
    info=open('D:\\IDE\\PythonProjects\\knowledge_project\\'+name+'.txt','a')
    yourinput = input('please add your text：')
    words=info.write(yourinput+'\b')
    info.close()

def clear():
    name = input('please input clear_file\'s name:')
    info2 = open('D:\\IDE\\PythonProjects\\knowledge_project\\' + name + '.txt', 'w')
    info2.write('')
    info2.close()

def encode():
    name1 = input('please input original_file\'s name:')
    info1=open('D:\\IDE\\PythonProjects\\knowledge_project\\'+name1+'.txt', 'r',encoding='utf-8')
    name2=input('please input encode_file\'s name:')
    info2=open('D:\\IDE\\PythonProjects\\knowledge_project\\'+name2+'.txt', 'w',encoding='utf-8')
    text='1'
    while text !='':
        text = info1.read(1)
        if text !='':

            words=info2.write(str(chr(ord(text)^0x24)))
        else:
            break
    info1.close()
    info2.close()

def operate():
    n = int(input('请选择以下操作\n-1.退出\n1.写文件\n2.清除内容\n3.加密文件\n'))
    while n != -1:
        if n == 1:
            write114514()
        if n == 2:
            clear()
        if n == 3:
            encode()
        n = int(input('请选择以下操作\n-1.退出\n1.写文件\n2.清除内容\n3.加密文件\n'))

  
