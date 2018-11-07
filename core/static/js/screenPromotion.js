var control = 0;
var divDescricao = document.getElementById('descricao')
var imgImage = document.getElementById('image')
var divPreco = document.getElementById('preco')

function loadPromotion() {
    if (control + 1 > produtos.length) {
        control = 0
        // location.pathname = redirectToPath
    }
    divDescricao.textContent = produtos[control].name
    divPreco.textContent = 'R$ ' + produtos[control].preco
    imgImage.src = produtos[control].image
    control++
}

// Load main function when page is ready
if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", loadPromotion);
} else {
    loadPromotion();
}
