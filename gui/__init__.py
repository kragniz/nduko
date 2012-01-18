import sys

try:
    import gi
    from gi.repository import Gtk
except:
    import gtk as Gtk

class gui(object):
    def __init__( self ):
        gladeFile = "main.glade"
        builder = Gtk.Builder()
        builder.add_from_file(gladeFile)
        builder.connect_signals(self)

    def on_undoButton_clicked(self, widget):
    	self.undo()

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
