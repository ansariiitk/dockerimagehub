from app import app 

def test_home():
    response= app.test_client().get("/")

    assert response.status_code==200
    assert response.data== "This is Ansar from IIITK, Reg. no 2024PHD21006"
