import pika, os, time

def pdf_process_function(msg):
  print(" PDF processing")
  print(" [x] Received " + str(msg))

  time.sleep(5) # delays for 5 seconds
  print(" PDF processing finished")
  return


#
params = pika.ConnectionParameters("localhost")
connection = pika.BlockingConnection(params)
channel = connection.channel() # start a channel
channel.queue_declare(queue='pdfprocess') # Declare a queue

# create a function which is called on incoming messages
def callback(ch, method, properties, body):
  pdf_process_function(body)
  ch.basic_ack(delivery_tag = method.delivery_tag)

# set up subscription on the queue
channel.basic_consume('pdfprocess',
  callback)
  # auto_ack=True)

# start consuming (blocks)
channel.start_consuming()
connection.close()