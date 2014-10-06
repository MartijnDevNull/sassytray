#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import gtk, gobject, os

TIMER = 2
DEBUG = False
LAST_STATUS = ""

class CPUTimer:
    def __init__(self, timeout):
        self.tray = gtk.StatusIcon()
        self.tray.set_from_stock(gtk.STOCK_ABOUT)
        gobject.timeout_add_seconds(timeout, self.timer_callback)
        self.timer_callback()

    def timer_callback(self):
        global LAST_STATUS
        cpu_temp = self.get_CPU_Heat()
        self.debug('update CPU: ' + cpu_temp)
        icon_name = self.get_icon_name(int(cpu_temp))
        self.tray.set_tooltip(('CPU: ' + cpu_temp))
        self.debug("Setting LAST_STATUS: " + LAST_STATUS + " to " + icon_name)
        if LAST_STATUS != icon_name:
            self.debug("LAST_STATUS does not match icon_name, setting new icon")
            self.tray.set_from_file("icons/" + icon_name + ".svg")
        LAST_STATUS = icon_name
        return True

    def get_CPU_Heat(self):
        return os.popen('sensors | grep "temp1:" | cut -d+ -f2 | cut -c1-2').read()

    def get_icon_name(self, heat):
        if heat < 30:
            return "1"
        if heat < 50:
            return "2"
        if heat < 55:
            return "3"
        if heat < 65:
            return "4"
        if heat < 70:
            return "5"
        else:
            return "didn't catogorize heat"

    def debug(self, mesg):
        if DEBUG == True:
            print mesg
if __name__ == '__main__':
    timer = CPUTimer(TIMER) 
    gtk.main()
