idx=0;

function load(){
	$.getJSON("pasties.json", function(data) {
	    for(i=idx;i<idx+5;i++){
	    	id = data[i].id;
	    	$(".panel-group").append('<div class="panel panel-default"><div id="p'+id+'" class="panel-heading"><h4 id="pp' + id + '" class="panel-title">');
	    	$("#pp"+id).append('<a data-toggle="collapse" data-parent="#accordion" href="#pastie' + data[i].id + '"><h3>'+ data[i].title +'</h3></a>');
	    	console.log($("#pp"+id));
			$('#p'+id).append('<div id="pastie'+data[i].id+'" class="panel-collapse collapse"><div id="dv' + id + '" class="panel-body">');
	        $('#dv' + id).append('<p>' + data[i].content + '</p><br>');
	        $('#dv' + id).append('<p>Owner: ' + data[i].owner + '</p>');
	        $('#dv' + id).append('<p>Private: ' + data[i].private + '</p>');
	    }
	    idx=idx+5;
	});
}
