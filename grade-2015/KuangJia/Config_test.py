# coding=UTF-8

import ConfigParser

class Config:
    def __init__(self):
        '''self.scene_config = SceneConfig()'''
        self.listen_port = None
        self.listen_address = None
        self.db_url = None
        self.instances_base_dir = None
        self.repository_base_dir = None
        self.hypervisor_type = None


    def load(self):
        # TODO load from config/mt.cfg use ConfigParser
        cf = ConfigParser.ConfigParser()
        cf.read("mt.cfg")
        
        self.listen_port = cf.get("server","listen_port")
        self.listen_address = cf.get("server","listen_address")
        self.db_url = cf.get("db","db")
        self.instances_base_dir = cf.get("instances","base_dir")
        self.repository_base_dir = cf.get("templates","repository")
        self.hypervisor_type = cf.get("hypervisor","type")

test = Config()
test.load()
print test.listen_port
print test.listen_address
print test.db_url
print test.instances_base_dir
print test.repository_base_dir
print test.hypervisor_type
