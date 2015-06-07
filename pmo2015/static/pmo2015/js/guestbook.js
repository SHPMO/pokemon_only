function bindEvents() {
    $('#text-page').keypress(function (e){
        var code = e.keyCode;
        if (code == 13) {
            $('#page-submit').click();
        }
    });
    var ss = $('#button-submit');
    ss.click(function () {
        var mi = $('#message-input');
        var data = mi.serialize();
        ss.addClass("button-submitting");
        ss.text("提交中");
        ss.attr("disabled", "disabled");
        $.post(
            mi[0].action,
            data,
            function (data) {
                var msg;
                switch(data.error){
                    case 0:
                        msg = '留言成功'; location.replace(location.href); break;
                    case 1:
                        msg = '*为必填项目'; break;
                    case 2:
                        msg = '验证码错误'; break;
                    default:
                        msg = '未知错误';
                }
                ss.removeClass("button-submitting");
                ss.text("提交");
                ss.removeAttr("disabled");
                $('.error-message-text').text(msg);
            }
        );
    });
}

$(document).ready(bindEvents);
