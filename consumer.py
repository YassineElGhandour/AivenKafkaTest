from kafka import KafkaConsumer
import psycopg2
import json

# Credentials of a Postgresql service offered by Aiven Postgresql.
DB_NAME = "defaultdb"
DB_USER = "avnadmin"
DB_PASSWORD = "ic3kr3bq4rnd562q"
DB_HOST = "pg-19d6c33f-yassine-6bec.aivencloud.com"
DB_PORT = "29421"

try:

	# Connection to Postgresqldatabase.
	conn = psycopg2.connect(	database= DB_NAME,
							user= DB_USER,
							password = DB_PASSWORD,
							host = DB_HOST,
							port = DB_PORT)

	print("\n ======================== CONNECTION TO DATABASE : SUCCESS. ========================\n")

	# Create cursor to run operations.
	cur = conn.cursor()

	# Creation of a table.
	table_creation_query = """CREATE TABLE IF NOT EXISTS EventNumbers(ID SERIAL PRIMARY KEY NOT NULL, DATANUMBER TEXT NOT NULL, PRODUCER TEXT NOT NULL)""" 
	cur.execute(table_creation_query)

	print("\nConsumer in action ...\n")
	
	# Consumer operates throught the topic : aiven_test_topic
	consumer = KafkaConsumer('aiven_test_topic',
							 bootstrap_servers="kafka-3f47692f-yassine-6bec.aivencloud.com:29423",
    						 client_id="aiven-test-client",
    						 group_id="aiven-test-group",
    						 # SSL Security measurements in consumer side
    						 security_protocol="SSL",
    						 ssl_cafile="SSL/ca.pem",
    						 ssl_certfile="SSL/service.cert",
    						 ssl_keyfile="SSL/service.key")
	
	for msg in consumer:
		# The type of msg type is ConsumerRecord, we want the value of this msg which exists
		# in the 6th index of a ConsumerRecord, therefore we'll use msg[6]
		data = json.loads(msg[6])
		# Insert the data in our table whithin the database.
		insert_data_query = """INSERT INTO EventNumbers (DATANUMBER, PRODUCER) VALUES (%s, %s)"""
		# the type of data is dict, to take the exact value of a number in each row, it should be written like : str(data["number"])
		record_to_insert = (str(data['number']), str(data['producer']))
		cur.execute(insert_data_query, record_to_insert)
		# We have to commit in each row, otherwise we won't be able to insert all of the data, the previous one will erase
		# the one afterwards, this won't create a problem for creating a table, since we mentionned in the early query
		# that we will only create a table IF NOT EXISTS.
		print(data)
		conn.commit()

	
except Exception as exp:
	# We raise expections in cases of error to treat problems in an easier way
	print("\nException : " + str(exp))