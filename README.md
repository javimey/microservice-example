### Intro

 docker run -t -p 9557:9557 be:latest

#
# Common Configurations
#

[defaults]

wsgi-file = ./%X/service.py

callable = app

master = true

reload-mercy = 1

worker-reload-mercy = 1

;spooler = ./common/spoolers

;spooler-processes=1

http = :%(port)

processes = 3

;cheaper = 1

gevent = 100

thunder-lock = true

;uid = %(port)

;gid = %(port)

;master-fifo = ./common/fifos/%(port):%X:%(ver)

ini = :DBs

ini = :patterns

ini = :endpoint-profile

ini = :credentials

ini = :resources

ini = :logging

[madness/javi]

port = 9557

ini = :defaults
