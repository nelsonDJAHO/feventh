// Formulaire d authentification
const contactform = document.getElementById('contactform')
    // const csrftoken = document.getElementsByName('csrfmiddlewaretoken')[0].value


contactform.addEventListener('submit', (e) => {
    e.preventDefault()

    let last_name = document.getElementById('last_name').value
    let first_name = document.getElementById('first_name').value
    let email = document.getElementById('email').value
    let phone = document.getElementById('phone').value
    let subject = document.getElementById('subject').value
    let message = document.getElementById('message').value

    mydata = new FormData()
    mydata.append('last_name', last_name)
    mydata.append('first_name', first_name)
    mydata.append('email', email)
    mydata.append('phone', phone)
    mydata.append('subject', subject)
    mydata.append('message', message)
    mydata.append('csrfmiddlewaretoken', csrftoken)

    $.ajax({
        method: 'POST',
        url: '/contactForm/',
        data: mydata,
        processData: false,
        contentType: false,
        success: function(data) {
            if (data.status == true) {
                alert(data.message)
                contactform.reset()
            } else {
                alert(data.message)
            }
        }
    })
})