from bs4 import BeautifulSoup
import requests

# アットコスメの情報の更新を確認する


def cosme_bs(url, old_file):
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "html.parser")

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
        return True

# 花王のサイトの更新を確認する


def kao_bs(kurl, kold_file):
    res = requests.get(kurl)
    soup = BeautifulSoup(res.text, "html.parser")

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
        return True

# koseのサイトの更新を確認する


def kose_bs(surl, sold_file):
    res = requests.get(surl)
    soup = BeautifulSoup(res.text, "html.parser")

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
        return True

# どんぐり共和国の更新を通知


def donguri_bs(durl, dold_file):
    res = requests.get(durl)
    soup = BeautifulSoup(res.text, "html.parser")

    # 今回取り込んだ情報を取り出す
    new_elem = str(soup.select(".photo-box")[0])

    # 前回のデータを取り込む
    try:
        with open(dold_file) as f:
            old_elem = f.read()
    except:
        old_elem = ""

    if new_elem == old_elem:
        return False
    else:
        with open(dold_file, "w") as f:
            f.write(new_elem)
        return True


if __name__ == "__main__":
    url = "https://cosmeet.cosme.net/product/search/page/0/sad/0/srt/1/fw/%89%D4%89%A4"
    kurl = "https://www.kao.com/jp/products/newproducts/"
    # surl = "https://maison.kose.co.jp/site/goods/search.aspx?sort=rd&search=%E6%A4%9C%E7%B4%A2%E3%81%99%E3%82%8B&search_reservationnew=1"
    majo_url = "https://www.donguri-sora.com/products/list.php?category_id=252"
    buta_url = "https://www.donguri-sora.com/products/list.php?category_id=255"

    old_file = "old_elem.txt"
    kold_file = "k_old_elem.txt"
    # sold_file = "s_old_elem.txt"
    majo_file = "majo_old_elem.txt"
    buta_file = "buta_old_elem.txt"

    if cosme_bs(url, old_file) == True:
        print("アットコスメのWEBページが更新されました！")
        print(url)

    if kao_bs(kurl, kold_file) == True:
        print("花王のWEBページが更新されました！")
        print(kurl)

    # if kose_bs(surl, sold_file) == True:
    #     print("KOSEのWEBページが更新されました！")
    #     print(surl)

    if donguri_bs(majo_url, majo_file) == True:
        print("魔女の宅急便のWEBページが更新されました！")
        print(majo_url)

    if donguri_bs(buta_url, buta_file) == True:
        print("紅の豚のWEBページが更新されました！")
        print(buta_url)
