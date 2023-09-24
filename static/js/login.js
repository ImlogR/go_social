var card = document.getElementById("card");


// login and registration flip

function openRegister(){
    card.style.transform = "rotateY(-180deg)";
}
function openLogin(){
    card.style.transform = "rotateY(0deg)";
}