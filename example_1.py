import customtkinter
from CTkXYFrame import *

root = customtkinter.CTk()

xy_frame = CTkXYFrame(root)
xy_frame.pack(fill="both", expand=True, padx=10, pady=10)

for i in range(20):
    for j in range(10):
        customtkinter.CTkButton(xy_frame).grid(row=i, column=j, padx=5, pady=5)
    
root.mainloop()
