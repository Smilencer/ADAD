var recorder, player;
var playList;
var counter = 1;

$(document).on("pageshow", function () {
    recorder = Recorder();
    player = new Audio(`/static/images/moca/${playList[0]}.mp3`)
    player.addEventListener("ended", function () {
        if (counter < playList.length) {
            player.src = `/static/images/moca/${playList[counter]}.mp3`;
            setTimeout(function () {
                player.play();
                counter++;
            }, 1000);
        } else {
            $(".working_svg").hide();
            $("#play,#start").attr("disabled", false);
            player.src = `/static/images/moca/${playList[0]}.mp3`;
            counter = 1;
        }
    });
});

function playAudio() {
    player.play();
    $(".working_svg").hide();
    $("#audio_svg").show();
    $("#play,#start,#stop").attr("disabled", true);
}

function startRecording() {
    $(".working_svg").hide();
    $("#puff_svg").show();
    $("#play,#start").attr("disabled", true);
    $("#stop").attr("disabled", false);
    recorder.open(function () {
        recorder.start();
    }, function (msg, isUserNotAllow) {
        console.log((isUserNotAllow ? "UserNotAllow，" : "") + "cannot record: " + msg);
    });
}

function stopRecording(cmd) {
    $(".working_svg").hide();
    $("#play,#start").attr("disabled", false);
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
}