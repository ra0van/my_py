#https://sourceforge.net/projects/pywin32/files/
# Download compatible version of win32api from above url


import win32api,win32con
import thread
import time

def click(x,y):
	win32api.SetCursorPos((x,y))
	win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
	win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)

def getIdleTime():
    return (win32api.GetTickCount() - win32api.GetLastInputInfo()) / 1000

def idle():
	while True:
		idleTime = getIdleTime()
		if idleTime>=150:
			click(100,0)
		if idleTime<30:
			sleepTime = 150
		else:
			sleepTime = max(150-idleTime,10)
		print 'sleeping for',sleepTime
		time.sleep(sleepTime)
idle()
