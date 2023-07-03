# CTkXYFrame
**A better scrollable frame for customtkinter!**

![Screenshot](https://github.com/Akascape/CTkXYFrame/assets/89206401/859b6733-3c91-4093-a511-d6f1060a18ca)

## Features
- Both x and y scrollability at the same time
- Proper mousewheel bindings
- Dynamic scrollbars, hides automatically when reaches full size
- Full customisability just like ctkscrollable frame

## Installation

### [<img alt="GitHub repo size" src="https://img.shields.io/github/repo-size/Akascape/CTkXYFrame?&color=white&label=Download%20Source%20Code&logo=Python&logoColor=yellow&style=for-the-badge"  width="400">](https://github.com/Akascape/CTkXYFrame/archive/refs/heads/main.zip)

**Download the source code, paste the `CTkXYFrame` folder in the directory where your program is present.**

## Usage
```python
import customtkinter
from CTkXYFrame import *

root = customtkinter.CTk()

xy_frame = CTkXYFrame(root)
xy_frame.pack()

root.mainloop()
```

**All other methods and arguments of CTkScrollableFrame can be used with CTkXYFrame**
