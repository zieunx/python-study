money = 2000
card = False

if money >= 3000 or card:
    print('택시를 타고 가라.')
elif money >= 2000:
    print('버스를 타라.')
else:
    print('걸어 가라.')

if 1 not in [1, 2, 3]:
    print('1이 없다.')
else:
    print('1이 있다.')


score = 50
if score >= 60:
    message = "success"
else:
    message = "failure"

# 조건부 표현식 (위의 if문과 동일.)
message = "success" if score >= 60 else "failure"
print('\n\n')

# while문으로 별 찍기
n = 1
while n <= 5:
    print('*' * n)
    n = n + 1

# for문으로 별 찍기
for i in range(5):
    print('*' * (i+1))

# for문으로 별 찍기 (오른쪽 정렬)
for i in range(5):
    print('{:>5}'.format('*' * (i+1)))

print('\n\n ======== \n\n ')

a = "Life is too short, You need Python"
print(a[2:4])

print('\n\n ======== \n\n ')

a = "Error is %d%%." % 98
b = "Error is %s%%." % 98

print(a + '\n' + b)

print('\n\n ======== \n\n ')

tu1 = (1, 2, 'a', 'b')
print(tu1 + (2,))
