from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/install_config.html', methods=['POST', 'GET'])
def installation_fun():
    if request.method == 'POST':
        if request.form['submit'] == 'Save':
            fi = open('ks.cfg', 'w')
            install_new_installation = request.form['install_new_installation']
            install_source = request.form['install_source']
            install_source_server = request.form['install_source_server']
            install_source_dict = request.form['install_source_dict']
            install_check_ftp = "false"
            install_ftp_user = request.form['install_ftp_user']
            install_ftp_pass = request.form['install_ftp_pass']
            if request.form.get("install_check_ftp"):
                install_check_ftp = "True"
            install_new_installation = install_new_installation.split("$$")
            fi.write("\n" + install_new_installation[0] + "\n" + install_new_installation[1])
            if install_source == "# Use CDROM installation media $$cdrom":
                cdrom = install_source.split("$$")
                fi.write("\n" + cdrom[0] + "\n" + cdrom[1])
            elif install_source == "# Use NFS installation media $$nfs":
                nfs = install_source.split("$$")
                fi.write("\n" + nfs[0] + "\n" + "nfs --server=" + install_source_server + " --dir=" + install_source_dict)
            elif install_source == "# Use network installation $$http":
                http = install_source.split("$$")
                fi.write("\n" + http[0] + "\nurl --url=\"http://" + install_source_server + "/" + install_source_dict + "\"")
            elif install_source == "# Use network installation $$ftp":
                ftp = install_source.split("$$")
                if install_check_ftp == "false":
                    fi.write("\n" + ftp[0] + "\nurl --url=\"ftp://" + install_source_server + "/" + install_source_dict + "\"")
                if install_check_ftp == "True":
                    fi.write("\n" + ftp[0] + "\nurl --url=\"ftp://" + install_ftp_user + ":" + install_ftp_pass + "@" + install_source_server + "/" + install_source_dict + "\"")
            elif install_source == "# Use hard drive installation media $$hard_drive":
                hard_drive = install_source.split("$$")
                fi.write("\n" + hard_drive[0] + "\nharddrive --dir=" + install_source_server + " --partition=" + install_source_dict + "\"")
            fi.close()
            return render_template('install_config.html')
    elif request.method == 'GET':
        return render_template('install_config.html')


if __name__ == '__main__':
    app.run()

