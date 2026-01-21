import json
import requests

cookies = {
    '4254a0f0261d625588eb965162ce583c': '8e1bc17faa3ee0d162bb9078f591594e',
    '_ym_uid': '1768296969322503568',
    '_ym_d': '1768296969',
    '_ym_isad': '2',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:146.0) Gecko/20100101 Firefox/146.0',
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3',
    # 'Accept-Encoding': 'gzip, deflate, br, zstd',
    'DNT': '1',
    'Sec-GPC': '1',
    'Connection': 'keep-alive',
    'Referer': 'https://b2b.moysklad.ru/public/8Qrg0GNn9Toh/catalog?categoryId=b384fb32-9ecd-11f0-0a80-07040011e5f5',
    # 'Cookie': '4254a0f0261d625588eb965162ce583c=8e1bc17faa3ee0d162bb9078f591594e; _ym_uid=1768296969322503568; _ym_d=1768296969; _ym_isad=2',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    # Requests doesn't support trailers
    # 'TE': 'trailers',
}



with open("../handlers/keyboards/parsers/new_category2.json", "r", encoding="utf-8") as f:
    items = json.load(f)
    for item in items:
        response = requests.get(
            f'https://b2b.moysklad.ru/desktop-api/public/8Qrg0GNn9Toh/products.json?category_id={item["id"]}&limit=100&offset=0&search=',
            cookies=cookies,
            headers=headers,
        )

        with open(f"../bot/parsers/pods/{item["name"]}.json", "w") as file:
            json.dump(response.json(), file, indent=4, ensure_ascii=False)

        print("*** access successfully")

print(response.text)