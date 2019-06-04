$(function () {
    $('.captcha').click(function () {
        var p = this
        var q = this.parentElement.children[1]
        $.get('?newsn=1', function (result) {
            p.setAttribute('src', result)
            q.setAttribute('value', result.split('/')[3])
        })
    })
})
