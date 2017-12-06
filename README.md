Role Name
=========

Ansible role to install and configure nginx.

This role commes with a default ssl reverse proxy configuration.
This default conf can be override with the `nginx_conf_content` var.

Requirements
------------

This role requires `letsencrypt` role to automate the request for a ssl
certificate.

Role Variables
--------------

The `nginx_server_name` var is mandatory.

Default variables:

    nginx_basic_auth_user: ""
    nginx_basic_auth_password: ""
    nginx_conf_content: "{{ lookup('template', 'default.conf.j2') }}"
    nginx_server_name: example.com
    nginx_vhost_service_host: 127.0.0.1
    nginx_vhost_service_port: 8080

Dependencies
------------

letsencrypt role.

Example Playbook
----------------

    - hosts: webserver
      roles:
         - role: nginx
           nginx_basic_auth_user: "admin"
           nginx_basic_auth_password: "{{ my_admin_password }}"
           nginx_conf_content: "{{ lookup('template', 'mysite.conf.j2') }}"
           nginx_server_name: mysite.example.com

License
-------

MIT
