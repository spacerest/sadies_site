
function scrollToId(x){
	$('html, body').animate({
		scrollTop: $('#' + x).offset().top - 41
	}, 1000);
};


