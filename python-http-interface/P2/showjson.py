import json
name=input("请输入你的姓名：")
phone=input("请输入你的电话号码：")

dict_info={"name":name,"phone":phone}
print(dict_info)
print(json.dumps(dict_info,ensure_ascii=False,indent=4))

'''
ensure_ascii参数默认为True,utf-8格式的非ASCII编码内容会被编译成ASCII码
要想得到字符的真实表示，需要将这个参数设置为False.
'''

