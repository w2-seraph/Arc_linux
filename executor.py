import requests
import re
import json
import itertools
import threading
from concurrent import futures


proxies = {
  'http': 'http://p.webshare.io:19999',
  'https': 'http://p.webshare.io:19999'
}

url = "http://www.tokyochronos.net/cute/submit"


payload = "------WebKitFormBoundaryu8Fo7fCN2j8kJ2FD\r\nContent-Disposition: form-data; name=\"reply_numero\"\r\n\r\n2176\r\n------WebKitFormBoundaryu8Fo7fCN2j8kJ2FD\r\nContent-Disposition: form-data; name=\"reply_bokunonome\"\r\n\r\nBIG CHUNGUS\r\n------WebKitFormBoundaryu8Fo7fCN2j8kJ2FD\r\nContent-Disposition: form-data; name=\"reply_elitterae\"\r\n\r\n\r\n------WebKitFormBoundaryu8Fo7fCN2j8kJ2FD\r\nContent-Disposition: form-data; name=\"reply_talkingde\"\r\n\r\n\r\n------WebKitFormBoundaryu8Fo7fCN2j8kJ2FD\r\nContent-Disposition: form-data; name=\"reply_chennodiscursus\"\r\n\r\nI wanne POG!!!!\r\n------WebKitFormBoundaryu8Fo7fCN2j8kJ2FD\r\nContent-Disposition: form-data; name=\"reply_nymphassword\"\r\n\r\nNR1t7HP\r\n------WebKitFormBoundaryu8Fo7fCN2j8kJ2FD\r\nContent-Disposition: form-data; name=\"reply_postas\"\r\n\r\nN\r\n------WebKitFormBoundaryu8Fo7fCN2j8kJ2FD\r\nContent-Disposition: form-data; name=\"reply_gattai\"\r\n\r\ntrue\r\n------WebKitFormBoundaryu8Fo7fCN2j8kJ2FD\r\nContent-Disposition: form-data; name=\"reply_last_limit\"\r\n\r\nnull\r\n------WebKitFormBoundaryu8Fo7fCN2j8kJ2FD\r\nContent-Disposition: form-data; name=\"latest_doc_id\"\r\n\r\n21\r\n------WebKitFormBoundaryu8Fo7fCN2j8kJ2FD\r\nContent-Disposition: form-data; name=\"theme\"\r\n\r\nfoolz/foolfuuka-theme-foolfuuka\r\n------WebKitFormBoundaryu8Fo7fCN2j8kJ2FD\r\nContent-Disposition: form-data; name=\"csrf_token\"\r\n\r\n5f2b14c373ef69.44597252\r\n------WebKitFormBoundaryu8Fo7fCN2j8kJ2FD\r\nContent-Disposition: form-data; name=\"file_image\"\r\n\r\nundefined\r\n------WebKitFormBoundaryu8Fo7fCN2j8kJ2FD--\r\n"

headers = {
  'accept': 'application/json, text/javascript, */*; q=0.01',
  'accept-encoding': 'gzip, deflate',
  'accept-language': 'en-US,en;q=0.9',
  'content-length': '1450',
  'content-type': 'multipart/form-data; boundary=----WebKitFormBoundaryu8Fo7fCN2j8kJ2FD',
  'cookie': 'foolframe_8ix_rememberme=a%3A3%3A%7Bs%3A7%3A%22user_id%22%3Bs%3A1%3A%221%22%3Bs%3A8%3A%22login_id%22%3Bs%3A40%3A%22009e8571ae6568174b194a4564830b711f0a671e%22%3Bs%3A10%3A%22login_hash%22%3Bs%3A40%3A%220075d3958284202f90f7e3b1377028981cad192f%22%3B%7D; foolframe_8ix_reply_password=NR1t7HP; foolframe_8ix_reply_name=BIG+CHUNGUS; foolframe_8ix_csrf_token=5f2b14c373ef69.44597252; foolframe_8ix_reply_name=BIG+CHUNGUS; foolframe_8ix_reply_password=NR1t7HP; foolframe_8ix_csrf_token=5f2b151c1e25d8.93348588',
  'host': 'www.tokyochronos.net',
  'origin': 'http://www.tokyochronos.net',
  'proxy-connection': 'keep-alive',
  'referer': 'http://www.tokyochronos.net/cute/thread/226/',
  'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36',
  'x-requested-with': 'XMLHttpRequest'
}



#res = requests.request("POST", url, headers=headers, data = payload, proxies=proxies)


with futures.ThreadPoolExecutor(max_workers=48) as executor:
    futures = [
        executor.submit(
            lambda: requests.request("POST", url, headers=headers, data = payload, proxies=proxies))
        for _ in range(256)
    ]

results = [
    f.result().status_code
    for f in futures
]

print("Results: %s" % results)
