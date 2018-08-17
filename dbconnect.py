import pymysql



def insertdata(url, html, image):
	sql = 'INSERT INTO onion_urls (url, html, image) VALUES(%s, %s, %s)'
	# global curs
	conn = pymysql.connect(host='localhost', user='root', password='toor', db='tor', charset='utf8')
	curs = conn.cursor()
	curs.execute(sql, (url, html, image))
	conn.commit()




