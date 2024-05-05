# Python 基础

## 一、变量和简单数据类型

### 1.变量名命名

- 只能包含字母、数字和下划线
- 只能以字母、下划线打头，不能以数字打头
- 不能包含空格，可使用下划线分隔
- 不用关键字和函数名命名
- 变量名简短且具有描述性
- 慎用小写字母l与大写字母O，会被错看1和0
- Python命名区分大小写
- NameError是名称错误，检查变量名称是否正确

### 2.变量使用

1.变量的认识：变量是可以被赋值的标签

2.使用：
- 字符串：一系列字符，可用''或""引起
    - 修改字符串大小写：
    ```Python3
        name = "MiKu"
        print(name.upper()) #MIKU
        print(name.lower()) #miku
    ```
    - 字符串拼接：
    ```
        first_name = "hatsune"
        last_name = "miku"
        full_name = f"{first_name} {last_name}" #hatsune miku
        print(f"Hello,{full_name.title()}")
        # Hello,Hatsune Miku 
        # full_name.title()中（.）让Python执行title()方法
        #title()首字母大写显示每个单词
        #f进行花括号内变量拼接，f = format
    ```
    - 删除空白：
    ```
        name = " miku "
        name.rstrip()#删除右边空格
        name.lstrip()#删除左边空格
        name.strip()#删除两端空格
        #name被赋予的值不变
    ```
    - 删除前缀：
    ```
        url = "https://bilibili.com"
        simple_url = url.removeprefix("https://")
        #url被赋予的值不变
    ```
    - SyntaxError是语法错误
- 数
    - 分为整数和浮点数
    - 运算：(+)加、 (-)减、 (*)乘、 (/)除、 (**)乘方
    - 下划线：
      ```
      big_num = 14_000_000_000
      #python不会打印这个下划线，但写程序时便于阅读
      ```
    - 多变量赋值：
      ```
      x,y,z = 1,2,3
      ```
- 常量：命名时全大写，可用下划线分割
  