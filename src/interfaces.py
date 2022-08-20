from abc import ABCMeta, abstractmethod
import os

class Actions(metaclass=ABCMeta):
    
    def __init__(self, client):
        self.client = client
        self.env = {
            'development': self.development,
            'test': self.test,
            'production': self.production,
        }

    @abstractmethod
    def development(self, ):
        raise NotImplementedError()

    @abstractmethod
    def test(self,):
        raise NotImplementedError()

    @abstractmethod
    def production(self, ):
        raise NotImplementedError()

    def exec(self, ):
        return self.env[os.environ['ENVIRONMENT']]


class Config(metaclass=ABCMeta):

    def __init__(self, env):
        self.env = env
        self.bot_token = os.environ['BOT_TOKEN']

    def get_token(self, ):
        return self.bot_token