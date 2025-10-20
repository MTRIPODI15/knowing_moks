import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;
import static org.mockito.Mockito.*;

public class TransferServiceTest {

    @Test
    public void testValidTransfer() {
        BankApi mockApi = mock(BankApi.class);
        when(mockApi.transfer("123456", "654321", 100))
            .thenReturn(new TransferResponse("success", "Transfer completed"));

        TransferService service = new TransferService(mockApi);
        TransferResponse response = service.executeTransfer("123456", "654321", 100);

        assertEquals("success", response.getStatus());
        assertEquals("Transfer completed", response.getMessage());
    }

    @Test
    public void testInsufficientBalance() {
        BankApi mockApi = mock(BankApi.class);
        when(mockApi.transfer("123456", "654321", 1000000))
            .thenReturn(new TransferResponse("error", "Insufficient balance"));

        TransferService service = new TransferService(mockApi);
        TransferResponse response = service.executeTransfer("123456", "654321", 1000000);

        assertEquals("error", response.getStatus());
        assertEquals("Insufficient balance", response.getMessage());
    }

    @Test
    public void testInvalidAccount() {
        BankApi mockApi = mock(BankApi.class);
        when(mockApi.transfer("000000", "654321", 50))
            .thenReturn(new TransferResponse("error", "Invalid account number"));

        TransferService service = new TransferService(mockApi);
        TransferResponse response = service.executeTransfer("000000", "654321", 50);

        assertEquals("error", response.getStatus());
        assertEquals("Invalid account number", response.getMessage());
    }
}