function getSelectedProd () {
    var selectedProd = document.querySelectorAll('input[name="group-prod"]:checked')[0].id
    inputProd.value = selectedProd
    M.updateTextFields()
}

var searchProd = document.getElementById('select-prod')
var inputProd = document.getElementById('produto')

searchProd.addEventListener('click', getSelectedProd)
