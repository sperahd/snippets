import logging
from consul_logging_handler import ConsulLoggingHandler
class Main:
    def __init__(self):
        logging.basicConfig(
            level=logging.INFO
            )
        print('here 0')
        self.logger = logging.getLogger('consul.client.logger')
        print('here 2')
        kh = ConsulLoggingHandler("127.0.0.1", "8500")
        kh.setLevel(logging.INFO)
        print('here 3')
        self.logger.addHandler(kh)
        print('here 4')
    def run(self):
        for i in range(20):
            log = f'abc/def/{i}:value_{i}'
            print(log)
            self.logger.info(log)
if __name__ == "__main__":
    main = Main()
    main.run()
