import pymysql
    
def find_infor(db_name,ql_name,page_num):
    db=pymysql.Connect(host="localhost",port=3306,user="root",password="123456",db=db_name,charset="utf8")
    cursor=db.cursor()

    ql='''select * from %s '''%ql_name

    #执行SQL语句
    cursor.execute(ql)

    result = cursor.execute(ql)
    #num网页名称编号的起始
    num=0

    result_cut=result//page_num+1
    result_end=result//page_num+1
    
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
                    <style >
                        a {
                            display:block;
                            width: 249px;
                            height: 48px;
                            background-color: #828888;
                            font-size: 14px;
                            color: #fff;
                            text-decoration: none;	
                            text-indent: 2em;
                            line-height: 48px;
                        }
                        /* 鼠标经过链接变换背景颜色 */
                        a:hover{
                            background-color: #ff5500;
                        }
                        span {
                            
                            /* 把行内元素转换为行内块元素，可以设置宽和高 ，行内每一个变成的块元素*/
                            display: inline-block;
                        }
                        span .nav{
                            padding-top: 0;
                        }
                    </style>
                </head>
                <body>
                    <span>
                        <a href="1.html">第1页</a>
        """
        f.write(message1)
        
        str7=int(result_end)+1
        
        for n in range(1,str7):
            message2 ="""
            <a href="%s.html">第%s页</a>
            """%(n,n)
            f.write(message2)

        message3 =  """
                    </span>
                    <span >
                        <table width=500 height=248 class=".nav">
                        
                            <tr>
                                <th>姓名</th>
                                <th>性别</th>
                                <th>身份证号</th>
                                <th>联系地址</th>
                                <th>得分</th>
                            </tr>
        """
        f.write(message3)

        #如果能取到数据则开始构造网页
            
        for i in range (0,page_num):
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
                message4 ="""
                            <tr>
                                <td>%s</td>
                                <td>%s</td>
                                <td>%s</td>
                                <td>%s</td>
                                <td>%s</td>
                            </tr>               
                """% (str0,str1,str2,str3,str4)
                
                f.write(message4)

        str7=int(result_end)
        
        message5 = """  
                        </table>
                    </span >
                </body>
            </html>
        """        

        f.write(message5)
                        
        # 关闭文件
        f.close()
        
    db.close()#关闭数据库连接

if __name__ == "__main__":
    # find_infor("information",ql_name="people",page_num=5)
    find_infor("information",ql_name="people",page_num=4)
