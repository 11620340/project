import pprint
import requests, json


# data = {
#     "username":"admin",
#     "password":"12334"
# }
# # data = json.dumps(data)
# response = requests.get('https://97a7ea5e244c4a1d801166104cef719e.apig.cn-east-3.huaweicloudapis.com/test', params=data)
#
#
# print(response.status_code)
# if response.text == 'yes':
#     print(response.text)
# else:
#     print(response.text)

import user
if "admin" in user.dirt_user:
    print(1)