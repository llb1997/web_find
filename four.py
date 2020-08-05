import pymysql
 
db=pymysql.Connect(host="localhost",port=3306,user="root",password="123456",db="information",charset="utf8")
cursor=db.cursor()

ql='''select * from people '''

#执行SQL语句
cursor.execute(ql)

#num网页名称编号的起始
num=0

while 1: 
    
    row = cursor.fetchone()
 
    #如果能取到数据则开始构造网页
    if row:
        num=num+1
 
        GEN_HTML =str(num) + ".html"

        # 打开文件，准备写入
        # 准备相关变量
        str0 = str(row[0])
        print(str0,'str0')
        str1 = str(row[1])
        print(str1,'str1')
        str2 = str(row[2][:16]+'**')
        print(str2,'str2')
        str3 = str(row[3])
        print(str3,'str3')
        str4 = str(row[4])
        print(str4,'str4')
        str5 = str(num-1)
        print(str5,'str5')
        str6 = str(num+1)
        print(str6,'str6')
    
   # 写入HTML界面中
        message = """
    <!DOCTYPE html>
        <html>
	        <head>
		        <meta charset="utf-8">
		        <title>信息</title>
	        </head>
	        <body>
                <table>
                    <tr>
                        <th>姓名</th>
                        <th>性别</th>
                        <th>身份证号</th>
                        <th>联系地址</th>
                        <th>得分</th>
                    </tr>
                    <tr>
                        <td>%s</td>
                        <td>%s</td>
                        <td>%s</td>
                        <td>%s</td>
                        <td>%s</td>
                    </tr>
                </table>
                <a href="%s.html">上一页</a>
                <a href="%s.html">下一页</a>
            </body>
        </html>
        """ % (str0,str1,str2,str3,str4,str5,str6)

        f = open(GEN_HTML,'w',encoding='UTF-8')
        # 写入文件
        f.write(message)
        # 关闭文件
        f.close()
    else:#无法取到数据则退出
        break
        #print(row)
    #db.commit()
db.close()#关闭数据库连接