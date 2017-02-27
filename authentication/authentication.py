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
                if request.form.get("auth_broadcast_nis"):
                    pass
                else:
                    auth_line2 += " --nisserver=" +	request.form['auth_nis_server']
            if request.form.get("auth_enable_ldap"):
                auth_line2 += " --enableldap --enableldapauth --ldapserver=" + request.form['auth_ldap_server'] + " --ldapbasedn=" + request.form['auth_ldap_base']
                if request.form.get("auth_ldap_certificate"):
                    auth_line2 += " --ldaploadcacert=" + request.form['auth_ldap_cert_url']
            if request.form.get("auth_enable_krb5"):
                auth_line2 += " --enablekrb5 --krb5realm=" + request.form['auth_krb5_realm'] + " --krb5kdc=" + request.form['auth_kerberos_domain'] + " --krb5adminserver=" + request.form['auth_krb5_master']
            if request.form.get("auth_enable_smb"):
                auth_line2 += " --enablesmbauth --smbservers=" + request.form['auth_smb_server'] + " --smbworkgroup=" + request.form['auth_smb_workgrp']
            if request.form.get("auth_switch_cache"):
                auth_line2 += " --enablecache"
            fi.write("\n" + "# System authorization information\n" + auth_line2)
            fi.close()
            return render_template('auth.html')
    elif request.method == 'GET':
        return render_template('auth.html')


if __name__ == '__main__':
    app.run()

