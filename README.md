# SukaForex Bot - Vercel Deployment Guide

## 🚀 Cara Deploy ke Vercel

### 1. Persiapan
- Pastikan sudah punya akun [Vercel](https://vercel.com)
- Install Vercel CLI: `npm i -g vercel`

### 2. Deploy Project
```bash
# Login ke Vercel
vercel login

# Deploy project
vercel
```

Ikuti instruksi di layar:
- Pilih "Link and deploy to an existing project" atau "Create a new project"
- Pilih framework "Other" (ini static site + serverless functions)
- Deploy!

### 3. Environment Variables (Opsional)
Tidak perlu environment variables untuk deployment ini karena:
- API key dari Yahoo Finance (gratis)
- Tidak menggunakan database
- Semua data diambil secara real-time dari public APIs

## ⚠️ Perubahan dari Versi Flask

### Yang Dihapus:
- ❌ Flask server (port 5000)
- ❌ SocketIO/WebSocket (real-time connection)
- ❌ Backend folder (sudah dikonversi ke serverless functions)

### Yang Ditambahkan:
- ✅ Vercel Serverless Functions di folder `api/`
- ✅ `vercel.json` untuk konfigurasi Vercel
- ✅ `api/requirements.txt` untuk Python dependencies

### Yang Berubah:
- 📝 Frontend sekarang menggunakan `/api` instead of `http://localhost:5000/api`
- 📝 Real-time updates diganti dengan polling (setiap 5 detik)
- 📝 WebSocket manager di-disable untuk Vercel serverless

## 📋 Struktur Project

```
/
├── index.html              # Halaman utama
├── app.js                  # JavaScript utama
├── styles.css              # Styling
├── vercel.json             # Konfigurasi Vercel
├── api/                    # Vercel Serverless Functions
│   ├── requirements.txt    # Python dependencies
│   ├── utils.py           # Shared utilities
│   ├── pairs.py           # Get available pairs
│   ├── data.py            # Get market data
│   ├── analyze.py         # Analyze market (FITUR UTAMA!)
│   └── price.py           # Get current price
├── frontend/              # Frontend modules
│   ├── api.js            # API client (sudah diupdate)
│   ├── websocket.js      # WebSocket manager (disabled)
│   ├── state.js          # State management
│   └── router.js         # Routing
└── backend/              # Folder lama (bisa dihapus)
```

## 🔧 API Endpoints

Semua endpoints diakses via `/api/...`:

- `GET /api/pairs` - Mendapatkan list trading pairs
- `GET /api/data/{pair}?timeframe={timeframe}` - Mendapatkan market data
- `POST /api/analyze` - Analisa market dan generate signal (FITUR UTAMA!)
- `GET /api/price/{pair}` - Mendapatkan harga saat ini

## 🎯 Fitur yang Tetap Berfungsi

✅ **Analisa Trading ICT & SNR** - Semua fitur analisa tetap berfungsi!
- RSI, MACD, Bollinger Bands
- EMA & ATR
- Support & Resistance levels
- ICT patterns (Order Blocks, FVG)
- Buy/Sell signals dengan Entry, SL, TP

✅ **Price Ticker** - Update harga real-time (via polling)
✅ **Chart Component** - Display market data
✅ **Multi-timeframe** - Support berbagai timeframe
✅ **Multi-pair** - Support 8 trading pairs

## 🐛 Troubleshooting

### Error: "Pastikan Python backend berjalan"
Ini error sudah diperbaiki! Sekarang backend berjalan sebagai Vercel serverless functions.

### Error: "CORS"
CORS sudah di-handle di semua API endpoints dengan headers:
```json
{
  "Access-Control-Allow-Origin": "*",
  "Access-Control-Allow-Methods": "GET, POST, OPTIONS",
  "Access-Control-Allow-Headers": "Content-Type"
}
```

### Deployment timeout
Jika deployment timeout saat build:
1. Cek `api/requirements.txt` - dependencies terlalu banyak
2. Pastikan semua dependencies compatible dengan Python 3.9

## 💡 Tips

1. **Testing lokal** - Deploy dulu ke Vercel untuk test, gak perlu install semua dependencies
2. **Performance** - Vercel serverless functions auto-scale, jadi gak perlu khawatir traffic
3. **Cost** - Gratis untuk hobby plan dengan 100GB bandwidth/bulan
4. **Updates** - Setiap push ke GitHub akan otomatis deploy jika connect repo

## 🎉 Selamat Trading!

Semua fitur analisa trading tetap berfungsi dengan sempurna. Happy trading bro! 🚀