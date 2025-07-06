from ldapauthenticator import LDAPAuthenticator
auth = LDAPAuthenticator(
    server_address='ldaps://ad.example.com',
    server_port=636,
    use_ssl=True,
    bind_dn='CN=binduser,CN=Users,DC=example,DC=com',
    bind_password='binduser_password',
    user_search_base='OU=Users,DC=example,DC=com',
    user_attribute='sAMAccountName',
    lookup_dn=True,
    lookup_dn_search_filter='({login_attr}={login})',
    lookup_dn_user_dn_attribute='cn'
)
result = auth.authenticate(None, {'username': 'testuser', 'password': 'testpassword'})
print(result)
