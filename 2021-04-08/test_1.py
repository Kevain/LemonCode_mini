# -*- coding: utf-8 -*-
"""
@FileName：test_1.py
@Description：
@Author：Ken
@Time：2021/6/6 21:21
"""
# (0)输入0后效果如下：
# 	0
# 	["郭易","汤碗珍"..]
#
# (1)输入1后效果如下：
# 	1
# 	请输入增加人的姓名：张三
# 	["郭易","汤碗珍",'张三'..]
#
# (2)输入2后效果如下：
# 	2
# 	请输入删除人的姓名：张三
# 	["郭易","汤碗珍"..]
#
# (3)输入3后效果如下：<注意：如果list中没有这个学员则打印：T666班没有这个学员>
# 	3
# 	请输入需要修改人的姓名：张三
# 	请输入需要修改后的姓名：李四
# 	["郭易","汤碗珍",'李四'..]
#
# (4)输入4后效果如下：<注意：如果list中没有这个学员则打印：T666班没有这个学员>
# 	请输入查询人的姓名：张三
# 	郭易在座位号(3<下标>)的位置。
#
# (5)输入exit后效果如下：
# 	exit
# 	欢迎使用T666的学生管理系统，下次再见。
#
#
info = []


# 有界面，就像我们去银行取钱,我们在控制台也给1个界面
def info_print():
    print('-----------------------欢迎进入 T666 班学生管理系统-----------------------------')
    print('0:显示所有学员信息')
    print('1:添加一个学员信息')
    print('2:删除一个学员信息')
    print('3:修改一个学员信息')
    print('4:查询一个学员信息')
    print('5:exit:退出学生管理系统')
    print('-' * 80)


# 添加学员信息:
# 1.用户帮你输入学员信息，输入学员编号，学员姓名，学员性别
# 2.输入完信息保存到哪保存到字典中
# 3.一个班级中的学员，信息保存到列表中
# 考虑：名字相同的学员，给个友好提示：学员姓名已存在
def add_stu():
    # 用户帮你输入学员信息
    new_id = input('请输入学员编号:')
    new_name = input('请输入学员姓名:')
    new_age = input('请输入学员年龄:')

    # 名字相同的学员，给个友好提示：学员姓名已存在
    # 是不是要先把所有的名字都循环一遍，在对比你输入的名字是不是重复的
    # 循环info，拿到所有学员的信息
    for i in info:
        print('所有学员信息%s' % i)
        if i['name'] == new_name:
            print('此用户已经存在')
            # 退出当前函数，后面不添加学员信息
            return

    # 2.输入完信息保存到哪保存到字典中,定义一个空字典，字典怎么添加值？增加一个键，在给个值
    info_dict = {}
    info_dict['id'] = new_id
    info_dict['name'] = new_name
    info_dict['age'] = new_age
    # print(info_dict)
    info.append(info_dict)
    print(info)


# 删除学员
# 1.用户输入学员姓名，学员存在就删除
# 2.学员不存在就提示该学员不存在

# 删除学员
def del_stu():
    # 输入要删除的学员名字
    del_name = input('请输入要删除的学员姓名:')
    # 判断学员姓名是否存在，存在则删除，否则提示该学员不在
    # 整个循环结束后，执行else
    for i in info:
        if del_name == i['name']:
            # 列表删除数据
            info.remove(i)
            break
    else:
        print('要删除的学员不存在')
    print(info)


# 修改学员
# 1.用户输入修改学员姓名，学员存在就修改
# 2.学员不存在就提示该学员不存在
# 修改学员
def update_stu():
    upd_stu = input('请输入要修改的学员姓名：')
    # 判断学员是否已存在
    for i in info:
        if i['name'] == upd_stu:
            i['name'] = input('请输入要修改的名字：')
            break
    else:
        print('要修改的学员不存在')
    print(info)


# 查询学员
# 1.用户输入查询学员姓名，学员存在就查询
# 2.学员不存在就提示该学员不存在
# 查询学员信息函数
def search_info():
    # 输入要查询的学员姓名
    search_name = input('请输入要查询的学员姓名:')
    # 检查学员是否存在  遍历  遍历什么，遍历info
    for i in info:
        if i['name'] == search_name:
            print(f"学员信息：学号是{i['id']},姓名是{i['name']}，年龄是{i['age']}")
            break
    else:
        print('要查询的学员不存在')
    print(info)


# 查询所有学员,直接遍历所有学员信息
def search_all():
    # 打印提示字
    print('学号\t姓名\t手机号')
    # 打印所有学员的数据
    for i in info:
        print(f"{i['id']},{i['name']},{i['age']}")


while True:
    info_print()
    # 用户输入不同的序号，能执行不同的功能
    user_print = int(input('用户请输入功能序号:'))
    # 在不退出学员系统的情况下，是可以一直添加修改学员的，那我现在想要做到不按5之前，就不退出，用循环

    # 判断，如果输入0，就显示所有学员信息
    if user_print == 0:
        # print('0:显示所有学员信息')
        search_all()
    elif user_print == 1:
        # print('1:添加一个学员信息')
        add_stu()
    elif user_print == 2:
        # print('2:删除一个学员信息')
        del_stu()
    elif user_print == 3:
        # print('3:修改一个学员信息')
        update_stu()
    elif user_print == 4:
        # print('4:查询一个学员信息')
        search_info()
    elif user_print == 5:
        print('5:exit:退出学生管理系统')
        # 直接给个5就能退出
        # break
        exit_flag = input('确定要退出系统吗?yes or no')
        if exit_flag == 'yes':
            break
    else:
        print('输入功能序号有误')
