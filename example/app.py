import json
import threading

from dotenv import load_dotenv

from example.services.rabbit import rabbit

load_dotenv()

if __name__ == '__main__':
    rabbit.init_app(queue_prefix="example", body_parser=json.loads, msg_parser=json.dumps)
    threading.Event().wait()
