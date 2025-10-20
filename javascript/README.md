# JavaScript Module – Mocked Transfer Test

# Objective

This module simulates a bank transfer flow using mocked HTTP responses. It helps validate how the system behaves when the backend is not available, using Node.js and Jest.

# Tools

- Node.js 18+
- `jest` – testing framework
- `nock` – HTTP mocking library
- `axios` – HTTP client

# Files

- `test_transfer_mocked.mjs`: main test file
- `package.json`: dependencies and test script
- `diagrams/transfer_flow.png`: flow diagram

# Test Scenarios

1. ✅ Valid transfer between two accounts
2. ❌ Transfer with insufficient balance
3. ❌ Transfer with invalid account number

# How to run

1. Install dependencies:

```bash
npm install