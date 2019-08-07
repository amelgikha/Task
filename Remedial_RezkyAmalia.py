# SOAL 1
def find_sort(s):
    kata = s.split()
    a = []
    for loop in kata:
        a.append(len(loop))
    a.sort()
    return print(panjang[0])
find_sort("many people get up early in the morning")
find_sort("every office would getting newest monitor")
find_sort("create new file after this morning")



# SOAL 2
def presistance(x):
    total_global = x
    step = 0
    while (total_global>=10):
        z = total_global
        y = str(z)
        total = 1

        for item in range (len(y)):
            total *= int (y[item])
        step += 1
        total_global = total
    return print(step)
presistance(39)
presistance(999)
presistance(4)


# SOAL 3
def multiplication_table(row,col):
    a=[1,2,3]
    z=''
    for item in range(row):
        for item1 in range(col):
            if item1 > item:
                z+='{}'.format(a[item1]*(item+1))
            else:
                z+='{}'.format(a[item]*(item1+1))
        z+='\n'
    print(z)
multiplication_table(5,3)
multiplication_table(3,3)
multiplication_table(3,5)


# SOAL NO 4
def alphabet_position(huruf):
    dict = {'a':'1','b':'2','c':'3','d':'4','e':'5','f':'6','g':'7','h':'8',
    'i':'9','j':'10','k':'11','l':'12','m':'13','n':'14','o':'15','p':'16','q':'17',
    'r':'18','s':'19','t':'20','u':'21','v':'22','w':'23','x':'24','y':'25','z':'26'
    }
    lists = []
    kata = huruf.lower()
    for item in list(kata):
        for idx, val in dict.items():
            if idx == item:
                lists.append(val)
    return ' '.join(lists)
print(alphabet_position("The sunset sets at twelveo'clock"))
print(alphabet_position("It's never too late to try"))
print(alphabet_position("Have you done your homework"))


# SOAL BONUS
def is_prime(nomor):
    if nomor == 1:
        prime = False
    elif nomor == 2:
        prime = True
    elif nomor < 1:
        prime = False    
    else:
        prime = True
        for check_number in range(2, int(nomor/2)+1):
            if nomor % check_number == 0:
                prime = False
                break
    print(prime)
is_prime(1)
is_prime(2)
is_prime(-1)
is_prime(5099)