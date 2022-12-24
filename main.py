from bs4 import BeautifulSoup
import requests
import json
from linebot import LineBotApi
from linebot.models import TextSendMessage
from check_site import cosme_bs, kao_bs, m_donguri_bs, k_donguri_bs, send_line
import os


if __name__ == "__main__":
    # 環境変数の取り込み
    access_token = os.environ['ACCESS_TOKEN']
    user_id = os.environ['LINE_ID']

    # スクレイピングを実行
    # cosme = cosme_bs()
    kao = kao_bs()
    majo = m_donguri_bs()
    buta = k_donguri_bs()

    all_datas = [kao, majo, buta]

    for data in all_datas:
        if data != False:
            send_line(access_token, user_id, data)
        else:
            pass
