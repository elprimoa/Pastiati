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
	        $('#dv' + id).append('<p>' + data[i].content + '</p><br>');
	        $('#dv' + id).append('<p><b>Owner:</b> ' + data[i].owner + '</p>');
	        
	    }
	    idx=idx+5;
	    $("#morePasties").blur();
	});
}
