from slackbot.bot import respond_to

@respond_to(r'.+')
def all_respond_func(message):
    text = message.body['text']
    line_cnt = text.count('\n')
    msg = 'メッセージは\n```'+text+'```\n'
    msg += '文字数:'+str(len(text)-line_cnt)
    message.reply(msg)
