#!/usr/bin/python

import cobbler.api as capi
handle = capi.BootAPI()

systems = handle.find_system(name="*", return_list=True)

for s in systems:
    print s.name, s.netboot_enabled
