function setNumber(result, index) {
    if (index < 5) {
        if (result.trim() == "") {
            result = "?";
        }
        $(".num:eq(" + index + ")").html(result);
    }
}

function save(cmd) {
    let arr = [];
    $(".ipt-result").each(function () {
        arr.push($(this).val());
    });
    let dataStr = `mocaID=${$("#mocaID").val()}&cmd=${cmd}&results=${arr.join(",")}`;
    $.ajax({
        type: "POST",
        data: dataStr,
        url: "/ajax/",
        dataType: "json",
        success: function (result) {
            if (result.success == "ok") {
                console.log('ok');
                return true;
            } else {
                console.log('fail');
                return false;
            }
        }
    });
}