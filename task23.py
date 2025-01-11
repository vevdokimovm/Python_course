import requests

api_url = "http://numbersapi.com"

params = {
    'default': 'Boring',
    'json': 'true'
}

with open("dataset.txt", "r") as infile:
    numbers = infile.read().splitlines()
    
# print(numbers)

for number in numbers:
    url = f'{api_url}/{number}/math'
    res = requests.get(url, params=params)
    data = res.json()
#     print(data)
    if data['text'] == 'Boring':
        print('Boring')
    else:
        print('Interesting')