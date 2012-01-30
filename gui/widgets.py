#!/usr/bin/env python

import math
import cairo 
try:
    import gi
    from gi.repository import Gtk
except:
    #make gtk2 look like gtk3
    import gtk as Gtk

class NdukoItem(Gtk.DrawingArea):
    '''Class to draw a single item in an nduko grid. Holds and can change a
    single value'''
    def __init__(self):
        Gtk.DrawingArea.__init__(self)
        self.set_events(Gtk.gdk.BUTTON_PRESS_MASK
                      | Gtk.gdk.POINTER_MOTION_MASK)
        self.set_size_request(19, 19)

        self.connect('expose_event', self._on_expose_event)
        self.connect('button_press_event', self._on_button_press)
        self.connect('motion_notify_event', self._on_motion_notify_event)

        self.rect = self.get_allocation()

        self._value = 0
        self._selected = False

    def _on_button_press(self, widget, event):
        '''Event called whenever a mouse button is pressed on this widget'''
        button = event.button
        if button == 1:
            self.value += 1
            self.selected = True
        else:
            self.value -= 1
            self.selected = False
        self.queue_draw_area(self.x,
                             self.y,
                             self.window_width,
                             self.window_height)
        return True

    def _on_motion_notify_event(self, width, event):
        print 'mouse moved!', event.x, event.y

    @property
    def window_width(self):
        '''Width of the drawable window'''
        return self.rect.width

    @property
    def window_height(self):
        '''Height of the drawable window'''
    	return self.rect.height

    @property
    def x(self):
        '''Return the x coordinate of the upper left corner of the DrawingArea'''
        return self.rect.x

    @property
    def y(self):
        '''Return the y coordinate of the upper left corner of the DrawingArea'''
        return self.rect.y

    @property
    def width(self):
        '''Return the width of the visable inner square'''
    	return min(self.window_width, self.window_height)

    @property
    def value(self):
        '''Return the value of the item'''
    	return self._value

    @value.setter
    def value(self, value):
        '''Set the value for the items'''
    	self._value = value

    @property
    def _center(self):
        '''Return the coordinates for the center of the widget'''
    	return ((self.window_width + self.x) / 2,
                (self.window_height + self.y) / 2)

    @property
    def selected(self):
        return self._selected

    @selected.setter
    def selected(self, value):
        self._selected = value

    def _on_expose_event(self, widget, event):
        '''Event called for every re-draw'''
        self.context = widget.window.cairo_create()
        self.rect = self.get_allocation()

        # speed up by setting a clip region for the expose event
        self.context.rectangle(self.x, self.y,
                               self.window_width, self.window_height)
        self.context.clip()

        self._draw(self.context)
        return False

    def _draw_value(self, context):
        '''Draw the text on the item'''
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
        '''Draw the box around the text. Can be filled with a colour'''
        m1, m2 = self._center
        width = self.width / 1.05 #magic number.

        context.rectangle(m1-(width/2)+inset,
                          m2-(width/2)+inset,
                          width-inset*2,
                          width-inset*2)

        context.set_line_width(self.width/20)
        if fill or self.selected:
            context.set_source_rgba(*fillColor)
            context.fill_preserve()
        if stroke:
            context.set_source_rgba(*strokeColor)
            context.stroke()

        context.save()
        context.clip()
        context.paint()
        context.restore()


    def _draw(self, context):
        '''Call the draw methods'''
        self._draw_square(context, fill=False, stroke=True)
        self._draw_value(context)

if __name__ == '__main__':
    '''Do a bit of self testing'''
    window = Gtk.Window()
    item = NdukoItem()
    item.value = 0
    
    window.add(item)
    window.connect('destroy', Gtk.main_quit)
    window.show_all()
    
    Gtk.main()