# 设置会话的过期时间为10年
SESSION_COOKIE_AGE = 60 * 60 * 24 * 365 * 10  # 10年

# 确保会话在浏览器关闭后不会被清除
SESSION_EXPIRE_AT_BROWSER_CLOSE = False

# 启用持久会话，每次请求都保存会话
SESSION_SAVE_EVERY_REQUEST = True
