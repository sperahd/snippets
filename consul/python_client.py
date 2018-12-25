import requests
import traceback
import os

class ConsulClient:
    def __init__(self, address):
        self.address = address

    def put_kv(self, key, value):
        data = value
        try:
            response = requests.put(f'{self.address}/v1/kv/{key}', data=data)
            if str(response.text) == 'true':
                print(f'posted value: {data}, for key: {key}')
            else:
                print(f'could not post value: {data}, for key: {key}')
                
        except:
            traceback.print_exc()
            os._exit(-1)
    
    def get_kv(self, key):
        try:
            response = requests.get(f'{self.address}/v1/kv/{key}')
            print(f'{response.text}')
        except:
            traceback.print_exc()
            os._exit(-1)
    
    def delete_kv(self, key):
        try:
            response = requests.delete(f'{self.address}/v1/kv/{key}')
            print(f'{response.text}')
        except:
            traceback.print_exc()
            os._exit(-1)

if __name__ == "__main__":
    c = ConsulClient('http://127.0.0.1:8500/')
    c.put_kv('abc/def/ghi', 'aeiou')
    c.get_kv('abc/def/ghi')
