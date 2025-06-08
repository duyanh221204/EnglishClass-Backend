from passlib.context import CryptContext

bcrypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class Hashing:
    @staticmethod
    def hash_password(plain_password: str) -> str:
        return bcrypt_context.hash(plain_password)

    @staticmethod
    def verify_password(plain_password: str, hashed_password: str) -> bool:
        return bcrypt_context.verify(plain_password, hashed_password)
