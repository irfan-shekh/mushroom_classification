#!/usr/bin/env python
"""
Root-level test script for Mushroom Classification ML models.
Can be run directly with: python test_models.py
"""
import sys
import importlib.util
from pathlib import Path

# Ensure UTF-8 output on Windows consoles
if sys.stdout.encoding and sys.stdout.encoding.lower() != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

# Add Code/mysite to sys.path to access polls models and sub-scripts
BASE_DIR = Path(__file__).resolve().parent
DJANGO_DIR = BASE_DIR / "Code" / "mysite"

if str(DJANGO_DIR) not in sys.path:
    sys.path.insert(0, str(DJANGO_DIR))

# Import the test runner
try:
    from Code.mysite.test_models import test_ml_models
except ImportError:
    spec = importlib.util.spec_from_file_location("test_models_inner", str(DJANGO_DIR / "test_models.py"))
    if spec and spec.loader:
        test_models_inner = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(test_models_inner)
        test_ml_models = test_models_inner.test_ml_models
    else:
        raise ImportError("Could not load test_models from Code/mysite/test_models.py")

if __name__ == '__main__':
    success = test_ml_models()
    sys.exit(0 if success else 1)
