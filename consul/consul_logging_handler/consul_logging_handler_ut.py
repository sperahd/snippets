import logging
import logging.config
import yaml

from consul_logging_handler import ConsulLoggingHandler
class Main:
    def __init__(self):
        logging.basicConfig(
            level=logging.INFO
            )
        self.logger = logging.getLogger('consul.client.logger')
        ch = ConsulLoggingHandler("127.0.0.1", "8500")
        ch.setLevel(logging.INFO)
        self.logger.addHandler(ch)
    def run(self):
        for i in range(20):
            log = f'abc/def/{i}:value_{i}'
            print(log)
            self.logger.info(log)

class Main2:
    def __init__(self):
        logging.handlers.ConsulLoggingHandler = ConsulLoggingHandler
        logger_cfg = (
            """
            version: 1
            handlers:
                consul:
                    class: logging.handlers.ConsulLoggingHandler
                    level: INFO
                    host: "127.0.0.1"
                    port: "8500"
            loggers:
                consul.put:
                    level: INFO
                    handlers: [consul]
            """
                )
        logging.config.dictConfig(yaml.load(logger_cfg))
        self.logger = logging.getLogger("consul.put.kv")
        # This logger should not push to consul since we have not 
        # defined the handler for it
        self.logger2 = logging.getLogger("consul.get")
    
    def run(self):
        for i in range(20):
            log = f'foo/boo/{i}:value_2_test_{i}'
            print(log)
            self.logger.info(log)
            log2 = f'not/exist/{i}:value_2_test_{i}'
            print(log2)
            self.logger2.info(log2)


if __name__ == "__main__":
    main = Main()
    main.run()

    main2 = Main2()
    main2.run()
