<h4 id="서블릿-생명-주기">서블릿 생명 주기</h4>
<p>1) init() 메서드 : 서블릿 생성되면서 기본적으로 수행되어야 하는 내용이 있다면 재정의
2) service() 메서드 : init으로 서블ㄹ릿 초기화하고 서블릿 컨테이너는 service 메서드를 호출 &gt; 서블릿의 고유의 기능인 비즈니스 로직을 수행하는 메서드임
3) destory() 메서드 : 서블릿 인스턴스가 컨테이너에서 제거되거나 웹서버가 종료될때 호출됨 (init과 마찬가지로 1번만 실행)</p>
<h4 id="서블릿-url-매핑">서블릿 url 매핑</h4>
<p>url 매핑 : 서블릿을 요청하기 위한 url과 서블릿을 연결하는 것, 브라우저를 통해 서블릿을 실행하려면 반드시 url 매핑을 사용해야함
web.xml : </p>
<pre><code>    &lt;servlet&gt;
          &lt;servlet-mapping&gt; 이름
        &lt;servlet-class&gt; 패키지를 포함하는 서블릿 클래스 이름
</code></pre><pre><code>      &lt;servlet-mapping&gt;
          &lt;servlet-name&gt;이름
        &lt;url-mapping&gt; url 매핑 이름 (/문자로 시작)
</code></pre><p> 애너테이션 매핑 : web.xml 없이 서블릿 내에서 url 매핑 정보를 직접 지정
          @webservlet(&quot;/매핑이름&quot;)
          @webservlet(description=&quot;서블릿정보&quot;, urlPatterns=&quot;/매핑이름&quot;)
          @webservlet(description=&quot;서블릿 정보&quot;, urlPatterns={&quot;/매핑이름1&quot;, &quot;/매핑이름2&quot;})</p>
<h4 id="servletcontext-객체">servletContext 객체</h4>
<pre><code>&lt;context-param&gt;
  &lt;param-name&gt; 파라미터 이름
  &lt;param-value&gt; 파라미터 값</code></pre><p>servletContext 파라미터 추출</p>
<blockquote>
<p>getInitParameter(String name) : name에 해당하는 파라미터의 값 반화</p>
</blockquote>
<blockquote>
<p>getInitParameterNames() : 모든 serveltContext 파라미터들의 이름을 Enumeration 타입으로 반환</p>
</blockquote>
<h4 id="servletcontext-바인딩">servletContext 바인딩</h4>
<p>: 서블릿 사이에서 정보를 공유하기 위해 사용</p>
<blockquote>
<p>setAttribute(String name, Object object) : object를 name이라는 속성으로 바인딩</p>
</blockquote>
<blockquote>
<p>getAttribute(String name) : 바인딩 되어잇는 name 속성 값을 추출</p>
</blockquote>
<blockquote>
<p>removeAttribute(String name) : 바인딩 되어있는 name 속성을 제거</p>
</blockquote>