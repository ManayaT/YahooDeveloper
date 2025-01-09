import os
from dotenv import load_dotenv
from modules import barcode_to_jan as btj
from modules import jan_to_productName as ptp

def main():
    # テスト用の画像パス(スゴイダイズ)
    target_path = 'images/スゴイダイズ.png'
    jan_code = btj.get_janCode(target_path)

    print(type(jan_code))

    if jan_code is None:
        print("JANコードが取得できませんでした")
        return

    print("JANコード:" + jan_code)

    # .envファイルのパスを指定して読み込む
    load_dotenv('.env')
    # 環境変数を利用する
    CLIENT_ID = os.getenv('CLIENT_ID')

    product_name = ptp.get_productName(CLIENT_ID, jan_code)

    print(type(product_name))
    
    if product_name is None:
        print("商品名が取得できませんでした")
        return
    else:
        for product in product_name:
            print("商品名:" + product)

if __name__ == "__main__":
    main()