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
#    
import socket 
import config
                  
#DO NOT CHANGE THESE FUCKING THINGS! FFS!
ircsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ircsock.connect((config.SERVER, 6667)) 
ircsock.send("USER "+ config.BOTNAME +" "+ config.BOTNAME +" "+ config.BOTNAME +" :lol\n") 
ircsock.send("NICK "+ config.BOTNAME +"\n") 

joinchan(config.CHANNEL) 

while 1: 
  ircmsg = ircsock.recv(2048)
  ircmsg = ircmsg.strip('\n\r')  

  
  for plugin in config.plugins:
      plugin(ircmsg, ircsock)
