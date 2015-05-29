function bindSeller() {
    var ss = $('#seller-submit');
    ss.click(function () {
        var mi = $('#seller-input');
        var data = mi.serialize();
        ss.addClass("button-submitting");
        ss.text("保存中");
        ss.attr("disabled", "disabled");
        $.post(
            mi[0].action,
            data,
            function (data) {
                var msg = data.message;
                ss.removeClass("button-submitting");
                ss.text("保存");
                ss.removeAttr("disabled");
                $('#error-information').text(msg);
            }
        );
    });
    var fci = $('#file-circle_image');
    var option = {
        dataType: 'json',
        formData: {'csrfmiddlewaretoken': $('[name=csrfmiddlewaretoken]')[0].value},
        done: function (e, data) {
            $('#image-circle_image').attr('src', data.result.circle_image_url);
            $('#error-upload-circle_image').text(data.result.message);
        }
    };
    fci.fileupload(option);
    $('#file-upload').click(function () {
        fci.click();
    });
}

$(document).ready(function () {
    bindSeller();
});
