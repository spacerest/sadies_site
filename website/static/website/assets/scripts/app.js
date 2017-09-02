
function scrollToId(x){
	$('html, body').animate({
		scrollTop: $('#' + x).offset().top - 41
	}, 1000);
};

function expandMail() {
	$(".reply-emails").animate({height:220},300);
}

function hideMail() {
	$(".reply-emails").animate({height:0},200);

}

$(window).scroll(function() {
	var viewPortHeight = $(window).height();
	if ($(document).scrollTop() > viewPortHeight / 2) {
		$('.back-to-top').addClass('bot-show');
	} else {
		$('.back-to-top').removeClass('bot-show');
	};
});
