from models.models import Users

def test_new_user():
    user = Users('217291313','test','test','password',1,'ex@gmail.com','991812665')
    assert user.rut == '21.729.131-3'
    assert user.password != 'password'
