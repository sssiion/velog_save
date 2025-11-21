<h4 id="스크립트-태그">스크립트 태그</h4>
<p>지시문 &lt;%@ .... %&gt;  : jsp 문서를 수행하기 위한 정보나 기능을 작성
선언문 &lt;%!  ... %&gt;  : JSP 문서에서 사용할 변수나 메서드를 선언
스크립트릿 &lt;%  ...%&gt; : 자바코드로 구성된 모든 jsp 스크립트 지정
표현식 &lt;%= .... %&gt;  :  print나 println 메서드 대신 간단한 데이터 출력
주석 &lt;%-- ...%&gt;     : 주석문 작성</p>
<h5 id="지시문">지시문</h5>
<p>종류 </p>
<blockquote>
<p>%@ page 속성=&quot;값% : jsp 문서의 수행을 위한 속성과 기능을 지정
%@ include file=&quot;파일명&quot;% : 현재 jsp 문서에 다른 jsp 문서를 삽입
%@ taglib prefix=&quot;프리픽스 url=&quot;URL&quot; % : jstl에서 태그 라이브러리를 지정</p>
</blockquote>
<h5 id="오류-처리">오류 처리</h5>
<p>지시문
page errorPage=&quot;--.jsp&quot; : 오류가 발생할 경우 오류를 처리하는 페이지 지정
page isErrorPage=&quot;true&quot; : 현재 페이지가 오류를 처리하는 페이지라는 것을 지정</p>
<p>web.xml 문서 사용</p>
<pre><code>&lt;error-page&gt;
  &lt;error-code&gt; 오류 코드 번호 
  &lt;location&gt; 오류 처리 페이지</code></pre><h4 id="jsp-내장-객체">jsp 내장 객체</h4>
<p>requeset : 클라이언트의 요청 정보를 저장
response : 클라이언트의 요청에 대한 응답 정보를 저장
out : 브라우저에 출력하기 위한 정보를 저장
session : HTTP의 세션 정보를 저장
application : 웹 애플리케이션에 대한 정보를 저장
config : JSP 문서의 초기화 파라미터 저장
page : JSP 문서 자체를 나타내는 객체
pageContext : 기본객체를 반환하거나 포워딩 수행
exception : 예외처리 위한 객체</p>
<h5 id="request-내장-객체">request 내장 객체</h5>
<p>파라미터
setCharaEncoding(encoding) : POST 방식으로 전달되는 문자열 인코딩 방식 지정
getParameter(String name ) : 파라미터 값 추출
getParameterNames(String name) : 파라미터 이름을 추출
getParameterValues(String name) : 파라미터값들을 배열로 반환</p>
<h5 id="response-내장객체">response 내장객체</h5>
<p>전 장에 잇음.</p>
<h6 id="한글-전달">한글 전달</h6>
<pre><code>&lt;% 
    String depart = URLEncoder.encode(&quot;소프트웨어&quot;, &quot;utf-8&quot;);
    response.sendRedirect(&quot;paramFormProc.jsp?depart=&quot;+depart);
%&gt;</code></pre><h5 id="out-내장객체">out 내장객체</h5>
<p>print() :인자로 가지는 데이터를 출력
println() : 인자로 가지는 데이터와 엔터 함께 출력</p>
<h5 id="pagecontext-내장-객체">pageContext 내장 객체</h5>
<p>forward(String path) : 현재 문서에서 path에 지정된 문서로 포워딩 수행
*서블릿 컨테이너
include(String path) : path에 해당하는 문서의 실행 결과를 현재 문서에 포함
*브라우저</p>
<blockquote>
<p>브라우저의 요청으로 수행되는 포워딩의 경우, 포워딩에 의해 새로운 요청이 발생하면 기존 request 객체는 소멸하고 새로운 request 객체가 생성 (response와 자바스크립트 포워딩 해당)</p>
</blockquote>
<blockquote>
<p>서블릿 컨테이너가 수행하는 포워딩의 경우, 포워딩에 의해 새로운 요청이 발생하면 새로운 request가 생성되지 않고 기존 request 객체가 전달됩니다. (pageContext 내장객체, RequestDispatcher 포워딩 해당)</p>
</blockquote>
<h5 id="config-내장-객체">config 내장 객체</h5>
<p>하나의 서블릿에 하나의 config 객체
web.xml</p>
<pre><code>&lt;servlet&gt;
      &lt;servlet-name&gt;서블릿 이름(임의 지정)
    &lt;jsp-file&gt; jsp 문서 이름
    &lt;init-param&gt;
          &lt;param-name&gt; 파라미터 이름
        &lt;param-value&gt; 파라미터 값
</code></pre><blockquote>
<p>사용
String nation = config.getInitParameter(&quot;nation&quot;);
String name = config.getInitParameter(&quot;name&quot;);</p>
</blockquote>
<h5 id="application-내장-객체">application 내장 객체</h5>
<p>같은 애플리케이션에 속산 모든 jsp문서는 application객체를 공유함.</p>
<pre><code>&lt;context-param&gt;
    &lt;description&gt;파라미터의 설명 문자열
    &lt;param-name&gt; 파라미터의 이름
    &lt;param-value&gt; 파라미터의 값
</code></pre><p>파라미터 추출</p>
<blockquote>
<p>getInitParameterNames() : 모든 파라미터의 이름을 추출
getInitParameter(String name) :  name에 해당하는 파라미터의 값 추출</p>
</blockquote>
<h5 id="exception-내장-객체">exception 내장 객체</h5>
<p>try-catch 구문에서 예외 처리를 사용하기 위해 사용</p>
<p>주요 메서드</p>
<blockquote>
<p>getMessage() : 오류 메시지를 문자열로 변환
printStackTrace() : 발생한 예외를 추적하기 위해 표준 스트림으로 스택 정보를 출력
toString() : 예외를 발생시킨 클래스의 이름과 함께 오류 메시지를 문자열로 반환) : 예외를 발생시킨 클래스의 이름과 함께 오류 메시지를 문자열로 반환</p>
</blockquote>
<p><img alt="" src="https://velog.velcdn.com/images/ssion/post/9ca68bb2-3410-4d30-8026-7a93d28c75f8/image.png" /></p>
<h5 id="내장객체의-용도">내장객체의 용도</h5>
<p>page : 하나의 jsp 문서 내에서 공유될 갑을 지정
request : 하나의 http 요청으로 처리되는 jsp 문서들 사이에서 공유되는 값을 저장 (주로 request 영역 내의 문서에 데이터 전달 목적)
session : 하나의 브라우저에서 실행되는 모든 jsp 문서들 사이에서 공유되는 값을 저장 (주로 로그인, 쇼핑몰 장바구니)
appliacation : 애플리케이션 전체에서 공유되는 값을 저장하기 위해 사용 (주로 애플리케이션의 공유 정보 지정에 사용)</p>
<p>내장객체 속성 바인딩 관련 메서드</p>
<blockquote>
<p>setAttribute( String name, Object value ) : value 값을 name 속성을 바인딩
getAttribute(String name) : name 속성 값을 추출
getAttributeNames() : 모든 속성의 이름을 enumeration 타입으로 변환
removeAttribute(String name) : name 속성을 제거</p>
</blockquote>
<blockquote>
<p>내장객체.setAttribute(속성 이름, 속성값);
데이터타입 변수 = (데이터타입)내장객체.getAttribute(속성이름);
내장객체.removeAttribute(속성이름);</p>
</blockquote>
<h4 id="액션태그">액션태그</h4>
<p>&lt;jsp:forward page=&quot;이동할 문서&quot;/&gt;
포워딩을 수행하는 액션 태그</p>
<blockquote>
<p>ex)
&lt;jsp:forward page=&quot;./target.jsp&quot; /&gt;
&lt;% String targetURL= &quot;./target.jsp&quot; %&gt;
&lt;jsp:forward page= &quot;&lt;%= targetURL %&gt;&quot; /&gt;</p>
</blockquote>
<p>form.jsp 문서를 처리하는 도중 <a href="">jsp:forward</a> 액션 태그를 만나면 page 속성에 지정된  to.jsp 문서로 포워딩이 발생 &gt; 브라우저가 요청한 문서는 form.jsp 지만 브라우저에 응답하는문서는 to.jsp이다</p>
<p><a href="">jsp:forward</a> 액션 태그의 포워딩 주체는 서블릿 컨테이너이다.
(url이 변경되지 않음)</p>
<p>일반적으로 새로운 요청이 발생하면 기존 request 내장 객체는 소멸하고 새로운 request 내장 객체가 생성됨 but <a href="">jsp:forward</a> 액션태그에 의해 새로운 요청이 발생하는 경우, 새로운 내장객체 생성이 아닌 기존 생성된 request 내장객체가 포워딩되는 문서로 전달됨.</p>
<h5 id="파라미터-전달">파라미터 전달</h5>
<p>&lt;jsp:forward page=&quot;이동할 문서&quot;&gt;
    &lt;jsp:param name=&quot;파라미터 이름&quot; value=&quot;파라미터 값&quot; /&gt;</p>
<h5 id="including">including</h5>
<blockquote>
<p>&lt;jsp:include page=&quot;포함할 문서&quot; flush=&quot;true/false&quot;&gt;</p>
</blockquote>
<p>forward 액션 태그는 clear() 메서드를 사용해 현재 버퍼의 내용을 강제로 비운 다음 포워딩을 수행하는 반면 include 는 현재 버퍼의 내용을 브라우저에 출력합니다.</p>
<p>*인클루딩 발생 &gt; 현재 문서의 실행을 멈추고 page 속성으로 지정된 문서를 실행하게되는데, 그때까지 버퍼에 저장되어 있던 내용을 브라우저로 출력한 다음 실행할지 아니면 현재 버퍼의 내용을 브라우저에 출력하지 않고 유지한 상태에서 실행할 지를 선택할 수 있음.</p>
<p>flush=&quot;true&quot; : 현재버ㅓㅍ의 내용을 브라우저로 출력해 버퍼를 비운 다음 page 속성에 지정된 문서를 실행(기본값)
false : 현재 버퍼의 내용을 유지한 상태로 page 속성에 지정된 문서를 실행함.</p>
<p>&lt;액션태그&gt;</p>
<table>
<thead>
<tr>
<th align="left">구분</th>
<th>forward</th>
<th>include</th>
</tr>
</thead>
<tbody><tr>
<td align="left">포워딩</td>
<td>포워딩 한번</td>
<td>포워딩 2번 (다시 원래 문서로 돌아옴)</td>
</tr>
<tr>
<td align="left">브라우저 응답</td>
<td>포워딩된 문서에서 응답</td>
<td>include 수행한 문서에서 응답</td>
</tr>
<tr>
<td align="left">기존 버퍼 내용</td>
<td>브라우저롤 전송하지 않고 강제로 비움</td>
<td>버퍼의 내용이 브라우저에 출력됨</td>
</tr>
</tbody></table>
<p>&lt;액션태그 vs 지시문&gt;</p>
<table>
<thead>
<tr>
<th align="left">구분</th>
<th>jsp include</th>
<th>include 지시문</th>
</tr>
</thead>
<tbody><tr>
<td align="left">결과처리</td>
<td>포함되는 문서의 실행결과만 포함</td>
<td>포함되는 문서의 소스코드를 삽입해 처리</td>
</tr>
<tr>
<td align="left">데이터 전달방법</td>
<td><a href="">jsp:param</a> 액션 태그</td>
<td>외부 문서에 변수를 선언해 사용</td>
</tr>
<tr>
<td align="left">컴파일</td>
<td>포함하는 파일과 포한되는 파일을 별도 컴파일</td>
<td>포함하는 파일과 포함되는 파일을 결합해 하나의 파일로 컴파일</td>
</tr>
</tbody></table>