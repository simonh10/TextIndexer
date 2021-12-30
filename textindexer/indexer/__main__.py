from .post_processor import PostProcessor
import os

def main():
    pp = PostProcessor(
        mongo={
            'username':os.environ.get('MONGO_INITDB_ROOT_USERNAME',''),
            'password':os.environ.get('MONGO_INITDB_ROOT_PASSWORD',''),
            'host': 'mongo'
        },
        mq={
            'username':os.environ.get('RABBITMQ_DEFAULT_USER','guest'),
            'password':os.environ.get('RABBITMQ_DEFAULT_PASS','guest'),
            'host': 'mq'
        }
    )
    pp.test()

if __name__ == '__main__':
    main()
