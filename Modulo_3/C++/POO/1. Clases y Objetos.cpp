#include <string>
#include <iostream>

using namespace std;

class Carro {
public:
    // Atributos (Miembros de datos)
    std::string marca;
    std::string modelo;
    int anio;
    int velocidad;

    // Métodos (Funciones miembro)
    void acelerar(int aumento) {
        velocidad += aumento;
    }

    void frenar(int decremento) {
        velocidad -= decremento;
    }

    void mostrarInfo() {
        cout << "Marca: " << marca << ", Modelo: " << modelo << ", Año: " << anio << ", Velocidad: " << velocidad << " km/h" << endl;
    }
};