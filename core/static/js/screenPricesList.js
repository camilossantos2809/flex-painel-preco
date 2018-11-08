var control = 0;
var divWrapper = document.getElementById('wrapper')

function loadPromotion() {
    divWrapper.innerHTML = ''
    if (control == 1) {
        control = 0
        location.pathname = redirectToPath
    }

    produtos.forEach(element => {
        var div = document.createElement('div')
        div.innerHTML = element.name
        div.setAttribute('class', 'descricao')
        divWrapper.appendChild(div)
    });
    control++
}

// Load main function when page is ready
if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", loadPromotion);
} else {
    loadPromotion();
}
