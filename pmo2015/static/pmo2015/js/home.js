function autoHeight() {
    var h = $(window).height();
    $('body').height(h);
    $('#home-header').height(h / 2 - 271);
}

$(document).ready(function (){
    $(window).resize(autoHeight);
    autoHeight();
});
