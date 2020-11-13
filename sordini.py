from kafka import KafkaProducer
import zlib
import os

try:
    defaultKafkaBroker = os.getenv("SORDINI_BROKER")
except:
    kErr("SORDINI_BROKER env variable not set - any calls without the broker specified will fail")
    defaultKafkaBroker = None

try:
    defaultKafkaTopic = os.getenv("SORDINI_TOPIC")
except:
    kErr("SORDINI_TOPIC env variable not set - any calls without the topic specified will fail")
    defaultKafkaBroker = None

def kErr(errMessage):
    print("KAFKAESQUE ERROR (you know there's an error, but you don't know who made it, why you're here, or what that strange castle is)") 
    print("  - ".join(errMessage))

def k