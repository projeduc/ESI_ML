#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pandas
import numpy
import random

NBR = 100

# Possible grades
GRADES = numpy.arange(0, 20.1, 0.25)

print(GRADES)

grade1 = numpy.array(random.choices(GRADES, k=NBR))

grade2 = numpy.array(random.choices(GRADES, k=NBR))

admitted = ((grade1 + grade2)/2.0 >= 10.0).astype(int)

dataset = pandas.DataFrame({"G1": notes1, "G2": notes2, "Admitted": admitted})


dataset.to_csv("./grades.csv", index=False)
