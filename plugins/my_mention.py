#from slackbot.bot import respond_to
#from slackbot.bot import listen_to
from slackbot.bot import default_reply

@default_reply()
def default_func(message):
    text = message.body['text']
    msg = 'メッセージは\n```'+text+'```\n'
    msg += '文字数:'+str(len(text))
    message.reply(msg)
