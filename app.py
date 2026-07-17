import streamlit as st
import requests
import time
import urllib3
import base64
from pathlib import Path

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def _img_b64(path: str) -> str:
    return base64.b64encode(Path(path).read_bytes()).decode()

LOGO_B64 = _img_b64("assets/dgc.png")
EOFFICE_B64 = _img_b64("assets/e-office.png")
GCHAT_B64   = _img_b64("assets/g-chat.png")
GDRIVE_B64  = _img_b64("assets/g-drive.png")

FONT_REGULAR_B64 = _img_b64("assets/fonts/Phetsarath-Regular.ttf")
FONT_BOLD_B64    = _img_b64("assets/fonts/Phetsarath-Bold.ttf")

st.set_page_config(
    page_title="DGC System Monitor",
    page_icon="🖥️",
    layout="wide"
)

_FONT_CSS = f"""
    <style>
    @font-face {{
        font-family: 'Phetsarath';
        font-weight: 400;
        src: url('data:font/truetype;base64,{FONT_REGULAR_B64}') format('truetype');
    }}
    @font-face {{
        font-family: 'Phetsarath';
        font-weight: 700;
        src: url('data:font/truetype;base64,{FONT_BOLD_B64}') format('truetype');
    }}
    </style>
"""

st.markdown(_FONT_CSS, unsafe_allow_html=True)

st.markdown("""
    <style>
    html, body, [class*="css"] {
        font-family: 'Phetsarath', sans-serif;
        background-color: #f0f4f8 !important;
    }

    /* ── Top header bar ── */
    .dgc-header {
        background: linear-gradient(135deg, #1a3d8f 0%, #2a5fc1 100%);
        padding: 0 40px;
        height: 64px;
        display: flex;
        align-items: center;
        justify-content: space-between;
        position: fixed;
        top: 0; left: 0; right: 0;
        z-index: 1000;
        box-shadow: 0 2px 12px rgba(26,61,143,0.35);
    }

    .dgc-header-left {
        display: flex;
        align-items: center;
        gap: 14px;
    }

    .dgc-logo-circle {
        width: 44px; height: 44px;
        border-radius: 50%;
        background: white;
        display: flex; align-items: center; justify-content: center;
        overflow: hidden;
        padding: 2px;
        flex-shrink: 0;
        border: 2px solid rgba(255,255,255,0.4);
    }

    .dgc-header-title {
        color: white;
        font-size: 1.05rem;
        font-weight: 700;
        line-height: 1.2;
        font-family: 'Phetsarath', sans-serif;
    }

    .dgc-header-title span {
        display: block;
        font-size: 0.7rem;
        font-weight: 400;
        opacity: 0.8;
        font-family: 'Phetsarath', sans-serif;
        letter-spacing: 0.03em;
    }

    .dgc-header-time {
        color: rgba(255,255,255,0.85);
        font-size: 0.82rem;
        font-weight: 600;
        font-family: 'Phetsarath', monospace;
    }

    /* ── Page layout ── */
    .block-container {
        padding-top: 88px !important;
        padding-left: 2rem !important;
        padding-right: 2rem !important;
        max-width: 1280px !important;
    }

    /* ── Section title bar ── */
    .section-bar {
        background: linear-gradient(90deg, #1a3d8f 0%, #2a5fc1 100%);
        color: white;
        padding: 10px 20px;
        border-radius: 10px;
        font-size: 1rem;
        font-weight: 700;
        margin-bottom: 16px;
        display: flex;
        align-items: center;
        gap: 8px;
        font-family: 'Phetsarath', sans-serif;
    }

    /* ── Service card wrapper ── */
    div[data-testid="stVerticalBlockBorderWrapper"] {
        background-color: #ffffff !important;
        border-radius: 12px !important;
        border: 1px solid #dde6f5 !important;
        box-shadow: 0 2px 12px rgba(26,61,143,0.08) !important;
        padding: 20px !important;
        margin-bottom: 14px !important;
        transition: box-shadow 0.2s ease, transform 0.2s ease;
    }

    div[data-testid="stVerticalBlockBorderWrapper"]:hover {
        box-shadow: 0 6px 24px rgba(26,61,143,0.15) !important;
        transform: translateY(-2px);
        border-color: #a8c0e8 !important;
    }

    div[data-testid="stVerticalBlockBorderWrapper"] > div {
        padding: 0 !important;
    }

    /* ── Card internals ── */
    .card-top {
        display: flex;
        justify-content: space-between;
        align-items: flex-start;
        margin-bottom: 14px;
    }

    .card-icon {
        width: 42px; height: 42px;
        border-radius: 10px;
        background: linear-gradient(135deg, #e8effc, #c8d8f8);
        display: flex; align-items: center; justify-content: center;
        font-size: 1.3rem;
        flex-shrink: 0;
        margin-right: 12px;
        overflow: hidden;
    }

    .card-icon img {
        width: 100%; height: 100%;
        object-fit: cover;
        border-radius: 10px;
    }

    .card-title-group {
        display: flex;
        align-items: center;
        flex: 1;
        min-width: 0;
    }

    .system-name {
        font-size: 1.1rem;
        font-weight: 800;
        color: #1a3d8f;
        margin: 0 0 2px 0;
        font-family: 'Phetsarath', sans-serif;
    }

    .system-name-en {
        font-size: 0.72rem;
        color: #7a9cc8;
        font-weight: 600;
        font-family: 'Phetsarath', sans-serif;
        letter-spacing: 0.05em;
        text-transform: uppercase;
    }

    /* ── Status badges ── */
    .badge {
        padding: 5px 13px;
        border-radius: 20px;
        font-size: 0.72rem;
        font-weight: 800;
        letter-spacing: 0.06em;
        text-transform: uppercase;
        white-space: nowrap;
        flex-shrink: 0;
    }
    .badge-online  { background: #e6f9f1; color: #0a7a4a; border: 1px solid #9ee8c5; }
    .badge-warning { background: #fff8e6; color: #b05e00; border: 1px solid #f5cc7a; }
    .badge-offline { background: #fde8e8; color: #b91c1c; border: 1px solid #f5a0a0; }

    /* ── Metric pills ── */
    .metrics-row {
        display: flex;
        gap: 8px;
        margin-bottom: 12px;
        flex-wrap: wrap;
    }

    .metric-pill {
        display: flex;
        align-items: center;
        gap: 6px;
        background: #f0f5ff;
        border: 1px solid #d0dff8;
        border-radius: 6px;
        padding: 6px 11px;
        font-size: 0.78rem;
        font-weight: 700;
        color: #2a4a80;
    }

    .metric-dot {
        width: 7px; height: 7px;
        border-radius: 50%;
        flex-shrink: 0;
    }
    .dot-green  { background: #10b981; box-shadow: 0 0 4px rgba(16,185,129,0.5); }
    .dot-yellow { background: #f59e0b; box-shadow: 0 0 4px rgba(245,158,11,0.5); }
    .dot-red    { background: #ef4444; box-shadow: 0 0 4px rgba(239,68,68,0.5); }

    /* ── URL bar ── */
    .url-bar {
        font-size: 0.72rem;
        color: #8aa6cc;
        font-family: 'Courier New', monospace;
        white-space: nowrap;
        overflow: hidden;
        text-overflow: ellipsis;
        padding-top: 10px;
        border-top: 1px solid #e8eef8;
    }

    /* ── Refresh button ── */
    .stButton > button {
        background: linear-gradient(135deg, #1a3d8f, #2a5fc1) !important;
        color: white !important;
        border-radius: 10px !important;
        height: 48px !important;
        font-weight: 700 !important;
        font-size: 0.9rem !important;
        width: 100% !important;
        margin-top: 8px !important;
        border: none !important;
        letter-spacing: 0.04em;
        transition: opacity 0.2s;
    }
    .stButton > button:hover { opacity: 0.88 !important; }

    /* ── Footer ── */
    .footer-note {
        text-align: center;
        margin-top: 20px;
        color: #7a9cc8;
        font-size: 0.8rem;
        font-weight: 600;
        padding: 10px;
        background: white;
        border-radius: 8px;
        border: 1px solid #dde6f5;
    }

    /* Hide default streamlit header */
    header[data-testid="stHeader"] { display: none !important; }
    </style>
""", unsafe_allow_html=True)

# ── helpers ───────────────────────────────────────────────────────────────────

def check_server(url: str, timeout: int = 10) -> tuple[str, str, str]:
    """Return (status_label, detail_text, badge_class)."""
    try:
        t0 = time.time()
        r = requests.get(url, timeout=timeout, verify=False,  # noqa: S501
                         allow_redirects=True)
        ms = round((time.time() - t0) * 1000)
        if r.status_code in (200, 301, 302, 401, 403):
            return "ONLINE", f"{r.status_code} · {ms} ms", "badge-online"
        return "WARNING", f"{r.status_code} · {ms} ms", "badge-warning"
    except requests.exceptions.ConnectionError:
        return "OFFLINE", "Connection refused", "badge-offline"
    except requests.exceptions.Timeout:
        return "OFFLINE", "Timeout", "badge-offline"
    except Exception as e:
        return "OFFLINE", str(e)[:40], "badge-offline"


def dot_class(status: str) -> str:
    return {"ONLINE": "dot-green", "WARNING": "dot-yellow"}.get(status, "dot-red")


def render_card(name_lo: str, name_en: str, icon: str, checks: list[dict], logo_b64: str = ""):
    priority = {"OFFLINE": 0, "WARNING": 1, "ONLINE": 2}

    rows = []
    for c in checks:
        status, detail, badge = check_server(c["url"])
        rows.append({"label": c["label"], "status": status, "detail": detail, "badge": badge})

    worst = min(rows, key=lambda r: priority[r["status"]])
    overall_badge = worst["badge"]
    overall_label = worst["status"]

    with st.container(border=True):
        pills_html = ""
        for row in rows:
            pills_html += f"""<div class="metric-pill">
                <span class="metric-dot {dot_class(row['status'])}"></span>
                <span>{row['label']}</span>
                <span style="color:#8aa6cc;font-weight:500;margin-left:2px">{row['detail']}</span>
            </div>"""

        primary_url = checks[0]["url"]

        st.markdown(f"""
        <div>
            <div class="card-top">
                <div class="card-title-group">
                    <div class="card-icon">{"<img src='data:image/png;base64," + logo_b64 + "' />" if logo_b64 else icon}</div>
                    <div>
                        <div class="system-name">{name_lo}</div>
                        <div class="system-name-en">{name_en}</div>
                    </div>
                </div>
                <span class="badge {overall_badge}">{overall_label}</span>
            </div>
            <div class="metrics-row">{pills_html}</div>
            <div class="url-bar">🔗 {primary_url}</div>
        </div>
        """, unsafe_allow_html=True)


# ── DGC header bar ────────────────────────────────────────────────────────────

st.markdown(f"""
<div class="dgc-header">
    <div class="dgc-header-left">
        <div class="dgc-logo-circle"><img src="data:image/png;base64,{LOGO_B64}" style="width:100%;height:100%;object-fit:contain;" /></div>
        <div class="dgc-header-title">
            ສູນບໍລິຫານລັດຖະກິດຈະດີຈິຕອນ
            <span>D-Government Center · System Monitor</span>
        </div>
    </div>
    <div class="dgc-header-time">🕐 {time.strftime("%d/%m/%Y %H:%M:%S")}</div>
</div>
""", unsafe_allow_html=True)

# ── systems definition ────────────────────────────────────────────────────────

SYSTEMS = [
    {
        "name_lo": "ລະບົບ e-Office",
        "name_en": "e-Office (MTC)",
        "icon": "🗂️",
        "logo": EOFFICE_B64,
        "checks": [
            {"label": "Server",  "url": "https://mtc.eoffice.la"},
            {"label": "Service", "url": "https://mtc.eoffice.la"},
        ],
    },
    {
        "name_lo": "ລະບົບ G-Chat",
        "name_en": "G-Chat",
        "icon": "💬",
        "logo": GCHAT_B64,
        "checks": [
            {"label": "Server",  "url": "https://g-chat.gov.la"},
            {"label": "Service", "url": "https://g-chat.gov.la"},
        ],
    },
    {
        "name_lo": "ລະບົບ G-Share",
        "name_en": "G-Share (G-Drive)",
        "icon": "🗄️",
        "logo": GDRIVE_B64,
        "checks": [
            {"label": "Server",  "url": "https://g-drive.gov.la"},
            {"label": "Service", "url": "https://g-drive.gov.la"},
        ],
    },
    {
        "name_lo": "ລະບົບ E-Mail",
        "name_en": "E-Mail (@mtc.gov.la)",
        "icon": "✉️",
        "checks": [
            {"label": "Mail Portal", "url": "https://mail.gov.la"},
            {"label": "M365 Cloud",  "url": "https://m365.cloud.microsoft"},
        ],
    },
]

# ── auto-refresh fragment ─────────────────────────────────────────────────────

@st.fragment(run_every=60)
def run_checks():
    st.markdown(
        '<div class="section-bar">📡 ສະຖານະລະບົບທັງໝົດ &nbsp;—&nbsp; System Status Overview</div>',
        unsafe_allow_html=True,
    )

    col1, col2 = st.columns(2, gap="medium")

    for i, sys in enumerate(SYSTEMS):
        target_col = col1 if i % 2 == 0 else col2
        with target_col:
            render_card(sys["name_lo"], sys["name_en"], sys["icon"], sys["checks"], sys.get("logo", ""))

    st.markdown(
        f"<div class='footer-note'>⏱️ Auto-refresh ທຸກໆ 60 ວິນາທີ &nbsp;·&nbsp; ກວດສອບລ່າສຸດ: {time.strftime('%H:%M:%S')}</div>",
        unsafe_allow_html=True,
    )


run_checks()

if st.button("🔄  ຣີເຟຣດທັງໝົດ / REFRESH ALL", use_container_width=True):
    st.rerun()
