import requests

url = "https://www.fast2sms.com/dev/bulk"

querystring = {"authorization":"65G7JVdb9ylc4D1o8RqFTrISjOQnpwWBshNkxumvLKXfaZEt3iRr5Y1ahyWfwuLPNKC0zIOmUegHq6b9","sender_id":"FSTSMS","language":"english","route":"p","numbers":"8999235150,8790690049","message":"hellooo hms"}

headers = {
    'cache-control': "no-cache"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)