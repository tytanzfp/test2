def funA(num):
    '''
    求列表奇数
    :param num: 输入一组数
    :return: 返回列表所有奇数
    '''
    sum=[]
    for x in num:
        if x%2==1:
            sum.append(x)
        pass
    return sum
    pass
# print(funA(range(100)))

def funB(dict):
    '''
    检查传入的字典value，如果长度大于2，只保留前2个字符
    :param dict:字典类型
    :return:
    '''
    for key,value in dict.items():

        if len(value)>=2:
            dict[key]=value[0:2]
            pass
        pass
    print(dict)
    return dict
    pass

funB({'a':'1','b':'22','c':'333','d':'4444','e':['福建','福州','南平']})