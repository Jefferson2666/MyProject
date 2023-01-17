def division(x,y):
    try:
        return x/y #try - except 指令
    except ZeroDivisionError: #除數為0時執行
        print("除數不可為0")

print(division(10,2))
print(division(3,0))