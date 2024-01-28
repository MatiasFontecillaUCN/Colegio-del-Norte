from validate_email import validate_email
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt()
class ValidationHelpers:

    def validate_rut(rut):
        rut = rut.replace('.','').replace('-','')
        rut_len = len(rut)
        if not rut:
            raise ValueError('No se ingreso un rut')
        else:
            if rut_len < 8 or rut_len > 9:
                raise ValueError('El rut debe tener entre 8 y 9 caracteres')
            validator_digit = rut[len(rut) - 1]
            verify_rut = rut[:len(rut) - 1]
            if validator_digit == 'K':
                if not verify_rut.isdigit():
                    raise ValueError('El rut debe tener numeros antes del digito verificador')
            else:
                if validator_digit.isdigit():
                    if not verify_rut.isdigit():
                        raise ValueError('El rut debe tener numeros antes del digito verificador')
                else:
                    raise ValueError('El digito verificador debe ser un numero o K')
            rut_len = rut_len + 1
            rut = rut[:-1] + '-' + rut[-1]  # Add "-" before the last character
            rut = rut[:rut_len-8] + '.'+rut[rut_len-8:rut_len-5]+ "." + rut[rut_len-5:-2] + rut[-2:]  # Add "." before the 3rd and 6th last characters
            return rut
         
    def validate_email(email):
        if validate_email(email):
            return email
        else: 
            return False
        

    def validate_phone_number(phone):
        phone_len = len(phone)
        if phone_len == 11:
            if phone[0] == "5" and phone[1] == "6" and phone[2] == "9" and phone.isdigit():
                return phone
        else:
            return False
        
    #def validate_status(status):

    #def validate_status_user(status):

    #def validate_year_school(year):

    def hash_password(password):
        return bcrypt.generate_password_hash(password,8)

