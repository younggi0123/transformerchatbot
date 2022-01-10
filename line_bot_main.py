from flask import Flask, request, abort
 
from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)
 
app = Flask(__name__)

# 라인디벨롭 관리자의 발급받은 액세스 키와 토큰은 타인에게 노출되어서는 안되기에 파일을 하나 만들어서씀
import line_bot_config
line_bot_api = LineBotApi(line_bot_config.CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(line_bot_config.CHANNEL_SECRET)
 
@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']
 
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
 
    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)
 
    return 'OK'
 
 
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text))
 
 
import os
# if __name__ == "__main__":
#     app.run()

# main.py
if __name__ == "__main__":
    # app.run()
    # port = int(os.getenv("PORT"))
    # app.run(host="0.0.0.0", port=port)
    port = os.getenv("0.0.0.0")
    app.run(host="127.0.0.1", port=port)