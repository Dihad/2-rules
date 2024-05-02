num = int(input('enter the number: '))
working_num = num
holding_list = []
holding_list.append(num)
loop_breaker = 0
while loop_breaker == 0:
    if working_num % 2 == 0:
        working_num = working_num/2
        holding_list.append(int(working_num))
        if working_num == 1:
            loop_breaker=1
    if working_num % 2 == 1:
        working_num = working_num * 3
        working_num = working_num + 1
        holding_list.append(int(working_num))
print(holding_list) 