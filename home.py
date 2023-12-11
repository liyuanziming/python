# 全局变量用来存储所有学生信息
import psycopg2
import random
student_infors = []



def s_connect():
    conn = psycopg2.connect(
        host="localhost",
        database="studentsname",
        user="postgres",
        password="postgres")
    return conn

def generate_random_str(randomlength=10):
  """
  生成一个指定长度的随机字符串
  """
  random_str =''
  base_str ='ABCDEFGHIGKLMNOPQRSTUVWXYZabcdefghigklmnopqrstuvwxyz0123456789'
  length =len(base_str) -1
  for i in range(randomlength):
    random_str +=base_str[random.randint(0, length)]
  return random_str


def Directory():
    #学生宿舍管理系统 V1.0
    # 1打印功能提示
    print('=' * 50)
    print('学生宿舍管理系统 V1.0')
    print('1:添加一个新的入住学生信息')
    print('2:删除一个学生的住宿信息')
    print('3:修改一个学生的住宿信息')
    print('4:查询一个学生的住宿信息')
    print('5:显示所有的学生的住宿信息')
    print('6.显示所有请假学生的信息')
    print('7:退出系统')
    print('=' * 50)

#添加学生信息函数
def  Add_infor():
    # 定义一个新的字典，用来存储一个新的学生信息
    c= s_connect()
    cur = c.cursor()
    new_infor = {}
    new_infor['student_name'] = input('请输入新入住的学生名字：')
    new_infor['D_num'] = input('请输入宿舍号+床位号（如313-3）：')
    new_infor['Class_num'] = input('请输入班级：')
    new_infor['status'] = input('请输入入住情况（在校or请假）：')
    # 将一个字典，添加到列表中
    #student_infors.append(new_infor)
    stu_id = generate_random_str(10)
    #print("INSERT INTO student (student_id,student_name,d_num,class_name,status) VALUES("+str(stu_id)+","+str(new_infor['student_name'])+','+str(new_infor['D_num'])+','+str(new_infor['Class_num'])+','+str(new_infor['status'])+")")

    cur.execute("INSERT INTO student (student_id,student_name,d_num,class_name,status) VALUES(\'"+stu_id+"\',\'"+new_infor['student_name']+'\',\''+new_infor['D_num']+'\',\''+new_infor['Class_num']+'\',\''+new_infor['status']+"\')")


    c.commit()
    print("Records created successfully")

#删除学生信息函数
def Delete_infor():
    c= s_connect()
    cur = c.cursor()
    stu_id = input("请输入要删除的退宿学生编号：")
    cur.execute("DELETE FROM student WHERE student_id = %s", (stu_id,))
    rows_deleted =cur.rowcount
    c.commit()

    if rows_deleted > 0:
        print("已删除！")
        c.close()
    else:
        print("系统不存在该学生的信息！")
        c.close()


# 修改某个学生的信息
def Update_one_infor():
    stu_id = input('请输入要修改的学生编号：')
    name = input('请输入需要修改的学生名字：')
    num = input('请输入需要修改的宿舍号+床位号（如313-3）：')
    class_num = input('请输入需要修改的班级：')
    status = input('请输入需要修改的入住情况（在校or请假）：')

    sql = """ UPDATE student
                SET student_name = %s ,d_num = %s ,class_name= %s,status =%s
                WHERE student_id = %s"""
    updated_rows = 0
    try:
        # read database configuration
        c= s_connect()
        cur = c.cursor()
        # execute the UPDATE  statement
        cur.execute(sql, (name,num,class_num,status,stu_id))
        # get the number of updated rows
        updated_rows = cur.rowcount
        # Commit the changes to the database
        c.commit()
        # Close communication with the PostgreSQL database
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if c is not None:
            c.close()
    if updated_rows>0:
        print("已修改！")
    else:
        print('系统不存在该学生的信息！')

# 查找某个学生的信息
def Find_one_infor():
    stu_name =input('请输入要查询的学生姓名：')
    c= s_connect()
    cur = c.cursor()
    sql = """ SELECT * FROM student where student_name = %s; """
    cur.execute(sql,(stu_name,))

    rows = cur.fetchall()

    if  cur.rowcount == 0:
        print("系统不存在该学生的信息！")
    else:
        print ('学生编号\t学生名字\t宿舍号-床位号\t班级\t\t\t入住情况')
        for item in rows:
            print(item[0]+'\t'+item[1]+'\t\t'+item[2]+'\t'+item[3]+'\t'+item[4])
        c.commit()
        cur.close()
        c.close()


#查找所有入住学生信息
def Find_all_infor():
    c= s_connect()
    cur = c.cursor()
    sql = """ SELECT * FROM student ;  """
    cur.execute(sql)

    rows = cur.fetchall()
    print ('学生编号\t学生名字\t宿舍号-床位号\t班级\t\t\t入住情况')
    for item in rows:
        print(item[0]+'\t'+item[1]+'\t\t'+item[2]+'\t'+item[3]+'\t'+item[4])
    c.commit()
    cur.close()
    c.close()
def Find_leave ():
    c= s_connect()
    cur = c.cursor()
    sql = """ SELECT * FROM student where status = '请假'; """
    cur.execute(sql,)

    rows = cur.fetchall()

    if  cur.rowcount == 0:
        print("系统不存在请假学生的信息！")
    else:
        print ('学生编号\t学生名字\t宿舍号-床位号\t班级\t\t\t入住情况')
        for item in rows:
            print(item[0]+'\t'+item[1]+'\t\t'+item[2]+'\t'+item[3]+'\t'+item[4])
        c.commit()
        cur.close()
        c.close()

def main():
    Directory()
    while True:
        # 2获取用户选择
        num = input('请输入操作序号:')
        if num.isdigit():
            num = int(num)
            if num == 1:
                print('1:添加一个新的入住学生信息')
                Add_infor()
            elif num == 2:
                print('2:删除一个学生住宿信息')
                Delete_infor()
            elif num == 3:
                print('3:修改一个学生住宿信息')
                Update_one_infor()
            elif num == 4:
                print('4:查询一个学生住宿信息')
                Find_one_infor()
            elif num == 5:
                print('5:显示所有的学生住宿信息')
                print()
                Find_all_infor()
            elif num == 6:
                print('6:显示所有请假学生信息')
                Find_leave()
            elif num == 7:
                print("已退出系统！")
                break
            else:
                print('输入有误！目前只有1-7项功能哦')
                continue
            print('')
        else:
            print("输入错误，请重新输入！1-7")

main()
