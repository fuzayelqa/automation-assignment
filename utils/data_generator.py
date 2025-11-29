import secrets
import string
import time

def random_username(prefix: str = "emp") -> str:
    return f"{prefix}_{int(time.time())}_{secrets.randbelow(1000)}"

def random_password(length: int = 10) -> str:
    alphabet = string.ascii_letters + string.digits
    return "".join(secrets.choice(alphabet) for _ in range(length))
