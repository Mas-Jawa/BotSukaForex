# 🚀 Quick Start - Deploy SukaForex Bot ke GitHub + Vercel

## ⚡ Cara Cepat (5 Menit)

### Step 1: Upload ke GitHub

```bash
# 1. Masuk ke folder project
cd /path/to/sukaforex-bot

# 2. Init git
git init

# 3. Add semua file
git add .

# 4. Commit
git commit -m "Initial commit: SukaForex Bot ready for Vercel"

# 5. Connect ke GitHub (ganti USERNAME)
git remote add origin https://github.com/USERNAME/sukaforex-bot.git

# 6. Push
git push -u origin main
```

### Step 2: Deploy ke Vercel

1. Buka [vercel.com](https://vercel.com)
2. Login dengan **GitHub**
3. Klik **"Add New Project"** → **Import**
4. Pilih repo `sukaforex-bot`
5. Settings:
   - Framework: **Other**
   - Build Command: **Kosongkan**
   - Output Directory: **./**
6. Klik **Deploy** ✨

### Step 3: Selesai!

Website lu akan live di: `https://sukaforex-bot.vercel.app`

---

## 📁 Cek Struktur Sebelum Push

```bash
# Cek tree structure
tree -L 3 -I '__pycache__|node_modules|outputs|.git|.agent_hooks' -a
```

**Expected: 28 files, 5 directories**

---

## ✅ Checklist Sebelum Deploy

- [ ] Struktur folder sesuai dengan `GITHUB_STRUCTURE.md`
- [ ] File `vercel.json` ada di root
- [ ] Folder `api/` dengan semua file Python ada
- [ ] `.gitignore` sudah update
- [ ] Tidak ada file `.env`, `__pycache__`, `*.zip`, dll

---

## 🧪 Test API Setelah Deploy

### Test Pairs
```
https://sukaforex-bot.vercel.app/api/pairs
```

### Test Analyze
```
POST https://sukaforex-bot.vercel.app/api/analyze
Body: {"pair": "EURUSD"}
```

---

## 📖 Dokumentasi Lengkap

- `GITHUB_STRUCTURE.md` - Struktur repository lengkap
- `GITHUB_DEPLOY.md` - Guide deploy detail
- `DEPLOY_GUIDE.md` - Quick deploy guide
- `README.md` - Full documentation

---

**Happy Trading! 🚀📈**