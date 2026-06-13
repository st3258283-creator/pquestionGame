import 玩家模塊
import 章節1_地圖
from 引擎指令 import results
from 引擎資料 import *
from 章節1_資料 import *

def judgment(results):
    if results["轉向"]:
        turn = results["轉向"]
        玩家模塊.turn_(turn)
    if results["移動"]:
        move = [results["移動"],results["步數"]]
        玩家模塊.move_(move)

def text_ud() :
    if results["功能指令"] in function:
        pass
    if results["特殊指令"] in special:
        pass
    if results["動作"] in interaction:
        if results["物件"] in object_ :
            if results["物件"] in 玩家模塊.player["面前物件"]:
                pass
            else:pass
        elif results["物件"] in items:
            if results["物件"] in 玩家模塊.player["背包"]:
                pass
            else:pass
    if results["物件"] :
        if results["物件"] in object_:
            pass
        if results["物件"] in items:
            pass








