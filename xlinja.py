# -*- coding: utf-8 -*- 

from zipfile import ZipFile
from jinja2 import Template
from io import BytesIO
import click
import json

def replace_xls(template, my_dict):
    f = ZipFile(template)
    in_memory = BytesIO()
    w = ZipFile(in_memory, "w")

    for name in f.namelist():
        s = f.read(name)
        if name == "xl/sharedStrings.xml":
            template = Template(s.decode("utf-8"))
            s = template.render(my_dict)
            s = s.encode("utf-8")
        w.writestr(name, s)

    f.close()
    w.close()
    in_memory.seek(0)
    return in_memory      


@click.command()
@click.argument("template")
@click.option("--output", "-o", default="xlinja.xlsx")
@click.option("--json_string", "-j")
def cmd(template, output, json_string):
    if json_string is not None:
        my_dic = json.loads(json_string)
    mf = replace_xls(template, my_dic)
    data = mf.read()                                                                                     
    with open(output, "wb") as wf:
        wf.write(data)

if __name__ == "__main__":
    cmd()