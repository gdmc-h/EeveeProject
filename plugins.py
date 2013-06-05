import utils
import re
import config
import sys

def explode_test(ircmsg, ircsock):
    try:
        print utils.GOD(ircmsg)
    except ValueError:
        print "invalid"

def gtfo(ircmsg, ircsock):
    try:
        if re.match("^!gtfo$", utils.content(ircmsg)):
	    if utils.sender(ircmsg) in config.MASTERS:
	        ircsock.send("QUIT see you later!\n")
		sys.exit(0) #it should quit itself, not just slack around.
	    else:
	        utils.sendmsg("gtfo to you, dipshit", utils.sender(ircmsg), ircsock)
    except ValueError:
        pass
