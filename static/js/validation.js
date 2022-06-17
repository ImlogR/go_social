var usernameError= document.getElementById('username-error');
var emaliError= document.getElementById('email-error');
var passwordError= document.getElementById('password-error');
var confirmationError= document.getElementById('confirm-error');
var signupError= document.getElementById('signup-error');

function validateName(){
    var name= document.getElementById('user-name').value;

    if(name.length == 0){
        usernameError.innerHTML = "Name is required!";
        return false;
    }
    if(!name.match(/^[A-Za-z]*[.][A-Za-z]{3,9}$/)){
        usernameError.innerHTML = "Place dot between names.";
        return false;
    }
    if(name == "." ){
        usernameError.innerHTML = "Place dot between names.";
        return false;
    }
    usernameError.innerHTML = '<i class= "fas fa-check-circle"></i>';
    return true;
}
function validateEmail(){
    var email= document.getElementById('user-email').value;

    if(email.length == 0){
        emaliError.innerHTML = "Email is required!";
        return false;   
    }
    if(!email.match(/^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/)){
        emaliError.innerHTML= "Of the form text@form.suffix";
        return false;
    }
    emaliError.innerHTML = '<i class= "fas fa-check-circle"></i>';
    return true;
}
function validatePassword(){
    var password= document.getElementById('user-password').value;

    if(password.length == 0){
        passwordError.innerHTML= "Password is required!";
        return false;
    }
    if(password.length != 8){
        passwordError.innerHTML= "Password should be upto 8 characters!";
        return false;
    }
    passwordError.innerHTML = '<i class= "fas fa-check-circle"></i>';
    return true;
}
function confirmPassword(){
    var password= document.getElementById('user-password').value;
    var confirm= document.getElementById('confirm-password').value;

    if(confirm.length == 0){
        confirmationError.innerHTML= "Confirmation required!";
        return false;
    }

    if (password != confirm){
        confirmationError.innerHTML= "Passwords should be matched!";
        return false
    }
    confirmationError.innerHTML = '<i class= "fas fa-check-circle"></i>';
    return true;  
}
function validateSignup(){
    if ( !validateName() || !validateEmail() || !validatePassword() || !confirmPassword()){
        signupError.style.display= 'block';
        signupError.innerHTML= "Fix errors to submit!";
        setTimeout(function(){signupError.style.display= 'none';}, 3000)
        return false;
    }
}