$(document).ready(function() {
    $('#auth_nis_block').hide();
    $('#auth_ldap_block').hide();
    $('#auth_krb_block').hide();
    $('#auth_smb_block').hide();
    $("#auth_ldap_cert_url_label").hide();
    $("#auth_ldap_cert_url").hide();

    $("#auth_enable_nis").click(auth_config1);
    $("#auth_enable_ldap").click(auth_config2);
    $("#auth_enable_krb5").click(auth_config3);
    $("#auth_enable_smb").click(auth_config4);
});

function auth_config1() {
    $('#auth_nis_block').toggle();
    $("#auth_broadcast_nis").click(function(){
    	$("#auth_nis_server_label").toggle();
    	$("#auth_nis_server").toggle();
	});
}

function auth_config2() {
    $('#auth_ldap_block').toggle();
    $("#auth_ldap_certificate").click(function(){
    	$("#auth_ldap_cert_url_label").toggle();
    	$("#auth_ldap_cert_url").toggle();
	});
}


function auth_config3() {
    $('#auth_krb_block').toggle();
}

function auth_config4() {
    $('#auth_smb_block').toggle();
}

