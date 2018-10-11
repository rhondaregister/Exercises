'''
A function to determine the number of pairs in an array.
'''

number_of_socks = 9
sock_colorways = [10, 20, 20, 10, 10, 30, 50, 10, 20]


def countPairs(n, ar):
	pairs = []
	count = 0
	for i in ar:
		if i in pairs:
			pass
		else:
			pairs.append(i)
			num = ar.count(i)
			pair = int(num / 2)
			count += pair
	return count

x = countPairs(number_of_socks, sock_colorways)
print(x)