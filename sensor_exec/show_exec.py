import json
import CsvLoader

def avg(arr):
	return sum(arr)/len(arr)

def output(list_arr):
	# getMS = lambda x: (x/1000000)-5 if (x/1000000)-5 > 0 else 0
	getMS = lambda x: (x/1000)
	# return [getMS(x[1]) for x in list_arr[2:100]]
	return [getMS(x) for x in list_arr[2:]]

def main():
	out1 = CsvLoader.load_single('out1.txt')
	out2 = CsvLoader.load_single('out2.txt')
	out3 = CsvLoader.load_single('out3.txt')

	# print(out1)
	# print(out2)
	# print(out3)

	out1 = output(out1)	
	out2 = output(out2)
	out3 = output(out3)

	avg_out1 = avg(out1)
	avg_out2 = avg(out2)
	avg_out3 = avg(out3)

	# print(len(out1))

	print('avg', avg_out1, avg_out2, avg_out3)

	print('total avg', avg([avg_out1, avg_out2, avg_out3]))
	
	import matplotlib.pyplot as plt
	# fig, (ax_delay1, ax_delay2, ax_delay3) = plt.subplots(3, 1)
	fig, (ax_out) = plt.subplots(1, 1)

	ax_out.plot(out1, 'red')
	ax_out.plot(out2, 'blue')
	ax_out.plot(out3, 'green')
	# ax_delay2.plot(delay2)
	# ax_delay3.plot(delay3)

	plt.tight_layout()
	plt.show()


if __name__ == '__main__':
	main()