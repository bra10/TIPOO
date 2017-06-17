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
            url: "/admin_exam",
            data: {"available":true,"em_id":id}
        }).done(function (data) {
            console.log(data);
        });
    });
    $(".delete_btn").on("click", function () {
        var $elem = $(this);
        var $id = $elem.attr("id");
        $.ajax({
            method: "POST",
            url: "/admin_exam",
            data: { "delete": true, "em_id": $id }
        }).done(function (data) {
            console.log(data);
            window.location.href = '/admin_exam';
        });
    });
});