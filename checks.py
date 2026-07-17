import time
import requests
import urllib3
import streamlit as st

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


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
                    <div class="card-icon{' card-icon-logo' if logo_b64 else ''}" style="{'background-image:url(data:image/png;base64,' + logo_b64 + ');background-size:contain;background-repeat:no-repeat;background-position:center;' if logo_b64 else ''}">{"" if logo_b64 else icon}</div>
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
