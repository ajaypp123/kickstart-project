from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/firewall_config.html', methods=['POST', 'GET'])
def firewall_config():
    if request.method == 'POST':
        if request.form['submit'] == 'Save':
            fi = open('ks.cfg', 'w')
            firewall_selinux_state = request.form['firewall_selinux_state']
            firewall_sequrity_level = request.form['firewall_sequrity_level']
            firewall_other_port = request.form['firewall_other_port']
            fi.write("\n" + "# SELinux configuration" + "\n" + firewall_selinux_state)
            if firewall_sequrity_level == "Disable_firewall":
                fi.write("\n" + "# Firewall configuration" + "\n" + "firewall --disabled")
            if firewall_sequrity_level == "Enable_firewall":
                fi.write("\n" + "# Firewall configuration" + "\n" + "firewall --enabled")
                if request.form.get("firewall_http_service"):
                    fi.write(" " + request.form['firewall_http_service'])
                if request.form.get("firewall_ftp_service"):
                    fi.write(" " + request.form['firewall_ftp_service'])
                if request.form.get("firewall_ssh_service"):
                    fi.write(" " + request.form['firewall_ssh_service'])
                if request.form.get("firewall_telnet_service"):
                    fi.write(" " + request.form['firewall_telnet_service'])
                if request.form.get("firewall_mail_service"):
                    fi.write(" " + request.form['firewall_mail_service'])
                if firewall_other_port != "":
                    fi.write(" --port=" + firewall_other_port)
            fi.close()
            return render_template('firewall_config.html')
    elif request.method == 'GET':
        return render_template('firewall_config.html')


if __name__ == '__main__':
    app.run()
