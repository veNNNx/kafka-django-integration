import time
import random
import json
from kafka import KafkaProducer

# {name: “User created”,
# uuid: 18d02d8c-8af1-4d55-b973-54cafc461bd4,
# source: “users”,
# created_at: “2021-10-18 10:33:35.472 +0200”,
# updated_at: null,
# description: “Dodano użytkownika”}

name = [f'name_{i}' for i in range(10)]
source = [f'source_{i}' for i in range(5)]
desc = [f'description_{i}' for i in range(20)]

def create_event():
    event={
        'name': random.choice(name),
        'source': random.choice(source),
        'description': random.choice(desc),
    }
    return event

def kafka_producer():
    producer = KafkaProducer(bootstrap_servers='kafka:9092',
                            value_serializer=lambda x: json.dumps(x).encode('utf-8'))

    while True:
        event = create_event()
        producer.send('events', value=event)
        print(f'[Producer] Send event: \n {event}')
        time.sleep(5)

if __name__ == "__main__":
    while True:
        try:
            kafka_producer()
        except Exception as e:
            print('ERROR!!')
        