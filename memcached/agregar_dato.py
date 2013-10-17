#!/usr/bin/env python
# -*- coding: utf-8 -*-
import memcache

s = memcache.Client(['127.0.0.1:11211'])
print "Conenctado a memcached"
s.set("demo", "memcached", 20)
print u"llave: demo\nvalor: memcached\nduración: 20 segundos"
