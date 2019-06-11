var recorder;

$(document).on("pageshow", function () {
    recorder = Recorder();
});

function playAudio() {
    player.play();
    $(".working_svg").hide();
    $("#audio_svg").show();
    $("#start,#stop").attr("disabled", true);
}

function startRecording() {
    $(".working_svg").hide();
    $("#puff_svg").show();
    $("#start").attr("disabled", true);
    $("#stop").attr("disabled", false);
    recorder.open(function () {
        recorder.start();
    }, function (msg, isUserNotAllow) {
        console.log((isUserNotAllow ? "UserNotAllow，" : "") + "cannot record: " + msg);
    });
}

function stopRecording(cmd) {
    $(".working_svg").hide();
    $("#start").attr("disabled", false);
    $("#stop").attr("disabled", true);
    recorder.stop(function (blob, duration) {
        recorder.close();
        let reader = new FileReader();
        reader.onloadend = function () {
            $.ajax({
                type: "POST",
                data: {
                    cmd: cmd,
                    mocaID: $("#mocaID").val(),
                    audio: (/.+;\s*base64\s*,\s*(.+)$/i.exec(reader.result) || [])[1]
                },
                url: "/ajax/",
                dataType: "json",
                success: function (result) {
                    if (result.success == "ok") {
                        console.log('ok');
                    } else {
                        console.log('fail');
                    }
                }
            });
        };
        reader.readAsDataURL(blob);
    }, function (msg) {
        console.log("Recording failed: " + msg);
    });
}

function save(cmd) {
    let arr = [];
    $("input[type='checkbox']:checked").each(function () {
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