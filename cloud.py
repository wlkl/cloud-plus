__author__ = 'wlkl'

from cloud-plus import app
from flask import render_template
from pxeserver import handle

#app = Flask(__name__)

@app.route('/')
def index():
    return render_template('layout.html')

@app.route('/systems')
def system():
    allsys = handle.systems()
    return render_template('systems.html', systems=allsys)

#if __name__ == '__main__':
#    app.run(host="0.0.0.0", debug=True)
