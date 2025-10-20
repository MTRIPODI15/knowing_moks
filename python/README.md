# 🐍 Python Module – Mocked Transfer Test

# Objective

This module simulates a bank transfer flow using mocked responses. It helps validate how the system behaves when the backend is not available, using Python and `pytest`.

# Tools

- Python 3.11+
- `pytest`
- `responses` (for mocking HTTP requests)

# Files

- `test_transfer_mocked.py`: main test file
- `requirements.txt`: dependencies
- `diagrams/transfer_flow.png`: flow diagram

# Test Scenarios

1. ✅ Valid transfer between two accounts
2. ❌ Transfer with insufficient balance
3. ❌ Transfer with invalid account number

# How to run

```bash
pip install -r requirements.txt
pytest test_transfer_mocked.py