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
    let iptArray = $(".scale").toArray();
    for (let ipt of iptArray) {
        if (!checkEmptyIndice($(ipt).val())) {
            return;
        }
    }
    let age = $("#age").val();
    let gender = $("#gender").val();
    if (gender == "M") {
        gender = "Male";
    } else {
        gender = "Female";
    }
    let dataset = {};
    let getVal = function (iptname) {
        let iptArr = $(`input[name='${iptname}']`);
        return [iptArr[0].value, iptArr[1].value];
    };
    let changeDate = function (dateArr) {
        return [dateArr[0].replace(/-/gi, "/"), dateArr[1].replace(/-/gi, "/")];
    };
    dataset["PTID"] = ["1", "2"];
    dataset["Age"] = [age, age];
    dataset["Sex"] = [gender, gender];
    dataset["ADAS13"] = getVal("adas");
    dataset["MMSE"] = getVal("mmse");
    dataset["Hippocampus"] = getVal("hippocampus");
    dataset["WholeBrain"] = getVal("whole");
    dataset["ICV"] = getVal("icv");
    dataset["EXAMDATE"] = changeDate(getVal("date"));
    dataset["ABETA"] = getVal("abeta");
    dataset["TAU"] = getVal("tau");
    dataset["PTAU"] = getVal("ptau");

    $.mobile.loading('show');
    $.ajax({
        type: "post",
        url: "../help_predict_AD_index/",
        datatype: "json",
        data: {
            dataJSON: JSON.stringify(dataset)
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

