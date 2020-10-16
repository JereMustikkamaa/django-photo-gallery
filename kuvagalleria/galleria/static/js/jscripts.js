
const setVertical = () => {
    console.log('setverti')
    const element = document.getElementById('pg-frontpage')
    element.classList.remove("photo-grid");
    element.classList.add("vertical-active");
    document.getElementById('grid').style.backgroundColor = '#FFFFFF'
    document.getElementById('vert').style.backgroundColor = '#000000'
}
const setGrid = () => {
    console.log('setgrid')
    const element = document.getElementById('pg-frontpage')
    element.classList.add("photo-grid");
    element.classList.remove("vertical-active");
    document.getElementById('grid').style.backgroundColor = '#000000'
    document.getElementById('vert').style.backgroundColor = '#FFFFFF'
}
const openSort = () => {
    var el = document.getElementById("sort-list");
    if (el.style.display === "block") {
        el.style.display = "none";
    } else {
        el.style.display = "block";
    }
}

