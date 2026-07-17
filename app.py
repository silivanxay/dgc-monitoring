from datetime import datetime, timezone, timedelta
import streamlit as st

LAO_TZ = timezone(timedelta(hours=7))

from assets import LOGO_B64
from styles import inject_styles
from checks import render_card
from systems import SYSTEMS

st.set_page_config(
    page_title="DGC System Monitor",
    page_icon="🖥️",
    layout="wide"
)

inject_styles()

st.markdown(f"""
<div class="dgc-header">
    <div class="dgc-header-left">
        <div class="dgc-logo-circle"><img src="data:image/png;base64,{LOGO_B64}" style="width:100%;height:100%;object-fit:contain;" /></div>
        <div class="dgc-header-title">
            ສູນບໍລິຫານລັດດີຈີຕອນ
            <span>D-Government Center · System Monitor</span>
        </div>
    </div>
    <div class="dgc-header-time">🕐 {datetime.now(LAO_TZ).strftime("%d/%m/%Y %H:%M:%S")}</div>
</div>
""", unsafe_allow_html=True)


@st.fragment(run_every=60)
def run_checks():
    st.markdown(
        '<div class="section-bar">📡 ສະຖານະລະບົບທັງໝົດ &nbsp;—&nbsp; System Status Overview</div>',
        unsafe_allow_html=True,
    )

    col1, col2, col3, col4 = st.columns(4, gap="medium")
    cols = [col1, col2, col3, col4]

    for i, sys in enumerate(SYSTEMS):
        with cols[i % 4]:
            render_card(sys["name_lo"], sys["name_en"], sys["icon"], sys["checks"], sys.get("logo", ""))

    st.markdown(
        f"<div class='footer-note'>⏱️ Auto-refresh ທຸກໆ 60 ວິນາທີ &nbsp;·&nbsp; ກວດສອບລ່າສຸດ: {datetime.now(LAO_TZ).strftime('%H:%M:%S')}</div>",
        unsafe_allow_html=True,
    )


run_checks()

if st.button("🔄  ຣີເຟຣດທັງໝົດ / REFRESH ALL", use_container_width=True):
    st.rerun()
