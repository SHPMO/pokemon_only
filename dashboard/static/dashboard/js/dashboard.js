var closetimer = null;
var q = null;
function showSubnav() {
    if (closetimer) {
        window.clearTimeout(closetimer);
        closetimer = null;
    }
    hideAllSubnav(this);
    $(this).children(".nav-href").css({"background": "#838ba3", "color": "#ffffff"});
    $("#sub" + this.id).css({"display": "block"});
}
function hideAllSubnav() {
    $(q).children(".nav-href").css({"background": "none", "color": "#000000"});
    $(".subnav-hrefs").css({"display": "none"});
}
function hideSubnav() {
    q = this;
    closetimer = window.setTimeout(hideAllSubnav, 500);
}

$(document).ready(function () {
    var sub = document.location.pathname.split('/')[2];
    var nl = $(".nav-list");
    nl.mouseenter(showSubnav);
    nl.mouseleave(hideSubnav);
    nl.click(showSubnav);
    $('body').addClass('bg' + Math.floor(Math.random() * 3 + 1));
});
