import requests
import json
from pathlib import Path

def fetch_package_data(package_name):
    url = f'https://pypi.org/pypi/{package_name}/json'


    response = requests.get(url, timeout = 10)

    if response.status_code == 200:
        data = response.json()
        info = data['info']
        return {
            'Name' : info['name'],
            'Version' : info['version'],
            'Summary' : info['summary']
        }

    else:
        print(f"Error Detected: {response.status_code}")
        return None

results = []

for pkg in ['numpy', 'django']:
    result = fetch_package_data(pkg)
    if result:
        results.append(result)

print(results)

while True:
    answer = input('Want To Save This To Json File(Y/N)?').upper().strip()
    if answer and answer[0] in ['Y', 'N']:
        if answer[0] == 'Y':
            with Path('api_data.json').open('w', encoding = 'utf-8') as file:
                json.dump(results, file, indent = 2)
            print("File Saved.")
        else:
            print('File Not Saved')
        break
    else:
        print("Only Yes And No Are Available.")
