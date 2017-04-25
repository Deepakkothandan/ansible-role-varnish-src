import testinfra.utils.ansible_runner
import pytest

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    '.molecule/ansible_inventory').get_hosts('all')


@pytest.mark.parametrize("name", [
    ("varnishd"),
    ("varnishadm"),
    ("varnishhist"),
    ("varnishlog"),
    ("varnishncsa"),
    ("varnishstat"),
    ("varnishtest"),
    ("varnishtop")
])
def test_varnish_binaries_exists(host, name):
    assert host.exists(name) is True


def test_varnish_is_enabled(host):
    assert host.service('varnish').is_running is True
    assert host.service('varnish').is_enabled is True
