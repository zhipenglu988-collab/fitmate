#!/usr/bin/env python
"""Upload FitMate project files to GitHub via API"""
import win32cred, base64, os, json, urllib.request, ssl

TOKEN = win32cred.CredRead(
    'GitHub - https://api.github.com/zhipenglu988-collab',
    win32cred.CRED_TYPE_GENERIC
)['CredentialBlob'].decode('ascii')

OWNER = 'zhipenglu988-collab'
REPO = 'fitmate'
API = f'https://api.github.com/repos/{OWNER}/{REPO}/contents'

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

def github_request(method, url, data=None):
    headers = {
        'Authorization': f'token {TOKEN}',
        'Accept': 'application/vnd.github.v3+json',
        'User-Agent': 'FitMate-Builder',
    }
    body = json.dumps(data).encode() if data else None
    req = urllib.request.Request(url, data=body, headers=headers, method=method)
    try:
        resp = urllib.request.urlopen(req, timeout=30, context=ctx)
        return json.loads(resp.read()) if resp.status != 204 else {}
    except urllib.error.HTTPError as e:
        return {'error': e.code, 'body': e.read().decode()[:200]}

def upload_file(local_path, repo_path):
    with open(local_path, 'rb') as f:
        content = base64.b64encode(f.read()).decode()
    
    # Get existing file SHA if it exists (for update)
    existing = github_request('GET', f'{API}/{repo_path}')
    sha = existing.get('sha')
    
    data = {
        'message': f'Add {repo_path}',
        'content': content,
        'branch': 'master',
    }
    if sha:
        data['sha'] = sha
    
    result = github_request('PUT', f'{API}/{repo_path}', data)
    if 'error' in result and result['error'] == 422:
        # File might exist in a different way, try different approach
        print(f'  Skipping {repo_path}: already exists ({result.get("body","")[:60]})')
        return True
    elif 'error' in result:
        print(f'  FAILED {repo_path}: {result}')
        return False
    else:
        print(f'  Uploaded {repo_path}')
        return True

def walk_and_upload(base_dir, repo_prefix=''):
    files_ok = 0
    files_fail = 0
    excludes = {'.git', '__pycache__', 'bin', 'build', '.spec', '.db', '.log', 'create_repo.py', 'decode_token.py', 'get_gh_token.ps1', 'push_to_github.py', 'check_wsl.ps1', 'fitmate.zip'}
    exclude_exts = {'.pyc', '.pyo', '.db', '.log', '.zip'}
    
    for root, dirs, files in os.walk(base_dir):
        # Skip excluded dirs
        dirs[:] = [d for d in dirs if d not in excludes]
        
        for f in sorted(files):
            if f in excludes:
                continue
            if any(f.endswith(ext) for ext in exclude_exts):
                continue
            
            full_path = os.path.join(root, f)
            rel_dir = os.path.relpath(root, base_dir)
            if rel_dir == '.':
                repo_path = f
            else:
                repo_path = rel_dir.replace('\\', '/') + '/' + f
            
            # Skip utility scripts
            if repo_path in ['create_repo.py', 'decode_token.py', 'get_gh_token.ps1', 'push_to_github.py', 'check_wsl.ps1']:
                continue
            
            if upload_file(full_path, repo_path):
                files_ok += 1
            else:
                files_fail += 1
    
    return files_ok, files_fail

print(f'Uploading FitMate project to {OWNER}/{REPO}...')
print()

proj_dir = r'C:\Users\lzp\Desktop\jianshen'
ok, fail = walk_and_upload(proj_dir)

print(f'\nDone: {ok} uploaded, {fail} failed')
print(f'Repo: https://github.com/{OWNER}/{REPO}')
print(f'Actions: https://github.com/{OWNER}/{REPO}/actions')
print('\nAPK will auto-build in 20-40 min on GitHub Actions.')
print('Download from Actions page when complete.')
