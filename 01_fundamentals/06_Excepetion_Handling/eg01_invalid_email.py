class InvalidEmailError(Exception):
    def __init__(self, email,msg="invalid email format"):
        self.email=email
        self.msg=msg
        super().__init__(self.msg)

    def __str__(self):
        return f"{self.email} -> {self.msg}"
    
def set_email(email):
    if '@' not in email:
        raise InvalidEmailError(email)
    print(f'Email set to:{email}')

try:
    set_email("mj.com")
except InvalidEmailError as e:
    print(e)