#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask, request, render_template, jsonify
import convert

app = Flask(__name__, static_folder="public", template_folder="views")


@app.route("/")
def homepage():
    return render_template("index.html")


@app.route("/api/convert")
def metric_imp_converter():
    input = request.args["input"].replace(" ", "")
    init_num = convert.get_num(input)
    init_unit = convert.get_unit(input)
    return_num = convert.convert(init_num, init_unit)
    return_unit = convert.get_return_unit(init_unit)
    string = convert.get_string(init_num, init_unit, return_num, return_unit)

    return jsonify(
        initNum=init_num,
        initUnit=init_unit,
        returnNum=return_num,
        returnUnit=return_unit,
        string=string,
    )


if __name__ == "__main__":
    app.run()
