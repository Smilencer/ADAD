function signin() {
    let username = $("#username").val();
    let password = $("#password").val();
    if (username != "" && password != "") {
        $.post("../ajax/", {
            "cmd": "signin",
            "username": username,
            "password": password,
        }, function (result) {
            if (result.userID == null) {
                $(".alert").hide();
                $("#nopass").show();
            } else {
                window.location.href = "../patient?userID=" + result.userID;
            }
        });
    }
}

function signup() {
    let username = $("#username").val();
    let password = $("#password").val();
    if (username != "" && password != "") {
        $.post("../ajax/", {
            "cmd": "signup",
            "username": username,
            "password": password,
        }, function (result) {
            if (result.userID == null) {
                $(".alert").hide();
                $("#duplicate").show();
            } else {
                window.location.href = "../patient?userID=" + result.userID;
            }
        });
    }
}