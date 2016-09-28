import cobbler.api as capi

handle = capi.BootAPI()
systems = handle.find_system(name="*", return_list=True)

