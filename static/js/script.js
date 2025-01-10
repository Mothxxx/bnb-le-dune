// Variabile per evitare scroll simultanei
let isScrolling = false;

// Inizializzazione della mappa
function initMap() {
    const location = { lat: 40.4168, lng: -3.7038 }; // Sostituisci con la posizione del tuo B&B
    const map = new google.maps.Map(document.getElementById('map'), {
        zoom: 12,
        center: location,
    });
    const marker = new google.maps.Marker({
        position: location,
        map: map,
        title: 'Le Dune Residence',
    });
}

document.querySelector('.scroll-to-rooms').addEventListener('click', function(e) {
    e.preventDefault(); // Impedisce il comportamento di default
    document.querySelector('#rooms').scrollIntoView({
        behavior: 'smooth',
        block: 'start'
    });
});

// Funzione per scorrere tra le sezioni
function scrollToSection(direction) {
    if (isScrolling) return;  // Blocca lo scroll se è già in corso

    isScrolling = true;

    // Trova tutte le sezioni
    const sections = document.querySelectorAll('.cover, .rooms');
    let currentSectionIndex = -1;
    
    // Trova la sezione corrente
    sections.forEach((section, index) => {
        if (section.getBoundingClientRect().top <= 0 && section.getBoundingClientRect().bottom > 0) {
            currentSectionIndex = index;
        }
    });

    // Determina quale sezione scorrere: successiva o precedente
    let nextSectionIndex = direction === 'down' ? currentSectionIndex + 1 : currentSectionIndex - 1;

    // Assicurati che l'indice non esca dai limiti
    if (nextSectionIndex < 0) nextSectionIndex = 0;
    if (nextSectionIndex >= sections.length) nextSectionIndex = sections.length - 1;

    const nextSection = sections[nextSectionIndex];

    // Scorri fino alla nuova sezione
    window.scrollTo({
        top: nextSection.offsetTop,
        behavior: 'smooth'
    });

    // Rimuovi il blocco di scrolling dopo 1 secondo
    setTimeout(() => isScrolling = false, 1000);  // Tempo per la transizione
}

// Gestione dello scroll con trackpad o mouse
document.addEventListener('wheel', function(e) {
    if (isScrolling) return;  // Blocca lo scroll se è già in corso

    isScrolling = true;

    // Scopri la direzione dello scroll
    const direction = e.deltaY > 0 ? 'down' : 'up';

    // Chiama la funzione di scroll in base alla direzione
    scrollToSection(direction);

    // Rimuovi il blocco di scrolling dopo 1 secondo
    setTimeout(() => isScrolling = false, 1000);  // Tempo per la transizione
});
