import discord

from interfaces import Actions

class BotActivityStatusAction(Actions):
    
    def __init__(self, client):
        super().__init__(client)

    def development(self):
        print('Bot Ready in Development')
        return self.client.change_presence(activity=discord.Game(name=f"開発環境での実行"))

    def test(self, ):
        print('Bot Ready in Test')
        return self.client.change_presence(activity=discord.Game(name=f"テスト環境での実行"))

    def production(self):
        print('Bot Ready')
        return self.client.change_presence(activity=discord.Game(name=f"がんばるます"))

class BotSendAction(Actions):

    def __init__(self, client,):
        super().__init__(client)

    def development(self, message):
        print('Development:{}'.format(message))
        return self.client.send('Development:{}'.format(message))

    def test(self, message):
        print('Test:{}'.format(message))
        return self.client.send('Test:{}'.format(message))

    def production(self, message):
        print(message)
        return self.client.send(message)