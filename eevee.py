#!/usr/bin/env python

#    Copyright (C) 2013 JustHvost
#
#    Eevee is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    Eevee is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with Eevee.  If not, see <http://www.gnu.org/licenses/>.
# Import some necessary libraries.

import socket 
import re

       
server = "irc.freenode.net" 
channel = "#alfaqui" 
botnick = "EeveeBot"
MASTERS=[] #who can say EeveeBot !gtfo? Their names are written here. 

PRIVMSG_TO_CHAN_REGEX=re.compile("^:(?P<username>\w+)!~(?P<hostname>\w+)@(?P<servername>[\w\.\-]+) PRIVMSG #(?P<channelname>\w+) :(?P<content>.+)")

def ping():
  ircsock.send("PONG :pingis\n")  

def sendmsg(chan , msg): 
  ircsock.send("PRIVMSG "+ chan +" :"+ msg +"\n") 

def joinchan(chan): 
  ircsock.send("JOIN "+ chan +"\n")

def userFromPrivMsg(ircmsg):
  try:
    return PRIVMSG_TO_CHAN_REGEX.findall(ircmsg)[0][0] #that's the username
  except IndexError:
    return "" #TODO:we have to control also the PRIVMSG_TO_USER_REGEX

def fb():
  ircsock.send("PRIVMSG "+ channel +" :Follow us on facebook! <link here>\n")
def hi():
  ircsock.send("PRIVMSG "+ channel +" :hi!\n")
                  
ircsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ircsock.connect((server, 6667)) 
ircsock.send("USER "+ botnick +" "+ botnick +" "+ botnick +" :lol\n") 
ircsock.send("NICK "+ botnick +"\n") 

joinchan(channel) 

while 1: 
  ircmsg = ircsock.recv(2048)
  ircmsg = ircmsg.strip('\n\r') 
  print(ircmsg)
  #print userFromPrivMsg(ircmsg) #decomment while testing
  if ircmsg.find(":!fb ") != -1: 
    fb()
  if ircmsg.find(":ciao "+ botnick) !=-1: 
    hi()
  if ircmsg.find(":!gtfo") !=-1 and userFromPrivMsg(ircmsg) in MASTERS:
    ircsock.send("QUIT\n")
  if ircmsg.find("PING :") !=-1: 
    ping()
