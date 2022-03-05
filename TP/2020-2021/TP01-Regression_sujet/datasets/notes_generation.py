#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pandas
import numpy
import random

NBR = 100

# Les notes possibles
NOTES = numpy.arange(0, 20.1, 0.25)

print(NOTES)

notes1 = numpy.array(random.choices(NOTES, k=NBR))

notes2 = numpy.array(random.choices(NOTES, k=NBR))

admis = ((notes1 + notes2)/2.0 >= 10.0).astype(int)

dataset = pandas.DataFrame({"Note1": notes1, "Note2": notes2, "Admis": admis})

#dataset["Admis"] = dataset["Admis"].map({"True": "1", "False": "0"})

dataset.to_csv("./notes.csv", index=False)
