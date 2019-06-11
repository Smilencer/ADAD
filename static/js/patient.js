function reset() {
    $("input[type='radio']").attr("checked", false).checkboxradio("refresh");
    $("#birthday").val("");
    $("#history").attr("checked", false).flipswitch("refresh");
    $("#address").val("");
    $(".ui-input-clear").click();
    $("#fullname").focus();
    $.mobile.silentScroll(0);
}

function next() {
    $.ajax({
        type: "POST",
        data: $("form").serialize(),
        url: "/ajax/",
        dataType: "json",
        success: function (result) {
            if (result.userID == null) {
                $("#toPop").click();
            } else {
                window.location.href = "/symptom?userID=" + result.userID;
            }
        }
    });
}

function calculateAge(obj) {
    let dateArr = $(obj).val().split("-");
    let birthYear = dateArr[0];
    let today = new Date();
    let currentYear = today.getFullYear();
    let age = currentYear - birthYear;
    $("#age").val(age);
}

$(document).on("pageshow", function (event) {
    calculateAge($("#birthday"));
});