$(document).ready(function() {
    $("#preview_all").click(function() {

        // Get the modal
        var modal = document.getElementById('myModal');

        // Get the button that opens the modal
        var btn = document.getElementById("preview_all");

        // Get the <span> element that closes the modal
        var span = document.getElementsByClassName("close")[0];

        // When the user clicks the button, open the modal 
        /*btn.onclick = function() */
        {
            modal.style.display = "block";
        }

        // When the user clicks on <span> (x), close the modal
        span.onclick = function() {
            modal.style.display = "none";
        }

        //file logic (authentication)
        var file_auth_line2 = "auth";
        var auth_security_algo = document.getElementById('auth_security_algo').value;
        if (document.getElementById("auth_shadow_pass").checked == true) {
            file_auth_line2 = file_auth_line2 + " --useshadow";
        }
        file_auth_line2 = file_auth_line2 + auth_security_algo;
        if (document.getElementById("auth_finger_reader").checked == true) {
            file_auth_line2 = file_auth_line2 + " --enablefingerprint";
        }
        if (document.getElementById("auth_enable_nis").checked == true) {
            file_auth_line2 = file_auth_line2 + " --enablenis --nisdomain=" + document.getElementById('auth_nis_domain').value;
            if (document.getElementById("auth_broadcast_nis").checked != true) {
                file_auth_line2 = file_auth_line2 + " --nisserver=" + document.getElementById('auth_nis_server').value;
            }
        }
        if (document.getElementById("auth_enable_ldap").checked == true) {
            file_auth_line2 = file_auth_line2 + " --enableldap --enableldapauth --ldapserver=";
            file_auth_line2 = file_auth_line2 + document.getElementById('auth_ldap_server').value;
            file_auth_line2 = file_auth_line2 + " --ldapbasedn=" + document.getElementById('auth_ldap_base').value;
            if (document.getElementById("auth_ldap_certificate").checked == true) {
                file_auth_line2 = file_auth_line2 + " --ldaploadcacert=" + document.getElementById('auth_ldap_cert_url').value;
            }
        }
        if (document.getElementById("auth_enable_krb5").checked == true) {
            file_auth_line2 = file_auth_line2 + " --enablekrb5 --krb5realm=" + document.getElementById('auth_krb5_realm').value;
            file_auth_line2 = file_auth_line2 + " --krb5kdc=" + document.getElementById('auth_kerberos_domain').value;
            file_auth_line2 = file_auth_line2 + " --krb5adminserver=" + document.getElementById('auth_krb5_master').value;
        }
        if (document.getElementById("auth_enable_smb").checked == true) {
            file_auth_line2 = file_auth_line2 + " --enablesmbauth --smbservers=" + document.getElementById('auth_smb_server').value;
            file_auth_line2 = file_auth_line2 + " --smbworkgroup=" + document.getElementById('auth_smb_workgrp').value;
        }
        if (document.getElementById("auth_switch_cache").checked == true) {
            file_auth_line2 = file_auth_line2 + " --enablecache";
        }
        $("#file_auth_config_line2").text(file_auth_line2);

        // When the user clicks anywhere outside of the modal, close it
        window.onclick = function(event) {
            if (event.target == modal) {
                modal.style.display = "none";
            }
        }
    });
});
