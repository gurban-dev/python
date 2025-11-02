'''
Syntax:
string[start:stop:step]

Assuming the step value is not negative:
start: The index where the slice begins (inclusive).
       If omitted, it defaults to the beginning of the sequence
       (index 0).

stop: The index where the slice ends (exclusive).
      If omitted, it defaults to one past the last index of the
      sequence.

step: The increment between elements. If omitted, it defaults to 1.

"!XeXgXaXsXsXeXmX XtXeXrXcXeXsX XeXhXtX XmXaX XI"[::-2]

In the context of the above example:

Taking into account that the step value is negative:
The absence of a value before the first colon indicates that
the slice starts from one index past the end of the string
(len("!XeXgXaXsXsXeXmX XtXeXrXcXeXsX XeXhXtX XmXaX XI")).

The absence of a value before the second colon indicates that
the slice stops at one index before the beginning of the string.

The -2 is the step value, which means move backward by 2
characters each time. The negative makes the slicing occur
in reverse order.
'''
print('\n!XeXgXaXsXsXeXmX XtXeXrXcXeXsX XeXhXtX XmXaX XI"[::-2]:\n',
      "!XeXgXaXsXsXeXmX XtXeXrXcXeXsX XeXhXtX XmXaX XI"[::-2], sep='')