import pika, os, time

def word_process_function(msg):
  print(" WORD processing")
  print(" [x] Received " + str(msg))

  time.sleep(5) # delays for 5 seconds
  print(" WORD processing finished")
  return

params = pika.ConnectionParameters("localhost")
connection = pika.BlockingConnection(params)
channel = connection.channel() # start a channel
channel.queue_declare(queue='wordprocess') # Declare a queue


# create a function which is called on incoming messages
def callback(ch, method, properties, body):
  word_process_function(body)
  # sending acknowledge package when process are done, so the queue remove the current task
  # if the process is death when processing, acknowledge package wont be sent => ReQueue unfinished task
  ch.basic_ack(delivery_tag = method.delivery_tag)

# set up subscription on the queue
channel.basic_consume('wordprocess',
  callback)
#   auto_ack=True)

# start consuming (blocks)
channel.start_consuming()
connection.close()