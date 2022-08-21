function Random() {
    var rnd = Math.floor(Math.random() * 1000000000);
    document.getElementById('tb').value = rnd;
}