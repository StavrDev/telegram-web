import config as c
from utils import TgBot

bot = TgBot(c.TOKEN_BOT)

if __name__ == '__main__':
    bot.start()
