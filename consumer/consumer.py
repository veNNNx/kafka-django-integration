import faust
import requests
app = faust.App('event_receiver',broker="kafka://kafka:9092")

class Event(faust.Record,validation=True):
    name: str
    source: str
    description: str

topic = app.topic("events",value_type=Event)

@app.agent(topic)
async def receiver(events):
    async for e in events:
        print(f"Data recieved is {e}")
        data = {'name': e.name, 'source': e.source, 'description': e.description}
        try:
            requests.post("http://django-api:8000/endpoint", data=data)
        except Exception as e:
            print('Error:', e)

if __name__ == '__main__':
    app.main()


# Kafka consumer

# to requirementas:
# kafka-python==1.4.7
# robinhood-aiokafka==1.1.6


# from kafka import KafkaConsumer
# import time
# import json
# def consume():
#     consumer = KafkaConsumer('events', bootstrap_servers='kafka:9092')
#     print('Created consumer\ntopic: events\nbootstrap_servers: kafka:9092')
#     while True:
#         for message in consumer:
#             event = json.loads(message.value)
#             print(event)
#             try:
#                 requests.post("http://django-api:8000/endpoint", data=event)
#                 print(f'[Consumer] Send event!\n{event}')
#             except Exception as e:
#                 print('Error:', e)

# if __name__ == "__main__":
#     while True:
#         try:
#             consume()
#         except Exception as e:
#             print('ERROR!!')