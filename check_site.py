from bs4 import BeautifulSoup
import requests
import json
from linebot import LineBotApi
from linebot.models import TextSendMessage
import os

# アットコスメの情報の更新を確認する


def cosme_bs():
    url = "https://cosmeet.cosme.net/product/search/page/0/sad/0/srt/1/fw/%89%D4%89%A4"
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "html.parser")
    old_file = "old_elem.txt"

    # 今回取り込んだ情報を取り出す
    new_elem = str(soup.select(".mdl-pdt-idv")
                   [0].select(".info")[0].get_text().split("クチコミ")[0].splitlines()[1])

    # 前回のデータを取り込む
    try:
        with open(old_file) as f:
            old_elem = f.read()
    except:
        old_elem = ""

    if new_elem == old_elem:
        return False
    else:
        with open(old_file, "w") as f:
            f.write(new_elem)
        return f"アットコスメの商品情報が更新されました！\n{url}"

# 花王のサイトの更新を確認する


def kao_bs():
    kurl = "https://www.kao.com/jp/products/newproducts/"
    res = requests.get(kurl)
    soup = BeautifulSoup(res.text, "html.parser")
    kold_file = "k_old_elem.txt"

    # 今回取り込んだ情報を取り出す
    new_elem = str(soup.select(".g-TileLinkVUnit__leadBlock")[0].get_text())

    # 前回のデータを取り込む
    try:
        with open(kold_file) as f:
            old_elem = f.read()
    except:
        old_elem = ""

    if new_elem == old_elem:
        return False
    else:
        with open(kold_file, "w") as f:
            f.write(new_elem)
        return f"花王の商品情報が更新されました！\n{kurl}"

# koseのサイトの更新を確認する


def kose_bs():
    surl = "https://maison.kose.co.jp/site/goods/search.aspx?sort=rd&search=%E6%A4%9C%E7%B4%A2%E3%81%99%E3%82%8B&search_reservationnew=1"
    res = requests.get(surl)
    soup = BeautifulSoup(res.text, "html.parser")
    sold_file = "s_old_elem.txt"

    # 今回取り込んだ情報を取り出す
    new_elem = str(soup.select(".c-product__product-name")
                   [0].get_text().strip())

    # 前回のデータを取り込む
    try:
        with open(sold_file) as f:
            old_elem = f.read()
    except:
        old_elem = ""

    if new_elem == old_elem:
        return False
    else:
        with open(sold_file, "w") as f:
            f.write(new_elem)
        return f"koseの商品情報が更新されました！\n{surl}"

# どんぐり共和国の更新を通知


def m_donguri_bs():
    majo_url = "https://www.donguri-sora.com/products/list.php?category_id=252"
    res = requests.get(majo_url)
    soup = BeautifulSoup(res.text, "html.parser")
    majo_file = "majo_old_elem.txt"

    # 今回取り込んだ情報を取り出す
    new_elem = str(soup.select(".photo-box")[0])

    # 前回のデータを取り込む
    try:
        with open(majo_file) as f:
            old_elem = f.read()
    except:
        old_elem = ""

    if new_elem == old_elem:
        return False
    else:
        with open(majo_file, "w") as f:
            f.write(new_elem)
        return f"魔女の宅急便の商品情報が更新されました！\n{majo_url}"


def k_donguri_bs():
    buta_url = "https://www.donguri-sora.com/products/list.php?category_id=255"
    res = requests.get(buta_url)
    soup = BeautifulSoup(res.text, "html.parser")
    buta_file = "buta_old_elem.txt"

    # 今回取り込んだ情報を取り出す
    new_elem = str(soup.select(".photo-box")[0])

    # 前回のデータを取り込む
    try:
        with open(buta_file) as f:
            old_elem = f.read()
    except:
        old_elem = ""

    if new_elem == old_elem:
        return False
    else:
        with open(buta_file, "w") as f:
            f.write(new_elem)
        return f"紅の豚の商品情報が更新されました！\n{buta_url}"


# メッセージを送る
def send_message(talk):
    # メッセージ送信用に変換
    message = TextSendMessage(text=talk)
    # jsonファイルを読み込む
    # file = open('info.json', 'r')
    # info = json.load(file)
    # secretsに登録した環境変数の呼び出し
    access_token = os.environ.get('ACCESS_TOKEN')
    user_id = os.environ.get('LINE_ID')
    # LINEbotにトークンを入力
    line_bot_api = LineBotApi(access_token)
    # LINEbotでメッセージを送る
    # line_bot_api.push_message(user_id, messages=message)
    # bot友達の全員に送信
    line_bot_api.broadcast(messages=message)


if __name__ == "__main__":
    print(m_donguri_bs())
