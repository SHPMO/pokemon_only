function bindPanels() {
    $(".switch-panel").click(function (){
        var y = $(".page-current");
        var z = $("#content-p" + this.id[this.id.length-1]);
        y.addClass("nodisplay-object");
        y.removeClass("page-current");
        z.addClass("page-current");
        z.removeClass("nodisplay-object");
        autoHeight();
    })
}

$(document).ready(bindPanels);
