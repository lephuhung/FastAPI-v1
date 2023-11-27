security_scopes: list [str] = ['security', 'admin', 'guest']
scopes: list[str] = ['security']

if scopes in security_scopes:
     print('True')
else:
    print('False')