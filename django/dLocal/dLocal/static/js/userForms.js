function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
      const cookies = document.cookie.split(';');
      for (let i = 0; i < cookies.length; i++) {
        const cookie = cookies[i].trim();
        // Does this cookie string begin with the name we want?
        if (cookie.substring(0, name.length + 1) === (name + '=')) {
          cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
          break;
        }
      }
    }
    return cookieValue;
  }
  
var csrftoken = getCookie('csrftoken');


function deleteform(formId) {
    var formCard = document.getElementById("form-"+formId);
    formCard.style.display = "none";
    formCard.parentNode.removeChild(formCard)

    fetch('/../deleteForm/', {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json',
        'X-CSRFToken': csrftoken
    },
    body: formId
    })
    .then(response => {
    // Handle the response from the Django view
        window.location.replace("https://commentcorner.ngrok.app/users/profiles");
    })
    .catch(error => {
    // Handle any errors that occur during the HTTP request
    // console.error(error);
    });
}