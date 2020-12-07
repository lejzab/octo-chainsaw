#!/usr/bin/env python
import pika
import sys


def main():
    credentials = pika.PlainCredentials('krolik', 'sdwan')
    connection = pika.BlockingConnection(
        pika.ConnectionParameters('localhost',
                                  5672,
                                  '/',
                                  credentials))
    channel = connection.channel()

    channel.queue_declare(queue='hello')

    def callback(ch, method, properties, body):
        b = body.decode()
        print(" [x] Received %r" % b)

    channel.basic_consume(queue='hello', on_message_callback=callback, auto_ack=True)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        sys.exit(0)
