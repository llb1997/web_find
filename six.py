import pymysql
 
db=pymysql.Connect(host="localhost",port=3306,user="root",password="123456",db="information",charset="utf8")
cursor=db.cursor()

ql='''select * from people '''

#执行SQL语句
cursor.execute(ql)

result = cursor.execute(ql)
#num网页名称编号的起始
num=0

result_cut=result//5+1
result_end=result//5+1
i=0
while result_cut: 
    result_cut-=1
    
    num=num+1
    GEN_HTML =str(num) + ".html"
    f = open(GEN_HTML,'w',encoding='UTF-8')
    message1 = """
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
                
    """
    f.write(message1)
    str5 = str(num-1)
    str6 = str(num+1)

    #如果能取到数据则开始构造网页
          
    for i in range (0,5):
        # if row:
        row = cursor.fetchone()
        if row:
            
            # 打开文件，准备写入
            # 准备相关变量
            str0 = str(row[0])          
            str1 = str(row[1])           
            str2 = str(row[2][:16]+'**')            
            str3 = str(row[3])            
            str4 = str(row[4])
              
    # 写入HTML界面中
            message2 ="""
                    <tr>
                        <td>%s</td>
                        <td>%s</td>
                        <td>%s</td>
                        <td>%s</td>
                        <td>%s</td>
                    </tr>               
            """% (str0,str1,str2,str3,str4)
            
            f.write(message2)
    str7=int(result_end)
    if int(str5) == 0 :
        message3 ="""        
                </table>
                <a href="%s.html">下一页</a>
                <a href="%s.html">尾页</a>
                
            </body>
        </html>
    """ % (str6,str7)       
    elif not row :
        message3 ="""        
                </table>
                <a href="1.html">首页</a>
                <a href="%s.html">上一页</a>               
            </body>
        </html>
    """ % (str5)
    else:
            message3 ="""        
                </table>
                <a href="1.html">首页</a>
                <a href="%s.html">上一页</a>
                <a href="%s.html">下一页</a>
                <a href="%s.html">尾页</a>
            </body>
        </html>
        """ % (str5,str6,str7)

    f.write(message3)
                     
    # 关闭文件
    f.close()
    
db.close()#关闭数据库连接