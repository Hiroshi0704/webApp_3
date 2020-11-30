var shiftApp = {};

shiftApp.util = {};

shiftApp.view = {};

shiftApp.dialog = {};

shiftApp.table = {};

var inherits = function(childCtor, parentCtor) {
    function tempCtor() { };
    tempCtor.prototype = parentCtor.prototype;
    childCtor.super = parentCtor.prototype;
    childCtor.prototype = new tempCtor();
    childCtor.prototype.constructor = childCtor;
};

$(function() {
    $('#sidebar-toggler').click(function() {
        if ($(this).prop('checked')) {
            $('.sidebar').css('left', '0px');
            $('#main').css('margin-left', '160px');
        } else {
            $('.sidebar').css('left', '-160px');
            $('#main').css('margin-left', '0px');
        }
    });
});
