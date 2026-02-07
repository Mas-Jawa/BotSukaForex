# 🚀 Quick Deploy ke Vercel

## Cara Cepat Deploy

### Option 1: Via Vercel CLI (Rekomendasi)

```bash
# 1. Install Vercel CLI
npm i -g vercel

# 2. Login
vercel login

# 3. Deploy dari folder project
vercel

# 4. Ikuti instruksi:
# - Link to existing project? N
# - Project name: sukaforex-bot
# - Framework: Other
# - Build command: (biarkan kosong)
# - Output directory: ./ (root folder)
```

### Option 2: Via Dashboard

1. Buka [vercel.com/new](https://vercel.com/new)
2. Import dari GitHub atau upload files
3. Settings:
   - Framework Preset: **Other**
   - Build Command: (kosongkan)
   - Output Directory: `./`
4. Deploy! 🎉

## 🔍 Test Setelah Deploy

Setelah deploy selesai, buka URL Vercel dan test:

1. **Test API Pairs**
   ```
   https://your-project.vercel.app/api/pairs
   ```

2. **Test API Data**
   ```
   https://your-project.vercel.app/api/data/EURUSD?timeframe=1h
   ```

3. **Test API Analyze** (FITUR UTAMA!)
   ```
   POST https://your-project.vercel.app/api/analyze
   Body: {"pair": "EURUSD"}
   ```

4. **Test API Price**
   ```
   https://your-project.vercel.app/api/price/EURUSD
   ```

## ⚠️ Note

- **Mock Data**: Karena Yahoo Finance API ada timezone issue, sistem otomatis fallback ke mock data yang realistic
- **Semua Fitur Analisa Tetap Berfungsi**: RSI, MACD, Bollinger, EMA, ATR, Support/Resistance, ICT Patterns (Order Blocks, FVG)
- **Real-time**: Harga update via polling (setiap 5 detik)
- **WebSocket**: Disabled (tidak bisa di serverless Vercel)

## 🎯 Fitur yang Berfungsi

✅ Analisa trading ICT & SNR lengkap
✅ Support 8 trading pairs (EURUSD, GBPUSD, USDJPY, USDCHF, AUDUSD, NZDUSD, USDCAD, XAUUSD)
✅ Multi-timeframe (1h, 4h, 1d, dll)
✅ Signal Buy/Sell/Wait dengan Entry, SL, TP
✅ Technical indicators lengkap
✅ Support & Resistance levels otomatis
✅ ICT patterns detection (Order Blocks, FVG)

## 🐛 Jika Error

### Error: "Pastikan Python backend berjalan"
**SOLVED!** Ini error dari versi Flask lama. Sekarang backend sudah dikonversi ke Vercel serverless functions.

### Error: CORS atau 404
Pastikan:
- `vercel.json` ada di root folder
- File `api/*.py` ada
- `api/requirements.txt` ada

### Deployment timeout
Cek:
- `api/requirements.txt` - dependencies compatible dengan Python 3.9
- Remove unnecessary dependencies

## 📞 Support

Kalau masih ada masalah:
1. Cek Vercel logs di dashboard
2. Pastikan file `vercel.json` benar
3. Cek API handlers di folder `api/`

---

**Happy Trading! 🚀**