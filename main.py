from bs4 import BeautifulSoup
import requests
import json
from linebot import LineBotApi
from linebot.models import TextSendMessage
from check_site import cosme_bs, kao_bs, m_donguri_bs, m_donguri_bs, k_donguri_bs, send_message
import os


if __name__ == "__main__":
    access_token = os.environ.get('ACCESS_TOKEN ')
    user_id = os.environ.get('LINE_ID ')
    send_message(access_token, user_id, "test")
