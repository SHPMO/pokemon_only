function bindSeller() {
    var ss = $('#seller-submit');
    ss.click(function () {

    });
    var fci = $('#file-circle_image');
    fci.fileupload({
        dataType: 'json',
        formData: {'csrfmiddlewaretoken': $('[name=csrfmiddlewaretoken]')[0].value},
        done: function (e, data) {
            var result = data.response().result;
            $('#image-circle_image').attr('src', result.circle_image_url);
            $('#error-upload-circle_image').text(result.message);
        }
    });
    $('#file-upload').click(function () {
        fci.click();
    });
}

$(document).ready(function () {
    bindSeller();
});
