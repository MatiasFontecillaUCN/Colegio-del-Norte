from models.models import Students


def test_check_student(test_client,create_student):
    student = create_student
    response = test_client.get('/student/'+student.rut)
    data = response.get_json()
    assert data.get('exists') == True