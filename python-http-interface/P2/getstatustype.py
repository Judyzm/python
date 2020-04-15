def printHttpMsg(statuscode,stauscodetpye):
    '''定义函数，输出状态码对应的类别及信息
    statuscode为getStatuscode函数的返回值
    stauscodetpye为状态码对应的类别，用statuscode[0]取该字符串的第一个元素+'XX'
    '''
    dictTypeMsg={
        '1XX':'服务器收到请求，需要请求者继续执行操作',
        '2XX':'成功，操作被成功接收并处理',
        '3XX':'重定向，需要进一步的操作以完成请求',
        '4XX':'客户端错误，请求包含语法错误或无法完成请求',
        '5XX':'服务器错误，服务器在处理请求的过程中发生了错误'
    }
    print("你输入的状态码"+str(statuscode)+'属于'+str(stauscodetpye)+'类')
    #
    print("分类描述"+dictTypeMsg[stauscodetpye])

def getStatuscode():
    '''定义的函数是为了确认输入的状态码合法，通过while将不合法的循环处理直到合法
    statuscode.isdigit()检查该字符串是否全部为数字
    如果合法，则return直接返回
    '''
    statuscode=input("请输入你要查询的状态码：")
    while not statuscode.isdigit()or int(statuscode)<100 or int(statuscode)>599:
        print("输入的状态码不合法，合法的状态码为100-599")
        statuscode=input("请输入你要查询的状态码：")
    else:
        return statuscode
statuscode=getStatuscode()
printHttpMsg(statuscode,statuscode[0]+'XX')








