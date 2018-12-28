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
	os.system('python -m pip install pyHook.whl')

if input("First use?\n1. yes\n2.No\n") == "1":
	os.system('netsh advfirewall firewall add rule name="ArmaLagg" dir=out action=block program="'+input("Your Arma path:\n")+'" enable=yes')
print("Press 4 on the Keyboard to activate and deactivate the Laggswitch")

class Keystroke_Watcher(object):
	def __init__(self):
		self.hm = HookManager()
		self.hm.KeyDown = self.on_keyboard_event
		self.hm.HookKeyboard()
		self.alreadyOn = True

	def on_keyboard_event(self, event):
		try:
			if event.KeyID  == 52:
				self.switchRule()
		finally:
			return True

	def switchRule(self):
		if (self.alreadyOn == False):
			self.alreadyOn = True
			os.system('netsh advfirewall firewall set rule name="Arma 3" new enable=yes')
			print("not active")
		else:
			self.alreadyOn = False
			os.system('netsh advfirewall firewall set rule name="Arma 3" new enable=no')
			print("active")
			
watcher = Keystroke_Watcher()
PumpMessages()