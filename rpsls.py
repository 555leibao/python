#coding:gbk
"""
��һ��С��Ŀ��Rock-paper-scissors-lizard-Spock
���ߣ����
���ڣ�2021/12/1
"""

import random

# 0 - ʯͷ
# 1 - ʷ����
# 2 - ֽ
# 3 - ����
# 4 - ����

# ����Ϊ�����Ϸ����Ҫ�õ����Զ��庯��

def name_to_number(name):
    """
    ����Ϸ�����Ӧ����ͬ������
    """

    if name=="ʯͷ":# ʹ��if/elif/else��佫����Ϸ�����Ӧ����ͬ������
       return 0
    elif name=="ʷ����":
        return 1
    elif name=="ֽ":
        return 2
    elif name=="����":
        return 3
    elif name=="����":
        return 4
    else:
        print("Error:No Correct Name")



def number_to_name(number):
    """
    ������ (0, 1, 2, 3, or 4)��Ӧ����Ϸ�Ĳ�ͬ����
    """
    if number==0:
        return "ʯͷ"
    elif number==1:
        return "ʷ����"
    elif number==2:
        return "��"
    elif number==3:
        return "����"
    elif number==4:
        return "����"
    # ʹ��if/elif/else��佫��ͬ��������Ӧ����Ϸ�Ĳ�ͬ����
    # ��Ҫ���Ƿ��ؽ��

#��дִ�д���,������ɺ�passɾ��


def rpsls(player_choice):
    """
    �û�����������һ��ѡ�񣬸���RPSLS��Ϸ��������Ļ�������Ӧ�Ľ��
    """
    print("-------")  # ���"-------- "���зָ�
    print("����ѡ��Ϊ��%s" % player_choice)  # ��ʾ�û�������ʾ���û�ͨ�����̽��Լ�����Ϸѡ��������룬�������player_choice
    player_choice_number = name_to_number(player_choice)  # ����name_to_number()�������û�����Ϸѡ�����ת��Ϊ��Ӧ���������������player_choice_number
    comp_number = random.randint(0, 4)  # ����random.randrange()�Զ�����0-4֮��������������Ϊ��������ѡ�����Ϸ���󣬴������comp_number
    computer_result = number_to_name(comp_number)  # ����number_to_name()����������������������ת��Ϊ��Ӧ����Ϸ����
    print("�������ѡ��Ϊ��%s" % computer_result)  # ����Ļ����ʾ�����ѡ����������
    gap=player_choice_number-comp_number
    if gap==1 or gap ==2 or gap ==-3 or gap ==-4:  # ����if/elif/else ��䣬����RPSLS������û�ѡ��ͼ����ѡ������жϣ�������Ļ����ʾ�жϽ��
        print("��Ӯ�ˣ�")
    elif gap==0:
        print("��ͼ��������һ���أ�")  # ����û��ͼ����ѡ��һ��������ʾ�����ͼ��������һ���ء�������û���ʤ������ʾ����Ӯ�ˡ�����֮����ʾ�������Ӯ�ˡ�
    else:
        print("����Ӯ�ˣ�")

#����������ʾ��дִ�д��룬������ɺ�ɾ����pass


# �Գ�����в���
print("��ӭʹ��RPSLS��Ϸ")
print("----------------")
print("����������ѡ��:")
my_choice=input()
rpsls(my_choice)


