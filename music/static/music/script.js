window.addEventListener("scroll", function(){
    var header = document.querySelector("header");
    header.classList.toggle("sticky", window.scrollY > 0);
})

function standby() {
    document.getElementById('profilepic').src = "https://stock.adobe.com/search?k=profile"
}