import customtkinter
import random
from CTkTable import *
from CTkXYFrame import *

root = customtkinter.CTk()

xy_frame = CTkXYFrame(root)
xy_frame.pack(fill="both", expand=True, padx=10, pady=10)

random_list = []

for i in range(20):
    sub_list = []
    for j in range(10):
        sub_list.append(random.randint(0,20))
    random_list.append(sub_list)
    
table = CTkTable(xy_frame, row=20, column=10, values=random_list)
table.pack()

root.mainloop()
