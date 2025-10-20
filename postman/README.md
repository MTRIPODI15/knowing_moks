# Postman Module – Mocked Transfer Test

# Objective

This module simulates a bank transfer flow using mocked API responses in Postman. It helps validate business logic and error handling without relying on a real backend.

# Tools

- Postman desktop or web app
- Postman Mock Server or example responses
- JSON collection export

# Files

- `Transfer_Mocked.postman_collection.json`: exported test collection
- `diagrams/transfer_flow.png`: flow diagram
- `evidence/`: screenshots of test results

# Test Scenarios

1. ✅ Valid transfer between two accounts
2. ❌ Transfer with insufficient balance
3. ❌ Transfer with invalid account number