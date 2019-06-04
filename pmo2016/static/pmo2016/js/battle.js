function bindSubmit() {
    var ss = $('#button-submit')
    ss.click(function () {
        var mi = $('#register-input')
        var data = mi.serialize()
        ss.addClass('button-submitting')
        ss.text('提交中')
        ss.attr('disabled', 'disabled')
        $.post(
            mi[0].action,
            data,
            function (data) {
                var msg
                switch (data.error) {
                    case 0:
                        msg = '报名信息提交成功！报名结果将以邮件形式发送。'
                        mi[0].reset()
                        break
                    case 1:
                        msg = '*为必填项目'
                        break
                    case 2:
                        msg = 'Email已被注册'
                        break
                    case 3:
                        msg = '内容超过限制'
                        break
                    case 4:
                        msg = '验证码错误'
                        break
                    case 5:
                        msg = 'ID号应为5位数字'
                        break
                    default:
                        msg = '未知错误'
                }
                ss.removeClass('button-submitting')
                ss.text('提交')
                ss.removeAttr('disabled')
                $('.error-message-text').text(msg)
                $('.captcha').click()
            }
        )
    })
}

$(document).ready(bindSubmit)
