# 要有狀態卡 移動 功能指令
from 引擎資料 import *
import 引擎指令
import 章節1_地圖


# 角色狀態(紀錄用)
player = {"X":0,"Y":0,"方向":2,"背包":[]}
base = [(0,-1),(-1,-1),(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1)] # 下 左下 左 左上 上 右上 右 右下
around = {'前': [(0, -1), '空'], '右前': [(-1, -1), '空'], '右': [(-1, 0), '空'], '右後': [(-1, 1), '床'],
          '後': [(0, 1), '床'], '左後': [(1, 1), '床'], '左': [(1, 0), '空'], '左前': [(1, -1), '空']}
# around = {"方向":[[對應方向座標],[對應方向物件]]}
#=====================================================================================================================
# 當前座標更新
def forward():
    global around
    around = {"前": [[], []], "右前": [[], []], "右": [[], []], "右後": [[], []],
              "後": [[], []], "左後": [[], []], "左": [[], []], "左前": [[], []]}
    for i,way in enumerate(around):
        if player["方向"] == 2: # 南
            shift = 0
        elif player["方向"] == 3: # 西
            shift = 2
        elif player["方向"] == 4: # 北
            shift = 4
        elif player["方向"] == 1: # 東
            shift = 6
        dx,dy = base[(i+shift)%8]
        around[way][0] = (player["X"] + dx,
                          player["Y"] + dy)

    for a, b in 章節1_地圖.block.items():
        for way in around:
            if around[way][0] in b:
                around[way][1] = a
    for a in around:
        if around[a][1] == []:
            around[a][1] = "空"


#=====================================================================================================================

#   移動函數+面前座標判定+面前物件判定

def move_(action_): # 移動函數(移動方式,移動步數)

    movement = action_[0]  # 移動方式
    stepcount = action_[1]  # 移動步數
    # 判定移動位置
    while stepcount > 0 :
        if movement == ["往前"]:
            if around["前"][1] == "空":
                if player["方向"] == 2 :
                    player["Y"] -= 1
                    stepcount -= 1
                elif player["方向"] == 4 :
                    player["Y"] += 1
                    stepcount -= 1
                elif player["方向"] == 1 :
                    player["X"] += 1
                    stepcount -= 1
                elif player["方向"] == 3 :
                    player["X"] -= 1
                    stepcount -= 1
            else:
                stepcount = 0  # 如果前方不是空的 就停止移動
        elif movement == ["往後"]:
            if around["後"][1] == "空":
                if player["方向"] == 2 :
                    player["Y"] += 1
                    stepcount -= 1
                elif player["方向"] == 4 :
                    player["Y"] -= 1
                    stepcount -= 1
                elif player["方向"] == 1 :
                    player["X"] -= 1
                    stepcount -= 1
                elif player["方向"] == 3 :
                    player["X"] += 1
                    stepcount -= 1
            else:
                stepcount = 0  # 如果後方不是空的 就停止移動
        elif movement == ["往左"]:
            if around["左"][1] == "空":
                if player["方向"] == 2 :
                    player["X"] += 1
                    stepcount -= 1
                elif player["方向"] == 4 :
                    player["X"] -= 1
                    stepcount -= 1
                elif player["方向"] == 1 :
                    player["Y"] += 1
                    stepcount -= 1
                elif player["方向"] == 3 :
                    player["Y"] -= 1
                    stepcount -= 1
            else:
                stepcount = 0  # 如果左方不是空的 就停止移動
        elif movement == ["往右"]:
            if around["右"][1] == "空":
                if player["方向"] == 2 :
                    player["X"] -= 1
                    stepcount -= 1
                elif player["方向"] == 4 :
                    player["X"] += 1
                    stepcount -= 1
                elif player["方向"] == 1 :
                    player["Y"] -= 1
                    stepcount -= 1
                elif player["方向"] == 3 :
                    player["Y"] += 1
                    stepcount -= 1
            else:
                stepcount = 0  # 如果右方不是空的 就停止移動
        else:
            # 非法或未知移動方式，停止
            stepcount = 0
        forward()

#=====================================================================================================================

# 改面向 轉向函數
def turn_(a):
    # 轉向偵測
    if a == ["右轉"]:
        player["方向"] = player["方向"] % 4 + 1
    elif a == ["左轉"]:
        player["方向"] = (player["方向"]-2) % 4 + 1
    elif a == ["向後轉"]:
        player["方向"] = (player["方向"]+1) % 4 + 1
    forward()
#=====================================================================================================================

