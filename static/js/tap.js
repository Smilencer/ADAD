var player;
var playList;
var counter = 1;
var tapList = [];

$(document).on("pageshow", function () {
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
            $("#play").attr("disabled", false);
            player.src = `/static/images/moca/${playList[0]}.mp3`;
            counter = 1;
        }
    });
});

function playAudio() {
    player.play();
    $(".working_svg").hide();
    $("#audio_svg").show();
    $("#play").attr("disabled", true);
    $("#tap").attr("disabled", false);
}

function tapA() {
    if (counter - 1 < 0) {
        tapList.push(playList.length - 1);
    } else {
        tapList.push(counter - 1);
    }
}

function save(cmd) {
    let dataStr = `mocaID=${$("#mocaID").val()}&cmd=${cmd}&taps=${tapList.join(",")}`;
    $.ajax({
        type: "POST",
        data: dataStr,
        url: "../ajax/",
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