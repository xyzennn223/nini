from telethon import TelegramClient, events
import requests

# Masukkan API ID, API Hash, dan nomor Anda
api_id = "29020994"  # Ganti dengan API ID Anda
api_hash = "902755de45a3728b90abb019ce5cfd31"  # Ganti dengan API Hash Anda
phone_number = "6285134345907"  # Ganti dengan nomor Telegram Anda (format: +62...)

# Inisialisasi Telegram Client
client = TelegramClient('session_name', api_id, api_hash)

# Fungsi untuk memanggil API AI
def call_ai_api(query):
    url = f"https://api.diioffc.web.id/api/ai/gemini?query={query}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json().get("response", "Tidak ada jawaban.")
    else:
        return "Terjadi kesalahan saat mengakses API."

# Event handler untuk menerima pesan
@client.on(events.NewMessage)
async def handler(event):
    if event.text.startswith("/ai"):  # Trigger perintah
        query = event.text[4:].strip()  # Ambil teks setelah '/ai'
        if not query:
            await event.reply("Silakan masukkan pertanyaan setelah perintah /ai.")
        else:
            await event.reply("Sedang memproses...")
            try:
                response = call_ai_api(query)
                await event.reply(response)
            except Exception as e:
                await event.reply(f"Terjadi kesalahan: {str(e)}")

# Jalankan client
print("Bot sedang berjalan...")
client.start(phone=phone_number)  # Login menggunakan nomor Anda
client.run_until_disconnected()
