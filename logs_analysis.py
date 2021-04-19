str1 = '''time=2012 18:00:00 method=POST cost=200ms
time=2012 18:00:00 method=POST cost=300ms
time=2012 18:00:00 method=get cost=400ms
time=2012 18:00:00 method=get cost=400ms'''


def avr(str_in, method):
    lines = str_in.split('\n')
    num = 0
    sum_1 = 0
    for line in lines:
        if line.split(' ')[-2].split('=')[-1] == method:
            num += 1
            sum_1 += int(line.split(' ')[-1].split('=')[-1][:3])
    print(sum_1/num)


if __name__ == '__main__':
    avr(str1, 'POST')