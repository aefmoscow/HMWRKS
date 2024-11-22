# комментарии не читайте!!! все для обучения на pythontutor.com

for lft_stn in range(3, 21): #(от 3 до 20) случайным образом
    rght_stn = f' Pass for [{lft_stn}]' #подготовка приставки в цикле
    for a in range(1, lft_stn):
        for b in range(2, lft_stn):
            if lft_stn % (a + b) == 0: #если нет- идем пересчитывать в 6 стр
                rght_stn =  f'{rght_stn}:  {a} {b} '
    print(rght_stn)
