from time import sleep
from json import dumps
from kafka import KafkaProducer

print("\nProducer in action ..\n")

# Creating a profucer
producer = KafkaProducer(#bootstrap_servers=['localhost:9092'],
						 bootstrap_servers=['kafka-3f47692f-yassine-6bec.aivencloud.com:29423'],
						 # SSL Security measurements in producer side
						 security_protocol="SSL",
    					 ssl_cafile="SSL/ca.pem",
    					 ssl_certfile="SSL/service.cert",
    					 ssl_keyfile="SSL/service.key",
                         value_serializer=lambda x: 
                         dumps(x).encode('utf-8'))

for e in range(20):
    data = {
    		'number' : e,
    		'producer': 'Producer : ' + str(e)
    	}
    # producer publishes data in the topic : aiven_test_topic
    producer.send('aiven_test_topic', value=data)
    # 1 sec delay between each operation to avoid collisions. 
    sleep(1)

producer.flush()