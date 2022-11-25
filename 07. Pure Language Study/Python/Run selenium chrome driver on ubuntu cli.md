# Run selenium chrome driver on ubuntu cli
* Get pure `chromedriver` file.
```bash
mv chromedriver /usr/bin/chromedriver
# /usr/bin/ 으로 파일 이동

chown root:root /usr/bin/chromedriver 

chmod +x /usr/bin/chromedriver
```
* Write code without absolute path
```python
driver = webdriver.Chrome()
```