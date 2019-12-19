from bot import telegram_chatbot
import random

bot = telegram_chatbot("config.cfg")


def make_reply(msg,type):
    reply = None
    if(type == "private"):
        if(msg == "/toss"):
            reply = random.choice(["Head", "Tail"])
    elif(type == "group"):
        if(msg == "/toss@futubebet_bot"):
            reply = random.choice(["Head", "Tail"])
            
    cmd = "Msg= {} Reply = {}".format(msg, reply)
    print(cmd)
    return reply

update_id = None
while True:
    updates = bot.get_updates(offset=update_id)
    updates = updates["result"]
    if updates:
        for item in updates:
            update_id = item["update_id"]
            try:
                message = str(item["message"]["text"])
            except:
                message = None
                
            if(item["message"]["chat"]["type"] == "private"):
                from_ = item["message"]["from"]["id"]
                reply = make_reply(message, "private")
            elif(item["message"]["chat"]["type"] == "group"):
                from_ = item["message"]["chat"]["id"]
                reply = make_reply(message, "group")
                
            bot.send_message(reply, from_)