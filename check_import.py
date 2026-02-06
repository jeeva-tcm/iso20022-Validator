
import sys
import os
sys.path.append(os.path.join(os.getcwd(), "backend"))
try:
    from app.services.validator import ISOValidator
    print("Import Success")
    v = ISOValidator()
    print("Instance Success")
except Exception as e:
    import traceback
    traceback.print_exc()
