import os 
try:
	from win32gui import PumpMessages
except:
	print ("Installing pypi\n")
	os.system('python -m pip install pypiwin32')
	from win32gui import PumpMessages
	
try:
	from pyHook import HookManager
except:
	print ("Installing pyHook\n")
	os.system('python -m pip install pyHook.whl')
	from pyHook import HookManager
	
os.system("title Arma3 Lagswitch | Made by github.com/Z01Ntasu")
os.system("cls")
print("Made by github.com/Z01Ntasu")
print("Press 5 on the Keyboard to generate the required rule(just needed on first start)")
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
			elif event.KeyID  == 53:
				self.generateRule()
		finally:
			return True
	def switchRule(self):
		if (self.alreadyOn == False):
			self.alreadyOn = True
			os.system('netsh advfirewall firewall set rule name="ArmaLagg" new enable=no')
			os.system('netsh advfirewall firewall set rule name="Arma 3" new enable=yes')
			print("not active")
		else:
			self.alreadyOn = False
			os.system('netsh advfirewall firewall set rule name="ArmaLagg" new enable=yes')
			os.system('netsh advfirewall firewall set rule name="Arma 3" new enable=no')
			print("active")
	def generateRule(self):
		os.system('netsh advfirewall firewall add rule name="ArmaLagg" dir=out action=block program="'+input("Your Arma path:\n")+'" enable=no')
watcher = Keystroke_Watcher()
PumpMessages()