#!/usr/bin/python

import sys
import cobbler.api as capi

handle = capi.BootAPI()

system = handle.find_system(name=str(sys.argv[1]))
system.netboot_enabled = str(sys.argv[2])
handle.add_system(system)

