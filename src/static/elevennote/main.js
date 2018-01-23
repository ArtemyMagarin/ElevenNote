(function($) { $(function() {
    // allow whole list item to note to be clickable
    // $("#notes li").click(function(){
    //     location.assign($(this).attr("data-url"));
    // });
    
    // add Title placeholder
    $("#id_title").attr("placeholder", "Title your note");
    
    // set sidebar height
    $('#sidebar').css("height", window.innerHeight - 55 );


    $(document).ready(function(){
       $("#delete-note").click(function(e){
            e.preventDefault();
            if (window.confirm("Are you sure?")) {
               $("#delete-note-form").submit();
           }
       });
    });

}); })(jQuery);


// for getting csrf token
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
