
$(document).ready(function(){
    $("select.firewall_sequrity_level").change(function(){
        var firewall_sequrity_status = $("#firewall_sequrity_level").val();

		if(firewall_sequrity_status == "Disable_firewall"){
			$('#firewall_trusted_service_config').hide();
		}
		if(firewall_sequrity_status == "Enable_firewall"){
			$('#firewall_trusted_service_config').show();
		}
    });
});

