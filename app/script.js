document.getElementById('geserKiri').addEventListener('click', function() {
    document.querySelector('.container').scrollBy({ left: -100, behavior: 'smooth' });
});

document.getElementById('geserKanan').addEventListener('click', function() {
    document.querySelector('.container').scrollBy({ left: 100, behavior: 'smooth' });
});

