function reset(num) {
    $("input[type='file']").val("");
    $(".gallery").hide();
    $(".mri").val("");
    $.mobile.silentScroll(0);
}

function loadImg(ipt, imgId) {
    let file = ipt.files[0];
    let reader = new FileReader();
    let imgFile;
    reader.onload = function (e) {
        imgFile = e.target.result;
        $("#img-" + imgId).attr("src", imgFile);
        $("#img-" + imgId).parent().show();
    }
    reader.readAsDataURL(file);
}

function checkEmptyImg(src) {
    if (src == "") {
        $("#emptyImg").popup("open");
        return false;
    }
    return true;
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
    let img1 = $("#img-axial").attr("src");
    let img2 = $("#img-sagittal").attr("src");
    let img3 = $("#img-coronal").attr("src");
    if (checkEmptyImg(img1) && checkEmptyImg(img2) && checkEmptyImg(img3)) {
        $.mobile.loading('show');
        let reg = /base64,(\S*)/;
        let img1_64 = img1.match(reg)[1];
        let img2_64 = img2.match(reg)[1];
        let img3_64 = img3.match(reg)[1];
        let dataset = {};
        let iptArray = $(".mri").toArray();
        for (let ipt of iptArray) {
            if (!checkEmptyIndice($(ipt).val())) {
                return;
            }
            dataset[$(ipt).attr("name")] = $(ipt).val();
        }
        let struct_data = [];
        struct_data.push(dataset);
        let data_result = JSON.stringify(struct_data);
        $.ajax({
            type: "post",
            url: "/help_diagnosis_AD_imgs/",
            datatype: "json",
            data: {
                age: age,
                gender: gender,
                data_result: data_result,
                img1: img1_64,
                img2: img2_64,
                img3: img3_64
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
}