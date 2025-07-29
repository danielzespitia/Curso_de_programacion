document.addEventListener('DOMContentLoaded', function() {
    const button = document.getElementById('changeTextColorBtn');
    const card = document.querySelector('.card-container');
    const elementsToChange = card.querySelectorAll('h1, .description, .interests-section h2, .interests-section li'); 

    const colors = [
        '#e74c3c',
        '#2980b9',
        '#8e44ad',
        '#f39c12',
        '#c0392b',
        '#d35400',
        '#3498db',
        '#9b59b6'
    ];

    let currentColorIndex = 0;

    button.addEventListener('click', function() {
        elementsToChange.forEach(element => {
            element.style.color = colors[currentColorIndex];
        });

        currentColorIndex++;

        if (currentColorIndex >= colors.length) {
            currentColorIndex = 0;
        }
    });

    const profileImage = document.getElementById('profileImage');
    const imageModal = document.getElementById('imageModal');
    const modalImg = document.getElementById("img01");
    const captionText = document.getElementById("caption");
    const closeButton = document.querySelector(".close-button");

    let isZoomed = false;

    profileImage.addEventListener('click', function(event) {
        event.preventDefault();
        imageModal.style.display = "block";
        modalImg.src = this.src;
        captionText.innerHTML = this.alt;
        modalImg.style.transform = 'scale(1)';
        modalImg.style.transformOrigin = 'center center';
        modalImg.classList.remove('zoomed');
        isZoomed = false;
    });

    closeButton.addEventListener('click', function() {
        imageModal.style.display = "none";
        modalImg.style.transform = 'scale(1)';
        modalImg.style.transformOrigin = 'center center';
        modalImg.classList.remove('zoomed');
        isZoomed = false;
    });

    window.addEventListener('click', function(event) {
        if (event.target == imageModal) {
            imageModal.style.display = "none";
            modalImg.style.transform = 'scale(1)';
            modalImg.style.transformOrigin = 'center center';
            modalImg.classList.remove('zoomed');
            isZoomed = false;
        }
    });

    modalImg.addEventListener('mousemove', function(e) {
        if (!isZoomed) return;

        const rect = this.getBoundingClientRect();
        const x = e.clientX - rect.left;
        const y = e.clientY - rect.top;
        const zoomLevel = 2;

        this.style.transformOrigin = `${x}px ${y}px`;
        this.style.transform = `scale(${zoomLevel})`;
    });

    modalImg.addEventListener('mouseleave', function() {
        if (!isZoomed) return;
        this.style.transform = 'scale(1)';
        this.style.transformOrigin = 'center center';
    });

    modalImg.addEventListener('click', function(e) {
        if (e.target.classList.contains('modal-content')) {
            isZoomed = !isZoomed;
            if (isZoomed) {
                const rect = this.getBoundingClientRect();
                const x = e.clientX - rect.left;
                const y = e.clientY - rect.top;
                const zoomLevel = 2;
                this.style.transformOrigin = `${x}px ${y}px`;
                this.style.transform = `scale(${zoomLevel})`;
                this.classList.add('zoomed');
            } else {
                this.style.transform = 'scale(1)';
                this.style.transformOrigin = 'center center';
                this.classList.remove('zoomed');
            }
        }
    });
});