# Ansible Role: Varnish from Source

The role is used to install [Varnish HTTP Cache](https://varnish-cache.org/) from source on RedHat/CentOS or Debian/Ubuntu Linux. Optionally, [varnish modules](https://github.com/varnish/varnish-modules) can also be installed.

## Note
The role is used only to install varnish from source, and inherits configuration templates from the role [Varnish Role from geerlingguy](https://github.com/geerlingguy/ansible-role-varnish). If installing varnish using package managers, it is recommended to use the above mentioned role.

## Test Requirements
Inorder to execute tests, the role requires molecule, testinfra and docker-py which can be installed using pip.
Docker is also required to be installed on the machine executing tests.
Note: tests were written using python2.7

## Role Variables
    varnish_version: 4.1.5
The version of varnish to install from source `https://repo.varnish-cache.org/source/`. Check the link for available varnish versions

    varnish_download_location: /opt/varnish
The location to download varnish sources

    varnish_modules_version: master
The version of [varnish modules](https://github.com/varnish/varnish-modules)  to install (specify git tags)

    varnish_default_vcl_template_path: default.vcl.j2
The path to varnish default.vcl template


    varnish_listen_port: "80"

The port on which Varnish will listen (typically port 80).

    varnish_default_backend_host: "127.0.0.1"
    varnish_default_backend_port: "8080"

Some settings for the default "default.vcl" template that will be copied to the `varnish_config_path` folder. The default backend host/port could be Apache or Nginx (or some other HTTP server) running on the same host or some other host (in which case, you might use port 80 instead).

    varnish_limit_nofile: 131072

The `nofiles` PAM limit Varnish will attempt to set for open files. The normal default is ~1024 which is much too low for Varnish usage.

    varnish_secret: "14bac2e6-1e34-4770-8078-974373b76c90"

The secret/key to be used for connecting to Varnish's admin backend (for purge requests, etc.).

    varnish_admin_listen_host: "127.0.0.1"
    varnish_admin_listen_port: "6082"

The host and port through which Varnish will accept admin requests (like purge and status requests).

    varnish_storage: "file,/var/lib/varnish/varnish_storage.bin,256M"

How Varnish stores cache entries (this is passed in as the argument for `-s`). If you want to use in-memory storage, change to something like `malloc,256M`. Please read Varnish's [Getting Started guide](http://book.varnish-software.com/4.0/chapters/Getting_Started.html) for more information.

    varnish_pidfile: /run/varnishd.pid

Varnish PID file path. Set to an empty string if you don't want to use a PID file.

    varnish_enabled_services:
      - varnish

Services that will be started at boot and should be running after this role is complete. You might need to add additional services if required, e.g. `varnishncsa` and `varnishlog`. If set to an empty array, no services will be enabled at startup.

    varnish_backends:
      apache:
        host: 10.0.2.2
        port: 80
      nodejs:
        host: 10.0.2.3
        port: 80
    
    varnish_vhosts:
      example.com:
        backend: apache
      nodejs.example.com:
        backend: nodejs

You can configure multiple backends (and direct traffic from multiple virtual hosts to different backends) using the `varnish_backends` and `varnish_vhosts` variables. If you only use one backend (defined via `varnish_default_backend_host` and `varnish_default_backend_port`), then you do not need to define these variables. Do not add a `www` to the `vhosts` keys; it is added automatically by the `default.vcl.j2` VCL template.

## Dependencies

None.

## Example Playbook

    - hosts: webservers
      vars_files:
        - vars/main.yml
      roles:
        - ansible-role-varnish-src

## License

MIT / BSD

