#https://sourceforge.net/projects/pywin32/files/
# Download compatible version from above url
#incomplete
'''
cmd options:
	1 -> start/resume click event
	2 -> pause the click event, but don't stop the process
	3 -> stop and exit
'''

import win32api,win32con
import thread
import time

def click(x,y):
	global cmd
	while cmd:
		if cmd==3:
			break
		elif cmd==1:
			print 'clicking.....'
			win32api.SetCursorPos((x,y))
			win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
			win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)
	thread.exit()

def help():
	print "start() -> start/resume click event"
	print "pause() -> pause the click event, but don't stop the process"
	print "stop()  -> stop and exit"

	ip = raw_input()
	if ip == 'start()' or ip == 'start':
		return 1
	elif ip == 'pause()' or ip == 'pause':
		return 2
	elif ip=='stop()' or ip == 'stop':
		return 3
	else:
		print "Unkown command"
		return help()

def trigger():
	global cmd
	while True:
		ip = help()
		if ip == 0:
			pass
		elif ip == 1:
			if cmd==1:
				print "Click event already running"
			else:
				cmd = 1
		elif ip==2:
			if cmd==1:
				cmd =2
			else:
				print "No click event is running"
		elif ip==3:
			cmd = 3
			break;
		time.sleep(5)
	thread.exit()
try:
	cmd = 1
	thread.start_new_thread(trigger())
	thread.start_new_thread(click(240,240))

except:
	print "Error: unable to start thread"
