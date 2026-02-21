// El encapsulamiento es el principio de agrupar los datos y los métodos que los manipulan 
// dentro de una clase, y restringir el acceso directo a los datos. 
// Esto se logra mediante los especificadores de acceso:
//
// public: Los miembros son accesibles desde cualquier parte del código.
// private: Los miembros solo son accesibles desde dentro de la misma clase. Es la
// práctica recomendada para los atributos.
// protected: Similar a private, pero también permite el acceso desde clases hijas 
// (lo veremos en Herencia).
//
// Para acceder o modificar datos privados, se utilizan métodos públicos especiales, 
// comúnmente llamados getters y setters.
//
// Ejemplo de Encapsulamiento

#include <iostream>
#include <string>

class CuentaBancaria {
private:
    // Atributo privado
    double saldo;

public:
    // Constructor para inicializar el saldo
    CuentaBancaria(double saldoInicial) {
        if (saldoInicial >= 0) {
            saldo = saldoInicial;
        } else {
            saldo = 0;
        }
    }

    // Getter: Método público para obtener el saldo
    double getSaldo() {
        return saldo;
    }

    // Setter: Método público para depositar dinero
    void depositar(double monto) {
        if (monto > 0) {
            saldo += monto;
        }
    }
    
    // Otro método que usa el dato privado
    bool retirar(double monto) {
        if (monto > 0 && saldo >= monto) {
            saldo -= monto;
            return true; // Retiro exitoso
        }
        return false; // Fondos insuficientes
    }
};

int main() {
    CuentaBancaria miCuenta(1000.0);

    // No podemos hacer esto porque 'saldo' es privado:
    // miCuenta.saldo = -500; // ¡ERROR DE COMPILACIÓN!

    // Usamos los métodos públicos para interactuar con el objeto
    miCuenta.depositar(500.0);
    std::cout << "Saldo actual: $" << miCuenta.getSaldo() << std::endl; // Salida: Saldo actual: $1500

    miCuenta.retirar(200.0);
    std::cout << "Saldo después del retiro: $" << miCuenta.getSaldo() << std::endl; // Salida: Saldo después del retiro: $1300

    return 0;
}

// Ventaja: El encapsulamiento nos da control sobre cómo se accede y se modifican los datos, asegurando la