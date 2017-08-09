import json

def avg(arr):
	return sum(arr)/len(arr)

def output(list_arr):
	# TIME IN SERVER	
	getMS = lambda x: x/1000000  # time exec, ms
	return [getMS(x[1]) for x in list_arr]

	# # TIME IN SENSOR
	# getMS = lambda x: x/1000
	# return [getMS(x) for x in list_arr]

def main_sensor(base):
	for x in range(1,11):		
		delay1 = json.load(open(base+'exec'+str(x)+'.json'))		
		delay1 = output(delay1)

		# every 10 seconds
		delay1 = [delay1[x:x+2000] for x in list(range(len(delay1)))[::2000]]
		
		print('###### DELAY ' + str(x) + ' ######')	
		sub1 = []
		for idx, sub in enumerate(delay1):
			sub1.append(avg(sub))
			print(idx, avg(sub))
		print('avg', avg(sub1))
	
def main_server(base):
	for x in range(1,11):		
		delay1 = json.load(open(base+'data'+str(x)+'.json'))		
		delay1 = output(delay1)

		# every 10 seconds
		delay1 = [delay1[x:x+2000] for x in list(range(len(delay1)))[::2000]]
		
		print('###### DELAY ' + str(x) + ' ######')	
		sub1 = []
		for idx, sub in enumerate(delay1):
			sub1.append(avg(sub))
			print(idx, avg(sub))
		print('avg', avg(sub1))


if __name__ == '__main__':
	# base = 'sensor/'
	base = 'server/'

	# main_sensor(base)
	main_server(base)