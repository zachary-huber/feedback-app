function LogInForm(event) {

    event.preventDefault();
  
    var valid = true;
    

    var elements = event.currentTarget;
    var email = elements[0].value; //Email
    var pswd = elements[1].value; //Password

    var regex_email = /^\w+@[a-zA-Z_]+?\.[a-zA-Z]{2,3}$/;
    var regex_pswd  = /^\S*$/;
  
    var msg_email = document.getElementById("msg_email");
    var msg_pswd = document.getElementById("msg_pswd");

    msg_email.innerHTML  = "";
    msg_pswd.innerHTML = "";

  
    //Variables for DOM Manipulation commands
    var textNode;
  
    // if email is left empty or email format is wrong, add an error message to the matching cell.
    if (email == null || email == "") {
      textNode = document.createTextNode("Please enter an email address.");
      msg_email.appendChild(textNode);
      valid = false;
    } 
    else if (regex_email.test(email) == false) {
      textNode = document.createTextNode("Please enter a valid email address.");
      msg_email.appendChild(textNode);
      valid = false;
    }
    else if (email.length > 60) {
      textNode = document.createTextNode("Email address too long. Maximum is 60 characters.");
      msg_email.appendChild(textNode);
      valid = false;
    }
  
    if (pswd == null || pswd == "") {
        textNode = document.createTextNode("Please enter a password.");
        msg_pswd.appendChild(textNode);
        valid = false;
    } 
    else if (regex_pswd.test(pswd) == false) {
        textNode = document.createTextNode("Password is invalid. It must not have spaces.");
        msg_pswd.appendChild(textNode);
        valid = false;
    }
    else if (pswd.length < 6) {
        textNode = document.createTextNode("Please enter a valid password.");
        msg_pswd.appendChild(textNode);
        valid = false;
    }

    if (valid == true) {
        window.location.href = 'default.html';
    }
  
}
  
function ResetForm(event) {
    var elements = event.currentTarget;
    var email = elements[0].value; //Email
    var pswd = elements[1].value; //Password

    email = "";
    pswd = "";
    
    var msg_email = document.getElementById("msg_email");
    var msg_pswd = document.getElementById("msg_pswd");

    msg_email.innerHTML  = "";
    msg_pswd.innerHTML  = "";
}
  
