import random
start = input('请输入范围下限： ')
start = int(start)
end = input('请输入范围上限： ')
end = int(end)
num = random.randint(start, end)
count = 0
while True:
	count += 1
	guess = input('请猜数字： ')
	guess = int(guess)
	if guess == num:
		print('厉害，猜中咯！您猜了', count, '次')
		break
	elif guess > num:
		print('太大了！已经猜了', count, '次')
	elif guess < num:
		print('太小了！已经猜了', count, '次')