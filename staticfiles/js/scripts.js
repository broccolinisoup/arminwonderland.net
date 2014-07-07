$(document).ready(function() {

$(".header-subtitle").on("click", function() {

    $(".call-to-action").slideToggle();

});

$(".call-button").on("click", function(e) {
    e.preventDefault();
    $(".column img").toggleClass("bigger");


});

});