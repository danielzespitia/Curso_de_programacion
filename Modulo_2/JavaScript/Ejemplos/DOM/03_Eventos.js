// 1. Evento de Input (Teclado/Entrada)
const input = document.getElementById('input-nombre');
const saludo = document.getElementById('saludo-nombre');

// 'input' se dispara cada vez que el valor cambia (mientras escribes)
input.addEventListener('input', (evento) => {
    // evento.target es el elemento que disparó el evento (el input)
    // evento.target.value es lo que está escrito
    const textoEscrito = evento.target.value;
    
    if (textoEscrito === '') {
        saludo.textContent = '...';
    } else {
        saludo.textContent = textoEscrito;
    }
});

// 2. Eventos de Mouse
const caja = document.getElementById('mi-caja');

// Click
caja.addEventListener('click', () => {
    console.log('Hiciste click en la caja');
    // Toggle alterna la clase: si está la quita, si no está la pone
    caja.classList.toggle('rojo');
    
    if (caja.classList.contains('rojo')) {
        caja.textContent = '¡Soy Rojo!';
    } else {
        caja.textContent = 'Pasa el mouse o haz click';
    }
});

// Mouse Enter (cuando el mouse entra al área)
caja.addEventListener('mouseenter', () => {
    caja.style.border = '5px solid black';
});

// Mouse Leave (cuando el mouse sale del área)
caja.addEventListener('mouseleave', () => {
    caja.style.border = 'none';
});

// 3. Evento de Carga (DOMContentLoaded)
// Es buena práctica envolver tu código aquí si el script está en el <head>
// para asegurar que el HTML ya existe antes de intentar buscar elementos.
document.addEventListener('DOMContentLoaded', () => {
    console.log('El DOM ha sido cargado completamente');
});
