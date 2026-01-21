- 경로 폴더의 쓰임 설명
    - `resources/static` ****는 정적 리소스를 저장하는 데 사용
        
        정적 리소스에는 HTML, CSS, JavaScript, 이미지 파일 등
        
    - `templates` ****은 동적 웹 페이지를 저장하는 경로로 사용
        
        여기에 저장된 HTML 파일은 타임리프와 같은 템플릿 엔진을 통해 처리되며, 이 과정에서 서버 측 데이터나 로직이 페이지에 반영되어 최종적인 HTML이 생성 
        
        ex) ${data}를 사용하여 서버로부터 data가 무엇인지에 따라 화면에 데이터가 바뀔 수 있음

- Controller
    
    ```java
    @Controller
    public class HelloController {
    	
    	@GetMapping("hello-mvc") //-> url 이름 ex) localhost:8080/hello-mvc
    	public String helloMvc(@RequestParam("name") String name, Nodel model) { //@RequestParmr: url에서 param인 name의 값을 요청함
    		model.addAttrivute("name", name);                                      //ex) localhost:8080/hello-mvc?name=spring!
    		return "hello-template"; //-> hello-template.html로 연
    	}
    }
    
    ```
    
- View
    경로: resources/template/hello-template.html
	```html
	<html xmlns:th="http://www.thymeleaf.org">
	<body>
	<p th:text="'hello ' + ${name}"> hello! empty</p>
	</body>
	</html>
	```