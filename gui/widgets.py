import math

try:
    import gi
    from gi.repository import Gtk
except:
	#make gtk2 look like gtk3
    import gtk as Gtk

class Grid(Gtk.DrawingArea):
    def __init__(self):
        Gtk.DrawingArea.__init__(self)
        self.set_size_request(300, 300)
        self.connect('expose_event', self.expose)
        self.drawable = self.window

    def expose(self, widget, event):
    	self.context = widget.window.cairo_create()

        # speed up by setting a clip region for the expose event
        self.context.rectangle(event.area.x, event.area.y,
                               event.area.width, event.area.height)
        self.context.clip()
        self.draw(self.context)
        return False

    def draw(self, context):
        rect = self.get_allocation()
        print rect.x, rect.y, rect.width, rect.height

        x = rect.x + rect.width / 2
        y = rect.y + rect.height / 2

        radius = min(rect.width / 2, rect.height / 2) - 5
        context.arc(x, y, radius, 0, 2 * math.pi)
        context.set_source_rgb(1, 1, 1)
        context.fill_preserve()
        context.set_source_rgb(0, 0, 0)
        context.stroke()

if __name__ == '__main__':
    window = Gtk.Window()
    grid = Grid()
    
    window.add(grid)
    window.connect('destroy', Gtk.main_quit)
    window.show_all()
    
    Gtk.main()