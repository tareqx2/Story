$(document).ready(function(){
	$.ajax({
	  url: "http://story-generator.herokuapp.com/api/v1.0/story"
	})
	.done(function(html){
		var json = jQuery.parseJSON(html);
		var description = $('.description');
		description[0].textContent = json["description"];
	});
});