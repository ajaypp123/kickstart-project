$(document).ready(function() {
    $("#preview_all").click(function() {

        // Get the modal
        var modal = document.getElementById('myModal');

        // Get the button that opens the modal
        var btn = document.getElementById("preview_all");

        // Get the <span> element that closes the modal
        var span = document.getElementsByClassName("close")[0];

        // When the user clicks the button, open the modal
      /*  btn.onclick = function() */{
            modal.style.display = "block";
        }

        // When the user clicks on <span> (x), close the modal
        span.onclick = function() {
            modal.style.display = "none";
        }

	//file logic
	var firewall_selinux_state = document.getElementById('firewall_selinux_state').value ;
	var firewall_sequrity_level = document.getElementById('firewall_sequrity_level').value ;
	if(firewall_sequrity_level == "Disable_firewall"){
		firewall_sequrity_level = "firewall --disabled" ;

	}
	if(firewall_sequrity_level == "Enable_firewall"){
		firewall_sequrity_level = "firewall --enabled" ;
		if(document.getElementById("firewall_http_service").checked == true){
			firewall_sequrity_level = firewall_sequrity_level + " --http";
		}
		if(document.getElementById("firewall_ftp_service").checked == true){
			firewall_sequrity_level = firewall_sequrity_level + " --ftp";
		}
		if(document.getElementById("firewall_ssh_service").checked == true){
			firewall_sequrity_level = firewall_sequrity_level + " --ssh";
		}
		if(document.getElementById("firewall_telnet_service").checked == true){
			firewall_sequrity_level = firewall_sequrity_level + " --telnet";
		}
		if(document.getElementById("firewall_mail_service").checked == true){
			firewall_sequrity_level = firewall_sequrity_level + " --smtp";
		}
		if(document.getElementById("firewall_other_port").value != ""){
			var port_data = document.getElementById("firewall_other_port").value;
			firewall_sequrity_level = firewall_sequrity_level + " --port=" + port_data;
		}
	}
	$("#file_firewall_line1").text("# SELinux configuration");
	$("#file_firewall_line2").text(firewall_selinux_state);
	$("#file_firewall_line3").text("# Firewall configuration");
	$("#file_firewall_line4").text(firewall_sequrity_level);

        // When the user clicks anywhere outside of the modal, close it
        window.onclick = function(event) {
            if (event.target == modal) {
                modal.style.display = "none";
            }
        }
    });
});
