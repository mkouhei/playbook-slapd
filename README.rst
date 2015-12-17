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

   1. Install ansible-ldap::

        (venv)$ install -d library
        (venv)$ cd library
        (venv)$ hg clone https://bitbucket.org/psagers/ansible-ldap
        (venv)$ ln -s ansible-ldap/modules/ldap_* .
        (venv)$ cd -


   2. Install mkouhei.include_csv::

        (venv)$ ansible-galaxy install -p ./library mkouhei.include_csv


4. edit parameters

   * hosts
   * group_vars/all

5. run `ansible-playbook`.
   
   (venv)$ ansible-playbook -i hosts site.yml -K

