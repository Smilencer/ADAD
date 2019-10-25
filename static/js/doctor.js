$(document).ready(function () {
    $(".adad").animatext({
        mode: "chars",
        speed: 150,
        effect: "flipInY",
        infinite: true,
        timeToRelaunch: 3000
    });
    var sketchpad_1 = new Sketchpad({
        element: "#canvas1",
        width: 300,
        height: 300,
        readOnly: true
    });
    var sketchpad_2 = new Sketchpad({
        element: "#canvas2",
        width: 300,
        height: 300,
        readOnly: true
    });
    var sketchpad_3 = new Sketchpad({
        element: "#canvas3",
        width: 300,
        height: 300,
        readOnly: true
    });
});

function showPad(padid, obj) {
    $(".subpad").hide();
    $(`#${padid}`).show();
    $(".menu-selected").removeClass();
    $(obj).addClass("menu-selected");
}