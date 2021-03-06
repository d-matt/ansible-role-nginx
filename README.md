Role Name
=========

Ansible role to install and configure nginx.

This role comes with a default ssl reverse proxy configuration balancing
a pool of hosts.
This default conf can be overriden with the `nginx_conf_content` var.

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
    nginx_conf_content: "{{ lookup('template', 'reverse_proxy.conf.j2') }}"
    nginx_server_name: example.com
    nginx_vhost_service_hosts:
      - 127.0.0.1
    nginx_vhost_service_port: 8080
    nginx_deactivate_default: False

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
