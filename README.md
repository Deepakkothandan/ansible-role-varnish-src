Role Name
=========

The role is used to install varnish from source.

Requirements
------------

Inorder to execute tests, the role required molecule, testinfra and docker which can be installed using pip. 
Note: tests were written using python2.7

Role Variables
--------------
varnish_version: 4.1.5
varnish_download_location: /opt/varnish
varnish_modules_version: master