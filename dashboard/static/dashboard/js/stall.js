var pmo = 'pmo2019'
var csrftoken = $.cookie('csrftoken')

function testRequired(mi) {
    var a = true
    mi.find('input').each(function () {
        if ($(this).prop('required') && !this.value) {
            a = false
        }
    })
    return a
}

function showError(page, msg) {
    $('body').animate({
        scrollTop: $('#error-' + page).html(msg).offset().top - 10
    })
}

function clearError(page) {
    $('#error-' + page).empty()
}

function startSaving(ss) {
    ss.addClass('button-submitting')
    ss.text(arguments[1] ? arguments[1] : '保存中')
    ss.attr('disabled', 'disabled')
}

function stopSaving(ss) {
    ss.removeClass('button-submitting')
    ss.text(arguments[1] ? arguments[1] : '保存')
    ss.removeAttr('disabled')
}

function bindNotice() {
    var cb = $('#cancel-button')
    var obj_url = cb.data('url')
    cb.click(function () {
        if (!confirm('您确定要撤销申请吗？'))
            return
        var name = cb.text()
        startSaving(cb, '撤销中')
        clearError('notice')
        $.post(
            obj_url, {
                'csrfmiddlewaretoken': csrftoken,
                'pmo': pmo
            },
            function (data, e) {
                stopSaving(cb, name)
                showError('notice', data.message)
                if (data.error == 0) {
                    location.href = '.'
                }
            }
        )
    })

}

var seller_edited = false

function bindSeller() {
    var ss = $('#seller-submit')
    var mi = $('#seller-input')
    mi.find('.form-control').change(function () {
        seller_edited = true
    })

    ss.click(function () {
        var data = mi.serialize()
        startSaving(ss)
        clearError('information')
        if (!seller_edited) {
            showError('information', '没有更改')
            stopSaving(ss)
            return
        }
        if (!testRequired(mi)) {
            showError('information', '*为必填项')
            stopSaving(ss)
            return
        }
        $.post(
            mi[0].action,
            data,
            function (data, e) {
                stopSaving(ss)
                showError('information', data.message)
                if (data.error == 0) {
                    seller_edited = false
                }
            }
        )
    })
    var fci = $('#file-circle_image')
    var fu = $('#file-upload')
    var option = {
        dataType: 'json',
        formData: {
            'csrfmiddlewaretoken': csrftoken,
            'pmo': pmo
        },
        add: function (e, data) {
            if (data.originalFiles[0]['size'] > 1048576) {
                $('#error-upload-circle_image').text('请上传小于 1 MB 的图片')
            } else {
                data.submit()
            }
            startSaving(fu, '上传中')
        },
        done: function (e, data) {
            stopSaving(fu, '上传文件')
            $('#image-circle_image').attr('src', data.result.circle_image_url)
            $('#error-upload-circle_image').text(data.result.message)
        }
    }
    fci.fileupload(option)
}

var item_id = null
var item_url = null
var item_edited = false

function showItem(itemid, number) {
    $('#item-info').removeClass('nodisplay-object')
    $('#items-input').load('?item_id=' + itemid, function (data, e) {
        item_edited = false
        bindItemForm()
        clearError('items')
        autoHeight()
    })
    $('#text-number').val(number)
    item_id = itemid
}

function deleteImage() {
    var $ii = $(this).children('.item-image')
    var ft = $('#file-' + $ii[0].name)
        .removeClass('image-uploaded')
        .addClass('image-deleting')
    $(this).unbind('click', deleteImage)
    $.post(
        item_url,
        {
            'csrfmiddlewaretoken': csrftoken,
            'item_id': item_id,
            'image_id': $ii.data('image_id'),
            'method': 'delete_image',
            'pmo': pmo
        },
        function (data, e) {
            ft.removeClass('image-deleting')
            if (data.error != 0) {
                ft.addClass('image-uploaded')
                $(this).click(deleteImage)
                alert(data.message)
            } else {
                ft.css('background', 'none')
            }
        }
    )
}

function itemSubmit() {
    var $this = $(this)
    var ii = $('#items-input')
    var data = ii.serialize()
    startSaving($this)
    clearError('items')
    if (!item_edited) {
        showError('items', '没有更改')
        stopSaving($this)
        return
    }
    if (!testRequired(ii)) {
        showError('items', '*为必填项')
        stopSaving($this)
        return
    }
    $.post(
        ii[0].action,
        data,
        function (data, e) {
            stopSaving($this)
            showError('items', data.message)
            if (data.error == 0) {
                item_edited = false
                loadTable()
            }
        }
    )
}

function bindItemForm() {
    var item_image_option = {
        url: item_url,
        dataType: 'json',
        formData: {
            'csrfmiddlewaretoken': csrftoken,
            'item_id': item_id,
            'method': 'upload_image',
            'pmo': pmo
        },
        add: function (e, data) {
            if (data.originalFiles[0]['size'] > 1048576) {
                alert('请上传小于 1 MB 的图片')
            } else {
                $('#file-' + this.name).addClass('image-uploading')
                data.submit()
            }
        },
        done: function (e, data) {
            var ft = $('#file-' + this.name)
            ft.removeClass('image-uploading')
            if (data.result.error != 0) {
                alert(data.result.message)
            } else {
                ft
                    .addClass('image-uploaded')
                    .css('background-image', 'url("' + data.result.image_url + '")')
                    .css('background-repeat', 'no-repeat')
                    .css('background-size', 'contain')
                $(this).data('image_id', data.result.image_id)
                $('#file-' + this.name + ' .image-method').click(deleteImage)
            }
        }
    }
    $('.item-image').fileupload(item_image_option)
    $('#items-input').find('.form-control').change(function () {
        item_edited = true
    })
    $('.image-uploaded').children('.image-method').click(deleteImage)
    $('#items-submit').click(itemSubmit)
    $('#items-delete').click(function (e) {
        if (!confirm('真的要删除吗？'))
            return
        $.post(
            item_url, {
                'csrfmiddlewaretoken': csrftoken,
                'item_id': item_id,
                'method': 'delete_item',
                'pmo': pmo
            }, function (data, e) {
                if (data.error != 0) {
                    alert(data.message)
                } else {
                    loadTable()
                    if (item_id == data.item_id) {
                        $('#item-info').addClass('nodisplay-object')
                        $('#items-input').empty()
                        autoHeight()
                    }
                }
            }
        )
    })
}

function bindTable() {
    var id = $('.item-delete')
    id.click(function (e) {
        e.stopPropagation()
        if (!confirm('真的要删除 ' + $(this).prev().text() + ' 吗？'))
            return
        $.post(
            item_url, {
                'csrfmiddlewaretoken': csrftoken,
                'item_id': $(this).parent().data('item_id'),
                'method': 'delete_item',
                'pmo': pmo
            }, function (data, e) {
                if (data.error != 0) {
                    alert(data.message)
                } else {
                    loadTable()
                    if (item_id == data.item_id) {
                        $('#item-info').addClass('nodisplay-object')
                        $('#items-input').empty()
                        autoHeight()
                    }
                }
            }
        )
    })

    var ir = $('.item-name')
    ir.click(function () {
        var $this = $(this)
        var tmp_item_id = $this.data('item_id')
        if (tmp_item_id && tmp_item_id != item_id &&
            (!item_edited || confirm('真的要放弃当前的更改吗？')))
            showItem(tmp_item_id, $this.prev().text())
    })
}

function loadTable() {
    var page = arguments[0] ? arguments[0] : $('.items-table').data('page')
    $('#items-table-container').load(
        '?page=' + page,
        bindTable
    )
}

function bindItems() {
    var ia = $('#items-add')
    item_url = ia.data('url')
    ia.click(function () {
        startSaving(ia, '添加中')
        clearError('items-add')
        $.post(
            item_url,
            {
                'csrfmiddlewaretoken': csrftoken,
                'method': 'add_item',
                'pmo': pmo
            },
            function (data, e) {
                stopSaving(ia, '添加')
                if (data.error == 0) {
                    loadTable(999)
                } else
                    showError('items-add', data.message)
            }
        )
    })

    $('.items-pages').click(function () {
        var q = parseInt(this.value) + parseInt($('.items-table').data('page'))
        loadTable(q)
    })
    bindTable()
}

var submit_edited = false

function bindSubmit() {
    var si = $('#submit-input')
    si.find('.form-control').change(function () {
        submit_edited = true
    })
    $('#submit-submit').click(function () {
        var $this = $(this)
        var data = si.serialize()
        var name = $this.text()
        startSaving($this, '提交中')
        clearError('submit')
        if (!testRequired(si)) {
            showError('submit', '*为必填项')
            stopSaving($this, name)
            return
        }
        if ((item_edited || seller_edited) && !confirm('放弃之前未保存的更改吗？')) {
            stopSaving($this, name)
            return
        }

        if (!confirm('申请之后将无法编辑信息，如需编辑请选择撤销申请。您确定要提交申请吗？'))
            return
        $.post(
            si[0].action,
            data,
            function (data, e) {
                stopSaving($this, name)
                showError('submit', data.message)
                if (data.error == 0) {
                    submit_edited = false
                    location.href = '.'
                }
            }
        )
    })
}

function bindStall() {
    if ($.cookie('status') == 1)
        window.onbeforeunload = function (event) {
            if (seller_edited || item_edited || submit_edited)
                return '您有更改没有保存'
        }
}

$(document).ready(function () {
    bindNotice()
    bindSeller()
    bindItems()
    bindStall()
    bindSubmit()
})
