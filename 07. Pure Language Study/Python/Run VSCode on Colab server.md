# Run VSCode on Colab server

* https://velog.io/@taki0412/%EA%B5%AC%EA%B8%80-Colab-%EC%84%9C%EB%B2%84%EB%A5%BC-%EB%A1%9C%EC%BB%AC%EC%97%90%EC%84%9C-%EC%82%AC%EC%9A%A9%ED%95%98%EA%B8%B0
* https://www.freecodecamp.org/news/how-to-use-google-colab-with-vs-code/
* Run code-server (vscode on web) on your google colab server for free!
* ssh setup guide included


```py
!pip install colabcode
!ngrok authtoken ----AUTH TOKEN HERE----
from colabcode import ColabCode
ColabCode(port=10000, password="PASSWORD_HERE")
```