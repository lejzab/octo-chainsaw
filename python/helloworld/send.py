#!/usr/bin/env python
import json
from datetime import datetime

import pika

credentials = pika.PlainCredentials('krolik', 'sdwan')
connection = pika.BlockingConnection(
    pika.ConnectionParameters('localhost',
                              5672,
                              '/',
                              credentials))
channel = connection.channel()

channel.queue_declare(queue='hello')

data = {'msg': 'witaj świecie',
        'data': datetime.now()}
payload = json.dumps(data, ensure_ascii=False, sort_keys=True, default=str)
channel.basic_publish(exchange='', routing_key='hello', body=payload)
print(f" [x] Sent {payload}")
connection.close()
