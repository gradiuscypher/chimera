import requests
import configparser
import time

config = configparser.RawConfigParser()
config.read("config.conf")

host = config.get('Config', 'host')
passwordHash = config.get('Config', 'passwordHash')
uid = config.get('Config', 'uid')

headers = {
    'Referer': 'app:/RagnarokClicker.swf',
    'User-Agent': 'Mozilla/5.0 (Android; U; en-US) AppleWebKit/533.19.4 (KHTML, like Gecko) AdobeAIR/24.0',
    'x-flash-version': '24,0,0,174'
}


def clans_raid(guild_name):
    timestamp = int(time.time())
    url = '/clans/getRaid.php'
    parameters = {
        'guildName': guild_name,
        'passwordHash': passwordHash,
        'uid': uid,
        'timestamp': str(timestamp)
    }

    r = requests.get(host+url, params=parameters)
    return r


def clans_titan_health(guild_name):
    timestamp = int(time.time())
    url = '/clans/getTitanHealth.php'
    parameters = {
        'guildName': guild_name,
        'passwordHash': passwordHash,
        'uid': uid,
        'timestamp': str(timestamp)
    }

    r = requests.get(host+url, params=parameters)
    return r


def guild_messages(guild_name):
    url = '/clans/getGuildMessages.php'

    parameters = {
        'guildName': guild_name,
        'passwordHash': passwordHash,
        'uid': uid,
    }

    r = requests.get(host+url, params=parameters)
    return r


def guild_info():
    url = '/clans/getGuildInfo.php'

    parameters = {
        'passwordHash': passwordHash,
        'uid': uid,
    }

    r = requests.get(host+url, params=parameters)
    return r


def clan_update_player(max_level):
    url = '/clans/updatePlayer.php'

    parameters = {
        'passwordHash': passwordHash,
        'uid': uid,
        'highestZone': max_level
    }

    r = requests.get(host+url, params=parameters)
    return r
