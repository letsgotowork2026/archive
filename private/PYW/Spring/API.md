- @ResponseBody 문자 반환
    
    ```java
    @Controller
    public class HelloController {
    
    	@GetMapping("hello-string")
    	@ResponseBody //return에 직접 넣어줌 view(template)부분이 없고 문자가 그대로 나옴
    	public String helloString(@RequestParam("name") String name){
    	    return "hello " + name;
    	}
    	
    }
    ```
    
    @ResponseBody를 사용하면 ViewResolver를 사용하지 않음
    
    대신에 HTTP의 BODY에 문자 내용을 직접 반환(HTML BODY TAG를 말하는 것이 아님)

    - @ResponseBody 객체 반환

    ```java
    @GetMapping("hello-api")
    @ResponseBody
    public Hello helloApi(@RequestParam("name") String name){
        Hello hello = new Hello();
        hello.setName(name);
        return hello;  //객체 반환하면 객체가 JSON으로 변환되어 반환
    }
    static class Hello {
        private String name;

        public String getName() {
            return name;
        }

        public void setName(String name) {
            this.name = name;
        }

    }```