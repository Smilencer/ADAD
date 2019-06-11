var sketchpad;

$(document).on("pageshow", function () {
    sketchpad = new Sketchpad({
        element: ".sketchpad",
        width: 300,
        height: 300
    });

    $(".undo").on("tap", function () {
        sketchpad.undo();
    });

    $(".redo").on("tap", function () {
        sketchpad.redo();
    });

    $(".clear").on("tap", function () {
        sketchpad.clear();
    });
});

function save(cmd) {
    let dataStr = `mocaID=${$("#mocaID").val()}&cmd=${cmd}&sketch=${sketchpad.toJSON()}`;
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