var deleteTag = function(e) {
	console.log(e.target)
} 

var addTag = function(target, pk) {
	console.log(target, pk)
	var data = [];

	// getting tags from bd
	$.ajax({
		url: "/tags/",
	})
	.done((d)=>{

		data = JSON.parse(d.replace(/\s/ig, '').replace(/\,\]$/ig, ']'))
		var options = {};
		var dataSet = {
		    source: substringMatcher(data)
		};
/*
		<div class="input-group">
	      <input type="text" class="form-control" placeholder="Search for...">
	      <span class="input-group-btn">
	        <button class="btn btn-secondary" type="button">Go!</button>
	      </span>
	    </div>
*/


	
		div = $("<div>").addClass("input-group");
		input = $("<input>").addClass("typeahead form-control").attr("id", "tag").attr("data-pk", pk).css("width", "180px")
		span = $('<span>').addClass("input-group-btn");
		button = $("<button>").addClass("btn btn-success").attr("onclick", "sendTag(this)").text("Add")
		
		$(span).append($(button));
		$(div).append($(input))
		$(div).append($(span))

		$(target).before($(div))
		$(target).css('display', 'none')
		$('.typeahead').typeahead(options, dataSet);
		$('.twitter-typeahead').css("width", "180px")

	})	
	
}

var sendTag = function(target) {
	tag = $("#tag").val()
	pk = $("#tag").attr("data-pk");
	$.ajax({
		url: "/notes/"+pk+"/"+tag+"/",
		method: "post",
		data: {
	  	"csrfmiddlewaretoken": getCookie('csrftoken'),
	  },
	})
	.done((d)=>{
		console.log($("#tags"));
		$("#tags span").first().before($("<span>").addClass("badge badge-pill badge-success").html(tag+' | <a href="#" class="deleteTagLink" onclick="deleteTag(this)">x</a>'));
		$("#tag").remove();
		$(target).remove();
		$("#tags a[display=none]").css("display", "inline")
	})
}


var deleteTag = function(target) {
	span = $(target).parent();
	tag = $(span).text().match(/\w+/)[0];
	pk = $("#note_id").val();

	$.ajax({
		url: "/notes/"+pk+"/"+tag+"/delete/",
		method: "post",
		data: {
	  	"csrfmiddlewaretoken": getCookie('csrftoken'),
	  },
	})
	.done((d)=>{
		$(span).remove()
	})
}