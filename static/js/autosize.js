function autoHeight() {
    $('body').height($(window).height())
}

$(document).ready(function () {
    $(window).resize(autoHeight)
    autoHeight()
})
