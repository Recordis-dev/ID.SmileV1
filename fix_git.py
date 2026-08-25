import subprocess
subprocess.run(['git', 'add', '-A'])
subprocess.run(['git', 'commit', '-m', 'chore: finalize files'])
out = subprocess.check_output(['git', 'status', '--porcelain'])
with open('git_status_now.txt', 'wb') as f:
    f.write(out)
