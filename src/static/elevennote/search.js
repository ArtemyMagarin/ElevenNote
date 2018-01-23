$(function() {
	$("#search").on("input", search)
})


var search = function() {
	query = $("#search").val();
	url = query?"/notes/search/"+query+"/":"/notes/notes/"

	$.ajax({
		url: url
	})
	.done((data)=>{
		$("#notes").html(data)
	})
}