function bindSubmit() {
    $("#button-submit").click(function () {
        var mi = $('#register-input');
        $.post(
            mi[0].action,
            mi.serialize(),
            function (data) {
                var x = $.parseJSON(data);
                var msg;
                switch(x.error){
                    case 0:
                        msg = '报名信息提交成功！'; mi[0].reset(); break;
                    case 1:
                        msg = '*为必填项目'; break;
                    case 2:
                        msg = 'Email已被注册'; break;
                    case 3:
                        msg = '内容超过限制'; break;
                    default:
                        msg = '未知错误';
                }
                $('#error-message-text').text(msg);
            }
        );
    });
}

$(document).ready(bindSubmit);
