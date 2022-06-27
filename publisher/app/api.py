import logging
from fastapi import FastAPI
import json
import os
from azure.servicebus import ServiceBusClient, ServiceBusMessage
from datetime import datetime

app = FastAPI()


@app.post("/publish")
async def publish_endpoint(item: dict):
    logging.info(f"Publishing the message {item}")

    CONN_STR = os.environ.get("SB_CONNECTION_STRING")
    QUEUE_NAME = os.environ.get("SB_QUEUE_NAME")

    servicebus_client = ServiceBusClient.from_connection_string(conn_str=CONN_STR, logging_enable=True)

    start = datetime.now()
    with servicebus_client:
        with servicebus_client.get_queue_sender(queue_name=QUEUE_NAME) as sender:
            sender.send_messages(ServiceBusMessage(json.dumps(item)))

    end = datetime.now()
    print(f"time={(end-start).total_seconds()}")

    return item