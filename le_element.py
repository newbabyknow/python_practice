# le element

phone = {'a': [111, 222], 'b': [333, 444], 'c': [555, 666]}
case ={'a': ['cases1', 'cases2'], 'b': ['cases3', 'cases4'], 'c':['case5']}
list_key = phone.keys()
for every_key in list_key:
    for item in case.get(every_key):
        print(item,phone.get(every_key))