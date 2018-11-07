function getSelectedProd () {
    var selectedProd = document.querySelectorAll('input[name="group-prod"]:checked')[0].id
    inputProd.value = selectedProd
    M.updateTextFields()
}

var searchProd = document.getElementById('select-prod')
var inputProd = document.getElementById('produto')

searchProd.addEventListener('click', getSelectedProd)

document.addEventListener('DOMContentLoaded', function () {
    var elems = document.querySelectorAll('.modal');
    var instances = M.Modal.init(elems, { startingTop: '1%', endingTop: '5%' });
    M.Tooltip.init(document.querySelectorAll('.tooltipped'));
});