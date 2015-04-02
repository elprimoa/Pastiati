idx=0;

$("#email-field").keypress(function(event) {
    if (event.which == 13) {
        event.preventDefault();
        login();
    }
});

$("#pass-field").keypress(function(event) {
    if (event.which == 13) {
        event.preventDefault();
        login();
    }
});

$("#exampleInputFile").change(function() {
	$(".help-block").text('File: ' + $("#exampleInputFile").val());
	console.log('File: ' + $("#exampleInputFile").val());
});

$("#sendemail").click(function () {
		var email = $("#email-field-ver").val(); 
		if(!email.match('[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,3}$')) {
			$("#email-div-ver").addClass("has-error");
			$("#email-div-ver").append('<span class="glyphicon glyphicon-remove form-control-feedback" aria-hidden="true"></span><span id="inputError2Status" class="sr-only">(error)</span>');
			return;
		}
  	$("#le-alert").addClass("in");
});

$('#close-forgot').click(function () {
  	$(this).parent().removeClass('in'); 
  	$("#forgot-form").submit();
});

function load(){
	$.getJSON("pasties.json", function(data) {
	    for(i=idx;i<idx+5;i++){
	    	id = data[i].id;
	    	$(".panel-group").append('<div class="panel panel-default"><div id="p'+id+'" class="panel-heading"><h4 id="pp' + id + '" class="panel-title">');
	    	if(data[i].private) {
	    		$("#pp"+id).append('<a data-toggle="collapse" data-parent="#accordion" href="#pastie' + data[i].id + '"> <b>'+ data[i].title +'</b>, ' + data[i].owner + '</a> <span class="glyphicon glyphicon-lock lock" aria-hidden="true"></span><br><br><i class="resumen" id="preview' + data[i].id + '">' + data[i].content.substring(0, 100) + '...</i>');
	    	}
	    	else {
	    		$("#pp"+id).append('<a data-toggle="collapse" data-parent="#accordion" href="#pastie' + data[i].id + '"> <b>'+ data[i].title +'</b>, ' + data[i].owner + '</a><br><br><i class="resumen" id="preview' + data[i].id + '">' + data[i].content.substring(0, 100) + '...</i>');
	    	}
	    	console.log($("#pp"+id));
			$('#p'+id).append('<div id="pastie'+data[i].id+'" class="panel-collapse collapse"><div id="dv' + id + '" class="panel-body">');
	        $('#dv' + id).append('<p id="dvp' + id + '">' + data[i].content + '</p><br>');
	        $('#dv' + id).append('<p><b>Owner:</b> ' + data[i].owner + '</p>');
	        $('#dv' + id).append('<p><b>URL: </b><a href="pastie.html">' + data[i].url + '</a></p>');
	    }
	    idx=idx+5;
	    $("#morePasties").blur();
	});
}

function login() {
	var memail = $("#email-field").val();
	var mpass = $("#pass-field").val();
	if(!memail.match('[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,3}$')) {
		$("#email-div").addClass("has-error");
		$("#email-div").append('<span class="glyphicon glyphicon-remove form-control-feedback" aria-hidden="true"></span><span id="inputError2Status" class="sr-only">(error)</span>');
		return;
	}
	$.ajax({
		method: 'POST', 
		url: "http://127.0.0.1:8000/login", 
		data: { email: memail, pass: mpass }
	})
	.done(function(data) {
		$("#login-form").remove();
		$("#navbar").append('<ul class="nav navbar-nav navbar-right" id="username"><li><a href="create">Crear Pastie</a></li><li class="dropdown"><a href="#" class="dropdown-toggle" data-toggle="dropdown" role="button" aria-expanded="false"><b>' + data + '</b> <span class="caret"></span></a><ul class="dropdown-menu" role="menu"><li><a href="profile">Profile</a></li><li><a href="#" onclick="logout(\'\')">Log out</a></li></ul></li></ul>');
	});
}

function logout(msj) {
	$.ajax({
		method: 'POST',
		url: "http://127.0.0.1:8000/logout"
	})
	.done(function() {
		window.location = "home";
	});
}

function loadOwn(){
	$.getJSON("pasties.json", function(data) {
	    for(i=idx;i<idx+5;i++){
	    	id = data[i].id;
	    	$(".panel-group").append('<div class="panel panel-default"><div id="p'+id+'" class="panel-heading"><h4 id="pp' + id + '" class="panel-title">');
	    	if(data[i].private) {
	    		$("#pp"+id).append('<a data-toggle="collapse" data-parent="#accordion" href="#pastie' + data[i].id + '"> <b>'+ data[i].title +' </b> </a> <span class="glyphicon glyphicon-lock lock" aria-hidden="true"></span><br><br><i class="resumen" id="preview' + data[i].id + '">' + data[i].content.substring(0, 100) + '...</i>');
	    	}
	    	else {
	    		$("#pp"+id).append('<a data-toggle="collapse" data-parent="#accordion" href="#pastie' + data[i].id + '"> <b>'+ data[i].title +' </b> </a><br><br><i class="resumen" id="preview' + data[i].id + '">' + data[i].content.substring(0, 100) + '...</i>');
	    	}
	    	console.log($("#pp"+id));
			$('#p'+id).append('<div id="pastie'+data[i].id+'" class="panel-collapse collapse"><div id="dv' + id + '" class="panel-body">');
	        $('#dv' + id).append('<p id="dvp' + id + '">' + data[i].content + '</p><br>');
	    }
	    idx=idx+5;
	    $("#morePasties").blur();
	});
}

function verifyPass(url, id) {
	var p1 = $("#Password2").val();
	var p2 = $("#Password3").val();
	if(p1 === p2) {
		if(url === "home.html") {
			return true;
		}
		else {
			$("#le-alert").addClass("in");
			$('#close-change').click(function () {
		  	$(this).parent().removeClass('in'); 
		  	return true;
			}); 
		}
	}
	else {
		$("#confirm-pass").addClass("has-error");
		$("#confirm-pass").append('<span class="glyphicon glyphicon-remove form-control-feedback" aria-hidden="true"></span><span id="inputError2Status" class="sr-only">(error)</span>');
		return false;
	}
}

function loadpastie(){
	$.getJSON("pastie.json", function(data) {

		if(data[0].private) {
			$('#mypastie').append('<h2>' + data[0].title + ' <span class="glyphicon glyphicon-lock lock" aria-hidden="true"></span> </h2>')
		}
		else {
			$('#mypastie').append('<h2>' + data[0].title + '</h2>')
		}
	    $('#mypastie').append('<h4>' + data[0].content + '</h4><br>');
	    $('#mypastie').append('<p><b>Owner:</b> ' + data[0].owner + '</p>');
	});

}
