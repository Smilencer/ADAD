function reset(num) {
    $(".scale").val("");
    $(".tab").collapsible("collapse");
    $(".tab:eq(0)").collapsible("expand");
    $.mobile.silentScroll(0);
}

function checkEmptyIndice(indice) {
    if (indice == "") {
        $("#emptyBio").popup("open");
        return false;
    }
    return true;
}

function diagnosis() {
    let age = $("#age").val();
    let gender = $("#gender").val();
    let dataset = {};
    let iptArray = $(".scale").toArray();
    let key = 0;
    for (let ipt of iptArray) {
        if (!checkEmptyIndice($(ipt).val())) {
            return;
        }
        dataset[key] = $(ipt).val();
        key++;
    }
    let struct_data = [];
    struct_data.push(dataset);
    let data_result = JSON.stringify(struct_data);
    $.mobile.loading('show');
    $.ajax({
        type: "post",
        url: "/help_diagnosis_AD_index/",
        datatype: "json",
        data: {
            age: age,
            gender: gender,
            data_result: data_result
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

$(document).on("pageshow", function (event) {
    $(".subtitle").css("font-size", "0.9em");
    $(".subcontent3").find("label").css("font-size", "0.9em");
});

