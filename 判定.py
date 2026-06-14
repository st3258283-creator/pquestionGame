import 玩家模塊
import 章節1_地圖
from 引擎指令 import results
from 引擎資料 import *
from 章節1_資料 import *

def judgment(results):
    interact_tiles = ["前","左前","右前"]
    if results["轉向"]:
        turn = results["轉向"]
        玩家模塊.turn_(turn)
    if results["移動"]:
        move = [results["移動"],results["步數"]]
        玩家模塊.move_(move)
    if results["動作"] == "打開":
        for a in interact_tiles:
            if 玩家模塊.around[a][1] == results["物件"]:
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

def text_ud() :
    if results["功能指令"] in function:
        pass
    if results["特殊指令"] in special:
        pass
    # if results["動作"] in interaction:
    #     if results["物件"] in object_ :
    #         if results["物件"] in 玩家模塊.player["面前物件"]:
    #             pass
    #         else:pass
    #     elif results["物件"] in items:
    #         if results["物件"] in 玩家模塊.player["背包"]:
    #             pass
    #         else:pass
    # if results["物件"] :
    #     if results["物件"] in object_:
    #         pass
    #     if results["物件"] in items:
    #         pass








