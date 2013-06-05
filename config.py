#\m/ coding:utf8 \m/

import plugins

"""
this is the EeveeBot config place.
just change something there and...
enjoy!
"""


#SERVER: this is the IP (or the Internet address)
#of the IRC server your bot have to connect.
#example: SERVER="irc.freenode.net"
SERVER=""

#CHANNEL: this is the channel your bot
#will connect to on startup
#example: CHANNEL="#MaHBeautifulChanxDDDD"
CHANNEL=""

#BOTNAME: this is the name of your bot.
#everyone will call your bot with this name, so...
#don't be a dick and choose a good name for your lovely bot.
#example: BOTNAME="Giorgia"
BOTNAME = ""

#MASTERS: this list contains the names of IRC users
#that can call some _high privileges_ functions of your bot
#(e.g.: ban, quit, reload...)
#just be careful: don't trust anyone. oh, yeah... maybe yourself.
#and your IRC chan admin :P
#example: MASTERS=["alfateam123", "JustHvost"]
MASTERS = []

plugins=(
     plugins.explode_test,
     plugins.gtfo,
     plugins.log,
     )
