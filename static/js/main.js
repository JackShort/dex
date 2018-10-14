document.addEventListener('DOMContentLoaded', function() {
	var errors = document.getElementsByClassName("errorlist");
	for (var i = 0; i < errors.length; i++) {
		errors[i].className += " alert alert-warning";
	}
});
