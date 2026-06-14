from 引擎資料 import *
from 章節1_資料 import *

#=============================================================================
# 解析函數
results = {"動作":[],"物件":[],"移動":[],"步數":0,"轉向":[],"功能指令":[],"特殊指令":[]}
def play_():
    command = input()
    ago, after = "", "" # 數字轉換器的倉儲
    num =  "".join(b for b in command if b.isdigit()) # 阿拉伯數字取出
    if num:
        results["步數"] = int(num)

    # 中文數字轉換器
    if "十" in command:
        ten_position = command.index("十")
        if ten_position != 0 and command[ten_position-1] in numbers :
            ago = command[ten_position-1]
        if ten_position != len(command)-1 and command[ten_position+1] in numbers :
            after = command[ten_position+1]
        if ago == "":
            n10 = 10
        elif ago != "":
            n10 = numbers[ago] * 10
        if after == "":
            n1 = 0
        elif after != "":
            n1 = numbers[after]
        results["步數"] = n1 + n10
    else:
        for a in command:
            if a in numbers:
                results["步數"] = numbers[a]

    for a in interaction:
        if a in command:
            results["動作"] = a

    for a in sorted(object_,key=len,reverse=turn):
        if a in command:
            results["物件"] = a
            break

    for a in move:
        if a in command:
            results["移動"] = a

    for a in turn:
        if a in command:
            results["轉向"] = a

    for a in function:
        if a in command:
            results["功能指令"] = a

    for a in special:
        if a in command:
            results["特殊指令"] = a
    return results

#=============================================================================
# 獲取玩家指令 跟上面的解析函數配套
# def play_():
#     action = input()
#     return parsing_(action)

#測試
if __name__ == "__main__":
    print(play_())



