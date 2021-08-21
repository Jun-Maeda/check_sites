from bs4 import BeautifulSoup
import requests
import json
from linebot import LineBotApi
from linebot.models import TextSendMessage
from check_site import cosme_bs, kao_bs, m_donguri_bs, m_donguri_bs, k_donguri_bs, send_line
import os


if __name__ == "__main__":
    access_token = os.environ['ACCESS_TOKEN']
    user_id = os.environ['LINE_ID']
    # LINEを送る
    # send_line(str(access_token), str(user_id), "test")
    print(access_token)
