from datetime import date
from database import session
from tables import Holiday

# 登録するデータの編集
holiday= Holiday(
    holi_date = date(2024, 11, 23),
    holi_text = "勤労感謝の日"
)
#INSERT処理
session.add(holiday)
#コミット
session.commit()
