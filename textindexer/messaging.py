from amqpstorm import Connection
import os


class DocsMessaging():

    def __init__(self, mq={}):
        mq_config = {
            'username': os.environ.get(
                'RABBITMQ_DEFAULT_USER',
                mq.get('username')),
            'password': os.environ.get(
                'RABBITMQ_DEFAULT_PASSWORD',
                mq.get('password')),
            'host': os.environ.get(
                'RABBITMQ_HOST',
                mq.get('host', 'mq'))}
        self._connection = Connection(
            mq_config.get('host'),
            mq_config.get('username'),
            mq_config.get('password'))

