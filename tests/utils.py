
def assert_status_code(status_code: int):
    assert status_code == 200, f"Status code of {status_code} was recieved"

headers = {'Content-type': 'application/json; charset=UTF-8', }
