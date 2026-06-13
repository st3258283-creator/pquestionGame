import 判定
import 引擎指令
import 玩家模塊
import 引擎資料
import 主頁面
import 章節1_地圖

while True:
    引擎指令.results = {"動作":[],"物件":[],"移動":[],"步數":0,"轉向":[],"功能指令":[],"特殊指令":[]}
    action = 引擎指令.play_() # 指令解析
    判定.judgment(action)
    # 臨時實驗.export_()

    print(引擎指令.results)
    print(玩家模塊.player)
    print(玩家模塊.around)
    if 引擎指令.results["功能指令"] == ["休息"]:
        break
    # print(引擎資料.direction[player["方向"]])