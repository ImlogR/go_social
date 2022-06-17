var settingsmenu = document.querySelector(".settings-menu");
var darkBtn= document.getElementById("dark-btn");
var LikeBtn= document.getElementById("like-button");


function settingsMenuToggle(){
    settingsmenu.classList.toggle("settings-menu-height");
}

darkBtn.onclick = function(){
    darkBtn.classList.toggle("dark-btn-on");
    document.body.classList.toggle("dark-theme");

    if (localStorage.getItem("theme") == "light"){
        localStorage.setItem("theme", "dark");
    }
    else {
        localStorage.setItem("theme", "light");
    }

}

if (localStorage.getItem("theme") == "light"){
    darkBtn.classList.remove("dark-btn-on");
    document.body.classList.remove("dark-theme");
}
else if (localStorage.getItem("theme") == "dark"){
    darkBtn.classList.add("dark-btn-on");
    document.body.classList.add("dark-theme");
}
else {
    localStorage.setItem("theme", "light");
}

LikeBtn.onclick = function(){
    darkBtn.classList.toggle("fa-regular");
    document.body.classList.toggle("fa-solid");
}


var state = true;

function like(element){
    if(state){
        var  currentElement = element.querySelector('.fa-heart');
        currentElement.style.color = "orange";
        localStorage.setItem("storedColor", "orange");

    }else{
        var  currentElement = element.querySelector('.fa-heart');
        currentElement.style.color = "black";
        localStorage.setItem("storedColor", "black");
    }
    state = !state;
}

window.addEventListener('DOMContentLoaded', e => {
    currentElement.style.color = localStorage.getItem("storedColor");
});