var getNoteView = function(url) {
	$.ajax({
	  async: true,
	  url: url,
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
	    $("#note-body").html("")
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
	  async: true,
	  url: "/notes/"+pk+"/edit/",
	  method: "post",
	  data: data,
	})
	  .done(function( data ) {
	    $('#note-body').html(data)
	  })
	  .fail(function() {
	    $('#note-body').html("<p>Error</p>")
	  });

	$.ajax({
	  async: true,
	  url: "/notes/notes/",
	  method: "get",
	})
	  .done(function( data ) {
	    $('#noteslist').html(data)
	  })
}


var save_new_ = function(pk) {
	$('textarea').each(function () {
	   var $textarea = $(this);
	   $textarea.val(CKEDITOR.instances['id_'+$textarea.attr('name')].getData());
	});	

	data = $('#data').serializeArray().reduce(function(obj, item) {
			    obj[item.name] = item.value;
			    return obj;
			}, {});
	$.ajax({
	  async: true,
	  url: "/notes/new/",
	  method: "post",
	  data: data,
	})
	  .done(function( data ) {
	    $('#note-body').html(data)
	  })
	  .fail(function() {
	    $('#note-body').html("<p>Error</p>")
	  });

	$.ajax({
	  async: true,
	  url: "/notes/notes/",
	  method: "get",
	})
	  .done(function( data ) {
	    $('#noteslist').html(data)
	  })
}

var create_ = function() {
	data = $('#data').serializeArray().reduce(function(obj, item) {
			    obj[item.name] = item.value;
			    return obj;
			}, {});
	$.ajax({
	  async: true,
	  url: "/notes/new/",
	  method: "get",
	  data: data,
	})
	  .done(function( data ) {
	    $('#note-body').html(data);
	  })
	  .fail(function() {
	    $('#note-body').html("<p>Error</p>")
	  });
}

// using jQuery
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
