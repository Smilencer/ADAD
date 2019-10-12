$(document).ready(function () {
    $(".banner").animatext({
        mode: mode,
        speed: 150,
        effect: "bounceIn",
        infinite: true,
        timeToRelaunch: 3000
    });
});

function reset() {
    $(".credential").val("");
}

function login() {
    var name = $("#username").val();
    if (name == "") {
        $("#username").addClass("error");
        return;
    }
    var pwd = $("#password").val();
    if (pwd == "") {
        $("#password").addClass("error");
        return;
    }
    $.post("../ajax/", {
        "cmd": "admin",
        "user": name,
        "pwd": pwd
    }, function (result) {
        if (result.userID == null) {
            $("#password").addClass("error");
        } else {
            window.location.href = "../doctor?userID=" + result.userID;
        }
    })
}

function inputing() {
    $(".credential").removeClass("error");
}