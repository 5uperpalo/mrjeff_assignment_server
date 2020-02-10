import pandas as pd
import requests

url = 'https://my-json-server.typicode.com/5uperpalo/mrjeff_assignment_server'
Linearl = pd.read_pickle('Linearl.pkl')

post_data = requests.post(url, data = Linearl.to_json())
url_test = requests.get(url).status_code

#print the response text (the content of the requested file):
if post_data == 200:
    print('0')
else:
    print('1')

if url_test == 200:
    print('API URL is healthy')
else: 
    print('API URL is not healthy!!!')
