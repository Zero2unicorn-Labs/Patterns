import time
import webbrowser

total_breaks=2
break_start=0

while(break_start<total_breaks):
    time.sleep(6)
    webbrowser.open("https://youtube.com/")
    break_start=break_start+1

