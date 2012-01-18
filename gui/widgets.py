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

        self.rect = self.get_allocation()

    @property
    def width(self):
        return self.rect.width

    @property
    def height(self):
    	return self.rect.height

    @property
    def x(self):
        return self.rect.x

    @property
    def y(self):
        return self.rect.y

    def expose(self, widget, event):
        self.context = widget.window.cairo_create()
        self.rect = self.get_allocation()

        # speed up by setting a clip region for the expose event
        self.context.rectangle(self.x, self.y,
                               self.width, self.height)
        self.context.clip()
        self.draw(self.context)
        return False

    def _draw_outline(self, context):
        print self.width, self.height, self.x, self.y
        context.rectangle(self.x+(self.width/4),
                          self.y+(self.width/4),
                          self.width-(self.width/4),
                          self.width-(self.width/4))

        context.set_line_width(4)
        context.set_source_rgba(0, 0, 0, 0.25)
        context.stroke()
        context.save()
        context.clip()
        context.paint()
        context.restore()


    def draw(self, context):
        context.set_line_width(3)

        x = self.x + self.width / 2
        y = self.y + self.height / 2

        radius = min(self.width / 2, self.height / 2) - 5
        context.arc(x, y, radius, 0, 2 * math.pi)
        context.set_source_rgb(1, 1, 1)
        context.fill_preserve()
        context.set_source_rgb(0, 0, 0)
        context.stroke()

        self._draw_outline(context)

if __name__ == '__main__':
    window = Gtk.Window()
    grid = Grid()
    
    window.add(grid)
    window.connect('destroy', Gtk.main_quit)
    window.show_all()
    
    Gtk.main()