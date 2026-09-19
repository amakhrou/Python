from datetime import datetime

nowdatetime = datetime.now()
secondsdatetime = nowdatetime.timestamp()
print(
    f"Seconds since January 1, 1970: {secondsdatetime:,.4f} or "
    f"{secondsdatetime:.2e} in in scientific notation"
)
print(nowdatetime.strftime("%b %d %Y"))
