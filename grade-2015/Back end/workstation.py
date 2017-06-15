# -*-coding:utf-8-*-
import os
#from mt_core.backends import Hypervisor

#os.system('g: && cd g:/vmware && vmrun.exe -T ws start "virtual machine/win7/Windows 7 x64.vmx"')


# TODO override all methods
class Workstation(Hypervisor):
    def Find_Vmrun(self,Sys_Info):
        if Sys_Info.lower()=='windows':
            Vmrun_Path="C:\Program Files (x86)\VMware\VMware VIX"#do something
        else:
            Vmrun_Path=""
        return Vmrun_Path
    def power_on(self,path):
        os.system("vmrun start \"%s\"" %path)
        pass
    def power_off(self,path):
        os.system("vmrun stop \"%s\"" % path)
        pass
    def clone_vm(self,OldSnap,NewSnap):
        os.system("vmrun clone \"%s\" \"%s\" linked" %(OldSnap,NewSnap))
        pass
    def put_file(self, vm, local_path, guest_path, guest_info):
        os.system("vmrun -T ws copyFileFromHostToGuest \"%s\" \"%s\" \"%s\"" % (vm,local_path,guest_path))
        pass
    def get_file(self, vm, host_path, guest_path, guest_info):
        os.system("vmrun -T ws CopyFileFromGuestToHost \"%s\" \"%s\" \"%s\"" % (vm, guest_path, host_path))
        pass
    def create_snapshot(self, vm, name):
        os.system("vmrun -T ws snapshot \"%s\" \"%s\"" % (vm,name))
    #still have to think about it
    def exec_guest(self, vm, cmd, guest_info):
        """
        在虚拟机中执行指定命令
        :param vm: 虚拟机路径
        :param cmd: 命令行
        :param guest_info: 客户操作系统信息
        :return: 返回值
        """
        pass
    def revert_snapshot(self, vm, name):
        """
        恢复快照
        :param vm: 虚拟机路径
        :param name: 快照名称
        """
        os.system("vmrun revertToSnapshot \"%s\" \"%s\"" % (vm,name))
        pass
    def shutdown_guest(self, vm):
        os.system("vmrun stop \"%s\" [software]" % vm)
        pass
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