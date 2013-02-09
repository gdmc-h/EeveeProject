#!/usr/bin/env python

#    Copyright (C) 2013 JustHvost & Alfateam123
#
#    EeveeProject is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    EeveeProject is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with EeveeProject.  If not, see <http://www.gnu.org/licenses/>.
# Import some necessary libraries.


import socket 
import re

       
server = "irc.freenode.net" #server name
chan = " " #channel name
bot = "EeveeProject" #bot name
MASTERS=[" "] #channel's op 


PRIVMSG_TO_CHAN_REGEX=re.compile("^:(?P<username>\w+)!~(?P<hostname>\w+)@(?P<servername>[\w\.\-]+) PRIVMSG #(?P<channelname>\w+) :(?P<content>.+)")
PRIVMSG_TO_USER_REGEX=re.compile("^:(?P<username>\w+)!~(?P<hostname>\w+)@(?P<servername>[\w\.\-]+) PRIVMSG (?P<receiver>\w+) :(?P<content>.+)")

def ping():
  ircsock.send("PONG :pingis\n")  

def sendmsg(chan , msg): 
  ircsock.send("PRIVMSG "+ chan +" :"+ msg +"\n") 
  
def kick(chan, user, why): #KICK <channel> <client> [<message>]
  ircsock.send("KICK "+ chan +" "+ user + " " + why + "\r\n")

def joinchan(chan): 
  ircsock.send("JOIN "+ chan +"\n")

def userFromPrivMsg(ircmsg):
  try:
    return PRIVMSG_TO_CHAN_REGEX.findall(ircmsg)[0][0] #that's the sender
  except IndexError:
    try:
      return PRIVMSG_TO_USER_REGEX.findall(ircmsg)[0][0] #that's the sender
    except IndexError:
      return "" #not a PRIVMSG message

def fb(): 
  sendmsg(chan, "Follow us on Facebook: <link here>\n")
def hi(): 
  sendmsg(chan, "Sup bro!?\n")
                  
#DO NOT CHANGE THESE FUCKING THINGS! FFS!
ircsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ircsock.connect((server, 6667)) 
ircsock.send("USER "+ bot +" "+ bot +" "+ bot +" :lol\n") 
ircsock.send("NICK "+ bot +"\n") 

joinchan(chan) 

while 1: 
  ircmsg = ircsock.recv(2048)
  ircmsg = ircmsg.strip('\n\r') 
  print(ircmsg)
  print userFromPrivMsg(ircmsg) 
  
  if ircmsg.find(":!fb ") != -1: 
    fb()

  if ircmsg.find(":ciao "+ bot) !=-1: 
    hi()

  if ircmsg.find(":!say") != -1:
    ss = ircmsg.split(":!say")
    ssc = ss[1].strip()
    sendmsg(chan ,str(ssc))

  if ircmsg.find(":!kick") != -1 and userFromPrivMsg(ircmsg) in MASTERS:
    kk = ircmsg.split(":!kick")
    kck = kk[1].strip()
    kick(chan, str(kck), "GTFO.")
    if str(kck) == bot:
      joinchan(chan)

  if ircmsg.find(":!gtfo") !=-1 and userFromPrivMsg(ircmsg) in MASTERS:
    ircsock.send("QUIT CYA!\n")

  if ircmsg.find("PING :") !=-1: 
    ping()
