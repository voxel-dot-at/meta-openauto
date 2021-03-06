#!/usr/bin/python

import sys
import dbus

bus = dbus.SystemBus()

if (len(sys.argv) < 2):
        print("Usage: %s [ Call Path ]" % (sys.argv[0]))
        sys.exit(1)

call = dbus.Interface(bus.get_object('org.ofono', sys.argv[1]),
                                                'org.ofono.VoiceCall')
call.Hangup()
