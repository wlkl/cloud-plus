import cobbler.api as capi

handle = capi.BootAPI()
systems = handle.find_system(name="*", return_list=True)
#class BootAPI():
#    def __init__(self, sys):
#        self.systems = sys


#handle = BootAPI(['Node1', 'Node2', 'Node3'])
