# 🛰️ Telemost CLI

A simple command-line tool to interact with the [Yandex Telemost API](https://yandex.ru/dev/telemost/doc/ru/): create
video meetings, fetch conference info, and list cohosts.

---

## 📦 Setup

1. Create a `.env.local` file in the root directory:
   ```env
   BASE_URL=https://cloud-api.yandex.net/v1/telemost-api
   CLIENT_ID=your_client_id
   CLIENT_SECRET=your_client_secret
   OAUTH_TOKEN=your_oauth_token
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

---

## 🚀 Usage

### ▶️ Create a Conference

Create a conference without cohosts:

```bash
python telemost.py create
```

Create a conference and add cohosts:

```bash
python telemost.py create --add email@domain.com email2@domain.com
```

✅ **Response:**

```json
{
  "join_url": "https://telemost.yandex.ru/j/0000000000",
  "id": "0000000000"
}
```

---

### 📄 Get Conference Info

```bash
python telemost.py info --id 0000000000
```

✅ **Response:**

```json
{
  "access_level": "PUBLIC",
  "join_url": "https://telemost.yandex.ru/j/0000000000",
  "waiting_room_level": "PUBLIC",
  "id": "0000000000"
}
```

---

### 👥 Get Cohosts

```bash
python telemost.py cohosts --id 0000000000
```

✅ **Response:**

```json
{
  "cohosts": [
    {
      "email": "email@domain.com"
    }
  ]
}
```

---