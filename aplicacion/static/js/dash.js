$(document).ready(function() {
    var items = $("li[class=nav-item]");
    items.on({
        mouseenter: function() {
            $(this).css("background-color", "GreenYellow");
        },
        mouseleave: function() {
            $(this).css("background-color", "white");
        }
    });
});