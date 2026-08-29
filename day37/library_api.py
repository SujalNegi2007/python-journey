import requests
from pathlib import Path
import json

def get_features(package_name):
    url = f'https://pypi.org/pypi/{package_name}/json'
    get_response = requests.get(url, timeout = 10)
    if get_response.status_code == 200:
        data = get_response.json()
        info = data['info']
        return {
            'Name' : info['name'],
            'Version' : info['version'],
            'Summary' : info['summary']
        }
    else:
        print(f"Error: {get_response.status_code}")

def create_user(name, job):
    url = 'https://reqres.in/api/users'
    response = requests.post(url, json = {
                'Name' : name,
                'Job' : job
            })
    
    if response.status_code not in [200, 201]:
        print(f'Error: {response.status_code}')
        return

    return response.json()

results = {
    "get_result" : get_features('numpy'),
    "post_result" : create_user('Sujal', 'MLOPS Enginner')
}

while True:
    answer = input('Do you want to save the file(Yes/No)?').upper().strip()
    if answer and answer[0] in ('Y', 'Yes'):
        with Path('combined.json').open('w', encoding = 'utf-8') as file:
            json.dump(results, file, indent = 2)
        print('File Saved')
        break
    else:
        print('File Not Saved.')
        break
