gen_sq_natural_nums_20 = (x**2 for x in range(1,(20+1)))

def gen_get_fibonacci(num):
    prev = 0
    curr = 1
    yield prev
    yield curr
    for i in range(2, num):
        yield curr + prev
        prev, curr = curr, curr+prev
#end gen_get_fibonacci

def normal_fibonacci(num):
    #l = [] or l = list()
    #Either of the below two is fine
    l = [0,1]
    #l.append(0)
    #l.append(1)
    for i in range(2, num):
        l.append(l[i-1] + l[i-2])
    
    return l

def recursion_fibonacci(num):
    if num == 0 or num == 1:
        return num
    return(recursion_fibonacci(num-1) + recursion_fibonacci(num-2))


def main():
    for element in gen_sq_natural_nums_20:
        print(element)
    for element in gen_get_fibonacci(5):
        print(element)
    print(normal_fibonacci(5))
    print(recursion_fibonacci(3))
if __name__ == '__main__':
    main()
