if '{{cookiecutter.initialize_git_repo}}'.strip().lower()[0] == 'y':
    import subprocess
    
    subprocess.call(['git', 'init', '-b', '{{cookiecutter.default_branch}}'])
    subprocess.call(['git', 'remote', 'add', 'origin', '{{cookiecutter.plugin_source}}'])
    # subprocess.call(['git', 'add', '*'])
    # subprocess.call(['git', 'commit', '-m', 'Initial commit'])
    # subprocess.call(['git', 'push', '-u', 'origin', '{{cookiecutter.default_branch}}'])
    
    subprocess.call(['pre-commit', 'install'])
