public interface BankApi {
    TransferResponse transfer(String from, String to, int amount);
}