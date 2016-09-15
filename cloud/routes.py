from cloud import app
from flask import render_template, request
from pxeserver.pxe import handle, systems



@app.route('/')
def index():
    return render_template('layout.html')


@app.route('/systems', methods=['POST', 'GET'])
def system():
    if request.method == 'POST':
        sys = handle.find_system(name=request.form.getlist('cur_sys'))
        print(sys)
#        sys.netboot_enabled = True
#        handle.add_system(sys)
    return render_template('systems.html', sys_all=systems)


@app.route('/config')
def config():
    return render_template('config.html')