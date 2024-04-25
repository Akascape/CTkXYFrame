"""
Advanced scrollable frame for customtkinter
Author: Akash Bora
License: MIT
"""

import customtkinter
from tkinter import Canvas

class CTkXYFrame(customtkinter.CTkFrame):
    def __init__(self,
                 master: any,
                 width: int = 100,
                 height: int = 100,
                 scrollbar_width: int = 16,
                 scrollbar_fg_color = None,
                 scrollbar_button_color = None,
                 scrollbar_button_hover_color = None,
                 **kwargs):

        self.parent_frame = customtkinter.CTkFrame(master=master, **kwargs)
        self.bg_color = self.parent_frame.cget("fg_color")
        self.xy_canvas = Canvas(self.parent_frame, width=width, height=height,
                                bg=self.parent_frame._apply_appearance_mode(self.bg_color),
                                borderwidth=0, highlightthickness=0)
        self.parent_frame.rowconfigure(0,weight=1)
        self.parent_frame.columnconfigure(0,weight=1)
        
        customtkinter.CTkFrame.__init__(self, master=self.xy_canvas, fg_color=self.parent_frame.cget("fg_color"),
                                        bg_color=self.parent_frame.cget("fg_color"))
        self.window_id = self.xy_canvas.create_window((0,0), window=self, anchor="nw")
        
        self.vsb = customtkinter.CTkScrollbar(self.parent_frame, orientation="vertical", command=self.xy_canvas.yview,
                                              fg_color=scrollbar_fg_color, button_color=scrollbar_button_color,
                                              button_hover_color=scrollbar_button_hover_color, width=scrollbar_width)
        self.hsb = customtkinter.CTkScrollbar(self.parent_frame, orientation="horizontal", command=self.xy_canvas.xview,
                                              fg_color=scrollbar_fg_color, button_color=scrollbar_button_color,
                                              button_hover_color=scrollbar_button_hover_color, height=scrollbar_width)
        
        self.xy_canvas.configure(yscrollcommand=lambda x,y: self.dynamic_scrollbar_vsb(x,y),
                                 xscrollcommand=lambda x,y: self.dynamic_scrollbar_hsb(x,y))
        self.xy_canvas.grid(row=0, column=0, sticky="nsew", padx=(7,0), pady=(7,0))
        
        self.bind("<Configure>", lambda event, canvas=self.xy_canvas: self.onFrameConfigure(canvas))
        self.xy_canvas.bind_all("<MouseWheel>", lambda e: self._on_mousewheel(e.delta, e.widget), add="+")
        self.xy_canvas.bind_all("<Shift-MouseWheel>", lambda e: self._on_mousewheel_shift(e.delta, e.widget), add="+")
        self.xy_canvas.bind_all("<Button-4>", lambda e: self._on_mousewheel(120, e.widget), add="+")
        self.xy_canvas.bind_all("<Button-5>", lambda e: self._on_mousewheel(-120, e.widget), add="+")
        self.xy_canvas.bind_all("<Shift-Button-4>", lambda e: self._on_mousewheel_shift(120, e.widget), add="+")
        self.xy_canvas.bind_all("<Shift-Button-5>", lambda e: self._on_mousewheel_shift(-120, e.widget), add="+")

        if type(master) is customtkinter.CTkScrollableFrame:
            master.check_if_master_is_canvas = self.disable_contentscroll
            
    def destroy(self):
        customtkinter.CTkFrame.destroy(self)
        self.parent_frame.destroy()

    def _set_appearance_mode(self, mode_string):
        super()._set_appearance_mode(mode_string)
        self.xy_canvas.config(bg=self.parent_frame._apply_appearance_mode(self.bg_color))

    def check_if_master_is_canvas(self, widget):
        if widget == self.xy_canvas:
            return True
        elif widget.master is not None:
            return self.check_if_master_is_canvas(widget.master)
        else:
            return False
        
    def disable_contentscroll(self, widget):
        if widget == self.xy_canvas:
            return True
        else:
            return False
        
    def dynamic_scrollbar_vsb(self, x, y):
        if float(x)==0.0 and float(y)==1.0:
            self.vsb.grid_forget()
        else:
            self.vsb.grid(row=0, column=1, rowspan=2, sticky="nse", pady=5)
        self.vsb.set(x,y)
        
    def dynamic_scrollbar_hsb(self, x, y):
        if float(x)==0.0 and float(y)==1.0:
            self.hsb.grid_forget()
        else:
            self.hsb.grid(row=1, column=0, sticky="nwe", padx=(5,0))
        self.hsb.set(x,y)
        
    def onFrameConfigure(self, canvas):
        canvas.configure(scrollregion=canvas.bbox("all"))
        
    def _on_mousewheel(self, event, widget):
        if self.check_if_master_is_canvas(widget):
            self.xy_canvas.yview_scroll(int(-1*(event/120)), "units")
        
    def _on_mousewheel_shift(self, event, widget):
        if self.check_if_master_is_canvas(widget):
            self.xy_canvas.xview_scroll(int(-1*(event/120)), "units")
        
    def pack(self, **kwargs):
        self.parent_frame.pack(**kwargs)

    def place(self, **kwargs):
        self.parent_frame.place(**kwargs)

    def grid(self, **kwargs):
        self.parent_frame.grid(**kwargs)

    def pack_forget(self):
        self.parent_frame.pack_forget()

    def place_forget(self, **kwargs):
        self.parent_frame.place_forget()

    def grid_forget(self, **kwargs):
        self.parent_frame.grid_forget()

    def grid_remove(self, **kwargs):
        self.parent_frame.grid_remove()

    def grid_propagate(self, **kwargs):
        self.parent_frame.grid_propagate()

    def grid_info(self, **kwargs):
        return self.parent_frame.grid_info()

    def lift(self, aboveThis=None):
        self.parent_frame.lift(aboveThis)

    def lower(self, belowThis=None):
        self.parent_frame.lower(belowThis)
        
    def configure(self, **kwargs):
        if "fg_color" in kwargs:
            self.bg_color = kwargs["fg_color"]
            self.xy_canvas.config(bg=self.bg_color)
            self.configure(fg_color=self.bg_color)
        if "width" in kwargs:
            self.xy_canvas.config(width=kwargs["width"])
        if "height" in kwargs:
            self.xy_canvas.config(height=kwargs["height"])
        self.parent_frame.configure(**kwargs)
