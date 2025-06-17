from functools import wraps
from time import time
from typing import Callable, Any

def time_tracker(func: Callable) -> Callable:
    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        start = time()
        result = func(*args, **kwargs)
        end = time()

        print(f"'{func.__name__}' executed in {end - start:.6f}s")

        return result

    return wrapper

def require_admin(func: Callable) -> Callable:
    @wraps(func)
    def wrapper(self, *args: Any, **kwargs: Any) -> Any:
        if not self.logged_user or self.logged_user.access_level() != "admin":
            return

        return func(self, *args, **kwargs)

    return wrapper
