### 2022 05 21
* TDD != 단위 테스트
* TDD = 테스트가 주도하는 개발 - 테스트 코드를 먼저 작성하는 것부터 시작
* 단위 테스트 = TDD의 첫 번째 단계인 기능 단위의 테스트 코드를 작성하는 것.
* **정말 많은 이유로 테스트 코드는 꼭 필요하다!**
* 패키지 명은 일반적으로 **웹 사이트 주소의 역순**으로 한다.
* `Execution failed for task ':test'. > No tests found for given includes:`에 대한 해결책 - https://stackoverflow.com/questions/55405441/intelij-2019-1-update-breaks-junit-tests
* JPA <- Hibernate <- Spring Data JPA 의 순서로 포팅이 되어있다고 생각하면 된다. 바로 Hibernate를 사용하지 않고 Spring Data JPA를 사용하는 이유는, JPA 구현체의 대세가 바뀌었을 때, 예를 들어 Hibernate가 대체될 때 쉽게 바꿀 수 있기 때문이다.
* 심지어 RDBMS -> NoSQL로 바꾸는 것도 가능하다.
* Getter / Setter 남용시 추후 언제 클래스의 인스턴스가 변해야하는지 알기가 힘들어진다. 따라서, **Entity 클래스에서는 절대 Setter 메소드를 만들지 않는다.** 대신 값 변경이 필요하면 그 명세에 정확히 맞춰서 메소드를 작성한다.
* 빌더를 사용하는 이유 = public test(String a, String b)가 있다고 할 때, a, b가 순서가 바뀌어도 실행 전까지 잘못된 것을 모른다. 그래서 빌더를 쓰면 어떤 필드에 어떤 값이 들어가는지 명시할 수 있다.