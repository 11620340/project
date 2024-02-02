dirt_user = {
    "admin":"666",
    "hgw":"123"
}

data = {
    "name":"admin",
    "paswd":"666"
}

if data.get('name') in dirt_user:
    if data.get('paswd') == dirt_user.get(data.get('name')):
        print(1)
else:
    print('没有这个用户')