import requests
import json

# for i in range(count):
#    print("商品名：", res_dict['hits'][i]['name'])
#    print("説明：", res_dict['hits'][i]['description'])
#    print("価格：", res_dict['hits'][i]['price'])
#    print("商品コード：", res_dict['hits'][i]['code'])
#    print("JANコード：", res_dict['hits'][i]['janCode'])
#    print("商品URL", res_dict['hits'][i]['url'])

def get_productName(client_id, jan_code):
    try:
        appid = client_id
        url = 'https://shopping.yahooapis.jp/ShoppingWebService/V3/itemSearch?appid={}&jan_code={}'.format(appid, jan_code)
        call = requests.get(url)
        res_dict = json.loads(call.content)
        count = len(res_dict['hits'])

        data_num = 9 # magic number

        if count:
            name_list = []
            for i in range(count):
                name_list.append(res_dict['hits'][i]['name'])
                if i == data_num:
                    break

            return name_list
        else:
            return None
        
    except Exception as e:
        print(e)
        return None