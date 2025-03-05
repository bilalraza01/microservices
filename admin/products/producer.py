import pika

# Define RabbitMQ connection credentials
credentials = pika.PlainCredentials('guest', 'Admin@123')

# Connect to RabbitMQ using its container name as the hostname
connection = pika.BlockingConnection(pika.ConnectionParameters(
    host='rabbitmq',  # Use 'rabbitmq' instead of 'localhost' inside Docker
    credentials=credentials
))
channel = connection.channel()

def publish():
  print('hi')
  channel.basic_publish(exchange='', routing_key='admin', body='Hello World')

def publish_to_main():
  channel.basic_publish(exchange='', routing_key='main', body='Sent to Main')
