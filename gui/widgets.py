import gtk

class Grid(gtk.DrawingArea):
    def __init__(self):
        gtk.DrawingArea.__init__(self)
        self.connect('expose_event', self.expose)

    def expose(self, widget, event):
        return False

if __name__ == '__main__':
    window = gtk.Window()
    grid = Grid()
    
    window.add(grid)
    window.connect('destroy', gtk.main_quit)
    window.show_all()
    
    gtk.main()