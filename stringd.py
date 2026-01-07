#*------------------------String and methods----------------------------*/
name = "Hello python programming"
print(name.upper())
print(name.lower())
print(name.capitalize())
print(name.title())
print(name.split())
ans = name.split()
print(len(name))
print(name.find('r'))
print(name.replace('h', 'k'))
print(name.count('p'))
print(ans)
myans = ' '.join(ans)
print(myans)

num = "123456"

print(int(num[0]) + int(num[5]))

# Slicing [start:end-1:steps] indexing -> list tuple string

numbers = "python"
# print(numbers[1:-4:1])
# print(numbers[-1:4:-1])
# print(numbers[-1::-1])
# print(numbers[1:4:-1])
# print(numbers[1:4:1])
# print(numbers[-1:-4:-1])
# print(numbers[-1:-4:1])
# print(numbers[-1:-5:-1])
# print(numbers[1:4:1])
# print(numbers[0:6:2])
# print(numbers[0:6:])
# print(numbers[:6:])
# print(numbers[::])
numbers = "python"
print(numbers[-1::-1])
print(numbers[::-1])
# print(numbers[0:-2:1])
numbers = "1235"
# numbers = numbers[-1] + numbers[1:-1:] + numbers[0]
print( int(numbers[0]) + int(numbers[-1]) )