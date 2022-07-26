perc = []
water = []
sort = []
j = 0
while j != 5:
    j+=1
    i = input('소금물의 농도(%)와 소금물의 양(g)을 입력하십시오 : ')
    if i != 'Done':
        perc.append(int(i.split('%')[0]))
        water.append(int(i.split(' ')[1].rstrip('g')))
        sort.append(((int(i.split('%')[0]))/(int(i.split(' ')[1].rstrip('g'))))*100)

                                    
    elif i == 'Done':
        reso = sum(sort)
        rewa = sum(water)
        re = (rewa/reso)*100
        print(f'{re}% {rewa}g')


