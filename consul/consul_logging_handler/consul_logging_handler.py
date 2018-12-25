from logging import StreamHandler
from consul_client import ConsulLoggerClient

class ConsulLoggingHandler(StreamHandler):

    def __init__(self, host = 'localhost', port = '8500'):
        StreamHandler.__init__(self)
        self.host = host
        self.port = port
        self.consul_logger = ConsulLoggerClient(host, port)
    
    #end __init__

    def emit(self, log):
        print(f'log received in emit function of consul_logging_handler: {log}')
        l = log.getMessage().split(':', 1)
        self.consul_logger.put_kv(l[0], l[1])
