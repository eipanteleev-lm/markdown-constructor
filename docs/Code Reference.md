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



### *class* `.markdown_constructor.Quote` [[source]](../markdown_constructor.py#L71)

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

> **.markdown\_constructor.Quote.\_\_init\_\_**(*self: Any*, *text: str*) -> *Any* [[source]](../markdown_constructor.py#L88)

Args:  
  
- **self**: Any  
- **text**: str  
  
Returns: Any  

> **.markdown\_constructor.Quote.render**(*self: Any*) -> *str* [[source]](../markdown_constructor.py#L91)

Returns markdown quoted text  



### *class* `.markdown_constructor.Link` [[source]](../markdown_constructor.py#L101)

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

> **.markdown\_constructor.Link.\_\_init\_\_**(*self: Any*, *text: str*, *link: str*, *quote: bool*) -> *Any* [[source]](../markdown_constructor.py#L120)

Args:  
  
- **self**: Any  
- **text**: str  
- **link**: str  
- **quote**: bool  
  
Returns: Any  

> **.markdown\_constructor.Link.render**(*self: Any*) -> *str* [[source]](../markdown_constructor.py#L130)

Returns Markdown link  



### *class* `.markdown_constructor.Image` [[source]](../markdown_constructor.py#L140)

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

> **.markdown\_constructor.Image.render**(*self: Any*) -> *Any* [[source]](../markdown_constructor.py#L159)

Returns Markdown image  



### *class* `.markdown_constructor.Paragraph` [[source]](../markdown_constructor.py#L164)

Base: MarkdownContainer

Class for Markdown paragraph element  

#### Methods

> **.markdown\_constructor.Paragraph.render**(*self: Any*) -> *str* [[source]](../markdown_constructor.py#L167)

Renders inner elements, with paragraph break in the end  



### *class* `.markdown_constructor.Header` [[source]](../markdown_constructor.py#L175)

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

> **.markdown\_constructor.Header.\_\_init\_\_**(*self: Any*, *elements: list[(MarkdownContainer | str)]*, *sep: (MarkdownContainer | str)*, *level: int*) -> *Any* [[source]](../markdown_constructor.py#L197)

Args:  
  
- **self**: Any  
- **elements**: list[(MarkdownContainer | str)]  
- **sep**: (MarkdownContainer | str)  
- **level**: int  
  
Returns: Any  

> **.markdown\_constructor.Header.render**(*self: Any*) -> *str* [[source]](../markdown_constructor.py#L206)

Returns Markdown header with inner elelements  



### *class* `.markdown_constructor.H1` [[source]](../markdown_constructor.py#L215)

Base: Header

Class for 1 level Markdown header  

#### Methods

> **.markdown\_constructor.H1.\_\_init\_\_**(*self: Any*, *elements: list[(MarkdownContainer | str)]*, *sep: (MarkdownContainer | str)*) -> *Any* [[source]](../markdown_constructor.py#L218)

Args:  
  
- **self**: Any  
- **elements**: list[(MarkdownContainer | str)]  
- **sep**: (MarkdownContainer | str)  
  
Returns: Any  



### *class* `.markdown_constructor.H2` [[source]](../markdown_constructor.py#L226)

Base: Header

Class for 2 level Markdown header  

#### Methods

> **.markdown\_constructor.H2.\_\_init\_\_**(*self: Any*, *elements: list[(MarkdownContainer | str)]*, *sep: (MarkdownContainer | str)*) -> *Any* [[source]](../markdown_constructor.py#L229)

Args:  
  
- **self**: Any  
- **elements**: list[(MarkdownContainer | str)]  
- **sep**: (MarkdownContainer | str)  
  
Returns: Any  



### *class* `.markdown_constructor.H3` [[source]](../markdown_constructor.py#L237)

Base: Header

Class for 3 level Markdown header  

#### Methods

> **.markdown\_constructor.H3.\_\_init\_\_**(*self: Any*, *elements: list[(MarkdownContainer | str)]*, *sep: (MarkdownContainer | str)*) -> *Any* [[source]](../markdown_constructor.py#L240)

Args:  
  
- **self**: Any  
- **elements**: list[(MarkdownContainer | str)]  
- **sep**: (MarkdownContainer | str)  
  
Returns: Any  



### *class* `.markdown_constructor.H4` [[source]](../markdown_constructor.py#L248)

Base: Header

Class for 4 level Markdown header  

#### Methods

> **.markdown\_constructor.H4.\_\_init\_\_**(*self: Any*, *elements: list[(MarkdownContainer | str)]*, *sep: (MarkdownContainer | str)*) -> *Any* [[source]](../markdown_constructor.py#L251)

Args:  
  
- **self**: Any  
- **elements**: list[(MarkdownContainer | str)]  
- **sep**: (MarkdownContainer | str)  
  
Returns: Any  



### *class* `.markdown_constructor.H5` [[source]](../markdown_constructor.py#L259)

Base: Header

Class for 5 level Markdown header  

#### Methods

> **.markdown\_constructor.H5.\_\_init\_\_**(*self: Any*, *elements: list[(MarkdownContainer | str)]*, *sep: (MarkdownContainer | str)*) -> *Any* [[source]](../markdown_constructor.py#L262)

Args:  
  
- **self**: Any  
- **elements**: list[(MarkdownContainer | str)]  
- **sep**: (MarkdownContainer | str)  
  
Returns: Any  



### *class* `.markdown_constructor.H6` [[source]](../markdown_constructor.py#L270)

Base: Header

Class for 6 level Markdown header  

#### Methods

> **.markdown\_constructor.H6.\_\_init\_\_**(*self: Any*, *elements: list[(MarkdownContainer | str)]*, *sep: (MarkdownContainer | str)*) -> *Any* [[source]](../markdown_constructor.py#L273)

Args:  
  
- **self**: Any  
- **elements**: list[(MarkdownContainer | str)]  
- **sep**: (MarkdownContainer | str)  
  
Returns: Any  



### *class* `.markdown_constructor.Bold` [[source]](../markdown_constructor.py#L281)

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

> **.markdown\_constructor.Bold.render**(*self: Any*) -> *str* [[source]](../markdown_constructor.py#L295)

Returns bolded inner elements  



### *class* `.markdown_constructor.Italic` [[source]](../markdown_constructor.py#L300)

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

> **.markdown\_constructor.Italic.render**(*self: Any*) -> *str* [[source]](../markdown_constructor.py#L314)

Returns italic inner elements  



### *class* `.markdown_constructor.BoldItalic` [[source]](../markdown_constructor.py#L319)

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

> **.markdown\_constructor.BoldItalic.render**(*self: Any*) -> *str* [[source]](../markdown_constructor.py#L333)

Returns bolded italic inner elements  



### *class* `.markdown_constructor.Strikethrough` [[source]](../markdown_constructor.py#L338)

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

> **.markdown\_constructor.Strikethrough.render**(*self: Any*) -> *Any* [[source]](../markdown_constructor.py#L352)

Args:  
  
- **self**: Any  
  
Returns: Any  



### *class* `.markdown_constructor.Blockquotes` [[source]](../markdown_constructor.py#L356)

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

> **.markdown\_constructor.Blockquotes.render**(*self: Any*) -> *str* [[source]](../markdown_constructor.py#L370)

Returns blockquotes with inner elements  



### *class* `.markdown_constructor.OrderedList` [[source]](../markdown_constructor.py#L378)

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

> **.markdown\_constructor.OrderedList.\_\_init\_\_**(*self: Any*, *elements: list[(MarkdownContainer | str)]*) -> *Any* [[source]](../markdown_constructor.py#L397)

Args:  
  
- **self**: Any  
- **elements**: list[(MarkdownContainer | str)]  
  
Returns: Any  

> **.markdown\_constructor.OrderedList.render**(*self: Any*) -> *str* [[source]](../markdown_constructor.py#L400)

Returns Markdown ordered list with inner elements as items  



### *class* `.markdown_constructor.UnorderedList` [[source]](../markdown_constructor.py#L413)

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

> **.markdown\_constructor.UnorderedList.render**(*self: Any*) -> *str* [[source]](../markdown_constructor.py#L432)

Returns Markdown unordered list with inner elements as items  



### *class* `.markdown_constructor.TaskItem` [[source]](../markdown_constructor.py#L445)

Base: MarkdownContainer

Class for Markdown task list item element  
  
Attributes:  
elements: list[MarkdownContainer | str], list of inner elements  
sep: (MarkdownContainer | str), elements separator  
is_done: bool, is the task done or not, False by default  

#### Methods

> **.markdown\_constructor.TaskItem.\_\_init\_\_**(*self: Any*, *elements: list[(MarkdownContainer | str)]*, *sep: (MarkdownContainer | str)*, *is\_done: bool*) -> *Any* [[source]](../markdown_constructor.py#L455)

Args:  
  
- **self**: Any  
- **elements**: list[(MarkdownContainer | str)]  
- **sep**: (MarkdownContainer | str)  
- **is_done**: bool  
  
Returns: Any  

> **.markdown\_constructor.TaskItem.render**(*self: Any*) -> *Any* [[source]](../markdown_constructor.py#L464)

Returns Markdown task list item with inner elements  



### *class* `.markdown_constructor.TaskList` [[source]](../markdown_constructor.py#L472)

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

> **.markdown\_constructor.TaskList.\_\_init\_\_**(*self: Any*, *elements: list[TaskItem]*) -> *Any* [[source]](../markdown_constructor.py#L495)

Args:  
  
- **self**: Any  
- **elements**: list[TaskItem]  
  
Returns: Any  



### *class* `.markdown_constructor.InlineCode` [[source]](../markdown_constructor.py#L499)

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

> **.markdown\_constructor.InlineCode.render**(*self: Any*) -> *str* [[source]](../markdown_constructor.py#L513)

Returns Mrkdown inline code with inner elements  



### *class* `.markdown_constructor.Code` [[source]](../markdown_constructor.py#L518)

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

> **.markdown\_constructor.Code.\_\_init\_\_**(*self: Any*, *elements: list[(MarkdownContainer | str)]*, *sep: (MarkdownContainer | str)*, *language: str*) -> *Any* [[source]](../markdown_constructor.py#L544)

Args:  
  
- **self**: Any  
- **elements**: list[(MarkdownContainer | str)]  
- **sep**: (MarkdownContainer | str)  
- **language**: str  
  
Returns: Any  

> **.markdown\_constructor.Code.render**(*self: Any*) -> *str* [[source]](../markdown_constructor.py#L553)

Returns markdown code block with inner elements  



### *class* `.markdown_constructor.ColumnOrientation` [[source]](../markdown_constructor.py#L562)

Base: str, Enum

Markdown table column orientation  

#### Methods



### *class* `.markdown_constructor.TableRow` [[source]](../markdown_constructor.py#L572)

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

> **.markdown\_constructor.TableRow.\_\_init\_\_**(*self: Any*, *elements: list[(MarkdownContainer | str)]*) -> *Any* [[source]](../markdown_constructor.py#L589)

Args:  
  
- **self**: Any  
- **elements**: list[(MarkdownContainer | str)]  
  
Returns: Any  



### *class* `.markdown_constructor.Table` [[source]](../markdown_constructor.py#L593)

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

> **.markdown\_constructor.Table.\_\_init\_\_**(*self: Any*, *header: TableRow*, *rows: list[TableRow]*, *orientation: (list[ColumnOrientation] | None)*) -> *Any* [[source]](../markdown_constructor.py#L626)

Args:  
  
- **self**: Any  
- **header**: TableRow  
- **rows**: list[TableRow]  
- **orientation**: (list[ColumnOrientation] | None)  
  
Returns: Any  

> **.markdown\_constructor.Table.render**(*self: Any*) -> *Any* [[source]](../markdown_constructor.py#L636)

Returns Markdown table  



### *class* `.markdown_constructor.HTMLComment` [[source]](../markdown_constructor.py#L654)

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

> **.markdown\_constructor.HTMLComment.render**(*self: Any*) -> *str* [[source]](../markdown_constructor.py#L668)

Returns markdown HTML comment with inner elements  



