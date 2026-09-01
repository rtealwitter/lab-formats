"""Starter functions for the Rosetta Stone lab."""

import json
import csv
import io
import yaml

# tomllib joined the standard library in Python 3.11. On earlier versions,
# `pip install tomli` provides the very same module under a different name.
try:
    import tomllib
except ModuleNotFoundError:
    import tomli as tomllib


def to_json(obj):
    r"""
    Serialize a Python object into a pretty-printed JSON string.

    This is the "dump string" direction: Python object -> JSON text. Pass
    indent=2 so the result is readable (the same trick you use to eyeball the
    shape of a response you did not write), and sort_keys=True so the output is
    deterministic no matter what order the dict happened to be built in.

    >>> print(to_json({'username': 'Trump', 'text': 'hello'}))
    {
      "text": "hello",
      "username": "Trump"
    }
    >>> print(to_json({'debug': True, 'author': None}))
    {
      "author": null,
      "debug": true
    }
    """
    # TODO: your code here (hint: json.dumps with indent=2 and sort_keys=True)


def from_json(s):
    r"""
    Parse a JSON string into a Python object ("load string").

    JSON strings and keys always use double quotes; once the data is a Python
    str, Python echoes it back with single quotes, and the double-quote rule no
    longer applies. Note that `true`/`false`/`null` become `True`/`False`/`None`.

    >>> from_json('{"text": "hello", "username": "Trump"}')
    {'text': 'hello', 'username': 'Trump'}
    >>> from_json('[1, 2, 3]')
    [1, 2, 3]
    >>> from_json('{"author": null, "debug": true}')
    {'author': None, 'debug': True}
    """
    # TODO: your code here (hint: json.loads)


def roundtrip_json(obj):
    r"""
    Flatten an object to JSON text and parse it back, returning True when the
    result equals what we started with.

    Most data survives the trip. Some does not: JSON object keys are always
    strings, so an int key like 1 comes back as the string '1', and the
    round-trip is no longer equal. That is worth seeing once.

    >>> roundtrip_json({'text': 'hello', 'username': 'Trump'})
    True
    >>> roundtrip_json([{'text': 'hi'}, {'text': 'yo'}])
    True
    >>> roundtrip_json({'n': 1, 'ok': True, 'nothing': None})
    True
    >>> roundtrip_json({1: 'a'})
    False
    """
    # TODO: your code here (hint: call your own to_json and from_json, then ==)


def count_keys(obj):
    r"""
    Count the number of top-level keys in a dict.

    "Top-level" means we do not descend: a value that is itself a list or a dict
    still counts as exactly one key.

    >>> count_keys({'title': 'My Blog', 'port': 8080, 'tags': ['python', 'web']})
    3
    >>> count_keys({})
    0
    """
    # TODO: your code here


def yaml_to_obj(s):
    r"""
    Parse a YAML string into a Python object with yaml.safe_load.

    YAML is the config format humans edit: comments, no braces, one key: value
    per line, nesting shown by indentation, and lists written as `-` bullets.
    Every value comes back as an ordinary Python object, the same kind
    json.loads produces, which is the joke that "YAML is just Python-like JSON."

    >>> yaml_to_obj('title: My Blog') == {'title': 'My Blog'}
    True
    >>> config = '''
    ... title: My Blog
    ... port: 8080
    ... tags:
    ...   - python
    ...   - web
    ... '''
    >>> yaml_to_obj(config) == {'title': 'My Blog', 'port': 8080, 'tags': ['python', 'web']}
    True
    """
    # TODO: your code here (hint: yaml.safe_load, never yaml.load)


def norway_value():
    r"""
    Demonstrate the Norway problem and return the value YAML parsed.

    YAML 1.1 treats the bare words yes/no/on/off/true/false as booleans, so the
    ISO country code for Norway, `no`, is read as the boolean False. A file of
    country codes silently turns Norway into False with no error to warn you.
    This function pins the gotcha: parse `country: no` and return the value
    under `country`, which is False.

    >>> norway_value()
    False
    """
    # TODO: your code here (hint: yaml.safe_load('country: no'), then read 'country')


def toml_get(toml_str, key):
    r"""
    Read a top-level value out of a TOML document with tomllib.

    TOML is the config format of the Python and Rust worlds; you meet it most
    often as pyproject.toml. tomllib.loads parses a TOML string into a dict, the
    same way json.loads parses JSON, and here we look up a single top-level key.
    (Values under a `[section]` header are nested one level deeper.)

    >>> pyproject = '''
    ... name = "introcs"
    ... version = "1.0"
    ... port = 8080
    ... '''
    >>> toml_get(pyproject, 'name')
    'introcs'
    >>> toml_get(pyproject, 'port')
    8080
    """
    # TODO: your code here (hint: tomllib.loads, then index the key)


def csv_to_rows(csv_text):
    r"""
    Parse CSV text into a list of row dicts with csv.DictReader.

    CSV is the flat-table format: the first line names the columns and every
    line after it is one row. DictReader hands back one dict per row, keyed by
    the header, exactly the shape our tweets take. Every value arrives as a
    string, because CSV has no types (the number 8080 would come back as
    '8080'): CSV's own version of the Norway problem.

    >>> tweets = '''text,username
    ... hello,Trump
    ... world,Obama'''
    >>> csv_to_rows(tweets) == [
    ...     {'text': 'hello', 'username': 'Trump'},
    ...     {'text': 'world', 'username': 'Obama'},
    ... ]
    True
    """
    # TODO: your code here (hint: csv.DictReader over io.StringIO(csv_text))


def rows_to_csv(rows):
    r"""
    Serialize a list of row dicts to CSV text with csv.DictWriter.

    This is the writing direction, and it is exactly Project 2's extra credit:
    you scraped a list of dicts and now you save it as a table. The header comes
    from the first row's keys. Set the line ending to '\n' because CSV's real
    default is the Windows '\r\n'.

    >>> rows_to_csv([{'text': 'hello', 'username': 'Trump'}])
    'text,username\nhello,Trump\n'
    >>> rows_to_csv([{'a': '1', 'b': '2'}, {'a': '3', 'b': '4'}])
    'a,b\n1,2\n3,4\n'
    """
    # TODO: your code here (hint: csv.DictWriter into io.StringIO,
    #       fieldnames from the first row, lineterminator='\n')


def json_to_csv_rows(json_str):
    r"""
    Turn a JSON array of flat records into a list of row dicts, the shape that
    csv.DictReader and csv.DictWriter speak.

    This is the JSON -> CSV bridge from Project 2's extra credit: you saved
    scraped listings as JSON, and now you want the same records as spreadsheet
    rows. A CSV is always a list of rows, so a lone object is wrapped in a
    one-row list.

    >>> json_to_csv_rows('[{"text": "hello"}, {"text": "world"}]') == [
    ...     {'text': 'hello'}, {'text': 'world'}]
    True
    >>> json_to_csv_rows('{"text": "solo"}') == [{'text': 'solo'}]
    True
    """
    # TODO: your code here (hint: json.loads, then wrap a lone dict in a list)
