import requests

api_endpoint = "http://127.0.0.1:8000/api/face-detect/"


class OCR(object):
    """
    Basically face detection from the API-Endpoint
    params: NID, selfie input 
    Return: When user provide NID card and selfie automatically accuracy or validation result return to the user
    """

    def __init__(self, nid_face, selfie):
        self.nid_face = nid_face
        self.selfie = selfie

    def face_validation(self):
        try:
            data = {'nid_face': self.nid_face, 'selfie': self.selfie}
            req = requests.post(api_endpoint, data=data, timeout=10)
            if req.json()['data']['accuracy'] > 80:
                res = {"accuracy": req.json()['data']['accuracy']}
                print(res)
            else:
                res = {"message": "Sorry! Image not match 80%"}
                print(res)
        except requests.Timeout:
            pass
        except requests.exceptions.ConnectionError as error:
            print("Error Connecting:", error)

    def calculation_accuracy(self):
        if self.nid_face is not None:
            pass
        else:
            return None


instance = OCR("NID bse64", "selfie image base64")
instance.face_validation()
