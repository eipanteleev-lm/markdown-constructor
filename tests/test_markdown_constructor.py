import os
import sys
import importlib.util

TESTS_PATH = os.path.dirname(os.path.abspath(__file__))
BASE_PATH = os.path.dirname(TESTS_PATH)
MODULE_PATH = os.path.join(BASE_PATH, 'markdown_constructor.py')

spec = importlib.util.spec_from_file_location(
    "markdown_constructor",
    MODULE_PATH
)
md = importlib.util.module_from_spec(spec)
sys.modules["markdown_constructor"] = md
spec.loader.exec_module(md)


def test_quote():
    assert (
        md.Quote('text_with_dashes').render() == 'text\\_with\\_dashes'
    )


def test_link():
    for args, expected in [
        (('Go here', 'README.md', False), '[Go here](README.md)'),
        (
            ('Code Reference', 'Code Reference.md', True),
            '[Code Reference](Code%20Reference.md)'
        ),
        (
            ('Link', 'https://example.com'),
            '[Link](https://example.com)'
        )
    ]:
        link = md.Link(*args)
        assert link.render() == expected


def test_image():
    for args, expected in [
        (('Image', 'image.png', False), '![Image](image.png)'),
        (
            ('Another image', 'Another image.md', True),
            '![Another image](Another%20image.md)'
        ),
        (
            ('Third image', 'https://example.com/image.png'),
            '![Third image](https://example.com/image.png)'
        )
    ]:
        image = md.Image(*args)
        assert image.render() == expected


def test_headers():
    for cls, args, expected in [
        (
            md.H1,
            (['Header 1']),
            '# Header 1'
        ),
        (
            md.H2,
            (['Header 2']),
            '## Header 2'
        ),
        (
            md.H3,
            (['Header 3']),
            '### Header 3'
        ),
        (
            md.H4,
            (['Header 4']),
            '#### Header 4'
        ),
        (
            md.H5,
            (['Header 5']),
            '##### Header 5'
        ),
        (
            md.H6,
            (['Header 6']),
            '###### Header 6'
        )
    ]:
        assert cls(*args).render().strip() == expected


def test_bold():
    assert md.Bold(['test']).render() == '**test**'


def test_italic():
    assert md.Italic(['test']).render() == '*test*'


def test_bold_italic():
    assert md.BoldItalic(['test']).render() == '***test***'


def test_strikethrough():
    assert md.Strikethrough(['test']).render() == '~~test~~'


def test_blockquotes():
    blockquoted_text = md.Blockquotes(['test'])
    assert blockquoted_text.render() == '> test'

    blockquoted_text = md.Blockquotes(
        [
            'test line\n'
            'test line'
        ]
    )

    expected = (
        '> test line\n'
        '> test line'
    )

    assert blockquoted_text.render() == expected


def test_ordered_list():
    ordered_list = md.OrderedList([
        'test line 1',
        'test line 2'
    ])

    expected = (
        '1. test line 1\n'
        '2. test line 2'
    )

    assert ordered_list.render() == expected

    ordered_list = md.OrderedList([
        'test line 1',
        md.Bold(['test line 2'])
    ])

    expected = (
        '1. test line 1\n'
        '2. **test line 2**'
    )

    assert ordered_list.render() == expected


def test_unordered_list():
    unordered_list = md.UnorderedList([
        'test line 1',
        'test line 2'
    ])

    expected = (
        '- test line 1\n'
        '- test line 2'
    )

    assert unordered_list.render() == expected

    unordered_list = md.UnorderedList([
        'test line 1',
        md.Bold(['test line 2'])
    ])

    expected = (
        '- test line 1\n'
        '- **test line 2**'
    )

    assert unordered_list.render() == expected


def test_task_list():
    task_list = md.TaskList(
        [
            md.TaskItem(['task 1'], is_done=True),
            md.TaskItem(['task 2'], is_done=False),
            md.TaskItem(['task 3'], is_done=True)
        ]
    )

    expected = (
        '- [x] task 1\n'
        '- [ ] task 2\n'
        '- [x] task 3'
    )

    assert task_list.render() == expected


def test_inline_code():
    assert md.InlineCode(['test']).render() == '`test`'


def test_code():
    code = md.Code(
        [
            'import pandas as pd\n'
            'import numpy as np'
        ],
        language='py'
    )

    expected = (
        '```py\n'
        'import pandas as pd\n'
        'import numpy as np\n'
        '```'
    )

    assert code.render() == expected


# TODO: add tests for other elements
