var pmo = 'pmo2015';

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
        formData: {
            'csrfmiddlewaretoken': $.cookie('csrftoken'),
            'pmo': pmo
        },
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

var item_id = null;

function showImages() {

}
function showItem(itemid) {
    $('#item-info').removeClass('nodisplay-object');
    $('#items-input').load('?item_id='+itemid, function (data, e) {
        autoHeight();
        bindItemForm();
    });
    $('#text-number').val(arguments[1] ? arguments[1] : 0);
    item_id = itemid;
}
function deleteImage() {
    var ft = $('#file-' + this.name)
        .removeClass('image-uploaded')
        .addClass('image-deleting');
    $.post(
        $(this).children('.item-image').data('url'),
        {
            "csrfmiddlewaretoken": $.cookie('csrftoken'),
            'item_id': item_id,
            'image_id': $(this).data('image_id'),
            'method': 'delete_image',
            'pmo': pmo
        },
        function (data, e) {
            ft
                .removeClass('image-deleting');
            if (data.error!=0) {
                ft.addClass('image-uploaded');
                alert(data.message);
            } else {
                ft.css('background', 'none');
                $(this).unbind('click', deleteImage);
            }
        }
    )
}
function bindItemForm() {
    var fci = $('.item-image');
    var option = {
        dataType: 'json',
        formData: {
            "csrfmiddlewaretoken": $.cookie('csrftoken'),
            'item_id': item_id,
            'method': 'upload_image',
            'pmo': pmo
        },
        add: function(e, data) {
            if(data.originalFiles[0]['size'] > 1048576) {
                alert('请上传小于 1 MB 的图片');
            } else {
                $('#file-' + this.name).addClass('image-uploading');
                data.submit();
            }
        },
        done: function (e, data) {
            var ft = $('#file-' + this.name);
            ft.removeClass('image-uploading');
            if (data.result.error!=0) {
                alert(data.result.message);
            } else {
                ft
                    .addClass('image-uploaded')
                    .css('background-image', 'url("' + data.result.image_url + '")');
                $('#file-' + this.name + ' .image-method').click(deleteImage);
                $(this).data('image_id', data.result.image_id);
            }
        }
    };
    fci.fileupload(option);
    var ss = $("#items-submit");
    ss.click(function () {

    });
}
function bindItems() {

    var page = 1;
    $('.items-pages').click(function () {
        page += parseInt(this.value);
        $('#items-table-body').load('?page='+page);
    });

    var ia = $('#items-add');
    ia.click(function () {
        startSaving(ia, '添加中');
        $.post(
            ia.data('url'),
            {
                "csrfmiddlewaretoken": $.cookie('csrftoken'),
                'method': 'add_item',
                'pmo': pmo
            },
            function (data, e) {
                stopSaving(ia, '添加');
                if (data.error==0)
                {
                    $('#items-table-body').load('?page='+page);
                    showItem(data.item_id);
                }
                else
                    $('#items-input').text(data.message);
            }
        )
    });
    var ir = $('.item-name');
    ir.click(function () {
        $this = $(this);
        item_id = $this.data('item_id');
        if (item_id)
            showItem($this.data('item_id'), $this.prev().text());
    });
    bindItemForm();
}


$(document).ready(function () {
    bindSeller();
    bindItems();
});
