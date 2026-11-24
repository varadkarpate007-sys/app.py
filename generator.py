def fun(max):
    cnt = 1
    while cnt <= max:
        yield cnt
        cnt += 1

ctr = fun(5)

for n in ctr:
    print(n)
def PowTwoGen(max=0):
    n = 0
    while n < max:
        yield 2 ** n
        n += 1

max_power = int(input("Enter the number of powers of 2 to generate: "))

print("Powers of 2 are:")
for value in PowTwoGen(max_power):
    print(value)
def count_up_to(max_val):
    count = 1
    while count <= max_val:
        yield count
        count += 1


counter = count_up_to(5)

print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
