import paho.mqtt.client as mqtt
import CsvLoader
from time import sleep

# CLIENT_ID = '02WXO01'
CLIENT_ID = 'ID001'

# Test sample
# numbers = [100]  # normal
numbers = [106]  # many PVC

INDEX_LIMIT = 1000

def build_message(index, sample):
	next_index = 1 if index + 1 > INDEX_LIMIT else index + 1
	return next_index, str(index)+':'+str(sample)

if __name__ == '__main__':
	client = mqtt.Client(client_id=CLIENT_ID)
	client.connect("localhost", 1883, 60)
	for number in numbers:
		number = 'TA-Data/MIT_BIH/' + str(number)
		index = 0

		print(number)

		# raw = CsvLoader.load(number + '/record.csv')[:2935]  # 8 second		
		# raw = CsvLoader.load(number + '/record.csv')[:12000] # 1 minute
		raw = CsvLoader.load(number + '/record.csv')[9360:] # cut up
		# raw = CsvLoader.load(number + '/record.csv') # till end
		for data in raw:
			index, message = build_message(index, data)
			client.publish(CLIENT_ID+"/sensor", message)
			sleep(0.005)
