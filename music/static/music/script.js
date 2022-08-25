function standby() {
    document.getElementById('profilepic').src = "https://stock.adobe.com/search?k=profile"
}

window.addEventListener("scroll", function(){
    var header = document.querySelector("header");
    header.classList.toggle("sticky", window.scrollY > 0);
})

function playmusic(name,artist,image,audio) {
    document.getElementById('musicplayer-song-name').innerHTML = name
    document.getElementById('musicplayer-song-artists').innerHTML = artist
    document.getElementById('musicplayer-album-cover').src = image
    document.getElementById('audio').src = audio
}

function pauseplay() {
    var audio = document.getElementById('audio')
    if (!audio.paused){
        audio.pause()
        document.getElementById('pauseplay-image').src = "/static/music/musicplayer-icons/play.png"
    }
    else {
        audio.play()
        document.getElementById('pauseplay-image').src = "/static/music/musicplayer-icons/pause.png"
    }
}
