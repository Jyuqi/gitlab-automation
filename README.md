# gitlab-automation

What does it do?
----------------

It automates several operations on gitlab:

- set up the administrator password(create_admin.py)
- create and save personal token so we can use it to visit gitlab API as an administrator(create_personal_token.sh)
- read configurations from flare-config.yml(parse_yaml.py)
- upload an ssh public key(parse_yaml.py)
- create a repository(parse_yaml.py)

After creating personal token, I save it in file "token" in current directory. To use it, copy and paste it in flare-config.yml.
