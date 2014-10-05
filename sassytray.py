#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import gtk, gobject, os

class CPUTimer:
    def __init__(self, timeout):
        self.tray = gtk.StatusIcon()
        self.tray.set_tooltip(('Sample tray app'))
        self.tray.set_from_stock(gtk.STOCK_ABOUT)
        # register a  timer
        gobject.timeout_add_seconds(timeout, self.timer_callback)
        self.timer_callback()

    def timer_callback(self):
        cpu_temp = os.popen('sensors | grep "temp1:" | cut -d+ -f2 | cut -c1-2').read()
        print 'update CPU: ' + cpu_temp
        self.tray.set_tooltip(('CPU: ' + cpu_temp))
        return True

if __name__ == '__main__':
    timer = CPUTimer(2) # sets 1 second update interval
    gtk.main()
