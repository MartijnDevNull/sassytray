#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import gtk, gobject, os

TIMER = 2
DEBUG = True

class CPUTimer:
    def __init__(self, timeout):
        self.tray = gtk.StatusIcon()
        self.tray.set_from_stock(gtk.STOCK_ABOUT)
        # register a  timer
        gobject.timeout_add_seconds(timeout, self.timer_callback)
        self.timer_callback()

    def timer_callback(self):
        cpu_temp = self.get_CPU_Heat()
        self.debug('update CPU: ' + cpu_temp)
        icon_name = self.get_icon_name(int(cpu_temp))
        self.tray.set_tooltip(('CPU: ' + cpu_temp))
        self.tray.set_from_file("icons/" + icon_name + ".svg")
        return True

    def get_CPU_Heat(self):
        return os.popen('sensors | grep "temp1:" | cut -d+ -f2 | cut -c1-2').read()

    def get_icon_name(self, heat):
        if heat < 30:
            return "cold_cpu"
        if heat < 50:
            return "med_cpu"
        if heat < 55:
            return "hot_cpu"
        if heat < 65:
            return "flame_cpu"
        else:
            return "didn't catogorize heat"

    def debug(self, mesg):
        if DEBUG is True:
            print mesg
if __name__ == '__main__':
    # The update interval for CPUTimer
    timer = CPUTimer(TIMER) 
    gtk.main()
