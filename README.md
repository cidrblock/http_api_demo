```

# the vault command was
# ansible-vault encrypt_string --vault-password-file password_file 'password'


pip install q

ansible-playbook site.yaml -i inventory.yaml --vault-password-file=password_file -vvvv

<demo> 
<demo> local domain socket path is /home/bthornto/.ansible/pc/285c61166c
Trying secret FileVaultSecret(filename='/home/bthornto/github/http_api_sample/password_file') for vault_id=default
ok: [demo] => {
    "changed": false,
    "password": "password",
    "username": "brad"
}



$ tail /tmp/q

 0.0s login: username='brad', password='password'

```
