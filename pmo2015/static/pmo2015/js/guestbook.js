function bindPages() {
    $("#text-page").keypress(function (e){
        var code = e.keyCode;
        if (code == 13) {
            window.location = ".?page=" + this.value;
        }
    });
    $("#button-submit").click(function () {
        var mi = $('#message-input');
        $.post(mi[0].action,
            mi.serialize(),
            function (data) {
                var x = $.parseJSON(data);
                var msg;
                switch(x.error){
                    case 0:
                        msg = '留言成功'; mi[0].reset(); break;
                    case 1:
                        msg = '*为必填项目';break;
                    default:
                        msg = '未知错误';
                }
                $('#error-message-text').text(msg);
            }
        );
    }

    )
}

$(document).ready(bindPages);
