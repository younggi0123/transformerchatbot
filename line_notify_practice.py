# 모듈을 읽어 들입니다.
import requests
# 요청을 위한 상수를 선언합니다: TOKEN은 자신의 것을 입력해주세요.
TARGET_URL = 'https://script.googleusercontent.com:443/macros/echo?user_content_key=PEejEiBaXvuGZzMjsC0AzDtCkDZb3rGCVFUtCHMfp9QP5o7G5nuAdW37kIbWDQdmewd_MwYMsw16_wSpFH__F6QfisI0b0Yhm5_BxDlH2jW0nuo2oDemN9CCS2h10ox_1xSncGQajx_ryfhECjZEnLqIxKUlZB_a7qb_GfDcXteHL3uH0Jv0ReFAizbAAa21sqZRhjvr0a5JfjL6e9Ml2g&lib=Mtu17ngu_ufD-ho6hoPS2ku6DSHdxfxLo'
TOKEN = 'Km9hZ0f/eKcsqI/dnm/jDHdQwZxpf61eTdSd1miOlcyZz6euF42XOJ58zUTxxi2L99bY7bNUWQtSGHpqnWY84v9x4Fibo9CXBZFMc9JiKYj1tmMcQaYYxOs+BcO5/02pxFRhRpb4hxtEunNZUP5rBwdB04t89/1O/w1cDnyilFU='
# 요청합니다.
response = requests.post(
  TARGET_URL,
  headers={
    'Authorization': 'Bearer ' + TOKEN
  },
  data={
    'message': '안녕하세요. LINE Notify 테스트입니다.'
  }
)
# 요청 완료
print(response.text)