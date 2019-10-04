var recorder;
var time = 60;
var interval;

$(document).on("pageshow", function () {
    recorder = Recorder();
});

function startRecording() {
    $(".working_svg").hide();
    $("#puff_svg").show();
    $("#start").attr("disabled", true);
    interval = setInterval(countdown, 10);
    recorder.open(function () {
        recorder.start();
        setTimeout(function () {
            recorder.stop(function (blob, duration) {
                time = 60;
                $(".sec").html(time.toFixed(2));
                $(".working_svg").hide();
                $("#start").attr("disabled", false);
                recorder.close();
                let reader = new FileReader();
                reader.onloadend = function () {
                    $.ajax({
                        type: "POST",
                        data: {
                            cmd: "Q5-3",
                            mocaID: $("#mocaID").val(),
                            audio: (/.+;\s*base64\s*,\s*(.+)$/i.exec(reader.result) || [])[1]
                        },
                        url: "../ajax/",
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
        }, 60000);
    }, function (msg, isUserNotAllow) {
        console.log((isUserNotAllow ? "UserNotAllow，" : "") + "cannot record: " + msg);
    });
}

function countdown() {
    time = time - 0.01;
    if (time <= 0) {
        window.clearInterval(interval);
    } else {
        $(".sec").html(time.toFixed(2));
    }
}