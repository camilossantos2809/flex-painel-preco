var actualPage = 1
var produtos = []
    
function getProducts() {
    fetch('/products?page='+actualPage, {
        headers: new Headers({
            'Content-Type': 'application/json'
        })
    }).then(response => response)
        .then(result => {
            produtos = result.json()
            buildRowsTable()
        })
}

function buildRowsTable() {
    clearAll()

    bodyTable = document.getElementById('body-prod')

    // TODO: código com input radio
    produtos.then(prod => {
        prod.forEach(el => {
            var tr = document.createElement('tr')
            var tdCod = document.createElement('td')
            var tdCodBarra = document.createElement('td')
            var tdDescricao = document.createElement('td')
            tdCod.innerHTML = el.cod
            tdCodBarra.innerHTML = el.cod_barra
            tdDescricao.innerHTML = el.descricao
            
            tr.appendChild(tdCod)
            tr.appendChild(tdCodBarra)
            tr.appendChild(tdDescricao)

            bodyTable.appendChild(tr)
        });
        
    });
}

function clearAll(){
    document.getElementById('body-prod').innerHTML = ""
}
function nextPage() {
    actualPage++
    getProducts()
    console.log(actualPage)
}

function previousPage() {
    if (actualPage > 1) {
        actualPage--
    }
    getProducts()
    console.log(actualPage)
}

document.getElementById('next').addEventListener('click', nextPage)
document.getElementById('previous').addEventListener('click', previousPage)
if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", getProducts);
} else {
    getProducts();
}