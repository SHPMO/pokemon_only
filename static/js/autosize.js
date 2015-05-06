function autoheight() {
    $('body').height($(window).height());
}

$(document).ready(function (){
    $(window).resize(autoheight);
    autoheight();
});
