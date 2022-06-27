from azure.servicebus import ServiceBusClient
import os


CONN_STR = os.environ.get("SB_CONNECTION_STRING")
QUEUE_NAME = os.environ.get("SB_QUEUE_NAME")

servicebus_client = ServiceBusClient.from_connection_string(conn_str=CONN_STR, logging_enable=True)

with servicebus_client:
    print("Waiting on messages...")
    with servicebus_client.get_queue_receiver(queue_name=QUEUE_NAME) as receiver:
        msg = next(receiver)
        receiver.complete_message(msg)
        print(msg)