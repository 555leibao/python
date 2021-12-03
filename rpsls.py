#coding:gbk
"""
第一个小项目：Rock-paper-scissors-lizard-Spock
作者：舒奎
日期：2021/12/1
"""

import random

# 0 - 石头
# 1 - 史波克
# 2 - 纸
# 3 - 蜥蜴
# 4 - 剪刀

# 以下为完成游戏所需要用到的自定义函数

def name_to_number(name):
    """
    将游戏对象对应到不同的整数
    """

    if name=="石头":# 使用if/elif/else语句将各游戏对象对应到不同的整数
       return 0
    elif name=="史波克":
        return 1
    elif name=="纸":
        return 2
    elif name=="蜥蜴":
        return 3
    elif name=="剪刀":
        return 4
    else:
        print("Error:No Correct Name")



def number_to_name(number):
    """
    将整数 (0, 1, 2, 3, or 4)对应到游戏的不同对象
    """
    if number==0:
        return "石头"
    elif number==1:
        return "史波克"
    elif number==2:
        return "布"
    elif number==3:
        return "蜥蜴"
    elif number==4:
        return "剪刀"
    # 使用if/elif/else语句将不同的整数对应到游戏的不同对象
    # 不要忘记返回结果

#编写执行代码,代码完成后将pass删除


def rpsls(player_choice):
    """
    用户玩家任意给出一个选择，根据RPSLS游戏规则，在屏幕上输出对应的结果
    """
    print("-------")  # 输出"-------- "进行分割
    print("您的选择为：%s" % player_choice)  # 显示用户输入提示，用户通过键盘将自己的游戏选择对象输入，存入变量player_choice
    player_choice_number = name_to_number(player_choice)  # 调用name_to_number()函数将用户的游戏选择对象转换为相应的整数，存入变量player_choice_number
    comp_number = random.randint(0, 4)  # 利用random.randrange()自动产生0-4之间的随机整数，作为计算机随机选择的游戏对象，存入变量comp_number
    computer_result = number_to_name(comp_number)  # 调用number_to_name()函数将计算机产生的随机数转换为对应的游戏对象
    print("计算机的选择为：%s" % computer_result)  # 在屏幕上显示计算机选择的随机对象
    gap=player_choice_number-comp_number
    if gap==1 or gap ==2 or gap ==-3 or gap ==-4:  # 利用if/elif/else 语句，根据RPSLS规则对用户选择和计算机选择进行判断，并在屏幕上显示判断结果
        print("你赢了！")
    elif gap==0:
        print("你和计算机出的一样呢！")  # 如果用户和计算机选择一样，则显示“您和计算机出的一样呢”，如果用户获胜，则显示“您赢了”，反之则显示“计算机赢了”
    else:
        print("机器赢了！")

#根据以上提示编写执行代码，代码完成后删除掉pass


# 对程序进行测试
print("欢迎使用RPSLS游戏")
print("----------------")
print("请输入您的选择:")
my_choice=input()
rpsls(my_choice)


