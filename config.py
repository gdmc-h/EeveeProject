#\m/ coding:utf8 \m/

import plugins

"""
this is the EeveeBot config place.

just change something there.
and don't forget to call !reload :D

"""


"""
"""
SERVER="irc.freenode.net"

CHANNEL="##datfreetalk"

BOTNAME = "Tsurugi"

MASTERS = ["alfateam123"]

def hi(ircmsg, ircsock):
    if "!hi" in ircmsg:
        return "hi!"

plugins=(hi, 
     plugins.explode_test,
     plugins.gtfo
     )

