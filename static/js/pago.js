function submitForm() {
    var selectedTime = document.getElementById('time').value;

    // Validar que la hora seleccionada esté dentro del rango permitido
    var minTime = new Date('1970-01-01T08:00:00');
    var maxTime = new Date('1970-01-01T19:00:00');
    var selectedDateTime = new Date('1970-01-01T' + selectedTime + ':00');

    if (selectedDateTime >= minTime && selectedDateTime <= maxTime) {
        // Aquí puedes agregar lógica adicional o enviar el formulario
        alert("¡Gracias por tu compra!");
        return true; // Envía el formulario
    } else {
        alert("Selecciona una hora válida entre las 8 AM y las 7 PM.");
        return false; // Evita el envío del formulario
    }
}
