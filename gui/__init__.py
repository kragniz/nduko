import sys

try:
    import gi
    from gi.repository import Gtk
except:
    import gtk as Gtk
    print 'falling back to gtk 2'

class gui(object):
    def __init__( self ):
        gladeFile = 'main.ui'
        builder = Gtk.Builder()
        builder.add_from_file(gladeFile)
        builder.connect_signals(self)

        #get some widgets in the local namespace
        self.aboutdialog = builder.get_object('aboutdialog')

    def on_undoButton_clicked(self, widget):
    	self.undo()

    def on_aboutMenuitem_activate(self, widget):
        self.aboutdialog.show()

    def on_quitmenuitem_activate(self, widget):
    	self.quit()

    def on_window_destroy(self, widget):
    	self.quit()

    def on_quitButton_clicked(self, widget):
    	self.quit()

    def undo(self):
    	print 'undone'

    def quit(self, errorCode=0):
    	print 'quitting with style'
    	sys.exit(errorCode)

if __name__ == '__main__':
	g = gui()
	Gtk.main()
