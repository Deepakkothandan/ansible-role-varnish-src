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
def test_varnish_binaries_exists(Command, name):
    assert Command.exists(name) is True
