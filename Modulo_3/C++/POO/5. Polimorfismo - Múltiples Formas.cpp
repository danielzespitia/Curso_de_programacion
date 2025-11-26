// El polimorfismo (del griego "muchas formas") permite que objetos de diferentes clases respondan al mismo mensaje (llamada a un método) de maneras distintas y específicas a su clase. 
// En C++, se implementa comúnmente a través de funciones virtuales.
//
// Una función virtual es una función miembro en una clase base que se espera que sea redefinida (sobrescrita) en las clases derivadas.
//
// Ejemplo de Polimorfismo
// Añadamos un método hacerSonido a nuestras clases. Obviamente, un perro y un gato hacen sonidos diferentes.

#include <iostream>

class Animal {
public:
    // La palabra clave 'virtual' y '= 0' la convierten en una función virtual pura.
    // Esto hace que Animal sea una clase abstracta.
    virtual void hacerSonido() = 0; 
};

class Perro : public Animal {
public:
    void hacerSonido() override { // 'override' es opcional pero recomendado
        std::cout << "Guau! Guau!" << std::endl;
    }
};

class Gato : public Animal {
public:
    void hacerSonido() override {
        std::cout << "Miau!" << std::endl;
    }
};

void sonidoAnimal(Animal* animal) {
    animal->hacerSonido();
}





int main() {
    Perro miPerro;
    Gato miGato;

    sonidoAnimal(&miPerro); // Salida: Guau! Guau!
    sonidoAnimal(&miGato);  // Salida: Miau!

    return 0;
}

// En este ejemplo, la función sonidoAnimal no sabe si está recibiendo un Perro o un Gato. 
// Simplemente sabe que recibe un Animal que puede hacerSonido. 
// El polimorfismo se encarga de llamar a la versión correcta del método en tiempo
