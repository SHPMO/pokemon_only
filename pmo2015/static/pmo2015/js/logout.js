function bindLogout() {
    var ss = $('#logout-button')
    ss.click(function () {
        ss.addClass('button-submitting')
        ss.text('注销中')
        ss.attr('disabled', 'disabled')
        $.get(
            ss.data('url'),
            function (data, status) {
                switch (data.error) {
                    case 0:
                        location.href = '../signupin/?validated=2'
                        break
                }
                ss.removeClass('button-submitting')
                ss.text('注销')
                ss.removeAttr('disabled')
            }
        )
    })
}

$(document).ready(function () {
    bindLogout()
})
