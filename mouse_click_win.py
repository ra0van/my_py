#https://sourceforge.net/projects/pywin32/files/
# Download compatible version of win32api from above url


import win32api,win32con
import thread
import time

def click(x,y):
	while True:
		print 'clicking.....'
		win32api.SetCursorPos((x,y))
		win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
		win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)
		#Wait for 170 seconds before next click
		time.sleep(170);

click(0,0)
