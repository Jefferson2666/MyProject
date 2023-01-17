def division(x,y):
    try:
        ans = x/y #try - except 指令
    except ZeroDivisionError: #除數為0時執行
        print("除數不可為0")
    else:
        return ans #傳回正確的執行結果

print(division(10,2),"\n",division(5,0))
