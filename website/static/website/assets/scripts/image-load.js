function hideUri(element_id, new_background_url) {
    var blurry_slide = document.getElementById(element_id);
    blurry_slide.style.backgroundImage = 'url(' + new_background_url + ')';
    blurry_slide.classList.remove("blurme");
}
