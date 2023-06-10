# *module* .markdown_constructor

## Classes

### *class* `.markdown_constructor.MarkdownContainer` [[source]](../markdown_constructor.py#L7)

Base: 

Base class for list of Markdown elements, also usefull for groupping  
other elements  
  
Attributes:  
elemens: list[MarkdownContainer | str], list of inner elements,  
could be another MarkdownContainer or python string  
sep: (MarkdownContainer | str), elements separator, could be another  
MarkdownContainer or python string  
  
Examples:  
Rendering multiple lines splitted by paragraph break  
  
```  
>> element = MarkdownContainer(  
>>     ['first paragraph', LINE, 'second paragraph'],  
>>     PARAGRAPH_BREAK  
>> )  
>> element.render()  
first paragraph  
  
---  
  
second paragraph  
  
```  

#### Methods

> **.markdown\_constructor.MarkdownContainer.\_\_init\_\_**(*self: Any*, *elements: list[MarkdownContainer | str]*, *sep: (MarkdownContainer | str)*) -> *Any* [[source]](../markdown_constructor.py#L36)

Args:  
  
- **self**: Any  
- **elements**: list[MarkdownContainer | str]  
- **sep**: (MarkdownContainer | str)  
  
Returns: Any  

> **.markdown\_constructor.MarkdownContainer.render**(*self: Any*) -> *str* [[source]](../markdown_constructor.py#L44)

Returns Markdown representation all inner elements,  
joined by separator  



### *class* `.markdown_constructor.Quote` [[source]](../markdown_constructor.py#L74)

Base: MarkdownContainer

Class for quoting Markdown symbols  
  
Attributes:  
text: str, element text  
  
Examples:  
Rendering string with quoted markdown symbols  
  
```  
>> element = Quote('text_with_dashes')  
>> element.render()  
text\_with\_dashes  
```  

#### Methods

> **.markdown\_constructor.Quote.\_\_init\_\_**(*self: Any*, *text: str*) -> *Any* [[source]](../markdown_constructor.py#L91)

Args:  
  
- **self**: Any  
- **text**: str  
  
Returns: Any  

> **.markdown\_constructor.Quote.render**(*self: Any*) -> *str* [[source]](../markdown_constructor.py#L94)

Returns markdown quoted text  



### *class* `.markdown_constructor.Link` [[source]](../markdown_constructor.py#L104)

Base: MarkdownContainer

Class for Markdown link element  
  
Attributes:  
text: str, link text  
link: str, link address  
quote: bool, need to quote link address, False by default  
  
Examples:  
Rendering link  
  
```  
>> element = Link('Go here', 'README.md')  
>> element.render()  
[Go here](README.md)  
```  

#### Methods

> **.markdown\_constructor.Link.\_\_init\_\_**(*self: Any*, *text: str*, *link: str*, *quote: bool*) -> *Any* [[source]](../markdown_constructor.py#L123)

Args:  
  
- **self**: Any  
- **text**: str  
- **link**: str  
- **quote**: bool  
  
Returns: Any  

> **.markdown\_constructor.Link.render**(*self: Any*) -> *str* [[source]](../markdown_constructor.py#L133)

Returns Markdown link  



### *class* `.markdown_constructor.Image` [[source]](../markdown_constructor.py#L143)

Base: Link

Class for Markdown image element  
  
Attributes:  
text: str, image text  
link: str, image address  
quote: bool, need to quote image address, False by default  
  
Examples:  
Rendering image  
  
```  
>> element = Image('Beautiful picture', 'image.png')  
>> element.render()  
![Beautiful picture](image.png)  
```  

#### Methods

> **.markdown\_constructor.Image.render**(*self: Any*) -> *Any* [[source]](../markdown_constructor.py#L162)

Returns Markdown image  



### *class* `.markdown_constructor.Paragraph` [[source]](../markdown_constructor.py#L167)

Base: MarkdownContainer

Class for Markdown paragraph element  

#### Methods

> **.markdown\_constructor.Paragraph.render**(*self: Any*) -> *str* [[source]](../markdown_constructor.py#L170)

Renders inner elements, with paragraph break in the end  



### *class* `.markdown_constructor.Header` [[source]](../markdown_constructor.py#L178)

Base: MarkdownContainer

Base class for Markdown header element  
  
Attributes:  
elements: list[MarkdownContainer | str], list of inner elements  
sep: (MarkdownContainer | str), elements separator  
level: int, optional, level of the header, 1 by default  
  
Examples:  
Rendering first level header  
  
```  
>> element = Header(  
>>     ['module', WHITESPACE, Quote(['markdown_constructor'])]  
>> )  
>> element.render()  
  
# module markdown\_constructor  
```  

#### Methods

> **.markdown\_constructor.Header.\_\_init\_\_**(*self: Any*, *elements: list[(MarkdownContainer | str)]*, *sep: (MarkdownContainer | str)*, *level: int*) -> *Any* [[source]](../markdown_constructor.py#L200)

Args:  
  
- **self**: Any  
- **elements**: list[(MarkdownContainer | str)]  
- **sep**: (MarkdownContainer | str)  
- **level**: int  
  
Returns: Any  

> **.markdown\_constructor.Header.render**(*self: Any*) -> *str* [[source]](../markdown_constructor.py#L209)

Returns Markdown header with inner elelements  



### *class* `.markdown_constructor.H1` [[source]](../markdown_constructor.py#L218)

Base: Header

Class for 1 level Markdown header  

#### Methods

> **.markdown\_constructor.H1.\_\_init\_\_**(*self: Any*, *elements: list[(MarkdownContainer | str)]*, *sep: (MarkdownContainer | str)*) -> *Any* [[source]](../markdown_constructor.py#L221)

Args:  
  
- **self**: Any  
- **elements**: list[(MarkdownContainer | str)]  
- **sep**: (MarkdownContainer | str)  
  
Returns: Any  



### *class* `.markdown_constructor.H2` [[source]](../markdown_constructor.py#L229)

Base: Header

Class for 2 level Markdown header  

#### Methods

> **.markdown\_constructor.H2.\_\_init\_\_**(*self: Any*, *elements: list[(MarkdownContainer | str)]*, *sep: (MarkdownContainer | str)*) -> *Any* [[source]](../markdown_constructor.py#L232)

Args:  
  
- **self**: Any  
- **elements**: list[(MarkdownContainer | str)]  
- **sep**: (MarkdownContainer | str)  
  
Returns: Any  



### *class* `.markdown_constructor.H3` [[source]](../markdown_constructor.py#L240)

Base: Header

Class for 3 level Markdown header  

#### Methods

> **.markdown\_constructor.H3.\_\_init\_\_**(*self: Any*, *elements: list[(MarkdownContainer | str)]*, *sep: (MarkdownContainer | str)*) -> *Any* [[source]](../markdown_constructor.py#L243)

Args:  
  
- **self**: Any  
- **elements**: list[(MarkdownContainer | str)]  
- **sep**: (MarkdownContainer | str)  
  
Returns: Any  



### *class* `.markdown_constructor.H4` [[source]](../markdown_constructor.py#L251)

Base: Header

Class for 4 level Markdown header  

#### Methods

> **.markdown\_constructor.H4.\_\_init\_\_**(*self: Any*, *elements: list[(MarkdownContainer | str)]*, *sep: (MarkdownContainer | str)*) -> *Any* [[source]](../markdown_constructor.py#L254)

Args:  
  
- **self**: Any  
- **elements**: list[(MarkdownContainer | str)]  
- **sep**: (MarkdownContainer | str)  
  
Returns: Any  



### *class* `.markdown_constructor.H5` [[source]](../markdown_constructor.py#L262)

Base: Header

Class for 5 level Markdown header  

#### Methods

> **.markdown\_constructor.H5.\_\_init\_\_**(*self: Any*, *elements: list[(MarkdownContainer | str)]*, *sep: (MarkdownContainer | str)*) -> *Any* [[source]](../markdown_constructor.py#L265)

Args:  
  
- **self**: Any  
- **elements**: list[(MarkdownContainer | str)]  
- **sep**: (MarkdownContainer | str)  
  
Returns: Any  



### *class* `.markdown_constructor.H6` [[source]](../markdown_constructor.py#L273)

Base: Header

Class for 6 level Markdown header  

#### Methods

> **.markdown\_constructor.H6.\_\_init\_\_**(*self: Any*, *elements: list[(MarkdownContainer | str)]*, *sep: (MarkdownContainer | str)*) -> *Any* [[source]](../markdown_constructor.py#L276)

Args:  
  
- **self**: Any  
- **elements**: list[(MarkdownContainer | str)]  
- **sep**: (MarkdownContainer | str)  
  
Returns: Any  



### *class* `.markdown_constructor.Bold` [[source]](../markdown_constructor.py#L284)

Base: MarkdownContainer

Class for Markdown bold element  
  
Examples:  
Rendering bold text  
  
```  
>> element = Bold(['some bold text'])  
>> element.render()  
**some bold text**  
```  

#### Methods

> **.markdown\_constructor.Bold.render**(*self: Any*) -> *str* [[source]](../markdown_constructor.py#L298)

Returns bolded inner elements  



### *class* `.markdown_constructor.Italic` [[source]](../markdown_constructor.py#L303)

Base: MarkdownContainer

Class for Markdown italic element  
  
Examples:  
Rendering italic text  
  
```  
>> element = Italic(['some italic text'])  
>> element.render()  
*some italic text*  
```  

#### Methods

> **.markdown\_constructor.Italic.render**(*self: Any*) -> *str* [[source]](../markdown_constructor.py#L317)

Returns italic inner elements  



### *class* `.markdown_constructor.BoldItalic` [[source]](../markdown_constructor.py#L322)

Base: MarkdownContainer

Class for Markdown bold italic element  
  
Examples:  
Rendering bold and italic text  
  
```  
>> element = BoldItalic(['some text'])  
>> element.render()  
**some text**  
```  

#### Methods

> **.markdown\_constructor.BoldItalic.render**(*self: Any*) -> *str* [[source]](../markdown_constructor.py#L336)

Returns bolded italic inner elements  



### *class* `.markdown_constructor.Strikethrough` [[source]](../markdown_constructor.py#L341)

Base: MarkdownContainer

Class for Markdown strikethrough element  
  
Examples:  
Rendering strikethrough text  
  
```  
>> element = Strikethrough(['some text'])  
>> element.render()  
~~some text~~  
```  

#### Methods

> **.markdown\_constructor.Strikethrough.render**(*self: Any*) -> *Any* [[source]](../markdown_constructor.py#L355)

Args:  
  
- **self**: Any  
  
Returns: Any  



### *class* `.markdown_constructor.Blockquotes` [[source]](../markdown_constructor.py#L359)

Base: MarkdownContainer

Class for Markdown blockquotes element  
  
Examples:  
Rendering block quotes  
  
```  
>> element = Blockquotes(['some text'])  
>> element.render()  
> some text  
```  

#### Methods

> **.markdown\_constructor.Blockquotes.render**(*self: Any*) -> *str* [[source]](../markdown_constructor.py#L373)

Returns blockquotes with inner elements  



### *class* `.markdown_constructor.OrderedList` [[source]](../markdown_constructor.py#L381)

Base: MarkdownContainer

Class for Markdown ordered list element  
  
Attributes:  
elements: list[MarkdownContainer | str], list of inner elements  
  
Examples:  
Rendering ordered list  
  
```  
>> element = OrderedList(['first item', 'second item', 'third item'])  
>> element.render()  
1. first item  
2. second item  
3. third item  
```  

#### Methods

> **.markdown\_constructor.OrderedList.\_\_init\_\_**(*self: Any*, *elements: list[(MarkdownContainer | str)]*) -> *Any* [[source]](../markdown_constructor.py#L400)

Args:  
  
- **self**: Any  
- **elements**: list[(MarkdownContainer | str)]  
  
Returns: Any  

> **.markdown\_constructor.OrderedList.render**(*self: Any*) -> *str* [[source]](../markdown_constructor.py#L403)

Returns Markdown ordered list with inner elements as items  



### *class* `.markdown_constructor.UnorderedList` [[source]](../markdown_constructor.py#L416)

Base: MarkdownContainer

Class for Markdown unordered list element  
  
Attributes:  
elements: list[MarkdownContainer | str], list of inner elements  
  
Examples:  
Rendering unordered list  
  
```  
>> element = UnorderedList(['first item', 'second item', 'third item'])  
>> element.render()  
- first item  
- second item  
- third item  
```  

#### Methods

> **.markdown\_constructor.UnorderedList.render**(*self: Any*) -> *str* [[source]](../markdown_constructor.py#L435)

Returns Markdown unordered list with inner elements as items  



### *class* `.markdown_constructor.TaskItem` [[source]](../markdown_constructor.py#L448)

Base: MarkdownContainer

Class for Markdown task list item element  
  
Attributes:  
elements: list[MarkdownContainer | str], list of inner elements  
sep: (MarkdownContainer | str), elements separator  
is_done: bool, is the task done or not, False by default  

#### Methods

> **.markdown\_constructor.TaskItem.\_\_init\_\_**(*self: Any*, *elements: list[(MarkdownContainer | str)]*, *sep: (MarkdownContainer | str)*, *is\_done: bool*) -> *Any* [[source]](../markdown_constructor.py#L458)

Args:  
  
- **self**: Any  
- **elements**: list[(MarkdownContainer | str)]  
- **sep**: (MarkdownContainer | str)  
- **is_done**: bool  
  
Returns: Any  

> **.markdown\_constructor.TaskItem.render**(*self: Any*) -> *Any* [[source]](../markdown_constructor.py#L467)

Returns Markdown task list item with inner elements  



### *class* `.markdown_constructor.TaskList` [[source]](../markdown_constructor.py#L475)

Base: UnorderedList

Class for Markdown task list element  
  
Attributes:  
elements: list[TaskItem], list of tasks  
  
Examples:  
Render task list  
  
```  
>> element = TaskList([  
>>     TaskItem(['First task'], is_done=True),  
>>     TaskItem(['Second task']),  
>>     TaskItem(['Third task'])  
>> ])  
>> element.render()  
- [x] First task  
- [ ] Second task  
- [ ] Third task  
```  

#### Methods

> **.markdown\_constructor.TaskList.\_\_init\_\_**(*self: Any*, *elements: list[TaskItem]*) -> *Any* [[source]](../markdown_constructor.py#L498)

Args:  
  
- **self**: Any  
- **elements**: list[TaskItem]  
  
Returns: Any  



### *class* `.markdown_constructor.InlineCode` [[source]](../markdown_constructor.py#L502)

Base: MarkdownContainer

Class for Markdown inline code element  
  
Examples:  
Rendering inline code  
  
```  
>> element = InlineCode(['code'])  
>> element.render()  
`code`  
```  

#### Methods

> **.markdown\_constructor.InlineCode.render**(*self: Any*) -> *str* [[source]](../markdown_constructor.py#L516)

Returns Mrkdown inline code with inner elements  



### *class* `.markdown_constructor.Code` [[source]](../markdown_constructor.py#L521)

Base: MarkdownContainer

Class for Markdown multiline code block  
  
Attributes:  
elements: list[MarkdownContainer | str], list of inner elements  
sep: (MarkdownContainer | str), elements separator  
language: str, language to highlight in code block  
  
Examples:  
Rendering multiline code block  
  
```  
>> element = Code(  
>>     [  
>>         'import pandas as pd\n'  
>>         'import numpy as np'  
>>     ],  
>>     language='py'  
>> )  
>> element.render()  
import pandas as pd  
import numpy as np  
```  

#### Methods

> **.markdown\_constructor.Code.\_\_init\_\_**(*self: Any*, *elements: list[(MarkdownContainer | str)]*, *sep: (MarkdownContainer | str)*, *language: str*) -> *Any* [[source]](../markdown_constructor.py#L547)

Args:  
  
- **self**: Any  
- **elements**: list[(MarkdownContainer | str)]  
- **sep**: (MarkdownContainer | str)  
- **language**: str  
  
Returns: Any  

> **.markdown\_constructor.Code.render**(*self: Any*) -> *str* [[source]](../markdown_constructor.py#L556)

Returns markdown code block with inner elements  



### *class* `.markdown_constructor.ColumnOrientation` [[source]](../markdown_constructor.py#L565)

Base: str, Enum

Markdown table column orientation  

#### Methods



### *class* `.markdown_constructor.TableRow` [[source]](../markdown_constructor.py#L575)

Base: MarkdownContainer

Class for Markdown table row element  
  
Attributes:  
elements: list[MarkdownContainer | str], table row elements  
  
Examples:  
Rendering table row  
  
```  
>> element = TableRow(['1', 'one'])  
>> element.render()  
1 | one  
```  

#### Methods

> **.markdown\_constructor.TableRow.\_\_init\_\_**(*self: Any*, *elements: list[(MarkdownContainer | str)]*) -> *Any* [[source]](../markdown_constructor.py#L592)

Args:  
  
- **self**: Any  
- **elements**: list[(MarkdownContainer | str)]  
  
Returns: Any  



### *class* `.markdown_constructor.Table` [[source]](../markdown_constructor.py#L596)

Base: MarkdownContainer

Class for Markdown table element  
  
Attributes:  
header: TableRow, table columns names  
rows: list[TableRow], list of table rows  
orientation: list[ColumnOrientation] or None, columns orientations,  
will be left for every column by default  
  
Examples:  
Rendering table  
  
```  
>> table = Table(  
>>     header=TableRow(['name', 'value']),  
>>     rows=[  
>>         TableRow(['1', 'one']),  
>>         TableRow(['2', 'two'])  
>>     ],  
>>     orientation=[  
>>         ColumnOrientation.LEFT,  
>>         ColumnOrientation.RIGHT  
>>     ]  
>> )  
>> table.render()  
name | value  
:-- | --:  
1 | one  
2 | two  
```  

#### Methods

> **.markdown\_constructor.Table.\_\_init\_\_**(*self: Any*, *header: TableRow*, *rows: list[TableRow]*, *orientation: (list[ColumnOrientation] | None)*) -> *Any* [[source]](../markdown_constructor.py#L629)

Args:  
  
- **self**: Any  
- **header**: TableRow  
- **rows**: list[TableRow]  
- **orientation**: (list[ColumnOrientation] | None)  
  
Returns: Any  

> **.markdown\_constructor.Table.render**(*self: Any*) -> *Any* [[source]](../markdown_constructor.py#L639)

Returns Markdown table  



### *class* `.markdown_constructor.HTMLComment` [[source]](../markdown_constructor.py#L657)

Base: MarkdownContainer

Class for HTML comment  
  
Examples:  
Rendering an HTML comment (not visible in Markdown)  
  
```  
>> element = HTMLComment(['very usefull information'])  
>> element.render()  
<!--very usefull information-->  
```  

#### Methods

> **.markdown\_constructor.HTMLComment.render**(*self: Any*) -> *str* [[source]](../markdown_constructor.py#L671)

Returns markdown HTML comment with inner elements  



### *class* `.markdown_constructor.Latex` [[source]](../markdown_constructor.py#L680)

Base: MarkdownContainer

Class for Latex formulas  

#### Methods

> **.markdown\_constructor.Latex.render**(*self: Any*) -> *Any* [[source]](../markdown_constructor.py#L685)

Args:  
  
- **self**: Any  
  
Returns: Any  



