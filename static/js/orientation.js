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
            $(".myPopup").on("popupafteropen", function (event, ui) {
                setInterval(function () {
                    let sec = parseInt($(".sec:eq(0)").html()) - 1;
                    $(".sec").html(sec);
                    if (sec == 0) {
                        window.location.href = "/menu/?userID=" + result.userID;
                    }
                }, 1000);
            });
            if (result.success == "ok") {
                console.log('ok');
                $("#myPopup1").popup("open");
            } else {
                console.log('fail');
                $("#myPopup2").popup("open");
            }
        }
    });
}
