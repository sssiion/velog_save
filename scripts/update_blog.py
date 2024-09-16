import feedparser
import git
import os

# 벨로그 RSS 피드 URL
# example : rss_url = 'https://api.velog.io/rss/@ssion'
rss_url = 'https://api.velog.io/rss/@ssion'

# 깃허브 레포지토리 경로
repo_path = '.'


    
# 'velog-posts' 폴더 경로
posts_dir = os.path.join(repo_path, 'velog-posts')
print(f"Current working directory: {os.getcwd()}")
print(f"Target posts directory: {posts_dir}")

# 'velog-posts' 폴더가 없다면 생성
if not os.path.exists(posts_dir):
    os.makedirs(posts_dir)
    print(f"Created directory: {posts_dir}")


# 레포지토리 로드
repo = git.Repo(repo_path)

# RSS 피드 파싱
feed = feedparser.parse(rss_url)
print(f"Feed title: {feed.feed.title}")


# 각 글을 파일로 저장하고 커밋
for entry in feed.entries:
    # 파일 이름에서 유효하지 않은 문자 제거 또는 대체
    file_name = entry.title
    file_name = file_name.replace('/', '-')  # 슬래시를 대시로 대체
    file_name = file_name.replace('\\', '-')  # 백슬래시를 대시로 대체
    # 필요에 따라 추가 문자 대체
    file_name += '.md'
    file_path = os.path.join(posts_dir, file_name)
    print(f"File path: {file_path}")

    # 파일이 이미 존재하지 않으면 생성/ 내용이 다르면 업데이트
    if os.path.exists(file_path):
        # 파일 내용 읽기
        with open(file_path, 'r', encoding='utf-8') as file:
            existing_content = file.read()
        
        # 새 내용
        new_content = entry.description
        
        # 내용이 다르면 파일 업데이트
        if existing_content != new_content:
            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(new_content)
            print(f"Updated file: {file_path}")
        # 깃허브 커밋
        try:
            repo.git.add(file_path)
            repo.git.commit('-m', f'Add post: {entry.title}')
            print(f"Committed file: {file_path}")
        except git.exc.GitCommandError as e:
            print(f"Git error: {e}")            
        

# 변경 사항을 깃허브에 푸시
try:
    repo.git.push()
    print("Changes pushed to remote repository.")
except Exception as e:
    print(f"Error pushing changes: {e}")
