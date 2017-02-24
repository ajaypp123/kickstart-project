from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/auth.html', methods=['POST', 'GET'])
def installation_fun():
    if request.method == 'POST':
        if request.form['submit'] == 'Save':
            fi = open('ks.cfg', 'w')
            auth_line2 = "auth"
            if request.form.get("auth_shadow_pass"):
                auth_line2 += " --useshadow"
            auth_security_algo = request.form['auth_security_algo']
            auth_line2 = auth_line2 + auth_security_algo
            if request.form.get("auth_finger_reader"):
                auth_line2 += " --enablefingerprint"
            if request.form.get("auth_enable_nis"):
                    auth_line2 += " --enablenis --nisdomain=" + request.form['auth_nis_domain']
            fi.write("\n" + "# System authorization information\n" + auth_line2)
            fi.close()
            return render_template('auth.html')
    elif request.method == 'GET':
        return render_template('auth.html')


if __name__ == '__main__':
    app.run()
