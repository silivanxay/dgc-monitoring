from assets import EOFFICE_B64, GCHAT_B64, GDRIVE_B64

SYSTEMS = [
    {
        "name_lo": "ລະບົບ e-Office",
        "name_en": "e-Office (MTC)",
        "icon": "🗂️",
        "logo": EOFFICE_B64,
        "checks": [
            {"label": "Server",  "url": "https://mtc.eoffice.la"},
            {"label": "Service", "url": "https://uat-api.eoffice.la"},
        ],
    },
    {
        "name_lo": "ລະບົບ G-Chat",
        "name_en": "G-Chat",
        "icon": "💬",
        "logo": GCHAT_B64,
        "checks": [
            {"label": "Server",  "url": "https://g-chat.gov.la"},
            {"label": "Service", "url": "https://g-chat.gov.la/api-static-resource/app/info/selectByPackageName?packageName=smart-link-auth-portal-app"},
        ],
    },
    {
        "name_lo": "ລະບົບ G-Share",
        "name_en": "G-Share (G-Drive)",
        "icon": "🗄️",
        "logo": GDRIVE_B64,
        "checks": [
            {"label": "Server",  "url": "https://g-drive.gov.la"},
            {"label": "Service", "url": "https://g-drive.gov.la/ocs/v2.php/apps/notifications/api/v2/notifications"},
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
    {
        "name_lo": "ລະບົບກອງປະຊຸມທາງໄກ",
        "name_en": "EVC (Video Conferencing)",
        "icon": "📹",
        "checks": [
            {"label": "Server",  "url": "https://evc.gov.la"},
        ],
    },
    {
        "name_lo": "ລະບົບ G-Web",
        "name_en": "G-Web (DGC Portal)",
        "icon": "🌐",
        "checks": [
            {"label": "dgc.gov.la",  "url": "https://dgc.gov.la"},
            {"label": "mtc.gov.la",  "url": "https://mtc.gov.la"},
        ],
    },
    {
        "name_lo": "ລະບົບ QR Code",
        "name_en": "QR Code Generator",
        "icon": "▦",
        "checks": [
            {"label": "Service", "url": "http://103.1.235.56/genqr/"},
        ],
    },
    {
        "name_lo": "ລະບົບ vCard",
        "name_en": "vCard",
        "icon": "👤",
        "checks": [
            {"label": "Service", "url": "http://103.1.235.56/vcard/"},
        ],
    },
    {
        "name_lo": "ລະບົບລົງຄະແນນສຽງ",
        "name_en": "E-Vote",
        "icon": "🗳️",
        "checks": [
            {"label": "Service", "url": "https://e-vote.gov.la/public/"},
        ],
    },
]
