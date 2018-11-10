document.addEventListener('DOMContentLoaded', function () {
    M.Modal.init(document.querySelectorAll('.modal'), { startingTop: '1%', endingTop: '1%' });
    M.Tooltip.init(document.querySelectorAll('.tooltipped'));
})