# Alpha Trader Client

A Python client for interacting with the Alpha Trader API.

## Setup

### 1. Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Environment Configuration

Copy the example environment file and configure your credentials:

```bash
cp .env.example .env
```

Edit the `.env` file with your Alpha Trader credentials:

```
USERNAME=your_username
PASSWORD=your_password
PARTNER_ID=your_partner_id
```

### 4. Run the Client

```bash
python client.py
```

## What it does

The client will:
1. Connect to the Alpha Trader API
2. Login with your credentials
3. Get your miner
4. Transfer coins automatically