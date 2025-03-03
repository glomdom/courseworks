import time

def student_information(**kwargs):
    for key, value in kwargs.items():
        print(f"{key.capitalize()}: {value}")

def time_tracker(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()

        print(f"Execution Time: {end_time - start_time:.2f} seconds.")
        
        return result
    
    return wrapper

@time_tracker
def slow_function():
    time.sleep(2)
    print("Finished running!")

def admin_required(func):
    def wrapper(*args, **kwargs):
        if kwargs.get("user_role") == "admin":
            kwargs.pop("user_role", None)

            return func(*args, **kwargs)
        else:
            print("Access Denied!")

    return wrapper

@admin_required
def delete_user():
    print("User Deleted!")

student_information(name="Emma", age=20, course="Computer Science", grade=4.5)
slow_function()
delete_user(user_role="admin")  # allowed
delete_user(user_role="guest")  # not allowed
