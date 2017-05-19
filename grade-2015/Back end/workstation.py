# -*-coding:utf-8-*-
import os

#from mt_core.backends import Hypervisor

#os.system('g: && cd g:/vmware && vmrun.exe -T ws start "virtual machine/win7/Windows 7 x64.vmx"')


# TODO override all methods
class Workstation():#Hypervisor
    def power_on(self,path):
        os.system("vmrun start \"%s\"" %path)
    def power_off(self,path):
        os.system("vmrun stop \"%s\"" % path)
    def clone_vm(self,OldSnap,NewSnap):
        os.system("vmrun clone \"%s\" \"%s\" linked" %(OldSnap,NewSnap))

test=Workstation()
print ("\"open\" open a vmx")
print ("\"close\" close a vmx")
print ("\"clone\" clone a vmx")
print ("\"quit\" quit")
while (True):
    temp=raw_input()
    if(temp!="quit"):
        if(temp=="open"):
            print ("enter path")
            path=raw_input()
            test.power_on(path)
        elif (temp=="close"):
            print ("enter path")
            path=raw_input()
            test.power_off(path)
        elif (temp=="clone"):
            print ("enter old and new path")
            path1=raw_input()
            path2=raw_input()
            clone_vm(path1,path2)
        else:
            print ("input error!")
    else:
        break