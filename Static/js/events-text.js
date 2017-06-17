// JavaScript source code
$(document).ready(function () {
    $(".onoffswitch-label").on("click", function () {
        //var checkbox = $(this).attr("checked");
        var $elem = $(this).prev();
        var id = $elem.attr("id");
        var $checked = $elem.prop("checked");
        if ($checked ==true) {
            $elem.prop('checked',false);
        }
        else {
            $elem.prop('checked', true);
        }
        $.ajax({
            method: "POST",
            url: "/admin_text",
            data: {"available":true,"tm_id":id}
        }).done(function (data) {
            console.log(data);
        });
    });
    $(".delete_btn").on("click", function () {
        var $elem = $(this);
        var $id = $elem.attr("id");
        $.ajax({
            method: "POST",
            url: "/admin_text",
            data: {"delete":true,"tm_id":$id}
        }).done(function(data){
            console.log(data);
            window.location.href = '/admin_text';
        });
    });
});