1. 쉽게 로컬에서 구동할 수 있게 하기 위한 `ollama`라는 툴이 있다고 함.  
* `GGUF` 포맷이라는 게 있는데, ML 모델을 한 파일에 묶어놓은 파일이라고 보면 될듯.  
&nbsp;

2. llama 모델을 선택
* 여러 LLM 모델 중에 가장 흔하게 들을 수 있었던 meta 사의 llama 모델을 구동해본다.
* 기본적으로 한국어 특화로 나온게 아니기 때문에, 한국어로 파인튜닝? 된 모델을 선택해야할듯.  
&nbsp;  

3. llama3 중 한국어 특화 모델을 찾는 과정
* 구글에 llama ko라고 검색하면 blossom, luxia, 등등이 나오는데 여러 글을 본 결과 [teddylee777님의 gguf](https://huggingface.co/teddylee777/Llama-3-Open-Ko-8B-gguf/tree/main)를 쓰면 될 것으로 판단.
* 8B와 40B는 모델 사이즈 차이로, 숫자 크면 돌리기 어려운 대신 성능 좋고 뭐 그런거다.  
&nbsp;

4. 목록 중에 어떤 것을 받아야 하는가  
<img width="324" alt="image" src="https://github.com/Portunecookie/TiTo/assets/62606632/05b131fe-ff7b-4cf0-8e01-e082b9268596">  
  
* 파일 이름 끝에 붙은 `QN`에서 N은 숫자를 의미하는데, 이 숫자가 높을 수록 높은 비트로 양자화 되어있다는 뜻. 성능 올라가지만 무거움.
* `K_M`, `K_S` 이런건 옵션을 뜻함. 정확히 뭔지 모르겠어서 더 검색해봄
* https://www.reddit.com/r/LocalLLaMA/comments/159nrh5/the_difference_between_quantization_methods_for/  
> Generally, the K_M models have the best balance between size and PPL, so q3_K_M, q4_K_M, q5_K_M, etc. I like q5, and q4 best usually. Here's some of my test data with tokens/s:
* 일단 돌리는게 목적이니 K_M을 사용해본다.  
&nbsp;
  
5. 실행 환경 설정
* 환경 : RTX 4090, WSL (Ubuntu)
* `Modelfile`이라는 파일을 생성해서 아래 내용을 넣어야 한다고 한다.
```modelfile
FROM Llama-3-Open-Ko-8B-Q8_0.gguf

TEMPLATE """{{- if .System }}
<s>{{ .System }}</s>
{{- end }}
<s>Human:
{{ .Prompt }}</s>
<s>Assistant:
"""

SYSTEM """A chat between a curious user and an artificial intelligence assistant. The assistant gives helpful, detailed, and polite answers to the user's questions."""

PARAMETER temperature 0
PARAMETER num_predict 3000
PARAMETER num_ctx 4096
PARAMETER stop <s>
PARAMETER stop </s>
```  
* Modelfile 내부 내용의 수정이 꽤 유의미 할 것 같아서, 이를 좀 더 공부해보자.
  
6. 실행 결과  
* `ollama create llama3-ko -f Modelfile`으로 모델을 만들고
* `ollama run llama3-ko` 한방으로 실행이 된다
* 하지만 결과가 만족스럽지 않다. 네이버 뉴스 아무거나 들어가서 전체선택하고 "한줄로 요약해줘" 라고 했을 때 우리가 평소에 쓰던 GPT랑은 완전히 다른것 같다. 아예 엉뚱하게 요약해준다. 빈칸을 뱉거나.
![image](https://github.com/Portunecookie/TiTo/assets/62606632/bcbd5fae-9793-4c10-b194-f46a5c7089fa)
* 그래도 GPU는 100% 쓰는 것으로 봐서 잘 동작 하는듯
  
1. 성능 개선
* 양자화된 모델을 사용해서인가? llama3-ko가 거의 GPT3.5-turbo 수준의 성능이 난다는데 이 정도로 처참한 이유를 모르겠다.
* 아마 parameters 수정을 통해 개선할 수 있을지도?  
* `oTerm`이라는 터미널 내부에서 사용할 수 있는 프롬프트식 툴을 발견했다.  
![image](https://github.com/Portunecookie/TiTo/assets/62606632/eddbbec7-6994-4ee6-94e4-b67c79c5c5ea)  
* 신기하다  
![image](https://github.com/Portunecookie/TiTo/assets/62606632/24aa56e3-91e2-499b-8b36-6f12eac0d477)  
   
1. 쌩 llama3를 돌려봐야겠다.

* 
  
1. 야놀자의 EEVE 모델도 참고해봐야겠다.
  * https://huggingface.co/yanolja/EEVE-Korean-Instruct-10.8B-v1.0

### 궁금한 점
* `토큰` 단위는 정확히 무엇을 뜻하는가? 
* Langchain을 통한 RAG 구현법 공부하기
* 그냥 쌩 LLM 모델이랑, Finetuning을 했을 때가 날 것의 느낌이 줄어든다는게 무슨 뜻이지?
  
---
  
| @Poxios, 2024.06.29.