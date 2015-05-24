function autoHeight() {
    var h = $(window).height();
    var w = $(window).width();
    var ph = Math.floor(h / 2) + 179.5;
    var body = $('#home-body');
    body.height(h);
    body.width(w);
//    $('#home-header').height(Math.floor(h / 2) - 271);
    $('#home-main-container').height(ph);
    var qh = ph - 506;
    if (qh<0) qh = 0;
    $('#home-content').css({"top": qh});
    $('.home-footer-side').width(Math.round((w - 1280) / 2));
    $('#home-footer').height(ph - 405);
    $('#home-footer-center-bottom').height(ph - 500);
}

$(document).ready(function (){
    $(window).resize(autoHeight);
    autoHeight();
});
