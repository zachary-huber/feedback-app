function SignUpForm(event) {

    event.preventDefault();
  
    var valid = true;

    var elements = event.currentTarget;
    var dob = elements[0].value;//dob
    var email = elements[1].value; //Email
    var uname = elements[2].value; //username
    var pswd = elements[3].value; //Password
    var pswdr = elements[4].value; //Confirm Password
    var avatar = elements[5].value; //avatar
    var comp = elements[6].value;//company name

    var regex_dob = /^(0[1-9]|[12][0-9]|3[01])[- /.]/;
    var regex_email = /^\w+@[a-zA-Z_]+?\.[a-zA-Z]{2,3}$/;
    var regex_pswd  = /^(?=.*[^a-zA-Z])/;
    var regex_uname = /^[a-zA-Z0-9]*$/;
    var regex_comp = /^[a-zA-Z0-9]*$/;
  
    var msg_dob = document.getElementById("msg_dob");
    var msg_email = document.getElementById("msg_email");
    var msg_pswd = document.getElementById("msg_pswd");
    var msg_uname = document.getElementById("msg_uname");
    var msg_pswdr = document.getElementById("msg_pswdr");
    var msg_avatar = document.getElementById("msg_avatar");
    var msg_comp = document.getElementById("msg_comp");
    
    msg_dob.innerHTML  = "";
    msg_email.innerHTML  = "";
    msg_pswd.innerHTML = "";
    msg_uname.innerHTML = "";
    msg_pswdr.innerHTML = "";
    msg_avatar.innerHTML = "";
    msg_comp.innerHTML = "";

    //Variables for DOM Manipulation commands
    var textNode;

    if (dob == null || dob == "") {
        textNode = document.createTextNode("Date of Birth empty.");
        msg_dob.appendChild(textNode);
        valid = false;
    } 
    else if (regex_dob.test(dob) == false) {
        textNode = document.createTextNode("Date of Birth wrong format. Use dd-mm-yyyy format");
        msg_dob.appendChild(textNode);
        valid = false;
    }

    if (comp == null || comp == "") {
        textNode = document.createTextNode("Company Name empty.");
        msg_comp.appendChild(textNode);
        valid = false;
    } 
    else if (regex_comp.test(comp) == false) {
        textNode = document.createTextNode("Company Name must not have non-word characters or spaces");
        msg_comp.appendChild(textNode);
        valid = false;
    }
  
    // if email is left empty or email format is wrong, add an error message to the matching cell.
    if (email == null || email == "") {
      textNode = document.createTextNode("Email address empty.");
      msg_email.appendChild(textNode);
      valid = false;
    } 
    else if (regex_email.test(email) == false) {
      textNode = document.createTextNode("Email address wrong format. example: username@somewhere.sth");
      msg_email.appendChild(textNode);
      valid = false;
    }
    else if (email.length > 60) {
      textNode = document.createTextNode("Email address too long. Maximum is 60 characters.");
      msg_email.appendChild(textNode);
      valid = false;
    }
  
    if (pswd == null || pswd == "") {
        textNode = document.createTextNode("Password empty.");
        msg_pswd.appendChild(textNode);
        valid = false;
    } 
    else if (regex_pswd.test(pswd) == false) {
        textNode = document.createTextNode("Password must have at least one non-letter character.");
        msg_pswd.appendChild(textNode);
        valid = false;
    }
    else if (pswd.length < 6) {
        textNode = document.createTextNode("Password is too short. It must be at least 6 characters long.");
        msg_pswd.appendChild(textNode);
        valid = false;
    }

    if (uname == null || uname == "") {
        textNode = document.createTextNode("Username empty.");
        msg_uname.appendChild(textNode);
        valid = false;
    } 
    else if (regex_uname.test(uname) == false) {
        textNode = document.createTextNode("Username must not have non-word characters or spaces");
        msg_uname.appendChild(textNode);
        valid = false;
    }

    if (pswdr == null || pswdr == "") {
        textNode = document.createTextNode("Confirm Password is empty.");
        msg_pswdr.appendChild(textNode);
        valid = false;
    } 
    else if (pswdr != pswd) {
        textNode = document.createTextNode("Password and Confirm Password must match.");
        msg_pswdr.appendChild(textNode);
        valid = false;
    }

    if(document.getElementById("avatar").checked == false && document.getElementById("female").checked == false
        && document.getElementById("other").checked == false){
        textNode = document.createTextNode("You must select an avatar.");
        msg_avatar.appendChild(textNode);
        valid = false;
    }

    if (valid == true) {
        window.location.href = 'login.html';
    }
  
}
  
function ResetForm(event) {
    var elements = event.currentTarget;
    var dob = elements[0].value; //dob
    var email = elements[1].value; //Email
    var uname = elements[2].value; //username
    var pswd = elements[3].value; //Password
    var pswdr = elements[4].value; //Confirm password
    var avatar = elements[5].value;
    
    dob = "";
    email = "";
    pswd = "";
    uname = "";
    pswdr ="";
    avatar = "";

    
    var msg_dob = document.getElementById("msg_dob");
    var msg_email = document.getElementById("msg_email");
    var msg_pswd = document.getElementById("msg_pswd");
    var msg_uname = document.getElementById("msg_uname");
    var msg_pswdr = document.getElementById("msg_pswdr");
    var msg_avatar = document.getElementById("msg_avatar");

    msg_email.innerHTML = "";
    msg_pswd.innerHTML = "";
    msg_dob.innerHTML = "";
    msg_uname.innerHTML = "";
    msg_pswdr.innerHTML = "";
    msg_avatar.innerHTML ="";
}