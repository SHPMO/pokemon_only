function bindPages() {
    $("#text-page").keypress(function (e){
        var code = e.keyCode;
        if (code == 13) {
            window.location = ".?page=" + this.value;
        }
    });
}

$(document).ready(bindPages);
