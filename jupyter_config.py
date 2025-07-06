c.JupyterHub.authenticator_class = 'ldapauthenticator.LDAPAuthenticator'

# AD server settings
c.LDAPAuthenticator.server_address = 'ldaps://ad.example.com'  # Use ldaps:// for secure connection (port 636)
c.LDAPAuthenticator.server_port = 636  # Default for LDAPS; use 389 for LDAP (insecure)
c.LDAPAuthenticator.use_ssl = True  # Set to True for LDAPS

# Bind credentials (optional, for searching AD)
c.LDAPAuthenticator.bind_dn = 'CN=binduser,CN=Users,DC=example,DC=com'  # AD service account
c.LDAPAuthenticator.bind_password = 'binduser_password'

# User search settings
c.LDAPAuthenticator.user_search_base = 'OU=Users,DC=example,DC=com'
c.LDAPAuthenticator.user_attribute = 'sAMAccountName'  # Common for AD; could be 'userPrincipalName'
c.LDAPAuthenticator.lookup_dn = True  # Enable DN lookup for AD
c.LDAPAuthenticator.lookup_dn_search_filter = '({login_attr}={login})'
c.LDAPAuthenticator.lookup_dn_user_dn_attribute = 'cn'

# Optional: Restrict to specific AD groups
c.LDAPAuthenticator.allowed_groups = ['CN=JupyterUsers,OU=Groups,DC=example,DC=com']

# Create home directories for users (if needed)
c.LDAPAuthenticator.create_user_home_dir = True
c.LDAPAuthenticator.create_user_home_dir_cmd = ['mkhomedir_helper']

# Admin users
c.Authenticator.admin_users = {'admin_username'}  # Replace with AD username(s)

# Allow all authenticated AD users (or restrict with allowed_users)
c.Authenticator.allow_all = True  # Set to False and use c.Authenticator.allowed_users = {'user1', 'user2'} for restrictions
