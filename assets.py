import base64
from pathlib import Path


def _img_b64(path: str) -> str:
    return base64.b64encode(Path(path).read_bytes()).decode()


LOGO_B64 = _img_b64("assets/dgc.png")
EOFFICE_B64 = _img_b64("assets/e-office.png")
GCHAT_B64   = _img_b64("assets/g-chat.png")
GDRIVE_B64  = _img_b64("assets/g-drive.png")
EMAIL_B64   = _img_b64("assets/email.png")
EVC_B64          = _img_b64("assets/evc.png")
LAOPORTAL_B64    = _img_b64("assets/laoportal.png")
LAOPEDIA_B64     = _img_b64("assets/laopedia.png")
GDX_B64          = _img_b64("assets/gdx.png")

FONT_REGULAR_B64 = _img_b64("assets/fonts/Phetsarath-Regular.ttf")
FONT_BOLD_B64    = _img_b64("assets/fonts/Phetsarath-Bold.ttf")
