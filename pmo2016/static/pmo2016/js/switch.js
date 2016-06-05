var sp;
function hashChange() {
    if (location.hash != "")
        switchContent(location.hash.substr(1));
    else
        switchContent(sp[0].id.substr(7));
}
function bindPanels() {
    location.hash = this.id.substr(7);
}
function switchContent(t) {
    var y = $(".page-current");
    var z = $("#content-" + t);
    if (z.length == 0) {
        switchContent(sp[0].id.substr(7));
        return;
    }
    var w = $(".panel-current");
    var v = $("#switch-" + t);
    y.addClass("nodisplay-object");
    y.removeClass("page-current");
    z.addClass("page-current");
    z.removeClass("nodisplay-object");
    w.removeClass("panel-current");
    v.addClass("panel-current");
}

$(document).ready(function () {
    sp = $(".switch-panel");
    sp.click(bindPanels);
    window.onhashchange = hashChange;
    hashChange();
});
