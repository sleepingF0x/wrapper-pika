# RabbitMQ Pika Wrapper

RabbitMQs pika library adapter. It's developed with the goal to make it easier to integrate the recommended RabbitMQ library.

For now our attention is focused on the `topic` exchange type.

## Installing

Install and update using [pip](https://pip.pypa.io/en/stable/quickstart/):

```bash
    pip install wrapper-pika
```

Set the following environment variables or set them in your app dict config :

- MQ_EXCHANGE=Your exchange name
- MQ_URL=Your MQ URL following [this format](https://pika.readthedocs.io/en/stable/examples/using_urlparameters.html)
- MQ_EXCHANGE_TYPE=Your exchange type
- MQ_EXCHANGE_DURABLE=exchange is durable or not
- MQ_DELIMITER=default is `.`

## Basic Example

```python

  from w_pika import RabbitMQ
  import json

  rabbit = RabbitMQ()

  # send message
  @app.route('ping', methods=['GET'])
  def ping():
    rabbit.send(body='ping', routing_key='ping.message')
    return 'pong'

  # listen to messages
  @rabbit.queue(routing_key='ping.message')
  def ping_event(routing_key, body):
    app.logger.info('Message received:')
    app.logger.info('\tKey: {}'.format(routing_key))
    app.logger.info('\tBody: {}'.format(body))

  rabbit.init_app(queue_prefix="example", body_parser=json.loads, msg_parser=json.dumps)

```

Check examples in the `examples` folder

## Contributing

Still learning how to make a good open source project. Any ideas would be great.
But feel free to open an `issue` or `pull request` if you have any problems or ideas.

## Author

I would like to extend my heartfelt thanks to the author and contributors of the GitHub project for their phenomenal work, and for allowing me to make a small contribution.
https://github.com/trela-official/rabbitmq-pika-flask


## License

#### [MIT](https://opensource.org/licenses/mit-license.php)