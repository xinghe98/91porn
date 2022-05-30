import requests
headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.62 Safari/537.36'}
data = requests.get('https://91porn.com/v.php',headers=headers,verify=False)
print(data)