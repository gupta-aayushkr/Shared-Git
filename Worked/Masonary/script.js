document.addEventListener('DOMContentLoaded', function () {
    var elem = document.querySelector('.container');
    var msnry = new Masonry(elem, {
        itemSelector: '.box',
        columnWidth: '.box',
        percentPosition: true
    });
});
