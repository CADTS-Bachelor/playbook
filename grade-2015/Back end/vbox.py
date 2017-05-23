from vboxapi import VirtualBoxManager


class VirtualBox():  # Hypervisor
    def __init__(self):
        self.mgr = VirtualBoxManager(None, None)
        self.vbox = self.mgr.vbox

    def getsession(self, vm):
        try:
            mach = self.vbox.findMachine(vm)
            session = self.mgr.getSessionObject(mach)
            mach.lockMachine(session, 1)
            return session
        except Exception,e:
            print e

    def power_on(self, vm):
        try:
            mach = self.vbox.findMachine(vm)
            session = self.mgr.getSessionObject(mach)
            progress = mach.launchVMProcess(session, "gui", "")
            progress.waitForCompletion(-1)
            self.mgr.closeMachineSession(session)
            print "power_on success !"
        except Exception, e:
            print e

    def power_off(self, vm):
        session = self.getsession(vm)
        try:
            progress = session.console.powerDown()
            progress.waitForCompletion(-1)
            session.unlockMachine()
            print "power_off success !"
        except Exception,e:
            print e

    def clone(self, src_vm, dst_vm):
        try:
            src_mach = self.vbox.findMachine(src_vm)
            dst_mach = self.vbox.createMachine("", dst_vm, "", src_mach.OSTypeId, "")
            progress = src_mach.cloneTo(dst_mach, 3, None)
            print "Cloning,please wait."
            progress.waitForCompletion(-1)
            dst_mach.saveSettings()
            self.vbox.registerMachine(dst_mach)
            print "clone success !"
        except Exception, e:
            print e

    def reset(self, vm):
        session = self.getsession(vm)
        try:
            session.console.reset()
            session.unlockMachine()
            print "reset success !"
        except Exception, e:
            print e

    def create_snapshot(self, vm, name):
        session = self.getsession(vm)
        try:
            progress = session.machine.takeSnapshot(name, "", True)[0]
            print "creating snapshot."
            progress.waitForCompletion(-1)
            session.unlockMachine()
            print "create_snapshot success !"
        except Exception, e:
            print e

    def revert_snapshot(self, vm, name):
        session = self.getsession(vm)
        try:
            progress = session.machine.restoreSnapshot(session.machine.findSnapshot(name))
            print "reverting snapshot."
            progress.waitForCompletion(-1)
            session.unlockMachine()
            print "revert_snapshot success !"
        except Exception, e:
            print e

    def add_nic(self, vm, index, vlan_name):
        raise NotImplementedError()


if __name__ == "__main__":
    test = VirtualBox()
    vm = raw_input("vm:")
    test.power_on(vm)
    raw_input("reset")
    test.reset(vm)
    raw_input("power_off")
    test.power_off(vm)
    raw_input("create_snapshot")
    test.create_snapshot(vm, "test")
    raw_input("revert_snapshot")
    test.revert_snapshot(vm, "test")
    raw_input("clone")
    test.clone(vm, "dst_test")