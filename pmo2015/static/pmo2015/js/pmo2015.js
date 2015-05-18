function autoHeight() {
    var h = $(window).height();
    var mc = $("#main-container");
    mc.css({"min-height": h - 74});
    var sc = $("#sub-container");
    var mc2 = $("#main-content");
    sc.css({"min-height": h - 110});
    mc2.css({"min-height": h - 280});
    sc.css({"height": mc2.height() + 170});
    mc.css({"height": sc.height() + 36});
    $("#sub-content").css({"height": sc.height() - 500})
}


var closetimer = null;
var q = null;
function showSubnav() {
    if (closetimer) {
        window.clearTimeout(closetimer);
        closetimer = null;
    }
    hideAllSubnav(this);
    $(this).children(".nav-href").css({"background": "#838ba3", "color": "#ffffff"});
    $("#sub"+this.id).css({"display": "block"});
}
function hideAllSubnav() {
    $(q).children(".nav-href").css({"background": "none", "color": "#000000"});
    $(".subnav-hrefs").css({"display": "none"});
}
function hideSubnav() {
    q = this;
    closetimer = window.setTimeout(hideAllSubnav, 500);
}

$(document).ready(function (){
    var sub = document.location.pathname.split('/')[2];
    $(window).resize(autoHeight);
    var nl = $(".nav-list");
    nl.mouseenter(showSubnav);
    nl.mouseleave(hideSubnav);
    nl.click(showSubnav);
    autoHeight();
});
