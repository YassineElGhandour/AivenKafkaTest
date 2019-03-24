# AivenKafkaTest

Before running this project, make sure that python3, Kafka and zookeeper are installed, and follow these instructions:

1 - Open the first terminal and run these commands (for the zookeeper):
	$ cd /usr/local/kafka
	$ bin/zookeeper-server-start.sh config/zookeeper.properties

2 - Open the second terminal and run these commands (for Kafka) : 
	$ cd /usr/local/kafka
	$ bin/kafka-server-start.sh config/server.properties

3 - Open the third terminal and run these commands (to run the consumer) :
	$ source aivenEnv/bin/activate
	$ python3 consumer.py

4 - Open the last terminal and run these commands (to run the producer) :
	$ source aivenEnv/bin/activate
	$ python3 producer.py

This will get the project working.

I have installed the kafka-python and psycopg2 packages in the virtual environnement, but in case there are any error these commands
will install these packages for you :
	$ sudo apt install python3-pip 
	$ python3 -m pip install kafka-python
	$ python3 -m pip install psycop2
