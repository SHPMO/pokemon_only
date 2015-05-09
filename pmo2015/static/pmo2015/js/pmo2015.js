function autoheight() {
    var h = $(window).height();
    $("#main-container").css({"min-height": h});
    $("#sub-container").css({"min-height": h - 120});
    $("#main-content").css({"min-height": h - 260});
    $("#sub-content").css({"height": $("#sub-container").height() - 500})
}

$(document).ready(function (){
    var sub = document.location.pathname.split('/')[2];
    $("#nav-"+ sub +" a").css({"color":"#ffffff","background":"#838ba3"});
    $(window).resize(autoheight);
    autoheight();
});
