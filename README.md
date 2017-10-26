Role Name
=========

Ansible role to install and configure nginx

Requirements
------------

This role requires `letsencrypt` role to automate the request for a ssl certificate

Role Variables
--------------

A description of the settable variables for this role should go here, including any variables that are in defaults/main.yml, vars/main.yml, and any variables that can/should be set via parameters to the role. Any variables that are read from other roles and/or the global scope (ie. hostvars, group vars, etc.) should be mentioned here as well.

Default variables:

    nginx_basic_auth_user: ""
    nginx_basic_auth_password: ""
    nginx_conf_content: "{{ lookup('template', 'default.conf.j2') }}"
    nginx_vhost_name: default

Dependencies
------------

letsencrypt role.

Example Playbook
----------------

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

    - hosts: webserver
      roles:
         - role: nginx
           nginx_basic_auth_user: "admin"
           nginx_basic_auth_password: "{{ my_admin_password }}"
           nginx_conf_content: "{{ lookup('template', 'mysite.conf.j2') }}"
           nginx_vhost_name: mysite

License
-------

MIT
