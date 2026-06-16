
import 玩家模塊
import 章節1_地圖
from 引擎指令 import results
from 引擎資料 import *
from 玩家模塊 import player
from 章節1_資料 import *
interact_tiles = ["前","左前","右前"]

def action():
    if results["動作"] == "打開":
        if "父物件" in results["物件"]:
            i = results["物件"]["父物件"]
        else: i = results["物件"]
        for a in interact_tiles:
            if 玩家模塊.around[a][1] == i:
                if "開啟" in object_[results["物件"]]:
                    if object_[results["物件"]]["開啟"]:
                        print("已開啟過")
                        break
                    else:
                        if "封鎖" not in object_[results["物件"]]:
                            object_[results["物件"]]["開啟"] = True
                            print(f"已成功開啟{results["物件"]}")
                            break
                        if "封鎖" in  object_[results["物件"]]:
                            if object_[results["物件"]]["封鎖"]:
                                print("已被上鎖")
                                break
                            if not object_[results["物件"]]["封鎖"]:
                                object_[results["物件"]]["開啟"] = True
                                print(f"已成功開啟{results["物件"]}")
                                break
                else:
                    print(f"你嘗試打開{results["物件"]}，但無從下手")
                    break
            else:print(f"你摸索了半天，發現前方沒有{results["物件"]}")

    if results["動作"] == "拿取":
        if results["物件"] in items :
            if "父物件" in object_[items[results["物件"]]["位置"]] :
                i = object_[items[results["物件"]]["位置"]]["父物件"]
            else:  i = object_[items[results["物件"]]["位置"]]
            for a in interact_tiles:
                if 玩家模塊.around[a][1] == i :
                    if object_[items[results["物件"]]["位置"]]["開啟"]:
                        player["背包"].append(results["物件"])
                        print(f"你把{results["物件"]}放入了背包")
                        break
                    elif not object_[items[results["物件"]]["位置"]]["開啟"]:
                        print(f"你試圖拿取{results["物件"]},但沒發現它的位置")
                        break

    if results["動作"] == "使用":
        if results["物件"] in items :
            if results["物件"] in player["背包"]:
                print(f"你已使用{results["物件"]}")
            else:print(f"你在身上摸索半天，發現沒有{results["物件"]}")
        else:print("這物件貌似不能使用")

#=================================================================================================
def function_() :
    if results["功能指令"] == "查看背包":
        print(f"背包裡有{player["背包"]}")
#==================================================================================================
def judgment(results):
    if results["轉向"]:
        turn = results["轉向"]
        玩家模塊.turn_(turn)
    if results["移動"]:
        move = [results["移動"],results["步數"]]
        玩家模塊.move_(move)
    if results["動作"]:
        action()
    if results["功能指令"]:
        function_()



    # if results["特殊指令"] in special:
    #     pass
    # if results["動作"] in interaction:
    #     action()
    #









