#!/usr/bin/env python
# -*- coding: utf-8 -*-
import memcache

s = memcache.Client(['127.0.0.1:11211'])
a = s.get('demo')
i = 1500
j = 0
while s.get('demo'):
    j += 1
    if i == j:
        j = 0
        print "El valor de 'demo' es: %s" % s.get('demo')

print u"La llave 'demo' no está presente en memcached"

