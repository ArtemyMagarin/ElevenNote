var getNoteView = function(pk) {
	$.ajax({
	  async: true,
	  url: "/notes/"+pk+"/",
	  method: "get",
	})
	  .done(function( data ) {
	    $('#note-body').html(data)
	  })
	  .fail(function() {
	    $('#note-body').html("<p>Error</p>")
	  });
}

var select = function(self) {
	$("#notes li").each((a, b)=>{
		$(b).removeClass("selected")
	})
	$(self).addClass("selected")
}

var delete_ = function(pk) {
	$.ajax({
	  async: true,
	  url: "/notes/"+pk+"/delete/",
	  method: "post",
	  data: {
	  	"csrfmiddlewaretoken": getCookie('csrftoken'),
	  },
	})
	  .done(function( data ) {
	    $("#notes li.selected").remove();
	    $("#note-body").html('<br><br><br><br><br><br><br><div class="create_btn" onclick="create_()"><a href="#" class="text"><i class="fa fa-plus-circle fa-5x" aria-hidden="true"></i></a><br><a href="#" class="text">Create a new note!</a></div>');
	})

	$.ajax({
	  async: false,
	  url: "/notes/notes/",
	  method: "get",
	})
	  .done(function( data ) {
	    $('#noteslist').html(data)
	    if (pk) {
	    	console.log(pk);
		    $('#noteslist #note_'+pk).addClass("selected");
		};
	  })
}

var close_ = function(pk) {
    $("#notes li.selected").removeClass("selected");
    $("#note-body").html('<br><br><br><br><br><br><br><div class="create_btn" onclick="create_()"><a href="#" class="text"><i class="fa fa-plus-circle fa-5x" aria-hidden="true"></i></a><br><a href="#" class="text">Create a new note!</a></div>');
}

var edit_ = function(pk) {
	$.ajax({
	  async: true,
	  url: "/notes/"+pk+"/edit/",
	  method: "get",
	})
	  .done(function( data ) {
	    $('#note-body').html(data)
	  })
	  .fail(function() {
	    $('#note-body').html("<p>Error</p>")
	  });
}

var save_ = function(pk) {
	$('textarea').each(function () {
	   var $textarea = $(this);
	   $textarea.val(CKEDITOR.instances['id_'+$textarea.attr('name')].getData());
	});

	data = $('#data').serializeArray().reduce(function(obj, item) {
			    obj[item.name] = item.value;
			    return obj;
			}, {});

	$.ajax({
	  async: false,
	  url: "/notes/"+pk+"/edit/",
	  method: "post",
	  data: data,
	})
	  .done(function( data ) {
	    $('#note-body').html(data);
	    console.log('pk ', pk, 'from save_ .done');
	  })
	  .fail(function() {
	    $('#note-body').html("<p>Error</p>")
	  });

	$.ajax({
	  async: false,
	  url: "/notes/notes/",
	  method: "get",
	})
	  .done(function( data ) {
	    $('#noteslist').html(data);
	    if (pk) {
	    	console.log(pk);
		    $('#noteslist #note_'+pk).addClass("selected");
		    $("#noteslist").scrollTop(0);
		};
	  })
}


var save_new_ = function() {
	$('textarea').each(function () {
	   var $textarea = $(this);
	   $textarea.val(CKEDITOR.instances['id_'+$textarea.attr('name')].getData());
	});	

	data = $('#data').serializeArray().reduce(function(obj, item) {
			    obj[item.name] = item.value;
			    return obj;
			}, {});

	let pk = '';

	$.ajax({
	  async: false,
	  url: "/notes/new/",
	  method: "post",
	  data: data,
	})
	  .done(function( data ) {
	    $('#note-body').html(data);
	    pk = $('#note-body #note_id').val();
	    console.log('pk ', pk, ' from save new');
	    
	  })
	  .fail(function() {
	    $('#note-body').html("<p>Error</p>")
	  });

	$.ajax({
	  async: false,
	  url: "/notes/notes/",
	  method: "get",
	})
	  .done(function( data ) {
	    $('#noteslist').html(data)
	    if (pk) {
	    	console.log(pk);
		    $('#noteslist #note_'+pk).addClass("selected");
		    $("#noteslist").scrollTop(0);
		};
	  })
}

var create_ = function() {
	data = $('#data').serializeArray().reduce(function(obj, item) {
			    obj[item.name] = item.value;
			    return obj;
			}, {});

	var pk = '';

	$.ajax({
	  async: false,
	  url: "/notes/new/",
	  method: "get",
	  data: data,
	})
	  .done(function( data ) {
	    $('#note-body').html(data);
	    pk = $('#note-body #note_id').val();
	  })
	  .fail(function() {
	    $('#note-body').html("<p>Error</p>")
	  });

	$.ajax({
	  async: false,
	  url: "/notes/notes/",
	  method: "get",
	})
	  .done(function( data ) {
	    $('#noteslist').html(data)
	    if (pk) {
	    	console.log(pk);
		    $('#noteslist #note_'+pk).addClass("selected");
		    $("#noteslist").scrollTop(0);
		};
	  })
}

