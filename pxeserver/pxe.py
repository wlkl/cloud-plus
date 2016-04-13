#import cobbler.api as capi

#handle = capi.BootAPI()

class BootAPI():
    def __init__(self, sys):
        self.systems = sys


handle = BootAPI(['Node1', 'Node2', 'Node3'])
