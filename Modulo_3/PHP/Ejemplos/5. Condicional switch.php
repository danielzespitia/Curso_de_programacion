<?php
echo "## 4. Ejemplo de switch ##\n";

$metodoDePago = "tarjeta";

switch ($metodoDePago) {
    case "efectivo":
        echo "Pago en efectivo seleccionado. Prepara el monto exacto.\n";
        break; // 'break' es crucial para salir del switch después de encontrar una coincidencia.

    case "tarjeta":
        echo "Pago con tarjeta de débito/crédito seleccionado. Inserta o desliza la tarjeta.\n";
        break;

    case "transferencia":
        echo "Pago por transferencia seleccionado. Muestra el comprobante.\n";
        break;
        
    case "paypal":
        echo "Pago con PayPal seleccionado. Serás redirigido para completar la transacción.\n";
        break;

    default:
        // El bloque 'default' es opcional y se ejecuta si ningún 'case' coincide.
        echo "Método de pago no válido o no seleccionado.\n";
        break;
}
?>