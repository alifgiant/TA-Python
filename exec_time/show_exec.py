import json

# base = 'sensor/'
base = 'server/'

def avg(arr):
	return sum(arr)/len(arr)

def output(list_arr):
	# TIME IN SERVER	
	getMS = lambda x: x/1000000  # time exec, ms
	return [getMS(x[1]) for x in list_arr[3:100]]

	# TIME IN SENSOR
	# getMS = lambda x: x/1000
	# return [getMS(x) for x in list_arr[1:]]

def main():
	delay1 = json.load(open(base+'data1.json'))	
	delay2 = json.load(open(base+'data2.json'))
	delay3 = json.load(open(base+'data3.json'))

	delay1 = output(delay1)	
	delay2 = output(delay2)
	delay3 = output(delay3)

	avg_delay1 = avg(delay1)
	avg_delay2 = avg(delay2)
	avg_delay3 = avg(delay3)

	print('avg', avg_delay1, avg_delay2, avg_delay3)

	print('total avg', avg([avg_delay1, avg_delay2, avg_delay3]))

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