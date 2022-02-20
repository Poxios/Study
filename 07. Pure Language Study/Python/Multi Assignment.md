# Python multi assignment order
* We know, `a,b=1,2` is easy to use
* In this situation, code below works like this
```python
a,b=1,2
a,b=3,a
print(a,b) # 3, 1
```
* So, we are easy to be mistaken to understand this work's order, on multi assignment, real assignment to variables is processing after the line.
* but,
```python
a=None
a,a.next=ListNode(1),ListNode(2)
```
* this line doesn't make error, nonetype has no attribute "xx"
* because, python does not process this work after the line, just saving right var's values in temp memory.
* explained!