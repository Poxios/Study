# Cost Tracking
```python
with get_openai_callback() as cb:
        result = llm.invoke([s,h]).content
        print(cb)
```