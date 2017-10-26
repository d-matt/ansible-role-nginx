import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_hosts_file(host):
    f = host.file('/etc/hosts')

    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'


def test_nginx_is_installed(host):
    nginx = host.package('nginx')

    assert nginx.is_installed


def test_nginx_is_running(host):
    nginx = host.service('nginx')

    assert nginx.is_running


def test_nginx_is_enabled(host):
    nginx = host.service('nginx')

    assert nginx.is_enabled


def test_port_80_is_open(host):
    assert host.socket("tcp://0.0.0.0:80").is_listening
