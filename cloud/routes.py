from cloud import app
from flask import render_template
from pxeserver.pxe import handle, systems



@app.route('/')
def index():
    return render_template('layout.html')


@app.route('/systems')
def system():
    return render_template('systems.html', sys_all=systems, nbenable=True)


@app.route('/config')
def config():
    return render_template('config.html')