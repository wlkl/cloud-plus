from cloud import app
from flask import render_template, request
from pxeserver.pxe import handle



@app.route('/')
def index():
    return render_template('layout.html')


@app.route('/systems', methods=['POST', 'GET'])
def system():
    if request.method == 'POST':
        systems = handle.find_system(name="*", return_list=True)
        sysname = request.form.getlist('cur_sys')
        for s in systems:
            if s.name in sysname:
                s.netboot_enabled = True
            else:
                s.netboot_enabled = False
            handle.add_system(s)
    return render_template('systems.html', all_systems=systems)


@app.route('/config')
def config():
    return render_template('config.html')