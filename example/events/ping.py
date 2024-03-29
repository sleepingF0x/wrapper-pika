from example.services.rabbit import rabbit


@rabbit.queue(routing_key='ping.*', dead_letter_exchange=True)
def ping_event(routing_key, body):
    print('Message received:')
    print('\tKey: {}'.format(routing_key))
    print('\tBody: {}'.format(body))

    if routing_key == 'ping.error':
        raise Exception('Generic Error')
