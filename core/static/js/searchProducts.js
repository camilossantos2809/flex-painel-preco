var actualPage = 1
var produtos = []
filterInputs = document.querySelectorAll('.in-filter')

function getFilters () {
    var filters = new URLSearchParams()
    filterInputs.forEach(input => {
        if (input.value != '') {
            filters.append(input.getAttribute('name'), input.value)
        }
    })
    return filters
}

function getProducts () {
    let params = getFilters()
    params.append('page', actualPage)
    let url = '/products?' + params.toString()

    fetch(url, {
        headers: new Headers({
            'Content-Type': 'application/json'
        })
    }).then(response => response)
        .then(result => {
            produtos = result.json()
            buildRowsTable()
        })
}

function buildRowsTable () {
    clearAll()

    bodyTable = document.getElementById('body-prod')

    produtos.then(prod => {
        prod.forEach(el => {
            var tr = document.createElement('tr')
            var label = document.createElement('label')
            var input = document.createElement('input')
            input.setAttribute('id', el['cod'])
            input.setAttribute('type', 'radio')
            input.setAttribute('name', 'group-prod')
            input.setAttribute('class', 'with-gap')
            label.appendChild(input)
            var span = document.createElement('span')
            span.innerHTML = el['cod']
            label.appendChild(span)
            tr.appendChild(label)

            for (const key in el) {
                if (el.hasOwnProperty(key) && key !== 'cod') {
                    const value = el[key];
                    var td = document.createElement('td')
                    td.innerHTML = value
                    tr.appendChild(td)
                }
            }
            bodyTable.appendChild(tr)
        });

    });
}

function clearAll () {
    document.getElementById('body-prod').innerHTML = ""
}
function nextPage () {
    actualPage++
    getProducts()
    console.log(actualPage)
}

function previousPage () {
    if (actualPage > 1) {
        actualPage--
    }
    getProducts()
    console.log(actualPage)
}

document.getElementById('next').addEventListener('click', nextPage)
document.getElementById('previous').addEventListener('click', previousPage)
filterInputs.forEach(elem => {
    elem.addEventListener('keypress', event => {
        if (event.key == 'Enter') {
            getProducts()
        }
    })

    elem.parentElement.addEventListener('toggle', event => {
        if (event.srcElement.open) {
            event.srcElement.children[1].focus()
        }
    })
})
if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", getProducts);
} else {
    getProducts();
}