from random import *
def new_list():
    measurement_list = [90,60,90]
    new_list = []
    for u in range(len(measurement_list)):
        x = measurement_list[u] + randint(-3,3)
        new_list.append(x)
    return new_list

def char_list():
    character_list = [
    "ngoan hiền",
    'dễ thương', 'lễ phép', 'thích ăn kem', 'đáng yêu', 'thông minh', 'hài hước',
    'biết chăm lo người yêu',
    'cá tính', 'tự lập', 'biết làm đẹp', 'nấu ăn ngon', 'hát hay', 'thổi kèn khéo léo'
    , 'thơm tho','không thả thính lung tung', 'mặc quần ren đỏ',]
    x = sample(character_list,4)
    new_desciption = '{0}, {1}, {2},{3}'.format(x[0], x[1], x[2], x[3])

    return new_desciption
