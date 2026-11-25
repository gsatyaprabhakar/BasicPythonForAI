import sys
import ipykernel

try:
    import pydantic  # type: ignore[import-not-found]
    print("pydantic imported successfully")
except ImportError:
    pydantic = None

print()
print("Python")
print(sys.executable)       ## Python exe location
## O/P ..................\.venv\Scripts\python.exe
print(sys.version)          ## Python version
print(sys.version_info)     ## Python version info


print()
print("ipykernel")
print(ipykernel.__version__)


print()
print("pydantic")
if pydantic is not None:
    print(pydantic.__version__)
else:
    print("pydantic not installed")
