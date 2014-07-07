$(document).ready(function() {

$(".start-button").on("click", function() {

    $(".white-banner").slideToggle();
    $("header").slideToggle();

});

$(".stabutton").on("click", function(e) {
    e.preventDefault();
    $(".column img").toggleClass("bigger");


});

});