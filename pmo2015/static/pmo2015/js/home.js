function autoHeight() {
    var h = $(window).height();
    var w = $(window).width();
    $('body').height(h);
    $('#home-header').height(Math.floor(h / 2) - 271);
    $('.home-footer-side').width(Math.floor((w - 1350) / 2));
    $('#home-footer').height(Math.floor(h / 2) - 219);
    $('#home-footer-center-bottom').height(Math.floor(h / 2) - 314);
}

$(document).ready(function (){
    $(window).resize(autoHeight);
    autoHeight();
});
