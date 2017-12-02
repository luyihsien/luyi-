line_bot_api = LineBotApi(cATmbAcpoB00KmtKDLael+ZvC4bTkViA466VScHTS633cTxhsetR60+j02uSYsELgF5pDw+BAi+dg6S1gpCPb6xywTB/i2qvYPhguH8EB2dzDZm9so5irv/p1ztnyFzxw17v5uMqvhNdRb0n5vjZ1AdB04t89/1O/w1cDnyilFU=)
handler = WebhookHandler(f671d61040ef404441e326b427be892e)


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
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text))


if __name__ == "__main__":
    app.run()