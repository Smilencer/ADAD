function reset(num) {
    $("input[type='file']").val("");
    $("#report").val("");
    $.mobile.silentScroll(0);
}

function loadText(ipt) {
    let file = ipt.files[0];
    let reader = new FileReader();
    reader.onload = function (e) {
        let txtFile = e.target.result;
        $("#report").val(txtFile);
        $("#report").textinput("refresh");
    }
    reader.readAsText(file, 'uft-8');
}

function diagnosis() {
    let age = $("#age").val();
    let gender = $("#gender").val();
    let text = $("#report").val();
    if (text == "") {
        $("#emptyText").popup("open");
        return;
    }
    $.mobile.loading('show');
    $.ajax({
        type: "post",
        url: "../help_diagnosis_AD_text/",
        datatype: "json",
        data: {
            age: age,
            gender: gender,
            text: text
        },
        success: function (data) {
            $.mobile.loading('hide');
            if (data === 'error') {
                console.log(data);
            } else {
                $("#result").html(data);
                $("#resultPopup").popup("open");
            }
        },
        error: function () {
            console.log('error 0');
        }
    });
}