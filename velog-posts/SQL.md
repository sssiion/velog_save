<h4 id="mysql의-jdbc-드라이버-로드">mysql의 jdbc 드라이버 로드</h4>
<blockquote>
<p>Class.forName(&quot;com.mysql.cj.jdbc.Driver&quot;)</p>
</blockquote>
<h4 id="connection-객체의-생성">Connection 객체의 생성</h4>
<p>jsp, 서블릿이 데이터베이스에 접근하기 위해 Connection 객체 생성해야함.</p>
<blockquote>
<p>Connection 객체이름 = DriverManager.getConnetion(데이터베이스정보, 아이디, 패스워드)</p>
</blockquote>
<h5 id="객체-생성을-통한-데이터-베이스-연결-ex">객체 생성을 통한 데이터 베이스 연결 ex</h5>
<blockquote>
<p>Class.forName(&quot;com.mysql.cj.jdbc.Driver&quot;);
String url = &quot;jdbc://mysql://localhost:3306/jspdp?serverTimezone=UTC&quot;;
String jdbcId= &quot;jspuser&quot;;
String jdebcPw= &quot;jsppass&quot;;
Connection conn = DriverManager.getConnection(url, jdbcId, jdbcPw);</p>
</blockquote>
<h4 id="질의-수행">질의 수행</h4>
<h5 id="statement-객체">Statement 객체</h5>
<blockquote>
<p>Statement 객체 = connection객체.createStatement();</p>
</blockquote>
<blockquote>
<p>Class.forName(&quot;...&quot;);
String url=&quot;...&quot;;
String jdbcId=&quot;..&quot;;
String jdbcPw=&quot;..&quot;;
Connection conn =DriverManager.getConnection(url,jdbcId, jdbcPw);
Statement stmt = conn.createStatement();</p>
</blockquote>
<h6 id="executeupdate-메서드">executeUpdate() 메서드</h6>
<blockquote>
<p>Statement stmt = conn.createStatement();
int 변수 = stmt.executeUpdate(&quot;select 포함되지 않은 질의문&quot;);</p>
</blockquote>
<p>*변수 : 수행된 질의문에 의해 영향을 받은 레코드의 수 
 delete로 2개의 레코드가 제거됐다면 2를 반환</p>
<blockquote>
<p>stmt.executeUpdate(&quot;..&quot;); 로 사용도 가능</p>
</blockquote>
<h6 id="executequery-메서드">executeQuery() 메서드</h6>
<p>select 질의문을 사용하기 위한 메서드</p>
<blockquote>
<p>Statement stmt = conn.createStatement();
ResultSet 객체 = stmt.executeQuery(&quot;select 질의문&quot;);</p>
</blockquote>
<h5 id="preparedstatement-객체">PreparedStatement 객체</h5>
<p>질의문에 값대신 ?로 지정한다음 위치값을 넣어주는 형식</p>
<blockquote>
<p>String Query = &quot;insert into student values (?,?,?,?,?)&quot;;
PreparedStatement pstmt = conn.prepareStatement(Query);
pstmt.setString(1,&quot;shlee&quot;);
pstmt.setString(2, &quot;이순신&quot;);
pstmt.setString(3, &quot;정보통신공학과&quot;);
pstmt.setInt(4, 1);
pstmt.setInt(5, 850);
pstmt.executeUpdate();</p>
</blockquote>
<p>1부터 시작하는 필드 순서를 의미함, 위치 홀더에 지정되는 값</p>
<h4 id="resultset-객체">ResultSet 객체</h4>
<p>select 질의문이 수행되면 조건에 부합하는 결과가 객체에 저장.</p>
<blockquote>
<p>next() : 커서를 현재의 위치에서 다음 레코드로 이동
previous() 커서를 현재 위치에서 이전 레코드로 이동
first() : 맨처음 레코드로 이동
last() : 맨 마지막 레코드로 이동</p>
</blockquote>