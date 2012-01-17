import sys

#we're only targeting gtk 2.31 at the moment.
try:  
    import pygtk  
    pygtk.require('2.0')
except:  
    pass
try:  
    import gtk  
    import gtk.glade  
except:  
    print('GTK 2.~ Not Availible')
    sys.exit(1)

class gui(object):
    def __init__( self ):
        gladeFile = "main.glade"
        builder = gtk.Builder()
        builder.add_from_file(gladeFile)
        builder.connect_signals(self)

    def undo(self, widget):
    	print 'undone'

    def on_window_destroy(self, widget):
    	self.quit()

    def on_quitButton_clicked(self, widget):
    	self.quit()

    def quit(self, errorCode=0):
    	print 'quitting with style'
    	sys.exit(errorCode)

if __name__ == '__main__':
	g = gui()
	gtk.main()