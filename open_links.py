from tkeasy import *
import webbrowser

def open_url(link):
    webbrowser.open_new_tab(link)
    
label(text="Python official website",
      colortext="blue",row=0,column=0,
      link="https://www.python.org/")
label_click().bind("<Button-1>",lambda url:open_url("https://www.python.org/"))

label(text="Google official website",
      colortext="blue",row=1,column=0)
label_click().bind("<Button-1>",lambda url:open_url("https://www.google.com"))

label(text="Gmail website",
      colortext="blue",row=2,column=0)
label_click().bind("<Button-1>",lambda url:open_url("https://www.gmail.com"))

loop()
