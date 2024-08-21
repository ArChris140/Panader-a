document.addEventListener('DOMContentLoaded', function () {
    const form = document.getElementById('signup-form');

    form.addEventListener('submit', function (event) {
        const telefonoValue = document.getElementById('form2ExamplePhone').value;
        const passwordValue = document.getElementById('form2ExamplePassword').value;

        if (telefonoValue.length < 9) {
            alert('El número de teléfono debe tener al menos 9 dígitos.');
            event.preventDefault(); // Evita que se envíe el formulario si la validación del teléfono falla
        }

        if (passwordValue.length < 8) {
            alert('La contraseña debe tener al menos 8 caracteres.');
            event.preventDefault(); // Evita que se envíe el formulario si la validación de la contraseña falla
        }
    });
});
