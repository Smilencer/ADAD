function save(cmd) {
    let dataStr = `mocaID=${$("#mocaID").val()}&cmd=${cmd}&animal=${$("#animalname").val()}`;
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