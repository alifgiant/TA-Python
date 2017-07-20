import json

def avg(arr):
	return sum(arr)/len(arr)

def output(list_arr):
	# getMS = lambda x: (x/1000000)-5 if (x/1000000)-5 > 0 else 0
	getMS = lambda x: (x/1000000)
	# return [getMS(x[1]) for x in list_arr[2:100]]
	return [getMS(x[1]) for x in list_arr[2:]]

def main():
	delay1 = json.load(open('delay1.json'))	
	delay2 = json.load(open('delay2.json'))
	delay3 = json.load(open('delay3.json'))

	delay1 = output(delay1)	
	delay2 = output(delay2)
	delay3 = output(delay3)

	# avg_delay1 = avg(delay1)
	# avg_delay2 = avg(delay2)
	# avg_delay3 = avg(delay3)

	# print('avg', avg_delay1, avg_delay2, avg_delay3)

	# print('total avg', avg([avg_delay1, avg_delay2, avg_delay3]))

	# print(delay1)
	import matplotlib.pyplot as plt
	# fig, (ax_delay1, ax_delay2, ax_delay3) = plt.subplots(3, 1)
	fig, (ax_delay1) = plt.subplots(1, 1)

	ax_delay1.plot(delay1, 'red')
	ax_delay1.plot(delay2, 'blue')
	ax_delay1.plot(delay3, 'green')
	# ax_delay2.plot(delay2)
	# ax_delay3.plot(delay3)

	plt.tight_layout()
	plt.show()


if __name__ == '__main__':
	main()