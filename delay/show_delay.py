import json
from collections import Counter

def avg(arr):
	return sum(arr)/len(arr)

def output(list_arr):	
	# getMS = lambda x: (x/1000000)-5 if (x/1000000)-5 > 0 else 0
	getMS = lambda x: (x/1000000)
	return [getMS(x[1]) for x in list_arr]

def output_time(list_arr):	
	getMS = lambda x: (x/1000)
	return [getMS(x) for x in list_arr]

def main():	
	for x in range(1,11):
		data = json.load(open('data' + str(x) + '.json'))
		time = json.load(open('sensor/exec' + str(x) + '.json'))

		data = output(data)
		time = output_time(time)

		# print(len(data), len(time))

		times = [abs(server - sensor) for server, sensor in zip(data, time)]

		# every 10 seconds
		times = [times[x:x+2000] for x in list(range(len(times)))[::2000]]
		print('###### DELAY ' + str(x) + ' ######')	
		sub1 = []
		for idx, sub in enumerate(times):
			sub1.append(avg(sub))
			print(idx, avg(sub))
		print('avg', avg(sub1))
	
	# delay1 = json.load(open('data1.json'))	
	# delay2 = json.load(open('data2.json'))
	# delay3 = json.load(open('data3.json'))

	# delay1 = output(delay1)	
	# delay2 = output(delay2)
	# delay3 = output(delay3)

	# avg_delay1 = avg(delay1)
	# avg_delay2 = avg(delay2)
	# avg_delay3 = avg(delay3)

	# print('avg', avg_delay1, avg_delay2, avg_delay3)

	# print('total avg', avg([avg_delay1, avg_delay2, avg_delay3]))

	# print(delay1)

	# import matplotlib.pyplot as plt
	# fig, (ax_delay1, ax_delay2, ax_delay3) = plt.subplots(3, 1)
	# fig, (ax_delay1) = plt.subplots(1, 1)

	# ax_delay1.plot(times, 'blue')

	# ax_delay1.plot(data, 'red')
	# ax_delay1.plot(time, 'blue')
	# ax_delay1.plot(delay3, 'green')

	# ax_delay2.plot(delay2)
	# ax_delay3.plot(delay3)

	# plt.tight_layout()
	# plt.show()


if __name__ == '__main__':
	main()