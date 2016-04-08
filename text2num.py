#!/usr/bin/python
# This library is a simple implementation of a function to convert textual
# numbers written in English into their integer representations.
#
# This code is open source according to the MIT License as follows.
#
# Copyright (c) 2008 Greg Hewgill
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

import re

smallNumbers = {
    'zero': 0,
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9,
    'ten': 10,
    'eleven': 11,
    'twelve': 12,
    'thirteen': 13,
    'fourteen': 14,
    'fifteen': 15,
    'sixteen': 16,
    'seventeen': 17,
    'eighteen': 18,
    'nineteen': 19,
    'twenty': 20,
    'thirty': 30,
    'forty': 40,
    'fifty': 50,
    'sixty': 60,
    'seventy': 70,
    'eighty': 80,
    'ninety': 90
}

magnitudes = {
    'thousand':     1000,
    'million':      1000000,
    'billion':      1000000000,
    'trillion':     1000000000000,
    'quadrillion':  1000000000000000,
    'quintillion':  1000000000000000000,
    'sextillion':   1000000000000000000000,
    'septillion':   1000000000000000000000000,
    'octillion':    1000000000000000000000000000,
    'nonillion':    1000000000000000000000000000000,
    'decillion':    1000000000000000000000000000000000,
}

class NumberException(Exception):
    def __init__(self, msg):
        Exception.__init__(self, msg)

# input: string, list of strings, integer, list of integers
def text2num(number):
    if isinstance(number, list):
      text = ' '.join([str(item) for item in number])
    else:
      text = str(number)

    if len(text) == 0:
        return None

    words = re.split(r"[\s-]+", text)

    if len(words) == 0:
        return None
    elif len(words) == 1:
        try:
            return int(float(words[0]))
        except ValueError:
            pass
    total = 0
    current = 0
    for word in words:
        num = smallNumbers.get(word, None)
        if num is not None:
            current += num
        elif word == "hundred" and current != 0:
            current *= 100
        else:
            num = magnitudes.get(word, None)
            if num is not None:
                total += current * num
                current = 0
            else:
                raise NumberException("Unknown number: "+word)
    return total + current

if __name__ == "__main__":
    assert 1 == text2num("one")
    assert 12 == text2num("twelve")
    assert 72 == text2num("seventy two")
    assert 300 == text2num("three hundred")
    assert 1200 == text2num("twelve hundred")
    assert 12304 == text2num("twelve thousand three hundred four")
    assert 6000000 == text2num("six million")
    assert 6400005 == text2num("six million four hundred thousand five")
    assert 123456789012 == text2num("one hundred twenty three billion four hundred fifty six million seven hundred eighty nine thousand twelve")
    assert 4000000000000000000000000000000000 == text2num("four decillion")

#    print text2num("one")
#    print text2num("twelve")
#    print text2num("seventy two")
#    print text2num("three hundred")
#    print text2num("twelve hundred")
#    print text2num("twelve thousand three hundred four")
#    print text2num("six million")
#    print text2num("six million four hundred thousand five")
#    print text2num("one hundred twenty three billion four hundred fifty six million seven hundred eighty nine thousand twelve")
#    print text2num("four decillion")
    print text2num(["one", "hundred", "twenty", "three"])
    print text2num("one hundred twenty three")
    print text2num("123")
    print text2num(["123"])
    print text2num(123)
    print text2num([123])
