import os
import markdown_constructor as md

path = os.path.abspath(__file__)
filename = os.path.basename(path)

with open(path) as f:
    code = f.read()

markdown = md.MarkdownContainer(
    [
        md.Image(
            'Workflow Badge',
            (
                'https://github.com/eipanteleev-lm/markdown-constructor'
                '/actions/workflows/python-app.yml/badge.svg'
            )
        ),
        md.PARAGRAPH_BREAK,
        md.H1(['markdown-constructor']),
        md.Paragraph([
            'A simple python module for object oriented generating '
            'Markdown formatted text'
        ]),
        md.H2(['Installation']),
        md.Paragraph([
            md.Code(
                (
                    'git clone '
                    'https://github.com/eipanteleev-lm/markdown-constructor\n'
                    'cd markdown-constructor\n'
                    'pip install -e .'
                ),
                language='sh'
            )
        ]),
        md.H2(['Usage']),
        md.Paragraph([
            'This README generated by ',
            md.Link(filename, filename, quote=True)
        ]),
        md.Code(code, language='py'),
        md.PARAGRAPH_BREAK,
        md.Paragraph([
            "For more information about supported elements see ",
            md.Link('docs', 'docs/Code Reference.md', quote=True)
        ]),
        md.H2(['Testing']),
        md.Code(
            (
                'pip install tox\n'
                'tox'
            ),
            language='sh'
        )
    ]
)

with open('README.md', 'w') as f:
    f.write(markdown.render())
