const setVertical = () => {
    const element = document.getElementById('pg-frontpage')
    element.classList.remove("photo-grid");
    element.classList.add("vertical-active");
    document.getElementById('grid').style.backgroundColor = '#FFFFFF'
    document.getElementById('vert').style.backgroundColor = '#000000'

    var elements = document.getElementsByClassName("big-card");
    for (var i = 0; i < elements.length; i++) {
        elements[i].classList.remove("card-wide")
        elements[i].classList.remove("card-tall")
    }
    var elements = document.getElementsByClassName("tall-card");
    for (var i = 0; i < elements.length; i++) {
        elements[i].classList.remove("card-tall")
    }
    var elements = document.getElementsByClassName("wide-card");
    for (var i = 0; i < elements.length; i++) {
        elements[i].classList.remove("card-wide")
    }
}
const setGrid = () => {
    const element = document.getElementById('pg-frontpage')
    element.classList.add("photo-grid");
    element.classList.remove("vertical-active");
    document.getElementById('grid').style.backgroundColor = '#000000'
    document.getElementById('vert').style.backgroundColor = '#FFFFFF'

    var elements = document.getElementsByClassName("big-card");
    for (var i = 0; i < elements.length; i++) {
        elements[i].classList.add("card-wide")
        elements[i].classList.add("card-tall")
    }
    var elements = document.getElementsByClassName("tall-card");
    for (var i = 0; i < elements.length; i++) {
        elements[i].classList.add("card-tall")
    }
    var elements = document.getElementsByClassName("wide-card");
    for (var i = 0; i < elements.length; i++) {
        elements[i].classList.add("card-wide")
    }
}
const openSort = () => {
    var el = document.getElementById("sort-list");
    if (el.style.display === "block") {
        el.style.display = "none";
    } else {
        el.style.display = "block";
    }
}

const search = () => {
    const searchTerm = document.getElementById('search-field').value
    console.log(searchTerm)
    let port = window.location.port === '80' ? '' : ':' + window.location.port
    window.location = location.protocol + "//" + location.hostname + port + '/search/?search=' + searchTerm;
}