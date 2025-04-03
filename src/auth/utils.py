from passlib.context import CryptContext

passwd_context = CryptContext(
    schemes=['bcrypt']
)

def generate_password_hash(password:str) -> str:
    hash = passwd_context(password)
    return hash

def verify_password(password:str, hash:str) -> bool:
    return passwd_context.verify(password, hash)