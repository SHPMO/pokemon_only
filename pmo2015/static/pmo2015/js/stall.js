function testRequired(mi) {
    var a = true;
    mi.find('input').each(function(){
        if($(this).prop('required') && !this.value){
            a = false;
        }
    });
    return a;
}
function startSaving(ss) {
    ss.addClass("button-submitting");
    ss.text(arguments[1] ? arguments[1] : "保存中");
    ss.attr("disabled", "disabled");
}
function stopSaving(ss) {
    ss.removeClass("button-submitting");
    ss.text(arguments[1] ? arguments[1] : "保存");
    ss.removeAttr("disabled");
}

function bindSeller() {
    var ss = $('#seller-submit');
    ss.click(function () {
        var mi = $('#seller-input');
        var data = mi.serialize();
        startSaving(ss);
        if(!testRequired(mi)) {
            $('#error-information').text("*为必填项");
            stopSaving(ss);
            return
        }
        $.post(
            mi[0].action,
            data,
            function (data) {
                var msg = data.message;
                stopSaving(ss);
                $('#error-information').text(msg);
            }
        );
    });
    var fci = $('#file-circle_image');
    var option = {
        dataType: 'json',
        formData: {'csrfmiddlewaretoken': $.cookie('csrftoken')},
        add: function(e, data) {
            if(data.originalFiles[0]['size'] > 1048576) {
                $('#error-upload-circle_image').text("请上传小于 1 MB 的图片");
            } else {
                data.submit();
            }
        },
        done: function (e, data) {
            $('#image-circle_image').attr('src', data.result.circle_image_url);
            $('#error-upload-circle_image').text(data.result.message);
        }
    };
    fci.fileupload(option);
}

function bindItems() {
    var ss = $("#items-input");
    var fci = $('#file-circle_image');
    var option = {
        dataType: 'json',
        formData: {'csrfmiddlewaretoken': $.cookie('csrftoken')},
        add: function(e, data) {
            if(data.originalFiles[0]['size'] > 1048576) {
                $('#error-upload-circle_image').text("请上传小于 1 MB 的图片");
            } else {
                data.submit();
            }
        },
        done: function (e, data) {
            $('#image-circle_image').attr('src', data.result.circle_image_url);
            $('#error-upload-circle_image').text(data.result.message);
        }
    };
    fci.fileupload(option);
}


$(document).ready(function () {
    bindSeller();
    bindItems();
});
