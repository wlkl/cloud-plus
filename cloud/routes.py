from cloud import app
from flask import render_template, request
from pxeserver.pxe import handle, systems



@app.route('/')
def index():
    return render_template('home.html')


@app.route('/systems')
def system():
    return render_template('systems.html', all_systems=systems)


@app.route('/config', methods=['POST', 'GET'])
def config():
    if request.method == 'POST':
        sysname = request.form.getlist('cur_sys')
        for s in systems:
            if s.name in sysname:
                handle.remove_system(s.name)
    return render_template('config.html', all_systems=systems)