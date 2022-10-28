import requests, time
url = input("Your url ~> ")
headers = {
    'authority': 'shortlinkit.com',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'id,en;q=0.9,en-GB;q=0.8,en-US;q=0.7',
    # Already added when you pass json=
    # 'content-type': 'application/json',
    'origin': 'https://shortlinkit.com',
    'referer': 'https://shortlinkit.com/',
    'sec-ch-ua': '" Not;A Brand";v="99", "Microsoft Edge";v="103", "Chromium";v="103"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.66 Safari/537.36 Edg/103.0.1264.44',
    'x-csrftoken': 'null',
}

json_data = {
    'full_url': url,
}

response = requests.post('https://shortlinkit.com/api/v1/shortlinks-public/', headers=headers, json=json_data).text
check_short = "short_url"
check_stat = "admin_url"
if check_short and check_stat in response:
        short = response.split('"short_url":"')[1].split('"')[0]
        sts = response.split('"admin_url":"')[1].split('"')[0]
        print ("shorten url...")
        time.sleep(1)
        print (f"Shortlink: {short}\nStats from shortlink: {sts}")
else:
        print ("whoops, failed to load short_url and admin_url on response!")
