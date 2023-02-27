// Formulaire d authentification
const newsletterForm = document.getElementById('newsletterForm')
const csrftoken = document.getElementsByName('csrfmiddlewaretoken')[0].value

// Traitement
newsletterForm.addEventListener('submit', (e) => {
    e.preventDefault()

    let emailAdress = document.getElementById('emailAdress').value

    mydata = new FormData()
    mydata.append('emailAdress', emailAdress)
    mydata.append('csrfmiddlewaretoken', csrftoken)

    $.ajax({
        method: 'POST',
        url: '/newsLetterSubscribtion/',
        data: mydata,
        processData: false,
        contentType: false,
        success: function(data) {
            if (data.status == true) {
                alert('Abonnement éffectué, Merci de votre interêt')
                newsletterForm.reset()
            } else {
                alert(data.message)
            }
        }
    })

})