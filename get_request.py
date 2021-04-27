# requests模块发送get请求，并将返回结果转换成json格式


import requests
import time


time_stamp = int(time.time())
url = 'https://mxshorts.dev.mxplay.com/v2/config?cur_time='+str(time_stamp)
print(url)
# dict_para = {'cur_time': str(time_stamp)}
headers_dict = {'method':	'GET',
                'path':	'/v2/config?cur_time=1619514001784',
                'authority':	'mxshorts.dev.mxplay.com',
                'scheme':	'https',
                'x-os-version':	'23',
                'x-brand':	'Xiaomi',
                'x-wid':	'4bd6208273beddf81ed35a38dc2b61e2394ce6a73339bae2d60857b79b631055',
                'x-locale':	'zh-CN',
                'x-cpu-count':	'10',
                'x-nonce':	'D30B4FDDCA9505BE7DEA58FB68383906',
                'x-guard-value': '33lXKQGzGgxJAUBc0gHcWzCsY7c=',
                'x-resolution':	'1080x1920',
                'x-env-type': '0',
                'x-density': '3.0',
                'x-timestamp':	'1619514001786',
                'x-time-server':	'0',
                'x-mcc':	'0',
                'x-platform':	'1',
                'x-timezone':	'Asia/Shanghai',
                'x-total-memory':	'3908960256',
                'x-device-id':	'73e3ab4774fe2172',
                'x-guard-version':	'1',
                'x-guard-key-version':	'1',
                'x-userid':	'9496780b-4db7-49d3-8f80-8e516aced273589444131',
                'x-app-version': '11309',
                'x-model': 'Redmi Note 4',
                'x-guard-key':'LD1cWqTThYIuRG2t/EiiyfcDaqbnkS1Vvu+DmJmXBfiBQZl7ig+4gjMQrnVsMSLJXc5nxMl9LPHkP8+erylgMR6Q5aKBI06Z0WWzQA8/qVykCXnZ314HqlePje5XCwPOH7WTv+UR77BNkSnz1WNCFrkRMHYg3uF0pg/y561Jui4=',
                'accept-encoding':'gzip',
                'user-agent':	'okhttp/3.12.11'}
r = requests.get(url, headers = headers_dict)
print(r.status_code)
result_json = r.json()
print(result_json)