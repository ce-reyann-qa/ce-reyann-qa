import configparser


def getConfig():
    config = configparser.ConfigParser()
    config.read('C:\\Users\\Reyann\\PycharmProjects\\BEAutomation\\utilities\\properties.ini')

    return config

def getPassword():
     return "dddsd"