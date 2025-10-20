import nock from 'nock';
import axios from 'axios';

const BASE_URL = 'https://api.mockbank.com';

describe('Mocked Bank Transfer Tests', () => {
  afterEach(() => {
    nock.cleanAll(); // Limpia los mocks después de cada test
  });

  test(' Valid transfer', async () => {
    // Simulamos una respuesta exitosa
    nock(BASE_URL)
      .post('/transfer')
      .reply(200, { status: 'success', message: 'Transfer completed' });

    const payload = {
      from_account: '123456',
      to_account: '654321',
      amount: 100
    };

    const response = await axios.post(`${BASE_URL}/transfer`, payload);

    expect(response.status).toBe(200);
    expect(response.data.status).toBe('success');
    expect(response.data.message).toContain('Transfer completed');
  });

  test(' Insufficient balance', async () => {
    // Simulamos error por saldo insuficiente
    nock(BASE_URL)
      .post('/transfer')
      .reply(400, { status: 'error', message: 'Insufficient balance' });

    const payload = {
      from_account: '123456',
      to_account: '654321',
      amount: 1000000
    };

    try {
      await axios.post(`${BASE_URL}/transfer`, payload);
    } catch (error) {
      expect(error.response.status).toBe(400);
      expect(error.response.data.status).toBe('error');
      expect(error.response.data.message).toContain('Insufficient balance');
    }
  });

  test(' Invalid account number', async () => {
    // Simulamos error por cuenta inválida
    nock(BASE_URL)
      .post('/transfer')
      .reply(404, { status: 'error', message: 'Invalid account number' });

    const payload = {
      from_account: '000000',
      to_account: '654321',
      amount: 50
    };

    try {
      await axios.post(`${BASE_URL}/transfer`, payload);
    } catch (error) {
      expect(error.response.status).toBe(404);
      expect(error.response.data.status).toBe('error');
      expect(error.response.data.message).toContain('Invalid account number');
    }
  });
});