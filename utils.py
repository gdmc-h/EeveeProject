#lol coding:utf8 lol
import re
import config

"""
this module has all the CoolThings that
could be useful in the app.

just be careful if you modify this file.
it could fix something, but can break another point
of the bot.
y'know... from sources come great responsabilities.

"""
import config


PRIVMSG_TO_CHAN_REGEX=re.compile("^:(?P<username>\w+)!~(?P<hostname>\w+)@(?P<servername>[\w\.\-]+) PRIVMSG #(?P<channelname>[\w#]+) :(?P<content>.+)")
PRIVMSG_TO_USER_REGEX=re.compile("^:(?P<username>\w+)!~(?P<hostname>\w+)@(?P<servername>[\w\.\-]+) PRIVMSG (?P<receiver>\w+) :(?P<content>.+)")

def isPrivMsg(ircmsg):
    """
    isPrivMsg : str -> bool
    
    this function checks if a message is a private message.
    it does not a check about receiver (channel or user).

    in case the message is not a message at all, the function
    will raise a ValueError.
    """
    return bool(_explode(ircmsg)["receiver"])

def isPubMsg(ircmsg):
    """
    isPubMsg : str -> bool

    this function checks if a message is a public message.

    in case the message is not a message at all, the functio
    will raise a ValueError
    """
    return bool(_explode(ircmsg)["channelname"])

def _explode(ircmsg):
    """
    _explode : str -> dict

    INTERNALS. DON'T USE THIS, or the wrath of the killer lolis
    will track you down and they will kill you.

    it breaks the message down and builds a dict.
    keys: username, hostname, servername, channelname, receiver, content.
    it could be useful, but IT IS INTERNALS.
    JUST USE THE OTHER FUNCTIONS.

    if the string is not an IRC message at all,
    the function will raise a ValueError.
    """
    try:
        exploded=PRIVMSG_TO_CHAN_REGEX.findall(ircmsg)[0]
	data=dict(zip(
	            ("username", "hostname", "servername", "channelname", "content")
	            , exploded))
	data["receiver"]=None
	return data
    except IndexError: #if does not match, exploded=[]
        try:
	    exploded=PRIVMSG_TO_USER_REGEX.findall(ircmsg)[0]
	    data=dict(zip(
	              ("username", "hostname", "servername", "receiver", "content"), exploded))
            data["channelname"]=None
	    return data
	except IndexError:
	    raise ValueError("this is not an IRC Message")

GOD = _explode #just jokin'

def sender(ircmsg):
    """
    sender : str -> str

    this function just gives back the sender,
    as known as 'the one that says sh*t'.

    it the string is not an IRC message at all,
    the function will raise a ValueError.
    """
    return _explode(ircmsg)["username"]

def receiver(ircmsg):
    try:
        return _explode(ircmsg)["receiver"]
    except KeyError:
        return _explode(ircmsg)["channelname"]

def content(ircmsg):
    return _explode(ircmsg)["content"]

def reload():
    config=reload(config)

def sendmsg(msg, chan, ircsock):
    ircsock.send("PRIVMSG %s : %s\n"%(chan, msg) )

def kick(user, chan, reason):
    ircsock.send("KICK %s %s %s\r\n"%(chan, user, reason))
