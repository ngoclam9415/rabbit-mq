import pika, os, logging
import random
logging.basicConfig()

params = pika.ConnectionParameters("localhost")
params.socket_timeout = 5
connection = pika.BlockingConnection(params) # Connect to CloudAMQP
channel = connection.channel() # start a channel
channel.queue_declare(queue='pdfprocess') # Declare a queue
channel.queue_declare(queue='wordprocess') # Declare a queue
# send a message

# BINDING EXCHANGE TO QUEUE

if random.randint(0,1) == 0:
    print ("[x] PDF sent to consumer")
    channel.basic_publish(exchange='', routing_key='pdfprocess', body='PDF information')
else:
    print ("[x] WORD sent to consumer")
    channel.basic_publish(exchange='', routing_key='wordprocess', body='Word information')
connection.close()