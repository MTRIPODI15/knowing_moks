# Java Module – Mocked Transfer Test

# Objective

This module simulates a bank transfer flow using mocked service responses. It helps validate how the system behaves when the backend is unavailable, using Java, JUnit 5, and Mockito.

# Tools

- Java 17+
- JUnit 5 – testing framework
- Mockito – mocking library
- Maven or Gradle – build tool

# Files

- `TransferServiceTest.java`: main test file
- `TransferService.java`: business logic
- `BankApi.java`: mocked interface
- `TransferResponse.java`: response model
- `diagrams/transfer_flow.png`: flow diagram

# Test Scenarios

1. ✅ Valid transfer between two accounts
2. ❌ Transfer with insufficient balance
3. ❌ Transfer with invalid account number

# How to run

### Using Maven

1. Open terminal in the `java/` folder
2. Run:

```bash
mvn test