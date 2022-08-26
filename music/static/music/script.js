// index page
window.addEventListener("scroll", function(){
    var header = document.querySelector("header");
    header.classList.toggle("sticky", window.scrollY > 0);
})

function playmusic(name,artist,image,audio) {
    document.getElementById('musicplayer-song-name').innerHTML = name;
    document.getElementById('musicplayer-song-artists').innerHTML = artist;
    document.getElementById('musicplayer-album-cover').src = image;
    document.getElementById('audio').src = audio;
    console.log("playmusic")
}

function pauseplay() {
    var audio = document.getElementById('audio')
    if (!audio.paused){
        audio.pause();
        document.getElementById('pauseplay-image').src = "/static/music/musicplayer-icons/play.png";
    }
    else {
        audio.play();
        document.getElementById('pauseplay-image').src = "/static/music/musicplayer-icons/pause.png";
    }
}

function popup() {
    document.getElementById('musicplayer').style.height = "400px";
    document.getElementById('musicplayer-song-info').style.transform = "translate(0,-150px)"
    document.getElementById('musicplayer-control-buttons-container').style.transform = "translate(0,-150px)"
    document.getElementById('musicplayer-extra-buttons-container').style.transform = "translate(0,-150px)"
    document.getElementById('underneath-footer').style.display = "flex"
    console.log("popup")
}

function closePopup() {
    document.getElementById('underneath-footer').style.display = "none"
    document.getElementById('musicplayer-song-info').style.transform = "translate(0,0px)"
    document.getElementById('musicplayer-control-buttons-container').style.transform = "translate(0,0px)"
    document.getElementById('musicplayer-extra-buttons-container').style.transform = "translate(0,0px)"
    document.getElementById('musicplayer').style.height = "100px";
}
function search(ele) {
    if(event.key === 'Enter') {
        var title = document.getElementById('song-dropdown').getAttribute('data-title');
        var artist = document.getElementById('song-dropdown').getAttribute('data-artist');
        var image = document.getElementById('song-dropdown').getAttribute('data-image');
        var audio = document.getElementById('song-dropdown').getAttribute('data-audio');

        alert(ele.value);
        playmusic(title,artist,image,audio);
        popup();

    }
}