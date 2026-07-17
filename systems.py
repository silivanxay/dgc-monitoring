from assets import EOFFICE_B64, GCHAT_B64, GDRIVE_B64, EMAIL_B64, EVC_B64, LAOPORTAL_B64, LAOPEDIA_B64, GDX_B64

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
        "logo": EMAIL_B64,
        "checks": [
            {"label": "Mail 365", "url": "https://mail.gov.la"},
            {"label": "iRedMail",  "url": "https://email.gov.la/proxy/"},
        ],
    },
    {
        "name_lo": "ລະບົບກອງປະຊຸມທາງໄກ",
        "name_en": "EVC (Video Conferencing)",
        "icon": "📹",
        "logo": EVC_B64,
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
        "name_lo": "ລະບົບ QR Code & vCard",
        "name_en": "QR Code & vCard",
        "icon": "▦",
        "checks": [
            {"label": "QR Code", "url": "http://103.1.235.56/genqr/"},
            {"label": "vCard", "url": "http://103.1.235.56/vcard/"},
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
    {
        "name_lo": "ລະບົບ Lao Portal",
        "name_en": "Lao Portal",
        "icon": "🌏",
        "logo": LAOPORTAL_B64,
        "checks": [
            {"label": "Server", "url": "https://laoportal.gov.la/"},
        ],
    },
    {
        "name_lo": "ລະບົບ GDX",
        "name_en": "GDX",
        "icon": "🔗",
        "logo": GDX_B64,
        "checks": [
            {"label": "Server",    "url": "https://ndx.gov.la/"},
            {"label": "Admin",     "url": "https://admin.ndx.gov.la/login"},
            {"label": "Admin TSA", "url": "https://admin-tsa.ndx.gov.la/"},
        ],
    },
    {
        "name_lo": "ລະບົບ Laopedia",
        "name_en": "Laopedia",
        "icon": "📖",
        "logo": LAOPEDIA_B64,
        "checks": [
            {"label": "Server", "url": "https://laopedia.gov.la/"},
        ],
    },
    {
        "name_lo": "ລະບົບ G-HelpDesk",
        "name_en": "G-HelpDesk",
        "icon": "📞",
        "checks": [
            {"label": "Server", "url": "https://g-care.eoffice.la/"},
        ],
    },
]
