void incrementar(int& numero) {
    numero++; // Modifica la variable original
}

int main() {
    int miNumero = 10;
    incrementar(miNumero);
    std::cout << miNumero; // Salida: 11
    return 0;
}