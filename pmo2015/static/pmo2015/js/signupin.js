function bindSubmit() {
    var emt = $('.error-message-text');
    var ss = $("#signup-submit");
    ss.click(function () {
        var mi = $('#signup-input');
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
                        $(".content-page").addClass("nodisplay-object");
                        $(".switch-panel").addClass("nodisplay-object");
                        msg = data.message;
                        break;
                    case 1:
                        if(data.message.captcha!=undefined)
                            msg = "验证码错误";
                        else if(data.message.password!=undefined)
                            msg = "密码至少需要6位";
                        else
                            msg = "*为必填项";
                        break;
                    default:
                        msg = data.message;
                }
                ss.removeClass("button-submitting");
                ss.text("提交");
                ss.removeAttr("disabled");
                emt.html(msg);
                $(".captcha").click();
            }
        );
    });
    var ls = $("#login-submit");
    ls.click(function () {
        var mi = $('#login-input');
        var data = mi.serialize();
        ls.addClass("button-submitting");
        ls.text("提交中");
        ls.attr("disabled", "disabled");
        $.post(
            mi[0].action,
            data,
            function (data) {
                var msg;
                switch(data.error){
                    case 0:
                        $(".content-page").addClass("nodisplay-object");
                        $(".switch-panel").addClass("nodisplay-object");
                        emt.html(data.message);
                        location.href = data.redirect_to;
                        break;
                    case 1:
                        if(data.message.captcha!=undefined)
                            msg = "验证码错误";
                        else if(data.message.email!=undefined)
                            msg = "请输入正确的邮箱地址";
                        else
                            msg = "所有项目不能为空";
                        break;
                    default:
                        msg = data.message;
                }
                ls.removeClass("button-submitting");
                ls.text("提交");
                ls.removeAttr("disabled");
                emt.html(msg);
                $(".captcha").click();
            }
        );
    });
}

function bindOthers() {
    $(".captcha").click(function() {
        var p = this;
        var q = this.parentElement.children[1];
        $.get("?newsn=1", function(result){
            p.setAttribute("src", result);
            q.setAttribute("value", result.split('/')[3]);
        });
    });
    $(".switch-panel").click(function() {
        $('#error-message-text').empty();
    })
}

$(document).ready(function () {
    bindSubmit();
    bindOthers();
});
