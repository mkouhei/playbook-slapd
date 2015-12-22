===============================
 Playbook for OpenLDAP (slapd)
===============================

requirements
============

* Python 2.7
* virtualenv
* Ansible
* `ansible-ldap <https://bitbucket.org/psagers/ansible-ldap>`_

Prepare
=======

1. git clone
::

   $ git clone https://github.com/mkouhei/playbook-slapd
   $ cd playbook-slapd
   
2. install ansible.
::
      
   $ virtualenv .venv
   $ . .venv/bin/activate
   (venv)$ pip install ansible

3. Install dependency roles
::

   (venv)$ install -d library
   (venv)$ cd library
   (venv)$ ansible-galaxy install -p library -r requirements.yml --no-deps
   (venv)$ cd -


4. edit parameters

   * hosts
   * group_vars/all

5. run `ansible-playbook`.
::

   (venv)$ ansible-playbook -i hosts site.yml -K

