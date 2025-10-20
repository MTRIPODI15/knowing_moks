public class TransferService {
    private BankApi api;

    public TransferService(BankApi api) {
        this.api = api;
    }

    public TransferResponse executeTransfer(String from, String to, int amount) {
        return api.transfer(from, to, amount);
    }
}