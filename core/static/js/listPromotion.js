function deletePromotion (event) {
    let tr = event.srcElement.parentElement.parentElement.parentElement

    fetch(`promotion/delete/${tr.id}`, {
        method: 'POST',
        headers: new Headers({
            'Content-Type': 'application/json',
            'X-CSRFToken': getCookie('csrftoken')
        })
    }).then(response => response)
        .then(result => {
            if (result.status == '200') {
                M.toast({ html: `Promoção ${tr.id} deletada`, classes: 'indigo', displayLength: 10000 })
                tr.remove()
            } else {
                M.toast({ html: 'Ocorreu um erro! Verifique os logs', classes: 'indigo', displayLength: 10000 })
                console.log(result)
            }
        })
        .catch(err => {
            M.toast({ html: 'Ocorreu um erro! Verifique os logs', classes: 'indigo', displayLength: 10000 })
            console.log(err)
        })
}

tdDelete = document.querySelectorAll('tr td a.delete')
tdDelete.forEach(elem => {
    elem.addEventListener('click', deletePromotion)
});