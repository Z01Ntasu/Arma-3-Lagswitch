import os 

try:
	from win32gui import PumpMessages
except:
	print ("Trying to Install required module: pypi\n")
	os.system('python -m pip install pypiwin32')
try:
	from pyHook import HookManager
except:
	print ("Trying to Install required module: pyHook\n")
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
				self.your_method()
		finally:
			return True

	def your_method(self):
		if (self.alreadyOn == False):
			self.alreadyOn = True
			
			string = 'netsh advfirewall firewall set rule name="Arma3Laggswitch" new enable=' + "yes"
			os.system(str(string))
			print("active")
		else:
			
			self.alreadyOn = False
			string = 'netsh advfirewall firewall set rule name="Arma3Laggswitch" new enable=' + "no"
			os.system(str(string))
			print("not active")
			
	
        

	def shutdown(self):
		PostQuitMessage(0)
		self.hm.UnhookKeyboard()


with open("config.txt", "r+") as file:
	data = file.readlines()

if data[0] == "false":
	
	
	gamePath = input("Enter the path of Arma\n")
		
	command = 'netsh advfirewall firewall add rule name="Arma3Laggswitch" dir=out action=block program="' + gamePath + '" enable=no'
	os.system(command)
	print("Regel erstellt")
	data[0] = "true"
	open("config.txt",'w').write('\n'.join(data))


watcher = Keystroke_Watcher()
PumpMessages()







