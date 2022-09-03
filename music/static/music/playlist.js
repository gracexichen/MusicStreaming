var songNumber = 0;

function loadmusic() {
    playmusic(title[songNumber], artist[songNumber], image[songNumber], audio[songNumber],0, description[songNumber], 0);
    var music = document.getElementById('audio');
    music.addEventListener("ended", function(){changeSong('next');console.log("changed song")});
    console.log("listener fired");
}

function changeSong(direction){
    if(direction=='next'){
        if(songNumber == (title.length - 1))
        {
            songNumber = -1;
        }
        songNumber++;
    }
    else {
        if(songNumber == 0){
            songNumber = title.length;
        }
        songNumber--;
    }
    console.log(songNumber);
    loadmusic();
    pauseplay();
}

$(document).ready(function(){
    loadmusic();
    console.log(songNumber);

})
