function itemMove(){
    const section = document.getElementById("menu");
    section.style.position = "relative"
    section.style.left = "-100%"
    section.style.backgroundColor = "red"
    section.style.transitionDuration = "2s"
}

function customerMove(){
    const section = document.getElementById("menu");
    section.style.position = "relative"
    section.style.left = "0%"
    section.style.backgroundColor = "red"
    section.style.transitionDuration = "2s"
}

function orderMove(){
    const section = document.getElementById("menu");
    section.style.position = "relative"
    section.style.left = "-200%"
    section.style.backgroundColor = "red"
    section.style.transitionDuration = "2s"
}