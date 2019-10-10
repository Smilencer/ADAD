$(document).on("pageshow", "#page_ai", function (event) {
    $(".jump").each(function () {
        $(this).attr("href", $(this).attr("href") + location.search);
    });
});

$(document).on("pageshow", "#page_bca", function (event) {
    if (window.location.pathname.startsWith("/zh")) {
        $("#jumpMoCA").attr("href", "../moca/" + location.search + "&v=8.1&q=1-1");
    } else {
        $("#jumpMoCA").attr("href", "../moca/" + location.search + "&v=8." + RandomNumBoth(1, 3) + "&q=1-1");
    }
});

function RandomNumBoth(Min, Max) {
    let Range = Max - Min;
    let Rand = Math.random();
    let num = Min + Math.round(Rand * Range);
    return num;
}