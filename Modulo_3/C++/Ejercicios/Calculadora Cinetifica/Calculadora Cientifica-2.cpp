


//codigo


#include <iostream>
#include <cmath>
#define PI 3.14159265


using namespace std;

int main(){

    double num1;
    double num2;
    double resultado = 0.0;
    int menuselect;


    cout << "SUMA - 1" << endl;
    cout << "RESTA - 2" << endl;
    cout << "MULTIPLICACION - 3" << endl;
    cout << "DIVISION - 4" << endl;
    cout << "POTENCIA - 5" << endl;
    cout << "RAIZ CUADRADA - 6" << endl;
    cout << "SENO - 7" << endl;
    cout << "COSENO - 8" << endl;
    cout << "TANGENTE - 9" << endl;
    cout << "LOGARITMO NEPERIANO - 10" << endl;
    cout << "Seleccione su operacion: " << endl;
    cin >> menuselect;

    switch (menuselect)
    {
    case 1:
        cout << "Introduce el primer numero: ";
        cin >> num1;
        cout << "Introduce el segundo numero: ";
        cin >> num2;

        resultado = num1 + num2;
        
        cout << resultado;
        break;
    case 2:
        cout << "Introduce el primer numero: ";
        cin >> num1;
        cout << "Introduce el segundo numero: ";
        cin >> num2;

        resultado = num1 - num2;
        
        cout << resultado;
        break;
    case 3:
        cout << "Introduce el primer numero: ";
        cin >> num1;
        cout << "Introduce el segundo numero: ";
        cin >> num2;

        resultado = num1 * num2;
        
        cout << resultado;
        break;
    case 4:
        cout << "Introduce el primer numero: ";
        cin >> num1;
        cout << "Introduce el segundo numero: ";
        cin >> num2;

        resultado = num1 / num2;
        
        cout << resultado;
        break;
    case 5:
        cout << "Introduce el primer numero: ";
        cin >> num1;
        cout << "Introduce el segundo numero: ";
        cin >> num2;

        resultado = pow(num1, num2);
        
        cout << resultado;
        break;
    case 6:
        cout << "Introduce el numero: ";
        cin >> num1;

        resultado = sqrt(num1);

        cout << resultado;
        break;
    case 7:
        cout << "Introduce el numero: ";
        cin >> num1;

        resultado = sin (num1*PI/180);
        
        cout << resultado;
        break;
    case 8:
        cout << "Introduce el numero: ";
        cin >> num1;

        resultado = cos (num1*PI/180);
        
        cout << resultado;
        break;
    case 9:
        cout << "Introduce el numero: ";
        cin >> num1;

        resultado = tan (num1*PI/180);
        
        cout << resultado;
        break;
    case 10:
        cout << "Introduce el numero: ";
        cin >> num1;

        resultado = log (num1);
        
        cout << resultado;
        break;
    default:
        cout << "Nada";
        break;
    }
}