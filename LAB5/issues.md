# Static Code Analysis — Issue Report

| Issue | Type | Line(s) | Description | Fix Approach |
|---|---|---|---|---|
| Unsafe use of `eval()` | Security | Verify from report | Evaluates a Python expression dynamically and may allow arbitrary code execution. | Replace `eval()` with a safe calculation using validated numeric inputs. |
| Mutable default argument | Bug | Verify from report | The default list `baggage_tags=[]` can be shared across multiple function calls. | Change the default to `None` and initialize a new list inside the function. |
| Broad exception handling | Bug / Quality | Verify from report | A bare `except:` with `pass` can silently hide errors during booking cancellation. | Catch specific exceptions and handle them appropriately. |
| Hard-coded token | Security | Verify from report | A token embedded directly in the source code may expose sensitive information. | Read the token from an environment variable instead of hard-coding it. |
| Use of MD5 for hashing | Security | Verify from report | MD5 is not suitable for security-sensitive hashing because it has known weaknesses. | Use an appropriate modern hashing algorithm if security-sensitive hashing is required. |
| Unused variable | Code Quality | Verify from report | The unused `airport_fee` variable adds unnecessary code and reduces readability. | Remove the variable if it is not required. |
| Unsafe command execution | Security | Verify from report | Using `os.system()` to execute a command can introduce command-injection risks if input is incorporated unsafely. | Replace shell execution with a safer alternative, such as `subprocess.run()` with an argument list and `shell=False`. |
| File handling | Code Quality | Verify from report | Opening a file without a context manager may leave file resources unmanaged if an error occurs. | Use a `with open(...)` statement to manage the file automatically. |

