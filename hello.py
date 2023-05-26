my_dict = {'apple': 5, 'banana': 3, 'orange': 2}


for values in list(my_dict.keys()):
    if values.endswith("e"):
        print(values)