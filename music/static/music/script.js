
var currentSongID;
window.addEventListener("scroll", function(){
    var header = document.querySelector("header");
    header.classList.toggle("sticky", window.scrollY > 0);
})

function dropdown(input) {
    if(input==="hover"){
        document.getElementById("dropdown-content").style.display = "block";
    }
    else if(input==='leave'){
        document.getElementById("dropdown-content").style.display = "none";
    }
}
function search(ele) {
    if(event.key === 'Enter') {
        var id = document.getElementById('search-song-input').value
        var title = document.getElementById(id).getAttribute('data-title');
        var artist = document.getElementById(id).getAttribute('data-artist');
        var image = document.getElementById(id).getAttribute('data-image');
        var audio = document.getElementById(id).getAttribute('data-audio');

        playmusic(title,artist,image,audio);
        popup();
    }
}

//musicplayer
function playmusic(name,artist,image,audio,id, description, likes) {
    currentSongID= id;
    document.getElementById('all-comments').innerHTML="";
    document.getElementById('musicplayer-song-name').innerHTML = name;
    document.getElementById('musicplayer-song-artists').innerHTML = artist;
    document.getElementById('musicplayer-album-cover').src = image;
    document.getElementById('audio').src = audio;
    document.getElementById('favorite-button').value = id;
    document.getElementById('song-description').innerHTML = description;
    document.getElementById('display-likes-count').innerHTML = "Likes: " + likes;

    $.ajax({
        url: "/process_comment",
        type: 'POST',
        data: {
            csrfmiddlewaretoken: window.CSRF_TOKEN,
            song_id: id,
        },
        success: function(response) {
            var comments_texts = JSON.parse(response.comments_texts);
            var comments_users = JSON.parse(response.comments_users)
            console.log(comments_users);
            console.log(comments_texts);
            for (let i = 0; i < comments_users.length; i++){
                var h6 = document.createElement("h6");
                var p = document.createElement("p")
                var text = document.createTextNode(comments_users[i]);
                var person = document.createTextNode(comments_texts[i]);
                h6.appendChild(text)
                p.appendChild(person)
                var parent = document.getElementById("all-comments")
                parent.appendChild(h6)
                parent.appendChild(p)
            }
        }
    });
}
function hideMusicplayer() {
    document.getElementById('musicplayer').style.display = "none";
    document.getElementById('musicplayer').style.height = "0";
    document.getElementById('underneath-footer').style.display = "none";
    
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
    // document.getElementById("musicplayer").style.transition = "all 0.3s";
    // document.getElementById("underneath-footer").style.transition = "all 0.3s";
    document.getElementById('musicplayer').style.height = "400px";
    document.getElementById('musicplayer-song-info').style.transform = "translate(0,-150px)"
    document.getElementById('musicplayer-control-buttons-container').style.transform = "translate(0,-150px)"
    document.getElementById('musicplayer-extra-buttons-container').style.transform = "translate(0,-150px)"
    document.getElementById('underneath-footer').style.display = "flex";
    document.getElementById('underneath-footer').style.height = "300px";
    document.getElementById('hide-button').style.opacity = "1.0";
}

function closePopup() {
    document.getElementById('underneath-footer').style.height = "0px";
    document.getElementById('musicplayer-song-info').style.transform = "translate(0,0px)"
    document.getElementById('musicplayer-control-buttons-container').style.transform = "translate(0,0px)"
    document.getElementById('musicplayer-extra-buttons-container').style.transform = "translate(0,0px)"
    document.getElementById('musicplayer').style.height = "100px";
    document.getElementById('hide-button').style.opacity = "0";
}

$( document ).ready(function() {
    $("#like-form").on("submit", function(e){
        var val = $("#favorite-button").val();
        $.ajax({
            url: "/index",
            type: 'POST',
            data: {
                csrfmiddlewaretoken: window.CSRF_TOKEN,
                button_value: val,
            },
            success: function(response) {
                popup();
                $("#display-likes-count").html("Likes:" + response.likes);
            }
        });
        e.preventDefault();
    });

    $('.playlist-form').on("submit", function(e){
        var playlistName = $(this).attr("data-playlist");
        console.log(playlistName);
        var songName = $("#musicplayer-song-name").html();
        console.log(songName);
        var songID = $("#favorite-button").val();
        console.log(songID);
        $.ajax({
            url: "/addtoplaylist",
            type: 'POST',
            data: {
                csrfmiddlewaretoken: window.CSRF_TOKEN,
                playlist_name: playlistName,
                song_ID: songID,
            },
            success: function(response) {
                console.log(playlistName);
            }
        });
        e.preventDefault();
    })

    $('#add-playlist-form').on("submit", function(e){
        var newPlaylist = $("#input-add-playlist").val();
        console.log(newPlaylist);
        $.ajax({
            url: "/new_playlist",
            type: 'POST',
            data: {
                csrfmiddlewaretoken: window.CSRF_TOKEN,
                new_playlist: newPlaylist,
            },
            success: function(r) {
                pass
            }
        });
    })

    $('#comment-form').on("submit", function(e){
        var commentText = $("#comment-input").val();
        console.log(commentText);
        e.preventDefault();
        $.ajax({
            url: "/add_comment",
            type: 'POST',
            data: {
                csrfmiddlewaretoken: window.CSRF_TOKEN,
                "comment_text": commentText,
                "song_id": currentSongID,
            },
            success: function(response) {
                console.log(response.comment);
            }
        });
    })
    if ($('#data').val() ==="contact" || $('#data').val() ==="upload" || $('#data').val() ==="profile"){
        hideMusicplayer();
        document.getElementById('underneath-footer').style.display = "none";
    }

});