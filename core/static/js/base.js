document.addEventListener('DOMContentLoaded', function () {
    M.Modal.init(document.querySelectorAll('.modal'), { startingTop: '1%', endingTop: '1%' });
    M.Tooltip.init(document.querySelectorAll('.tooltipped'));
    M.FormSelect.init(document.querySelectorAll('select'));
})

function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i];
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}