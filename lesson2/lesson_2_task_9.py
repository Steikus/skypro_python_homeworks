var_1 = 37
var_2 = 99

# var_1, var_2 = var_2, var_1

# print("var_1 = ", var_1)
# print("var_2 = ", var_2)


def swap():
    return var_2, var_1


var_1, var_2 = swap()

print("var_1 = ", var_1)
print("var_2 = ", var_2)
