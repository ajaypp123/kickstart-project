# import crypt
from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        if request.form['save'] == 'Save File':
            fi = open('ks.cfg', 'w')
            ###Basic Configuration
            get_target = request.form.to_dict('target_architecture')
            target_architecture = get_target['target_architecture']
            print(target_architecture)
            fi.write("\n#platform=" + target_architecture + "")

            get_keyboard = request.form.to_dict('keyboard')
            keyboard = get_keyboard['keyboard']
            print(keyboard)
            fi.write("\n# Keyboard layouts\nkeyboard '" + keyboard + "'")

            get_language = request.form.to_dict('language')
            language = get_language['language']
            print(language)
            fi.write("\n# System language\n" + language + "")

            get_timezone = request.form.to_dict('timezone')
            timezone = get_timezone['timezone']
            utc_check = "false"
            if request.form.get('utc_check'):
                utc_check = "true"
            if utc_check == "false":
                fi.write("\n# System timezone\ntimezone " + timezone + "")
            elif utc_check == "true":
                fi.write("\n# System timezone\ntimezone " + timezone + " --isUtc")
            print(timezone)
            # rootpass = request.form['pass']
            # rerootpass = request.form['repass']
            # if rootpass == rerootpass:
            # if request.form.get('basic_encrypt'):
            #  print("basic encrypt **true**")
            #   fi.write(
            #        "\n# Root password\nrootpw --iscrypted " + crypt.crypt(rerootpass, crypt.mksalt(crypt.METHOD_MD5)))
            # else:
            #      print("basic encrypt **false**")
            #       fi.write("\n# Root password\nrootpw --plaintext " + rerootpass)

            if request.form.get("reboot"):
                fi.write("\n# Reboot after installation\nreboot")
            else:
                fi.write("\n# Halt after installation\nhalt")

            if request.form.get("textmode"):
                fi.write("\n# Use text mode install\ntext")
            else:
                fi.write("\n# Use graphical install\ngraphical")
            ###Installation Configuration
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
                fi.write(
                    "\n" + nfs[0] + "\n" + "nfs --server=" + install_source_server + " --dir=" + install_source_dict)
            elif install_source == "# Use network installation $$http":
                http = install_source.split("$$")
                fi.write(
                    "\n" + http[0] + "\nurl --url=\"http://" + install_source_server + "/" + install_source_dict + "\"")
            elif install_source == "# Use network installation $$ftp":
                ftp = install_source.split("$$")
                if install_check_ftp == "false":
                    fi.write("\n" + ftp[
                        0] + "\nurl --url=\"ftp://" + install_source_server + "/" + install_source_dict + "\"")
                if install_check_ftp == "True":
                    fi.write("\n" + ftp[
                        0] + "\nurl --url=\"ftp://" + install_ftp_user + ":" + install_ftp_pass + "@" + install_source_server + "/" + install_source_dict + "\"")
            elif install_source == "# Use hard drive installation media $$hard_drive":
                hard_drive = install_source.split("$$")
                fi.write("\n" + hard_drive[
                    0] + "\nharddrive --dir=" + install_source_server + " --partition=" + install_source_dict + "\"")
            ###Boot-Loader Configuration
            ###Partition Information
            if request.form.get("prt_check_zerombr"):
                fi.write("\n#Clear master boot record \nzerombr")
            if request.form.get("prt_check_rmallpart"):
                fi.write("\n#Partition Clearing Information\nclearpart --all")
                if request.form.get("prt_check_initlabel"):
                    fi.write(" --initlabel")
            else:
                fi.write("\n#Partition Clearing Information\nclearpart --none")
            if request.form.get("prt_check_autopart"):
                fi.write("\n#Disk partitioning information \nautopart")
            else:
                all_vg = request.form['prt_all_vg']
                all_lv = request.form['prt_all_lv']
                vg_list = all_vg.split("$$")
                lv_list = all_lv.split("$$")
                t1 = len(vg_list)
                t2 = len(lv_list)
                i = 0
                fi.write("\n#Disk partitioning information")
                for i in range(t1):
                    if i != 0:
                        vg_field = vg_list[i].split(" ")
                        vg_name = vg_field[1].split(":")
                        vg_disk = vg_field[2].split(":")
                        vg_size = vg_field[3].split(":")
                        vg_pesize = vg_field[4].split(":")
                        fi.write(
                            "\npart pv_" + vg_name[1] + ' --fstype="lvmpv" --ondisk=' + vg_disk[1] + " --size=" +
                            vg_size[
                                1])
                        fi.write("\nvolgroup " + vg_name[1] + " --pesize=" + vg_pesize[1] + " pv_" + vg_name[1])
                for i in range(t2):
                    if i != 0:
                        lv_field = lv_list[i].split(" ")
                        lv_mnt_pt = lv_field[1].split(":")
                        lv_vg = lv_field[2].split(":")
                        lv_name = lv_field[3].split(":")
                        lv_fst = lv_field[4].split(":")
                        lv_size = lv_field[5].split(":")
                        fi.write("\nlogvol " + lv_mnt_pt[1] + " --vgname=" + lv_vg[1] + " --name=" + lv_name[
                            1] + " --fstype=" + lv_fst[1] + " --size=" + lv_size[1])
                        if (len(lv_field) == 8):
                            lv_maxsize = lv_field[7].split(":")
                            fi.write(" --grow --maxsize=" + lv_maxsize[1])
            ###Network Configuration
            if request.form.get("net_check_default_network"):
                fi.write("\n#No network device information")
            else:
                all_dev = request.form['net_all_devices']
                dev_list = all_dev.split("$$")
                t1 = len(dev_list)
                i = 0
                fi.write("\n#Network device information")
                for i in range(t1):
                    if i != 0:
                        dev_field = dev_list[i].split(" ")
                        if len(dev_field) == 7:
                            dev_name = dev_field[1].split(':')
                            dev_protocol = dev_field[2].split(':')
                            dev_ip = dev_field[3].split(':')
                            dev_netmask = dev_field[4].split(':')
                            dev_gateway = dev_field[5].split(':')
                            dev_nameserver = dev_field[6].split(':')
                            fi.write(
                                "\nnetwork --device=" + dev_name[1] + ' --bootproto=' + dev_protocol[1] + ' --ip=' +
                                dev_ip[1] + " --netmask=" + dev_netmask[1] + " --gateway=" + dev_gateway[
                                    1] + " --nameserver=" + dev_nameserver[1])
                        else:
                            dev_name = dev_field[1].split(':')
                            dev_protocol = dev_field[2].split(':')
                            fi.write("\nnetwork --device=" + dev_name[1] + ' --bootproto=' + dev_protocol[1])
            ###Authentication Configuration
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
                    auth_line2 += " --nisserver=" + request.form['auth_nis_server']
            if request.form.get("auth_enable_ldap"):
                auth_line2 += " --enableldap --enableldapauth --ldapserver=" + request.form[
                    'auth_ldap_server'] + " --ldapbasedn=" + request.form['auth_ldap_base']
                if request.form.get("auth_ldap_certificate"):
                    auth_line2 += " --ldaploadcacert=" + request.form['auth_ldap_cert_url']
            if request.form.get("auth_enable_krb5"):
                auth_line2 += " --enablekrb5 --krb5realm=" + request.form['auth_krb5_realm'] + " --krb5kdc=" + \
                              request.form['auth_kerberos_domain'] + " --krb5adminserver=" + request.form[
                                  'auth_krb5_master']
            if request.form.get("auth_enable_smb"):
                auth_line2 += " --enablesmbauth --smbservers=" + request.form['auth_smb_server'] + " --smbworkgroup=" + \
                              request.form['auth_smb_workgrp']
            if request.form.get("auth_switch_cache"):
                auth_line2 += " --enablecache"
            fi.write("\n" + "# System authorization information\n" + auth_line2)
            ###firewall Configuration
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
            ###Display Configuration
            check_value = request.form.to_dict('display_checkbox')
            if request.form.get("display_checkbox"):
                print("checked")
                first_boot = check_value['first-boot']
                if first_boot == 'Enabled':
                    print("enable")
                    fi.write("\n# Run the Setup Agent on first boot\nfirstboot --enable")
                elif first_boot == 'Disabled':
                    print("disable")
                    fi.write("\n# Run the Setup Agent on first boot\nfirstboot --disable")
                elif first_boot == 'Reconfigure':
                    print("reconfigure")
                    fi.write("\n# Run the Setup Agent on first boot\nfirstboot --reconfig")
            else:
                print("uncheck")
                fi.write(
                    "\n# Run the Setup Agent on first boot\nfirstboot --reconfig\n# Do not configure the X Window System\nskipx")
            ###Package Configuration
            pkg_gnome_package = {request.form.get("pkg_group_epiphany"): "epiphany",
                                 request.form.get("pkg_group_gnome-games"): "gnome-games",
                                 request.form.get("pkg_group_gnome-desktop"): "gnome-desktop"}
            pkg_kde_package = {request.form.get("pkg_group_kde-desktop"): "kde-desktop",
                               request.form.get("pkg_group_kde-apps"): "kde-apps",
                               request.form.get("pkg_group_kde-education"): "kde-education",
                               request.form.get("pkg_group_kde-media"): "kde-media",
                               request.form.get("pkg_group_kde-office"): "kde-office",
                               request.form.get("pkg_group_kde-telepathy"): "kde-telepathy"}
            pkg_xfce_package = {request.form.get("pkg_group_xfce-apps"): "xfce-apps",
                                request.form.get("pkg_group_xfce-desktop"): "xfce-desktop",
                                request.form.get("pkg_group_xfce-extra-plugins"): "xfce-extra-plugins",
                                request.form.get("pkg_group_xfce-media"): "xfce-media",
                                request.form.get("pkg_group_xfce-office"): "xfce-office"}
            pkg_appli_package = {request.form.get("pkg_group_audio"): "audio",
                                 request.form.get("pkg_group_authoring-and-publishing"): "authoring-and-publishing",
                                 request.form.get("pkg_group_design-suite"): "design-suite",
                                 request.form.get("pkg_group_editors"): "editors",
                                 request.form.get("pkg_group_education"): "education",
                                 request.form.get("pkg_group_engineering-and-scientific"): "engineering-and-scientific",
                                 request.form.get("pkg_group_firefox"): "firefox",
                                 request.form.get("pkg_group_font-design"): "font-design",
                                 request.form.get("pkg_group_games"): "games",
                                 request.form.get("pkg_group_graphical-internet"): "graphical-internet",
                                 request.form.get("pkg_group_graphics"): "graphics",
                                 request.form.get("pkg_group_libreoffice"): "libreoffice",
                                 request.form.get("pkg_group_medical"): "medical",
                                 request.form.get("pkg_group_office"): "office",
                                 request.form.get("pkg_group_sound-and-video"): "sound-and-video",
                                 request.form.get("pkg_group_text-internet"): "text-internet"}
            pkg_lxde_package = {request.form.get("pkg_group_lxde-apps"): "lxde-apps",
                                request.form.get("pkg_group_lxde-desktop"): "lxde-desktop",
                                request.form.get("pkg_group_lxde-office"): "lxde-office",
                                request.form.get("pkg_group_lxde-media"): "lxde-media"}
            pkg_lxqt_package = {request.form.get("pkg_group_lxqt-apps"): "lxqt-apps",
                                request.form.get("pkg_group_lxqt-desktop"): "lxqt-desktop",
                                request.form.get("pkg_group_lxqt-office"): "lxqt-office",
                                request.form.get("pkg_group_lxqt-media"): "lxqt-media"}
            pkg_chinn_package = {request.form.get("pkg_group_cinnamon-desktop"): "cinnamon-desktop"}
            if request.form.get("auth_shadow_pass"):
                fi.write("\n\n%packages\n")
                if request.form.get("pkg_gnome"):
                    for pkg_name in pkg_gnome_package:
                        if pkg_name:
                            fi.write("\n@" + pkg_gnome_package[pkg_name])
                if request.form.get("pkg_kde"):
                    for pkg_name in pkg_kde_package:
                        if pkg_name:
                            fi.write("\n@" + pkg_kde_package[pkg_name])
                if request.form.get("pkg_xfce"):
                    for pkg_name in pkg_xfce_package:
                        if pkg_name:
                            fi.write("\n@" + pkg_xfce_package[pkg_name])
                if request.form.get("pkg_appli"):
                    for pkg_name in pkg_appli_package:
                        if pkg_name:
                            fi.write("\n@" + pkg_appli_package[pkg_name])
                if request.form.get("pkg_lxde"):
                    for pkg_name in pkg_lxde_package:
                        if pkg_name:
                            fi.write("\n@" + pkg_lxde_package[pkg_name])
                if request.form.get("pkg_lxqt"):
                    for pkg_name in pkg_lxqt_package:
                        if pkg_name:
                            fi.write("\n@" + pkg_lxqt_package[pkg_name])
                if request.form.get("pkg_chinn"):
                    for pkg_name in pkg_chinn_package:
                        if pkg_name:
                            fi.write("\n@" + pkg_chinn_package[pkg_name])
                fi.write("\n\n%end\n")
            ###Pre Configuration
            pre_interpreter_name = request.form['pre_interpreter_name']
            pre_interpreter_scr = request.form['pre_interpreter_scr']
            if request.form.get("pre_interpreter_enble"):
                fi.write("\n\n\n\n" + "%pre")
                if request.form.get("pre_inter_allow"):
                    fi.write(" --interpreter=" + pre_interpreter_name)
                fi.write("\n" + pre_interpreter_scr)
                fi.write("\n%end")
            ###Post Configuration
            post_interpreter_name = request.form['post_interpreter_name']
            post_interpreter_scr = request.form['post_interpreter_scr']
            fi.write("\n\n\n\n" + "%post")
            if request.form.get("post_inter_allow"):
                fi.write(" --interpreter=" + post_interpreter_name)
            if request.form.get("post_nochroot_allow"):
                fi.write(" --nochroot")
            fi.write("\n" + post_interpreter_scr)
            fi.write("\n%end")
            ##########################################################
            fi.close()
            return render_template('index.html')
    elif request.method == 'GET':
        return render_template('index.html')


@app.route('/help.html', methods=['POST', 'GET'])
def help():
    return render_template('help.html')


@app.route('/Customise.html', methods=['POST', 'GET'])
def Customise():
    return render_template('Customise.html')


@app.route('/Setup.html', methods=['POST', 'GET'])
def Setup():
    return render_template('Setup.html')


@app.route('/Credits.html', methods=['POST', 'GET'])
def Credits():
    return render_template('Credits.html')


if __name__ == '__main__':
    app.run(debug=True)
