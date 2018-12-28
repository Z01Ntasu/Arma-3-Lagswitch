import os 
try:
	from win32gui import PumpMessages
except:
	print ("Installing pypi\n")
	os.system('python -m pip install pypiwin32')
try:
	from pyHook import HookManager
except:
	print ("Installing pyHook\n")
	os.system('python -m pip install pyHook-1.5.1-cp37-cp37m-win_amd64.whl')

print("Press 4 on the Keyboard to activate and deactivate the Laggswitch")

class Keystroke_Watcher(object):
	def __init__(self):
		self.hm = HookManager()
		self.hm.KeyDown = self.on_keyboard_event
		self.hm.HookKeyboard()
		self.alreadyOn = False

	def on_keyboard_event(self, event):
		try:
			if event.KeyID  == 52:
				self.switchRule()
		finally:
			return True

	def switchRule(self):
		if (self.alreadyOn == False):
			self.alreadyOn = True
			string = 'netsh advfirewall firewall set rule name="Arma 3" new enable=' + "yes"
			os.system(str(string))
			print("not active")
		else:
			self.alreadyOn = False
			string = 'netsh advfirewall firewall set rule name="Arma 3" new enable=' + "no"
			os.system(str(string))
			print("active")
watcher = Keystroke_Watcher()
PumpMessages()