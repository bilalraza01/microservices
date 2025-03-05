import pika

# Define RabbitMQ connection credentials
credentials = pika.PlainCredentials('guest', 'Admin@123')

# Connect to RabbitMQ using its container name as the hostname
connection = pika.BlockingConnection(pika.ConnectionParameters(
    host='rabbitmq',  # Use 'rabbitmq' instead of 'localhost' inside Docker
    credentials=credentials
))


channel = connection.channel()

channel.queue_declare(queue='main')

def callback(ch, method, properties, body):
  print(body)

channel.basic_consume(queue='main', on_message_callback=callback)

print('Started Consuming')
channel.start_consuming()

channel.close()
