# coding=UTF-8
from topo import parse_xml_string
from SimpleXMLRPCServer import SimpleXMLRPCServer


# TODO RPC
class Server:
    def __init__(self, listen_address, listen_port, scene_instance_manager):
        self.listen_address = listen_address
        self.listen_port = listen_port
        self.scene_instance_manager = scene_instance_manager
        self.server = SimpleXMLRPCServer((self.listen_address, self.listen_port))

    def start(self):
        self.server.register_function(self.on_create,"create")
        self.server.register_function(self.stop, "stop")
        self.server.register_function(on_info,"info")
        self.server.register_function(on_destroy,"destory")
        self.server.serve_forever()

    def stop(self):
       # self.server.shutdown() 在网上看到的这条语句，在windows下测试没有反应，直接调用server_close()可以停止但是会返回一个错误
        self.server.server_close()

    def on_create(self, name, topo_content):
        topo = parse_xml_string(topo_content)
        return self.scene_instance_manager.create_scene(topo, name)

    def on_info(self, scene_id):
        return self.scene_instance_manager.query_scene(scene_id).to_info()

    def on_destroy(self, scene_id):
self.scene_instance_manager.destroy_scene(scene_id)