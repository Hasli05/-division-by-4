raw_numbers = int(input("Введи ціле число :"))
pre_result2 = raw_numbers % 2
pre_result4 = raw_numbers % 4

if pre_result2 == 0 and pre_result4 == 0:
    print("Число", raw_numbers, "парне і ділится націло на 4")
elif pre_result2 == 0 and pre_result4 != 0:
    print("Число", raw_numbers, "парне але не ділится націло на 4")
else:
    print("Число", raw_numbers, "не парне і не ділится націло на 4")