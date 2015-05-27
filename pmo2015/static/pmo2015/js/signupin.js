function bindSubmit() {
    $("#signup-submit").click(function () {
        var mi = $('#signup-input');
        $.post(
            mi[0].action,
            mi.serialize(),
            function (data) {
//                var x = $.parseJSON(data);
                var msg;
                switch(data.error){
                    case 0:
                        $(".content-page").addClass("nodisplay-object");
                        $(".switch-panel").addClass("nodisplay-object");
                        msg = data.message;
                        break;
                    case 1:
                        if(data.message.captcha[0] == "Invalid CAPTCHA")
                            msg = "验证码错误";
                        else
                            msg = "*为必填项";
                        break;
                    default:
                        msg = data.message;
                }
                $('#error-message-text').text(msg);
                $(".captcha").click();
            }
        );
    });
    $(".captcha").click(function(){
        var p = this;
        var q = this.parentElement.children[1];
        $.get("?newsn=1", function(result){
            p.setAttribute("src", result);
            q.setAttribute("value", result.split('/')[3]);
        });
    });
}

$(document).ready(bindSubmit);
