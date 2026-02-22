from pydantic import BaseModel, TypeAdapter, ValidationError, StrictStr

# ------------------------------------------------------------
# TypeAdapter: validate a single value without a model
# ------------------------------------------------------------

# Create a TypeAdapter that knows how to validate an int
UserId = TypeAdapter(int)

# Passing a real int -> accepted as-is
print(UserId.validate_python(42))  # 42

# Passing a string -> automatically coerced to int
print(UserId.validate_python("42"))  # 42

# Passing an invalid string -> raises ValidationError
try:
    print(UserId.validate_python("forty-two"))
except ValidationError as e:
    print("Validation failed for forty-two:", e)


# ------------------------------------------------------------
# BaseModel: structured validation for multiple fields
# ------------------------------------------------------------

class User(BaseModel):
    # int allows coercion (e.g. "42" -> 42)
    user_id: int

    # StrictStr disables coercion:
    # the value must already be a string
    username: StrictStr


# Valid input: correct types
usr = User(user_id=42, username="alice")
print(usr)

# Invalid input: username is an int, not a string
try:
    User(user_id=42, username=123)
except ValidationError as e:
    print("\nValidation failed for 123:", e)