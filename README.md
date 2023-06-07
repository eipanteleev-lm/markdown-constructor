# markdown-constructor

A simple python module for object oriented generating Markdown formatted text

## Usage

```py
import os
import markdown_constructor as md

path = os.path.abspath(__file__)

with open(path) as f:
    code = f.read()

markdown = md.MarkdownContainer(
    [
        md.H1(['markdown-constructor']),
        md.Paragraph([
            'A simple python module for object oriented generating '
            'Markdown formatted text'
        ]),
        md.H2(['Usage']),
        md.Code([code], language='py'),
        md.ParagraphBreak(),
        md.Paragraph([
            "For more information about supported elements see ",
            md.Link('docs', 'docs/Code Reference.md', quote=True)
        ]),
        md.H2(['Testing']),
        md.Code(
            [
                'pip install tox\n'
                'tox'
            ],
            language='sh'
        )
    ]
)

with open('README.md', 'w') as f:
    f.write(markdown.render())
```

For more information about supported elements see [docs](docs/Code%20Reference.md)

## Testing

```sh
pip install tox
tox
```