from cloud import app
from flask import render_template
from pxeserver.pxe import handle



@app.route('/')
def index():
    return render_template('layout.html')


@app.route('/systems')
def system():
    allsys = handle.systems
    return render_template('systems.html', systems=allsys)


