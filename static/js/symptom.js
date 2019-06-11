function reset() {
    $("#pageone").find("input[type='radio']").attr("checked", false).checkboxradio("refresh");
    $("#pageone").find("input[type='checkbox']").attr("checked", false).checkboxradio("refresh");
    $("#description").val("");
    $.mobile.silentScroll(0);
}

function next() {
    let arr = [];
    let iptArr = $("input[name='sympton']:checked");
    for (let i = 0; i < iptArr.length; i++) {
        arr.push(iptArr[i].value);
    }
    let dataStr = `userID=${$("#userID").val()}&cmd=symtom&adtype=${$("input[name='adtype']").val()}&sympton=${arr.join(',')}&description=${$("#description").val()}`;
    $.ajax({
        type: "POST",
        data: dataStr,
        url: "/ajax/",
        dataType: "json",
        success: function (result) {
            if (result.userID == null) {
                $("#toPop").click();
            } else {
                window.location.href = "/menu?userID=" + result.userID;
            }
        }
    });
}