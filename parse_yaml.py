import yaml
import gitlab

with open("flare-config.yml", 'r') as stream:
    try:
        yaml_dic = yaml.safe_load(stream)
    except yaml.YAMLError as exc:
        print(exc)

# private token or personal token authentication, or use login.py with username or password
gl = gitlab.Gitlab(yaml_dic['git']['remote']['server'], private_token=yaml_dic['git']['remote']['private-token'])

gl.auth()

# get a single user
# user = gl.user
user = gl.users.list(username=yaml_dic['git']['remote']['user-name'])[0]
# list ssh keys for user
keys = user.keys.list()
# create a new ssh key
k = user.keys.create({'title': 'test_key',
                      'key': open(yaml_dic['git']['remote']['ssh-key-private']).read()})
# create a new project
project = gl.projects.create({'name':'test-gl6'})
project.save()
