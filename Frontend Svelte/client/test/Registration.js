import { validateRUT } from "validar-rut";

function validateEmail(email) {
    const emailRegex = /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;
    const cleanEmail = email.trim();

    if (
        cleanEmail.length < 4 ||
        cleanEmail.length > 255 ||
        !emailRegex.test(cleanEmail)
    ) {
        return true;
    }

    return false;
}

function validateRut(rut) {
    const cleanRUT = String(rut).replace(/[.-]/g, "");

    if (cleanRUT.length < 7 || cleanRUT.length > 12) {
        return false;
    }
    const isValid = validateRUT(cleanRUT);
    return isValid;
}

QUnit.module('validate');

QUnit.test('email', asserts => {
    asserts.equal(validateEmail('prueba@gmail.com'), false);
    asserts.equal(validateEmail('correo_invalido'), true);
});

QUnit.test('rut', asserts => {
    asserts.equal(validateRut('20.784.533-7'), true);
    asserts.equal(validateRut('1234567890'), false);
});
