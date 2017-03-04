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

        //file logic (installation)
        var install_ser = document.getElementById('install_source_server').value;
        var install_dict = document.getElementById('install_source_dict').value;
        var install_user = document.getElementById('install_ftp_user').value;
        var install_pass = document.getElementById('install_ftp_pass').value;

        if (document.getElementById("install_new_install").checked == true) {
            var file_installation_line1 = "# Install OS instead of upgrade";
            var file_installation_line2 = "install";
        }
        if (document.getElementById("install_upgrade_install").checked == true) {
            var file_installation_line1 = "# Upgrade existing installation";
            var file_installation_line2 = "upgrade";
        }
        if (document.getElementById("install_cd_rom").checked == true) {
            var file_installation_line3 = "# Use CDROM installation media";
            var file_installation_line4 = "cdrom";
        }
        if (document.getElementById("install_nfs").checked == true) {
            var file_installation_line3 = "# Use NFS installation media";
            var file_installation_line4 = "nfs --server=" + install_ser + " --dir=" +
                install_dict;
        }
        if (document.getElementById("install_http").checked == true) {
            var file_installation_line3 = "# Use network installation";
            var file_installation_line4 = "url --url=\"http://" + install_ser + "/" +
                install_dict + "\"";
        }
        if (document.getElementById("install_ftp").checked == true) {
            var file_installation_line3 = "# Use network installation";
            if (document.getElementById("install_check_ftp").checked == true) {
                var file_installation_line4 = "url --url=\"ftp://" + install_user + ":" +
                    install_pass + "@" + install_ser + "/" + install_dict + "\"";
            }
            else {
                var file_installation_line4 = "url --url=\"ftp://" + install_ser + "/" +
                    install_dict + "\"";
            }
        }
        if (document.getElementById("install_hard_drive").checked == true) {
            var file_installation_line3 = "# Use hard drive installation media";
            var file_installation_line4 = "harddrive --dir=" + install_ser + " --partition=" +
                install_dict;
        }
        $("#file_installation_line1").text(file_installation_line1);
        $("#file_installation_line2").text(file_installation_line2);
        $("#file_installation_line3").text(file_installation_line3);
        $("#file_installation_line4").text(file_installation_line4);

        // When the user clicks anywhere outside of the modal, close it
        window.onclick = function(event) {
            if (event.target == modal) {
                modal.style.display = "none";
            }
        }
    });
});
