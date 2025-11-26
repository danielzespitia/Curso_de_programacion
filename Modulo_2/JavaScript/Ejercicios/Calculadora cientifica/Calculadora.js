// Definimos una clase Calculator para encapsular toda la lógica.
class Calculator {
    // El constructor inicializa la calculadora con los elementos de la pantalla.
    constructor(previousOperandTextElement, currentOperandTextElement) {
        this.previousOperandTextElement = previousOperandTextElement;
        this.currentOperandTextElement = currentOperandTextElement;
        this.angleMode = 'DEG'; // Modo de ángulo por defecto: Grados (Degrees)
        this.clear();
    }

    // Limpia todas las variables y la pantalla.
    clear() {
        this.currentOperand = '';
        this.previousOperand = '';
        this.operation = undefined;
        this.updateDisplay();
    }

    // Borra el último caracter del operando actual.
    delete() {
        this.currentOperand = this.currentOperand.toString().slice(0, -1);
    }

    // Agrega un número o un punto decimal al operando actual.
    appendNumber(number) {
        // Evita múltiples puntos decimales.
        if (number === '.' && this.currentOperand.includes('.')) return;
        this.currentOperand = this.currentOperand.toString() + number.toString();
    }
    
    // Maneja las funciones científicas.
    handleFunction(func) {
        if (this.currentOperand === '') return;

        switch (func) {
            case 'cos':
            case 'tan':
                this.currentOperand = this.trigonometric(func, parseFloat(this.currentOperand));
                break;
            case '√':
                this.currentOperand = Math.sqrt(parseFloat(this.currentOperand));
                break;
            default:
                return;
        }
        this.updateDisplay();
    }

    // Elige la operación a realizar.
    chooseOperation(operation) {
        if (this.currentOperand === '') return;
        if (this.previousOperand !== '') {
            this.compute();
        }
        this.operation = operation;
        this.previousOperand = this.currentOperand + ' ' + operation;
        this.currentOperand = '';
    }

    // Realiza el cálculo final.
    compute() {
        let computation;
        // Reemplazamos los símbolos de la UI por operadores de JS
        const expression = this.previousOperand.replace(/÷/g, '/').replace(/×/g, '*').replace(/\^/g, '**') + this.currentOperand;
        
        try {
            // Usamos el constructor Function para evaluar la expresión de forma segura.
            computation = new Function('return ' + expression)();
            if (isNaN(computation) || !isFinite(computation)) {
                throw new Error("Error de cálculo");
            }
        } catch (e) {
            computation = "Error";
        }

        this.currentOperand = computation;
        this.operation = undefined;
        this.previousOperand = '';
    }

    // Calcula funciones trigonométricas respetando el modo de ángulo.
    trigonometric(func, value) {
        let angle = value;
        if (this.angleMode === 'DEG') {
            // Convertimos grados a radianes porque Math.cos/tan usan radianes.
            angle = value * (Math.PI / 180);
        }
        switch (func) {
            case 'cos': return Math.cos(angle);
            case 'tan': return Math.tan(angle);
        }
    }

    // Actualiza lo que se ve en la pantalla de la calculadora.
    updateDisplay() {
        this.currentOperandTextElement.innerText = this.currentOperand;
        let displayOperation = this.operation || '';
        this.previousOperandTextElement.innerText = `${this.previousOperand} ${displayOperation}`;
    }
}


// --- SELECCIÓN DE ELEMENTOS DEL DOM ---
const numberButtons = document.querySelectorAll('[data-number]');
const operationButtons = document.querySelectorAll('[data-operation]');
const equalsButton = document.querySelector('[data-equals]');
const clearButton = document.querySelector('[data-clear]');
const deleteButton = document.querySelector('[data-delete]');
const functionButtons = document.querySelectorAll('[data-function]');
const previousOperandTextElement = document.querySelector('[data-previous-operand]');
const currentOperandTextElement = document.querySelector('[data-current-operand]');


// --- INICIALIZACIÓN DE LA CALCULADORA ---
const calculator = new Calculator(previousOperandTextElement, currentOperandTextElement);


// --- EVENT LISTENERS ---

// Para los botones de números
numberButtons.forEach(button => {
    button.addEventListener('click', () => {
        calculator.appendNumber(button.innerText);
        calculator.updateDisplay();
    });
});

// Para los botones de operaciones
operationButtons.forEach(button => {
    button.addEventListener('click', () => {
        calculator.chooseOperation(button.innerText);
        calculator.updateDisplay();
    });
});

// Para el botón de igual
equalsButton.addEventListener('click', button => {
    calculator.compute();
    calculator.updateDisplay();
});

// Para el botón de limpiar (AC)
clearButton.addEventListener('click', button => {
    calculator.clear();
    calculator.updateDisplay();
});

// Para el botón de borrar (DEL)
deleteButton.addEventListener('click', button => {
    calculator.delete();
    calculator.updateDisplay();
});

// Para los botones de funciones
functionButtons.forEach(button => {
    button.addEventListener('click', () => {
        calculator.handleFunction(button.dataset.function);
    });
});
