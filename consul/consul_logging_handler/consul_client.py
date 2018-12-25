import requests

class ConsulLoggerClient:
    def __init__(self, host = 'localhost', port = '8500'):
        self.address = f'http://{host}:{port}'

    def put_kv(self, key, value):
        data = value
        try:
            response = requests.put(f'{self.address}/v1/kv/test/{key}', data=data)
            if str(response.text) == 'true':
                print(f'posted value: {data}, for key: {key}')
            else:
                print(f'could not post value: {data}, for key: {key}')
                
        except Exception as e:
            raise
