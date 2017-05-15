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

    def clone(self,old,new):
        old_mach = self.vbox.findMachine(old)
        new_mach = self.vbox.createMachine("",new,"",old_mach.OSTypeId,"")
        progress = old_mach.cloneTo(new_mach,3,None)
        print "Cloning,please wait."
        progress.waitForCompletion(-1)
        new_mach.saveSettings()
        self.vbox.registerMachine(new_mach)

    def add_nic(self, vm, index, vlan_name):
        raise NotImplementedError()

if __name__ == "__main__":
    test = VirtualBox()
    name = raw_input("name:")
    test.power_on(name)
    raw_input()
    test.power_off()
    old_mach = name
    new_mach = raw_input("new_mach:")
    group = ""
    try:
        test.clone(old_mach,new_mach)
        print "success!"
    except Exception,e:
        print e




