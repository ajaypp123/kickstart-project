$(document).ready(function() {
    $('.install_ser_dict').hide();
    $('.install_ftp_chk').hide();
    $('.install_ftp_userpass').hide();

    $("#install_cd_rom").click(install_media1);
    $("#install_nfs").click(install_media2);
    $("#install_http").click(install_media3);
    $("#install_ftp").click(install_media4);
    $("#install_hard_drive").click(install_media5);
    $("#install_check_ftp").click(install_media6);
});

function install_media1() {
    $('.install_ser_dict').hide();
    $('.install_ftp_chk').hide();
    $('.install_ftp_userpass').hide();
}

function install_media2() {
    $('.install_ser_dict').show();
    $('.install_ftp_chk').hide();
    $('.install_ftp_userpass').hide();
	$("#install_server_label").text("NFS Server");
	$("#install_directory_label").text("NFS Directory");
}

function install_media3() {
    $('.install_ser_dict').show();
    $('.install_ftp_chk').hide();
    $('.install_ftp_userpass').hide();
	$("#install_server_label").text("HTTP Server");
	$("#install_directory_label").text("HTTP Directory");
}

function install_media4() {
    $('.install_ser_dict').show();
    $('.install_ftp_chk').show();
    $('.install_ftp_userpass').hide();
	$("#install_server_label").text("FTP Server");
	$("#install_directory_label").text("FTP Directory");
}

function install_media5() {
    $('.install_ser_dict').show();
    $('.install_ftp_chk').hide();
    $('.install_ftp_userpass').hide();
	$("#install_server_label").text("Hard Drive Partition");
	$("#install_directory_label").text("Hard Drive Directory");
}

function install_media6() {
    $('.install_ftp_userpass').toggle();
}
