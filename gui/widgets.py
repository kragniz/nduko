#!/usr/bin/env python

import math
import cairo 
try:
    import gi
    from gi.repository import Gtk
except:
    #make gtk2 look like gtk3
    import gtk as Gtk

class Grid(Gtk.DrawingArea):
    def __init__(self):
        Gtk.DrawingArea.__init__(self)
        self.set_size_request(19, 19)
        events = {
            'expose_event' : self.expose
        }
        self.connect('expose_event', self.expose)
        self.connect('button-press-event', self.on_button_press)

        self.rect = self.get_allocation()

        self._value = 0
        self._selected = False

    def on_button_press(self, widget, event):
        print 'hey there'
        return True

    @property
    def window_width(self):
        return self.rect.width

    @property
    def window_height(self):
    	return self.rect.height

    @property
    def x(self):
        return self.rect.x

    @property
    def y(self):
        return self.rect.y

    @property
    def width(self):
    	return min(self.window_width, self.window_height)

    @property
    def value(self):
    	return self._value

    @value.setter
    def value(self, value):
    	self._value = value

    @property
    def _center(self):
    	return (self.window_width + self.x) / 2, (self.window_height + self.y) / 2

    def expose(self, widget, event):
        self.context = widget.window.cairo_create()
        self.rect = self.get_allocation()

        # speed up by setting a clip region for the expose event
        self.context.rectangle(self.x, self.y,
                               self.window_width, self.window_height)
        self.context.clip()

        self.draw(self.context)
        return False

    def _draw_value(self, context):
    	text = str(self.value)
    	m1, m2 = self._center

    	context.set_font_size(self.width/2)
    	context.select_font_face('', cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_NORMAL)

        (x, y, width, height, dx, dy) = context.text_extents(text)
        context.move_to(m1-dx/2, m2+height/2)
        context.text_path(text)

        context.set_source_rgb(0, 0, 0)
        context.fill_preserve()
        context.set_line_width(0)

        context.stroke()

    def _draw_square(self, context, fillColor = (1, 0, 0, 0.25),
                                    strokeColor = (0, 0, 0, 0.25),
                                    inset = 0,
                                    fill = False,
                                    stroke = True):
        m1, m2 = self._center
        width = self.width / 1.05 #magic number.

        context.rectangle(m1-(width/2)+inset,
                          m2-(width/2)+inset,
                          width-inset*2,
                          width-inset*2)

        context.set_line_width(self.width/20)
        if fill:
            context.set_source_rgba(*fillColor)
            context.fill_preserve()
        if stroke:
            context.set_source_rgba(*strokeColor)
            context.stroke()

        context.save()
        context.clip()
        context.paint()
        context.restore()


    def draw(self, context):
        self._draw_square(context, fill=True, stroke=True)
        self._draw_value(context)

if __name__ == '__main__':
    window = Gtk.Window()
    grid = Grid()
    grid.value = 99
    
    window.add(grid)
    window.connect('destroy', Gtk.main_quit)
    window.show_all()
    
    Gtk.main()
