import pygeoip


gip = pygeoip.GeoIP("C:\\Users\\91702\\Desktop\\Jarvis\\BOT\\GeoLiteCity.dat")
res = gip.record_by_addr('207.96.77.17')
for key, val in res.items():
    a = print('%s : %s' % (key, val))
