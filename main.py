#! /usr/bin/python3
# -*- coding: utf-8 -*-
#  ██████╗ ██████╗ ██████╗ ███████╗███╗   ███╗ █████╗ ███╗   ██╗
# ██╔════╝██╔═══██╗██╔══██╗██╔════╝████╗ ████║██╔══██╗████╗  ██║
# ██║     ██║   ██║██║  ██║█████╗  ██╔████╔██║███████║██╔██╗ ██║
# ██║     ██║   ██║██║  ██║██╔══╝  ██║╚██╔╝██║██╔══██║██║╚██╗██║
# ╚██████╗╚██████╔╝██████╔╝███████╗██║ ╚═╝ ██║██║  ██║██║ ╚████║
#  ╚═════╝ ╚═════╝ ╚═════╝ ╚══════╝╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝
#
# Version 1.0.0
# @tavo962
# README: 

import redis

# Variables
data = []

r = redis.StrictRedis(
	host = "localhost",
	port = 6379, 
	db = 0
)

for key in r.scan_iter():
	data.append( {
		"key": key,
		"value": r.get( key ),
	} )

print( data )

# r.set( "test", "Gus" )
# value = r.get( "test" )
# print( value )