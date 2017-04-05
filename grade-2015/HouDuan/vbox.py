#power_on & power_off
#by WangPeng & LiJiahe

from vboxapi import VirtualBoxManager

class VirtualBox(): #Hypervisor
    def __init__(self):
        self.mgr = VirtualBoxManager(None, None)
        self.vbox = self.mgr.vbox

    def power_on(self,vm):
	name = vm
	mach = self.vbox.findMachine(name)
	self.session = self.mgr.getSessionObject(self.vbox)
	progress = mach.launchVMProcess(self.session, "gui", "")
	progress.waitForCompletion(-1)
    
    def power_off(self):	
	self.session.console.powerDown()
	self.mgr.closeMachineSession(self.session)

    def add_nic(self, vm, index, vlan_name):
        raise NotImplementedError()

#test
test=VirtualBox()
name=raw_input()
test.power_on(name)
raw_input()
test.power_off()



