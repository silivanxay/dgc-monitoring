# DGC System Monitor

A real-time web dashboard for monitoring the status of Lao government digital services managed by the D-Government Center (ສູນບໍລິຫານລັດຖະກິດຈະດີຈິຕອນ).

## Features

- Live status checks for e-Office, G-Chat, G-Share, and E-Mail services
- HTTP response code and latency display per endpoint
- Online / Warning / Offline badge classification
- Auto-refresh every 60 seconds
- Lao-language UI with English labels

## Services Monitored

| Service | URL |
|---------|-----|
| e-Office (MTC) | https://mtc.eoffice.la |
| G-Chat | https://g-chat.gov.la |
| G-Share (G-Drive) | https://g-drive.gov.la |
| E-Mail Portal | https://mail.gov.la |

## Setup

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Run

```bash
streamlit run app.py
```

## Stack

- [Streamlit](https://streamlit.io) — UI framework
- [Requests](https://requests.readthedocs.io) — HTTP health checks
