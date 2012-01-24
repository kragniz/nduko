#!/usr/bin/env python

try:
    import gi
    from gi.repository import Gtk
except:
    import gtk as Gtk
    print 'falling back to gtk 2'

class gui(object):
    def __init__( self ):
        gladeFile = 'testScaledPanableGridGtk2.ui'
        builder = Gtk.Builder()
        builder.add_from_file(gladeFile)

if __name__ == '__main__':
	g = gui()
	Gtk.main()
