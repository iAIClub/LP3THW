# 如何使用python3对excel编程

> Excel 是 Windows 环境下流行的、强大的电子表格应用。 openpyxl 模块让 Python 程序能读取和修改 Excel 电子表格文件。例如，可能有一个无聊的任务，需要从一个电子表格拷贝一些数据，粘贴到另一个电子表格中。或者可能需要从几千行中挑选几行，根据某种条件稍作修改。或者需要查看几百份部门预算电子表格，寻找其中的赤字。正是这种无聊无脑的电子表格任务，可以通过 Python 来完成。LibreOffice Calc 和 OpenOffice Calc 都能处理 Excel 的电子表格文件格式，这意味着 openpyxl 模块也能处理来自这些应用程序的电子表格。你可以从 https://www.libreoffice.org/ 和 http://www.openoffice.org/ 下载这些软件。即使你的计算机上已经安装了Excel，可能也会发现这些程序更容易使用。但是，本章中的截屏图都来自于 Windows 7上的 Excel2010。

## 关于excel文档
首先，让我们来看一些基本定义。一个 Excel 电子表格文档称为一个工作簿。一个工作簿保存在扩展名为.xlsx 的文件中。每个工作簿可以包含多个表(也称为工作表，sheet)。用户当前查看的表(或关闭 Excel 前最后查看的表)，称为"活动表"。 每个表都有一些列(地址是从 A 开始的字母)和一些行(地址是从 1 开始的数 字)。在特定行和列的方格称为单元格(cell)。每个单元格都包含一个数字或文本值。单元格形成的网格和数据构成了表。

## 关于openyxl模块的安装
> 推荐安装Anacanda，并通过它来安装和管理你需要的模块。

Python 没有自带 openpyxl，所以必须安装。按照附录 A 中安装第三方模块的指 令，模块的名称是 openpyxl。要测试它是否安装正确，就在交互式环境中输入以下代码:
```
>>> import openpyxl
```
如果该模块正确安装，这应该不会产生错误消息。记得在运行本章的交互式环境例子之前，要导入 openpyxl 模块，否则会得到错误，NameError: name 'openpyxl'is not defined。
本书介绍了 openpyxl 的 2.1.4 版，但 OpenPyXL 团队会经常发布新版本。不过 不用担心，新版本应该在相当长的时间内向后兼容，支持本书中使用的指令。如果 你有新版本，想看看它提供了什么新功能，可以查看 OpenPyXL 的完整文档: http://openpyxl.readthedocs.org/。

## 读取excel文档
本章的例子将使用一个电子表格 example.xlsx，它保存在根文件夹中。你可以 自己创建这个电子文档，或从 http://nostarch.com/automatestuff/ 下载。图展示了 3 个默认的表，名为 Sheet1、Sheet2 和 Sheet3，这是 Excel 自动为新工作簿提供的(不同操作系统和电子表格程序，提供的默认表个数可能会不同)。 示例文件中的 Sheet 1 应该看起来像表 12-1(如果你没有从网站下载 example.xlsx，就应该在工作表中自己输入这些数据)。
### 用 openpyxl 模块打开 Excel 文档
在导入 openpyxl 模块后，就可以使用 openpyxl.load_workbook()函数。在交互式 环境中输入以下代码:
```
>>> import openpyxl
>>> wb = openpyxl.load_workbook('example.xlsx')
>>> type(wb)
<class 'openpyxl.workbook.workbook.Workbook'>
```
openpyxl.load_workbook()函数接受文件名，返回一个 workbook 数据类型的值。这个 workbook 对象代表这个 Excel 文件，有点类似 File 对象代表一个打开的文本文件。 要记住，example.xlsx 需要在当前工作目录，你才能处理它。可以导入 os，使用函数 os.getcwd()弄清楚当前工作目录是什么，并使用 os.chdir()改变当前工作目录。

### 从工作簿中取得工作表
调用 get_sheet_names()方法可以取得工作簿中所有表名的列表。在交互式环境中输入以下代码:
```
>>> import openpyxl
>>> wb = openpyxl.load_workbook('example.xlsx') >>> wb.get_sheet_names()
['Sheet1', 'Sheet2', 'Sheet3']
>>> sheet = wb.get_sheet_by_name('Sheet3')
>>> sheet
<Worksheet "Sheet3">
>>> type(sheet)
<class 'openpyxl.worksheet.worksheet.Worksheet'> >>> sheet.title
'Sheet3'
>>> anotherSheet = wb.get_active_sheet()
>>> anotherSheet
<Worksheet "Sheet1">

```
每个表由一个 Worksheet 对象表示，可以通过向工作簿方法 get_sheet_by_name()传递表名字符串获得。最后，可以调用 Workbook 对象的 get_active_sheet()方法，取得 工作簿的活动表。活动表是工作簿在 Excel 中打开时出现的工作表。在取得 Worksheet 对象后，可以通过 title 属性取得它的名称。

### 从表中取得单元格
有了 Worksheet 对象后，就可以按名字访问 Cell 对象。在交互式环境中输入以 下代码:
```
>>> import openpyxl
>>> wb = openpyxl.load_workbook('example.xlsx')
>>> sheet = wb.get_sheet_by_name('Sheet1')
>>> sheet['A1']
<Cell Sheet1.A1>
>>> sheet['A1'].value
datetime.datetime(2015, 4, 5, 13, 34, 2)
>>> c = sheet['B1']
>>> c.value
'Apples'
>>> 'Row ' + str(c.row) + ', Column ' + c.column + ' is ' + c.value 'Row 1, Column B is Apples'
>>> 'Cell ' + c.coordinate + ' is ' + c.value
'Cell B1 is Apples'
>>> sheet['C1'].value
73
```
Cell 对象有一个 value 属性，不出意外，它包含这个单元格中保存的值。Cell 对 象也有 row、column 和 coordinate 属性，提供该单元格的位置信息。
这里，访问单元格 B1 的 Cell 对象的 value 属性，我们得到字符串'Apples'。row 属性给出的是整数 1，column 属性给出的是'B'，coordinate 属性给出的是'B1'。
openpyxl 模块将自动解释列 A 中的日期，将它们返回为 datetime 值，而不是字 符串。datetime 数据类型将在第 16 章中进一步解释。
用字母来指定列，这在程序中可能有点奇怪，特别是在 Z 列之后，列开时使用 两个字母:AA、AB、AC 等。作为替代，在调用表的 cell()方法时，可以传入整数 作为 row 和 column 关键字参数，也可以得到一个单元格。第一行或第一列的整数 是 1，不是 0。输入以下代码，继续交互式环境的例子:
```

>>> sheet.cell(row=1, column=2)
<Cell Sheet1.B1>
>>> sheet.cell(row=1, column=2).value 'Apples'
>>> for i in range(1, 8, 2):
print(i, sheet.cell(row=i, column=2).value)
             1 Apples
             3 Pears
             5 Apples
             7 Strawberries
```
注意：我在终端中是无法输入下列代码，从而出来结果的
```
>>> for i in range(1, 8, 2):
print(i, sheet.cell(row=i, column=2).value)
```
我输入后的结果是：
```
>>> for i in range(1, 8, 2):
...     print(i, sheet.cell(row=i, column=2).value
...
```
然后就没有然后了。于是我写了一个文件pythonexcel1.py:

```
# excel test：name is:pythonexcel1.py
import openpyxl
wb = openpyxl.load_workbook('example.xlsx')
sheet = wb.get_sheet_by_name('Sheet1')

for i in range(1, 8, 2):
    print(i, sheet.cell(row=i, column=2).value)
```
在终端中运行，结果是：
```
bogon:automate yyy$ python pythonexcel1.py
1 Apples
3 Pears
5 Apples
7 Strawberries
```
这样就可以了。我上百度上搜索关于在终端中换行但是不执行的方法，没有找到说到点子上的。

可以看到，使用表的 cell()方法，传入 row=1 和 column=2，将得到单元格 B1的 Cell 对象，就像指定 sheet['B1']一样。然后，利用 cell()方法和它的关键字参数， 就可以编写 for 循环，打印出一系列单元格的值。
假定你想顺着 B 列，打印出所有奇数行单元格的值。通过传入 2 作为 range()函数 的“步长”参数，可以取得每隔一行的单元格(在这里就是所有奇数行)。for 循环 的 i 变量被传递作为 cell()方法的 row 关键字参数，而 column 关键字参数总是取 2。 请注意传入的是整数 2，而不是字符串'B'。
可以通过 Worksheet 对象的 get_highest_row()和 get_highest_column()方法，确定 表的大小。在交互式环境中输入以下代码:
```
>>> import openpyxl
>>> wb = openpyxl.load_workbook('example.xlsx') >>> sheet = wb.get_sheet_by_name('Sheet1')
>>> sheet.get_highest_row()
7
>>> sheet.get_highest_column()
3
```
经过我的实践发现get_highest_row()和get_highest_column()已经不在被支持，而是变为非函数，在交互终端直接使用max_row和max_colum就可以掉出来行和列数目。
在代码中也使用。这里需要强调了是max_row和max_colum已经不再是“函数”了，而是sheet对象的“属性”，直接调用即可。
```
>>> sheet.max_row # 第一种形式
7
>>> print(sheet.max_column) #第二种形式,注意不要忘记了sheet对象。
3

```
请注意，sheet.max_row返回一个整数，而不是 Excel 中出现的字母。

### 列字母和数字之间的转换
要从字母转换到数字，就调用 openpyxl.cell.column_index_from_string()函数。 要从数字转换到字母，就调用 openpyxl.cell.get_column_letter()函数。在交互式环境 中输入以下代码:
```
>>> import openpyxl
>>> from openpyxl.cell import get_column_letter, column_index_from_string
>>> get_column_letter(1) 'A'
>>> get_column_letter(2) 'B'
>>> get_column_letter(27) 'AA'
>>> get_column_letter(900) 'AHP'
>>> wb = openpyxl.load_workbook('example.xlsx')
>>> sheet = wb.get_sheet_by_name('Sheet1')
>>> get_column_letter(sheet.get_highest_column()) # 现在改为get_column_letter(sheet.max_column)
 'C'
>>> column_index_from_string('A')
 1
>>> column_index_from_string('AA')
 27

```
在从 openpyxl.cell 模块引入这两个函数后，可以调用 get_column_letter()，传入 像 27 这样的整数，弄清楚第 27 列的字母是什么。函数 column_index_string()做的事情 相反:传入一列的字母名称，它告诉你该列的数字是什么。要使用这些函数，不必 加载一个工作簿。如果你愿意，可以加载一个工作簿，取得 Worksheet 对象，并调 用 Worksheet 对象的方法，如 ～～～ get_highest_column()～～～sheet.max_column ，来取得一个整数。然后，将该整数传递给 get_column_letter()。

### 从表中取得行和列
可以将 Worksheet 对象切片，取得电子表格中一行、一列或一个矩形区域中的所有 Cell 对象。然后可以循环遍历这个切片中的所有单元格。在交互式环境中输入以下代码:
```
# pyxls2.py
import openpyxl
wb = openpyxl.load_workbook('example.xlsx')
sheet = wb.get_sheet_by_name('Sheet1')

tuple(sheet['A1':'C3'])

for rowOfCellObjects in sheet['A1':'C3']:
     for cellObj in rowOfCellObjects:
             print(cellObj.coordinate,cellObj.value)
     print('--- END OF ROW ---')

```
将脚本运行之后显示如下：
```
python pyxls2.py
A1 2015-04-05 13:34:02
B1 Apples
C1 73
--- END OF ROW ---
A2 2015-04-05 03:41:23
B2 Cherries
C2 85
--- END OF ROW ---
A3 2015-04-06 12:46:51
B3 Pears
C3 14
--- END OF ROW ---

```
这里，我们指明需要从 A1 到 C3 的矩形区域中的 Cell 对象，得到了一个 Generator 对象，它包含该区域中的 Cell 对象。为了帮助我们看清楚这个 Generator 对象，可以 使用它的 tuple()方法，在一个元组中列出它的 Cell 对象。
这个元组包含 3 个元组:每个元组代表 1 行，从指定区域的顶部到底部。这 3 个内部元组中的每一个包含指定区域中一行的 Cell 对象，从最左边的单元格到最右 边。所以总的来说，工作表的这个切片包含了从 A1 到 C3 区域的所有 Cell 对象， 从左上角的单元格开始，到右下角的单元格结束。

要打印出这个区域中所有单元格的值，我们使用两个 for 循环。外层 for 循环遍历 这个切片中的每一行。然后针对每一行，内层 for 循环遍历该行中的每个单元格。 要访问特定行或列的单元格的值，也可以利用 Worksheet 对象的 rows 和 columns
属性。在交互式环境中输入以下代码:

```
>>> import openpyxl
>>> wb = openpyxl.load_workbook('example.xlsx')
>>> sheet = wb.get_active_sheet()
>>> sheet.columns[1]
(<Cell Sheet1.B1>, <Cell Sheet1.B2>, <Cell Sheet1.B3>, <Cell Sheet1.B4>, <Cell Sheet1.B5>, <Cell Sheet1.B6>, <Cell Sheet1.B7>)
>>> for cellObj in sheet.columns[1]:
        print(cellObj.value)
             Apples
             Cherries
             Pears
             Oranges
             Apples
             Bananas
             Strawberries
```
实际上本库不能很好的运行，因为一些命令发生了更改，真正可用的代码如下：
```
>>> import openpyxl
>>> wb = openpyxl.load_workbook('example.xlsx')
>>> sheet = wb.get_active_sheet()
>>> list(sheet.columns)[1]
(<Cell 'Sheet1'.B1>, <Cell 'Sheet1'.B2>, <Cell 'Sheet1'.B3>, <Cell 'Sheet1'.B4>, <Cell 'Sheet1'.B5>, <Cell 'Sheet1'.B6>, <Cell 'Sheet1'.B7>)
```
可以用的代码是这样写的（写成一个py脚本运行）：
```
import openpyxl
wb = openpyxl.load_workbook('example.xlsx')
sheet = wb.get_active_sheet()
for cell in list(sheet.columns)[1]:
    print(cell.value)
```
运行结果如下：
```
bogon:automate yyy$ python pyxls3.py
Apples
Cherries
Pears
Oranges
Apples
Bananas
Strawberries
```

利用 Worksheet 对象的 rows 属性，可以得到一个元组构成的元组。内部的每个元 组都代表 1 行，包含该行中的 Cell 对象。columns 属性也会给你一个元组构成的元组， 内部的每个元组都包含 1 列中的 Cell 对象。对于 example.xlsx，因为有 7 行 3 列，rows 给出由 7 个元组构成的一个元组(每个内部元组包含 3 个 Cell 对象)。columns 给出由 3 个元组构成的一个元组(每个内部元组包含 7 个 Cell 对象)。
要访问一个特定的元组，可以利用它在大的元组中的下标。例如，要得到代表 B 列的元组，可以用 sheet.columns[1]。要得到代表 A 列的元组，可以用 sheet.columns[0]。 在得到了代表行或列的元组后，可以循环遍历它的对象，打印出它们的值。

### 工作簿、工作表、单元格
作为快速复习，下面是从电子表格文件中读取单元格涉及的所有函数、方法和 数据类型。
1.导入 openpyxl 模块。
2.调用 openpyxl.load_workbook()函数。
3.取得 Workbook 对象。
4.调用 get_active_sheet()或 get_sheet_by_name()工作簿方法。
5.取得 Worksheet 对象。
6.使用索引或工作表的 cell()方法，带上 row 和 column 关键字参数。
7.取得 Cell 对象。
8.读取 Cell 对象的 value 属性。


## 此处待补充剩下的章节。

### 补充：重要的逻辑结构

#### excel最重要的三种数据格式

NULL空值：对应于python中的None，表示这个cell里面没有数据。
numberic： 数字型，统一按照浮点数来进行处理。对应于python中的float。
string： 字符串型，对应于python中的unicode

##### Excel文件的三个对象

workbook： 工作簿，一个excel文件包含多个sheet。
sheet：工作表，一个workbook有多个，表名识别，如“sheet1”,“sheet2”等。
cell： 单元格，存储数据对象

### openpyxl的操作程序
#### 0.导入
```
from openpyxl import Workbook
from openpyxl import load_workbook
from openpyxl.styles import PatternFill, Border, Side, Alignment, Protection, Font, Color, Fill
from openpyxl.styles import colors
from openpyxl.styles import Fill,fills
from openpyxl.formatting.rule import ColorScaleRule
```
#### 1.打开工作簿（workbook）
```
 wb = load_workbook('file_name.xlsx')
```
#### 2.打开工作表（sheet）

##### 2.1通过名字
    ws = wb["frequency"]
    等同于 ws2 = wb.get_sheet_by_name('frequency')
    验证命令ws is ws2 is ws3 输出True
##### 2.2不知道名字用index
    sheet_names = wb.get_sheet_names()
    ws = wb.get_sheet_by_name(sheet_names[index])# index为0为第一张表

#### 2.3其他方法
    ws =wb.active
    等同于  ws = wb.get_active_sheet() #通过_active_sheet_index设定读取的表，默认0读第一个表。
    活动表表名wb.get_active_sheet().title

#### 3.新建表（sheet）
```
ws1 = wb.create_sheet() #默认插在最后
ws2 = wb.create_sheet(0) #插在开头
   建表后默认名按顺序，如sheet1，sheet2...
    ws.title = "New Title" #修改表名称

   简化 ws2 = wb.create_sheet(title="Pi")
```
#### 4.表背景颜色
```
ws.sheet_properties.tabColor = "1072BA" # set with RRGGBB color code
```
#### 5.单元格（cell）使用
```
c = ws['A4'] #read 等同于 c = ws.cell('A4')
ws['A4'] = 4 #write
#ws.cell有两种方式，行号列号从1开始
d = ws.cell(row = 4, column = 2) #行列读写
d = ws.cell('A4')
写入cell值
    ws.cell(row = 4, column = 2).value = 'test'
    ws.cell(row = 4, column = 2, value = 'test')
```
#### 6.访问多个单元格
```
cell_range = ws['A1':'C2']
读所有单元格数据
get_cell_collection()
```
#### 7.逐行列读写
```
a)逐行读
     ws.iter_rows(range_string=None, row_offset=0, column_offset=0): range-string(string)-单元格的范围：例如('A1:C4') row_offset-添加行 column_offset-添加列
 返回一个生成器, 注意取值时要用value,例如：
 for row in ws.iter_rows('A1:C2'):
     for cell in row:
         print cell
读指定行、指定列:
 rows=ws.rows#row是可迭代的
 columns=ws.columns#column是可迭代的
 打印第n行数据
 print rows[n]#不需要用.value
 print columns[n]#不需要用.value

b)逐行写
(http://openpyxl.readthedocs.io/en/default/_modules/openpyxl/worksheet/worksheet.html#Worksheet.append)
ws.append(iterable)
 添加一行到当前sheet的最底部 iterable必须是list,tuple,dict,range,generator类型的。 1,如果是list,将list从头到尾顺序添加。 2，如果是dict,按照相应的键添加相应的键值。
append([‘This is A1’, ‘This is B1’, ‘This is C1’])
append({‘A’ : ‘This is A1’, ‘C’ : ‘This is C1’})
append({1 : ‘This is A1’, 3 : ‘This is C1’})

```
#### 8.显示表格内信息
```
wb.get_sheet_names()  
#显示表名，表行数，表列数   
print ws.title  
print ws.max_row
print ws.max_column

ws.get_highest_row() #UserWarning: Call to deprecated function
ws.get_highest_column()# UserWarning: Call to deprecated function
```

#### 9.获得列号的字母
col = get_column_letter(x), x从1开始
```

from openpyxl.utils import get_column_letter
for  x  in  range( 1, len(record)+ 1 ):  
    col = get_column_letter(x)  
    ws.cell( '%s%s' %(col, i)).value = x

通过列字母获取多个excel数据块
cell_range = "E3:{0}28".format(get_column_letter(bc_col))
ws["A1"] = "=SUM(%s)"%cell_range
```
#### 10.excel文件内容的编码转换
excel文件是gbk编码，读入时需要先encode为gbk，再decode为unicode，再encode为utf8
```
cell_value.encode('gbk').decode('gbk').encode('utf8')
```
#### 11.公式计算
```
ws["A1"] = "=SUM(1, 1)"
ws["A1"] = "=SUM(B1:C1)
```

### 代码实例1（直接修改使用）

```
from openpyxl import Workbook
from openpyxl.compat import range
from openpyxl.cell import get_column_letter

dest_filename = 'empty_book.xlsx'

wb = Workbook()
ws1 = wb.active
ws1.title = "range names"
for row in range(1, 40):
   ws1.append(range(600))

ws3 = wb.create_sheet(title="Data")
for row in range(10, 20):
   for col in range(27, 54):
       _ = ws3.cell(column=col, row=row, value="%s" % get_column_letter(col))
print(ws3['AA10'].value)
wb.save(filename = dest_filename)

sheet_ranges = wb['range names']
print(sheet_ranges['D18'].value)

ws['A1'] = datetime.datetime(2010, 7, 21)
ws['A1'].number_format #输出'yyyy-mm-dd h:mm:ss'

rows = [
    ['Number', 'Batch 1', 'Batch 2'],
    [2, 40, 30],
    [3, 40, 25],
    [4, 50, 30],
    [5, 30, 10],
    [6, 25, 5],
    [7, 50, 10],
]

rows = [
    ['Date', 'Batch 1', 'Batch 2', 'Batch 3'],
    [date(2015,9, 1), 40, 30, 25],
    [date(2015,9, 2), 40, 25, 30],
    [date(2015,9, 3), 50, 30, 45],
    [date(2015,9, 4), 30, 25, 40],
    [date(2015,9, 5), 25, 35, 30],
    [date(2015,9, 6), 20, 40, 35],
]

for row in rows:
    ws.append(row)
```
### Excel里的图片处理（PIL模块）

```
try:
       from openpyxl.drawing import image
       import PIL            
   except ImportError, e:
       print "[ERROR]",e

   report_file = self.excel_path + "/frquency_report_%d.xlsx" %id
   shutil.copyfile(configs.PATTEN_FILE, report_file)
   if not os.path.exists(report_file):
      print "generate file failed: ", report_file
      sys.exit(1)

   wb = load_workbook(report_file)
   ws = wb.get_sheet_by_name('frequency')
   img_f = configs.IMAGE_LOGO
   if os.path.exists(img_f):
       try:
           img = image.Image(img_f)
           ws.add_image(img, 'A1')
       except Exception, e:
           print "[ERROR]%s:%s" % (type(e), e)
           ws['A1'] = "程序化营销平台"
       else:
           ws['A1'] = "程序化营销平台"

       font1 = Font(size=22)
       ws['A1'].font = font1
       ws['B4'] = ad_plan #等同ws.cell('B4') = ad_plan
       ws['B5'] = ad_names
       ws['B6'] = str(start_d) + '  to  ' + str(end_d)

       wb.save(report_file)


   try:
       wb = load_workbook(report_file)
       ws = wb.get_sheet_by_name('frequency')            
       row = 9
       for it in query_result:
           one_row = it.split('\t')
           print one_row
           if '10' == one_row[0]:
               one_row[0] = '10+'
           col = 1
           for one_cell in one_row:
               ws.cell(row = row, column = col).value = one_cell
               col = col + 1
           row = row + 1      
   except Thrift.TException, tx:
       print '[ERROR] %s' % (tx.message)
   else:
       wb.save(report_file)
   finally:
       pass
```
### Attention 注意事项
```
from openpyxl.writer.excel import ExcelWriter   
wb1=Workbook()#新建工作簿
ewb1=ExcelWriter(workbook=wb1)#新建一个ExcelWriter，用来写wb1  
ws1=wb1.worksheets[0]#取得wb1的第一个工作表ws1
one_cell = ws1.cell(row = row, column = col).value
ws1.cell(row = row, column = col).value = one_cell
ewb1.save(filename=dest_filename)#保存一定要有，否则不会有结果  
```

## Ref 参考
- 1.Python编程快速上手—让繁琐工作自动化第12章 https://automatetheboringstuff.com/chapter12/
- 2.python用openpyxl操作excel http://blog.csdn.net/longshenlmj/article/details/51706010
- 3.Python处理csv文件 http://www.cnblogs.com/sun-haiyu/p/7122329.html
- 4.OpenPyXl文档 https://openpyxl.readthedocs.io/en/stable/
- 5.Working with Excel Files in Python http://www.python-excel.org/
- 6.Python使用openpyxl读写excel文件的方法 http://www.jb51.net/article/117515.htm
- 7.python 学习小组http://www.thinksaas.cn/group/show/368/page/4
- 8.官网：
    https://pypi.python.org/pypi/openpyxl
    http://openpyxl.readthedocs.io/en/default/
- 9.good：
    http://blog.csdn.net/suofiya2008/article/details/6284208
    http://blog.csdn.net/zzukun/article/details/49946147
    http://www.thinksaas.cn/topics/0/501/501962.html

## Log
- 2018-02-13 创建。截止到“从表中取得单元格”，发现新到openpyxl模块中max_row等已经从函数get_highest_row()变为了sheet等一种属性。
- 2018-02-13 对文件进行了修订。在对照参考书《Python编程快速上手—让繁琐工作自动化第12章》学习的过程中，发现代码中许多已经不适用了，于是更多的参考了网上查找的解决方案，进行了更新。未完成，待补充剩下的章节内容。
