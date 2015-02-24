idx=0;

function load(){
	$.getJSON("pasties.json", function(data) {
	    for(i=idx;i<idx+5;i++){
	    	id = data[i].id;
	    	$(".panel-group").append('<div class="panel panel-default"><div id="p'+id+'" class="panel-heading"><h4 id="pp' + id + '" class="panel-title">');
	    	if(data[i].private) {
	    		$("#pp"+id).append('<a data-toggle="collapse" data-parent="#accordion" href="#pastie' + data[i].id + '"> <b>'+ data[i].title +'</b>, ' + data[i].owner + '</a> <img src="media/lock.png"/><br><br><i class="resumen" id="preview' + data[i].id + '">' + data[i].content.substring(0, 100) + '...</i>');
	    	}
	    	else {
	    		$("#pp"+id).append('<a data-toggle="collapse" data-parent="#accordion" href="#pastie' + data[i].id + '"> <b>'+ data[i].title +'</b>, ' + data[i].owner + '</a><br><br><i class="resumen" id="preview' + data[i].id + '">' + data[i].content.substring(0, 100) + '...</i>');
	    	}
	    	console.log($("#pp"+id));
			$('#p'+id).append('<div id="pastie'+data[i].id+'" class="panel-collapse collapse"><div id="dv' + id + '" class="panel-body">');
	        $('#dv' + id).append('<p id="dvp' + id + '">' + data[i].content + '</p><br>');
	        $('#dv' + id).append('<p><b>Owner:</b> ' + data[i].owner + '</p>');
	    }
	    idx=idx+5;
	    $("#morePasties").blur();
	});
}

function login() {
	var email = $("#email-field").val();
	$("#login-form").remove();
	$("#navbar").append('<ul class="nav navbar-nav navbar-right" id="username"><li class="dropdown"><a href="#" class="dropdown-toggle" data-toggle="dropdown" role="button" aria-expanded="false"><b>' + email + '</b> <span class="caret"></span></a><ul class="dropdown-menu" role="menu"><li><a href="#">Crear Pastie</a></li><li><a href="#">Perfil</a></li><li><a href="#" onclick="logout()">Log out</a></li></ul></li></ul>');
}

function logout() {
	$("#username").remove();
	$("#navbar").append('<form class="navbar-form navbar-right" id="login-form"><div class="form-group"><input type="text" placeholder="Email" class="form-control" id="email-field"> </div> <div class="form-group"> <input type="password" placeholder="Password" class="form-control" id="pass-field"> </div> <button type="button" class="btn btn-success" onclick="login()">Log in</button></form>');
}
