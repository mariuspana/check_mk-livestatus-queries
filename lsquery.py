#!/usr/bin/env python
import socket
import time

OMD_HOST = "127.0.0.1"
OMD_PORT = 6557

def lsquery(query):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((OMD_HOST, OMD_PORT))
    s.send(query)
    s.shutdown(socket.SHUT_WR)
    answer = ''
    while True:
        data = s.recv(1000000)
        answer += data
        if len(data) < 100000:
            break

    s.close()
    return answer

gg  = lsquery("GET hosts\nColumns: name address custom_variable_names custom_variable_values\nFilter: custom_variable_values = doit-company-0002\n")
#print type(gg)
rr = [ line.split(';') for line in gg.split('\n')[:-1] ]
#print type(rr)
for p in rr:
        print p
