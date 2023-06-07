# *module* .markdown_constructor

## Classes

### *class* `.markdown_constructor.MarkdownElement` [[source]](../markdown_constructor.py#L7)

Base: 

Base class for markdown renderers  

#### Methods

> **.markdown\_constructor.MarkdownElement.render**(*self: Any*) -> *str* [[source]](../markdown_constructor.py#L12)

Returns markdown representation of element  



### *class* `.markdown_constructor.Whitespace` [[source]](../markdown_constructor.py#L17)

Base: MarkdownElement

Markdown whitespace element  

#### Methods

> **.markdown\_constructor.Whitespace.render**(*self: Any*) -> *str* [[source]](../markdown_constructor.py#L20)

Returns whitespace  



### *class* `.markdown_constructor.NewLine` [[source]](../markdown_constructor.py#L25)

Base: MarkdownElement

Markdown new line element  

#### Methods

> **.markdown\_constructor.NewLine.render**(*self: Any*) -> *str* [[source]](../markdown_constructor.py#L28)

Returns new line character  



### *class* `.markdown_constructor.ParagraphBreak` [[source]](../markdown_constructor.py#L33)

Base: MarkdownElement

Markdown paragraph break element  

#### Methods

> **.markdown\_constructor.ParagraphBreak.render**(*self: Any*) -> *str* [[source]](../markdown_constructor.py#L36)

Returns two new line characters (for Markdown paragraph break)  



### *class* `.markdown_constructor.Line` [[source]](../markdown_constructor.py#L41)

Base: MarkdownElement

Markdown line break element  

#### Methods

> **.markdown\_constructor.Line.render**(*self: Any*) -> *str* [[source]](../markdown_constructor.py#L44)

Returns markdown line  



### *class* `.markdown_constructor.MarkdownContainer` [[source]](../markdown_constructor.py#L49)

Base: MarkdownElement

Base class for list of Markdown elements, also usefull for groupping  
other elements  
  
Attributes:  
elemens: list[MarkdownElement | str], list of inner elements,  
could be another MarkdownElement or python string  
sep: (MarkdownElement | str), elements separator, could be another  
MarkdownElement or python string  
  
Examples:  
Rendering multiple lines splitted by paragraph break  
  
```  
>> element = MarkdownContainer(  
>>     ['first paragraph', Line(), 'second paragraph'],  
>>     ParagraphBreak()  
>> )  
>> element.render()  
first paragraph  
  
---  
  
second paragraph  
  
```  

#### Methods

> **.markdown\_constructor.MarkdownContainer.\_\_init\_\_**(*self: Any*, *elements: list[(MarkdownElement | str)]*, *sep: (MarkdownElement | str)*) -> *Any* [[source]](../markdown_constructor.py#L78)

Args:  
  
- **self**: Any  
- **elements**: list[(MarkdownElement | str)]  
- **sep**: (MarkdownElement | str)  
  
Returns: Any  

> **.markdown\_constructor.MarkdownContainer.render**(*self: Any*) -> *str* [[source]](../markdown_constructor.py#L86)

Returns Markdown representation all inner elements,  
joined by separator  



### *class* `.markdown_constructor.Quote` [[source]](../markdown_constructor.py#L107)

Base: MarkdownElement

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

> **.markdown\_constructor.Quote.\_\_init\_\_**(*self: Any*, *text: str*) -> *Any* [[source]](../markdown_constructor.py#L124)

Args:  
  
- **self**: Any  
- **text**: str  
  
Returns: Any  

> **.markdown\_constructor.Quote.render**(*self: Any*) -> *str* [[source]](../markdown_constructor.py#L127)

Returns markdown quoted text  



### *class* `.markdown_constructor.Link` [[source]](../markdown_constructor.py#L137)

Base: MarkdownElement

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

> **.markdown\_constructor.Link.\_\_init\_\_**(*self: Any*, *text: str*, *link: str*, *quote: bool*) -> *Any* [[source]](../markdown_constructor.py#L156)

Args:  
  
- **self**: Any  
- **text**: str  
- **link**: str  
- **quote**: bool  
  
Returns: Any  

> **.markdown\_constructor.Link.render**(*self: Any*) -> *str* [[source]](../markdown_constructor.py#L166)

Returns Markdown link  



### *class* `.markdown_constructor.Paragraph` [[source]](../markdown_constructor.py#L176)

Base: MarkdownContainer

Class for Markdown paragraph element  

#### Methods

> **.markdown\_constructor.Paragraph.render**(*self: Any*) -> *str* [[source]](../markdown_constructor.py#L179)

Renders inner elements, with paragraph break in the end  



### *class* `.markdown_constructor.Header` [[source]](../markdown_constructor.py#L187)

Base: MarkdownContainer

Base class for Markdown header element  
  
Attributes:  
elements: list[MarkdownElement | str], list of inner elements  
sep: (MarkdownElement | str), elements separator  
level: int, optional, level of the header, 1 by default  
  
Examples:  
Rendering first level header  
  
```  
>> element = Header(  
>>     ['module', Whitespace(), Quote(['markdown_constructor'])]  
>> )  
>> element.render()  
  
# module markdown\_constructor  
```  

#### Methods

> **.markdown\_constructor.Header.\_\_init\_\_**(*self: Any*, *elements: list[(MarkdownElement | str)]*, *sep: (MarkdownElement | str)*, *level: int*) -> *Any* [[source]](../markdown_constructor.py#L209)

Args:  
  
- **self**: Any  
- **elements**: list[(MarkdownElement | str)]  
- **sep**: (MarkdownElement | str)  
- **level**: int  
  
Returns: Any  

> **.markdown\_constructor.Header.render**(*self: Any*) -> *str* [[source]](../markdown_constructor.py#L218)

Returns Markdown header with inner elelements  



### *class* `.markdown_constructor.H1` [[source]](../markdown_constructor.py#L227)

Base: Header

Class for 1 level Markdown header  

#### Methods

> **.markdown\_constructor.H1.\_\_init\_\_**(*self: Any*, *elements: list[(MarkdownElement | str)]*, *sep: (MarkdownElement | str)*) -> *Any* [[source]](../markdown_constructor.py#L230)

Args:  
  
- **self**: Any  
- **elements**: list[(MarkdownElement | str)]  
- **sep**: (MarkdownElement | str)  
  
Returns: Any  



### *class* `.markdown_constructor.H2` [[source]](../markdown_constructor.py#L238)

Base: Header

Class for 2 level Markdown header  

#### Methods

> **.markdown\_constructor.H2.\_\_init\_\_**(*self: Any*, *elements: list[(MarkdownElement | str)]*, *sep: (MarkdownElement | str)*) -> *Any* [[source]](../markdown_constructor.py#L241)

Args:  
  
- **self**: Any  
- **elements**: list[(MarkdownElement | str)]  
- **sep**: (MarkdownElement | str)  
  
Returns: Any  



### *class* `.markdown_constructor.H3` [[source]](../markdown_constructor.py#L249)

Base: Header

Class for 3 level Markdown header  

#### Methods

> **.markdown\_constructor.H3.\_\_init\_\_**(*self: Any*, *elements: list[(MarkdownElement | str)]*, *sep: (MarkdownElement | str)*) -> *Any* [[source]](../markdown_constructor.py#L252)

Args:  
  
- **self**: Any  
- **elements**: list[(MarkdownElement | str)]  
- **sep**: (MarkdownElement | str)  
  
Returns: Any  



### *class* `.markdown_constructor.H4` [[source]](../markdown_constructor.py#L260)

Base: Header

Class for 4 level Markdown header  

#### Methods

> **.markdown\_constructor.H4.\_\_init\_\_**(*self: Any*, *elements: list[(MarkdownElement | str)]*, *sep: (MarkdownElement | str)*) -> *Any* [[source]](../markdown_constructor.py#L263)

Args:  
  
- **self**: Any  
- **elements**: list[(MarkdownElement | str)]  
- **sep**: (MarkdownElement | str)  
  
Returns: Any  



### *class* `.markdown_constructor.H5` [[source]](../markdown_constructor.py#L271)

Base: Header

Class for 5 level Markdown header  

#### Methods

> **.markdown\_constructor.H5.\_\_init\_\_**(*self: Any*, *elements: list[(MarkdownElement | str)]*, *sep: (MarkdownElement | str)*) -> *Any* [[source]](../markdown_constructor.py#L274)

Args:  
  
- **self**: Any  
- **elements**: list[(MarkdownElement | str)]  
- **sep**: (MarkdownElement | str)  
  
Returns: Any  



### *class* `.markdown_constructor.H5` [[source]](../markdown_constructor.py#L282)

Base: Header

Class for 6 level Markdown header  

#### Methods

> **.markdown\_constructor.H5.\_\_init\_\_**(*self: Any*, *elements: list[(MarkdownElement | str)]*, *sep: (MarkdownElement | str)*) -> *Any* [[source]](../markdown_constructor.py#L285)

Args:  
  
- **self**: Any  
- **elements**: list[(MarkdownElement | str)]  
- **sep**: (MarkdownElement | str)  
  
Returns: Any  



### *class* `.markdown_constructor.Bold` [[source]](../markdown_constructor.py#L293)

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

> **.markdown\_constructor.Bold.render**(*self: Any*) -> *str* [[source]](../markdown_constructor.py#L307)

Returns bolded inner elements  



### *class* `.markdown_constructor.Italic` [[source]](../markdown_constructor.py#L312)

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

> **.markdown\_constructor.Italic.render**(*self: Any*) -> *str* [[source]](../markdown_constructor.py#L326)

Returns italic inner elements  



### *class* `.markdown_constructor.BoldItalic` [[source]](../markdown_constructor.py#L331)

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

> **.markdown\_constructor.BoldItalic.render**(*self: Any*) -> *str* [[source]](../markdown_constructor.py#L345)

Returns bolded italic inner elements  



### *class* `.markdown_constructor.Blockquotes` [[source]](../markdown_constructor.py#L350)

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

> **.markdown\_constructor.Blockquotes.render**(*self: Any*) -> *str* [[source]](../markdown_constructor.py#L364)

Returns blockquotes with inner elements  



### *class* `.markdown_constructor.OrderedList` [[source]](../markdown_constructor.py#L372)

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

> **.markdown\_constructor.OrderedList.\_\_init\_\_**(*self: Any*, *elements: list[(MarkdownContainer | str)]*) -> *Any* [[source]](../markdown_constructor.py#L391)

Args:  
  
- **self**: Any  
- **elements**: list[(MarkdownContainer | str)]  
  
Returns: Any  

> **.markdown\_constructor.OrderedList.render**(*self: Any*) -> *str* [[source]](../markdown_constructor.py#L394)

Returns Markdown ordered list with inner elements as items  



### *class* `.markdown_constructor.UnorderedList` [[source]](../markdown_constructor.py#L407)

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

> **.markdown\_constructor.UnorderedList.render**(*self: Any*) -> *str* [[source]](../markdown_constructor.py#L426)

Returns Markdown unordered list with inner elements as items  



### *class* `.markdown_constructor.InlineCode` [[source]](../markdown_constructor.py#L439)

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

> **.markdown\_constructor.InlineCode.render**(*self: Any*) -> *str* [[source]](../markdown_constructor.py#L453)

Returns Mrkdown inline code with inner elements  



### *class* `.markdown_constructor.Code` [[source]](../markdown_constructor.py#L458)

Base: MarkdownContainer

Class for Markdown multiline code block  
  
Attributes:  
elements: list[MarkdownElement | str], list of inner elements  
sep: (MarkdownElement | str), elements separator  
language: str, language to highlight in code block  
  
Examples:  
Rendering multiline code block  
  
```  
>> element = Code(  
>>     [  
>>         'import pandas as pd  
'  
>>         'import numpy as np'  
>>     ],  
>>     language='py'  
>> )  
>> element.render()  
import pandas as pd  
import numpy as np  
```  

#### Methods

> **.markdown\_constructor.Code.\_\_init\_\_**(*self: Any*, *elements: list[(MarkdownElement | str)]*, *sep: (MarkdownElement | str)*, *language: str*) -> *Any* [[source]](../markdown_constructor.py#L484)

Args:  
  
- **self**: Any  
- **elements**: list[(MarkdownElement | str)]  
- **sep**: (MarkdownElement | str)  
- **language**: str  
  
Returns: Any  

> **.markdown\_constructor.Code.render**(*self: Any*) -> *str* [[source]](../markdown_constructor.py#L493)

Returns markdown code block with inner elements  



### *class* `.markdown_constructor.ColumnOrientation` [[source]](../markdown_constructor.py#L502)

Base: str, Enum

Markdown table column orientation  

#### Methods



### *class* `.markdown_constructor.\_TableBorder` [[source]](../markdown_constructor.py#L509)

Base: MarkdownElement

Markdown table border element  

#### Methods

> **.markdown\_constructor.\_TableBorder.render**(*self: Any*) -> *Any* [[source]](../markdown_constructor.py#L512)

Returns markdown table border  



### *class* `.markdown_constructor.TableRow` [[source]](../markdown_constructor.py#L517)

Base: MarkdownContainer

Class for Markdown table row element  
  
Attributes:  
elements: list[MarkdownElement | str], table row elements  
  
Examples:  
Rendering table row  
  
```  
>> element = TableRow(['1', 'one'])  
>> element.render()  
1 | one  
```  

#### Methods

> **.markdown\_constructor.TableRow.\_\_init\_\_**(*self: Any*, *elements: list[(MarkdownElement | str)]*) -> *Any* [[source]](../markdown_constructor.py#L534)

Args:  
  
- **self**: Any  
- **elements**: list[(MarkdownElement | str)]  
  
Returns: Any  



### *class* `.markdown_constructor.Table` [[source]](../markdown_constructor.py#L538)

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
>> table = md.Table(  
>>     header=md.TableRow(['name', 'value']),  
>>     rows=[  
>>         md.TableRow(['1', 'one']),  
>>         md.TableRow(['2', 'two'])  
>>     ],  
>>     orientation=[md.ColumnOrientation.LEFT, md.ColumnOrientation.RIGHT]  
>> )  
>> table.render()  
name | value  
:-- | --:  
1 | one  
2 | two  
```  

#### Methods

> **.markdown\_constructor.Table.\_\_init\_\_**(*self: Any*, *header: TableRow*, *rows: list[TableRow]*, *orientation: (list[ColumnOrientation] | None)*) -> *Any* [[source]](../markdown_constructor.py#L568)

Args:  
  
- **self**: Any  
- **header**: TableRow  
- **rows**: list[TableRow]  
- **orientation**: (list[ColumnOrientation] | None)  
  
Returns: Any  

> **.markdown\_constructor.Table.render**(*self: Any*) -> *Any* [[source]](../markdown_constructor.py#L578)

Returns Markdown table  



### *class* `.markdown_constructor.HTMLComment` [[source]](../markdown_constructor.py#L596)

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

> **.markdown\_constructor.HTMLComment.render**(*self: Any*) -> *str* [[source]](../markdown_constructor.py#L610)

Returns markdown HTML comment with inner elements  



