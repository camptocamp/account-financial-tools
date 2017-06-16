.. :changelog:

.. Template:

.. 0.0.1 (2016-05-09)
.. ++++++++++++++++++

.. **Features and Improvements**

.. **Bugfixes**

.. **Build**

.. **Documentation**

Release History
---------------


Latest (unreleased)
+++++++++++++++++++

**Features and Improvements**

**Bugfixes**

**Build**

* Sync from odoo-template
* Load entrypoint to remove enterprise key on envs != prod
* Load entrypoint to be able to use a database containing S3 attachments

**Documentation**


10.0.18 (2017-06-16)
++++++++++++++++++++

**Bugfixes**

* fix issues with the second analytic axis


10.0.17 (2017-06-15)
++++++++++++++++++++

**Features and Improvements**

* Add new submodule OCA/account-analytic & Install analytic_tag_dimension BSRTL-211
* Install dimensions and tags data for account.analytic BSRTL-211
* Only admin can CUD others can R for account.analytic dimensions/tags BSRTL-211
* Add analytic tag on hr.department,hr.employee BSRTL-212
* Make analytic tag required on soline, poline, invline BSRTL-212
* Use employee's tag when creating analytic.line from expense BSRTL-212
* Force tag of employee into timesheet BSRTL-212


10.0.16 (2017-06-08)
++++++++++++++++++++

**Features and Improvements**

* Add mail.channels for process in companies
* Add specific_subscription for sale.order required fields in subscriptions
* Add sale_project_fixed_price_task_completed_invoicing BSRTL-208

**Bugfixes**

* Project name for inter company sales's project

**Build**

* upgrade Docker base image to camptocam/odoo-project:10.0-2.2.0
* Update odoo-cloud-platform to have Redis Sentinel support

**Documentation**


10.0.15 (2017-05-18)
++++++++++++++++++++

**Features and Improvements**

* SO change validation button visibility/process given product_category
* SO & crm.lead holding_amount_currency in tree view. Can be used as measure
* Add module 'sale_company_currency'
* Add and install specific_expense

**Bugfixes**

**Build**

**Documentation**


10.0.14 (2017-05-09)
++++++++++++++++++++

**Bugfixes**

* fix bug preventing saving a purchase order
* fix problem in intercompany set up

**Build**

* update Docker image to camptocamp/odoo-project:10.0-2.1.1


10.0.13 (2017-05-04)
++++++++++++++++++++

**Bugfixes**

* fix view of crm.lead
* improve view of customer license
* add website_contract to get subscriptions working

10.0.12 (2017-04-26)
++++++++++++++++++++

**Features and Improvements**

* Install sale_contract
* Remove signatures on leads
* update transitions checks in crm
* Add NDA Leads in customer's form
* Email temaplate & Button for 'final_quote'
* Add Customer's Licenses models & views
* Set intercompany rules
* Update filters & rules for NDA & stage3

**Bugfixes**

* String in button to step to 'Final Quote'
* Update label 'Sales Conditions'

**Build**

**Documentation**


10.0.11 (2017-04-12)
++++++++++++++++++++

**Features and Improvements**

* Update Lead, change place of fields and add buttons
* In SO: rename/move fields and tabs
* New permissions on project and tasks for salesman
* An employee can see only his contract
* Tasks are now named after project name and not the sales order name
* Ensure that the partner of a sale.order has a proper "reference" field

**Bugfixes**

* Set 'final_quote' after 'sent' & update checks & print to it

**Build**

* Updated odoo/src & removed 'update base'

**Documentation**


10.0.10 (2017-03-30)
++++++++++++++++++++

**Features and Improvements**

* Add link inbetween 'BOM' and 'project.task / project.project'
* Add fields in views for 'BOM' and 'project.task'
* Add smartbutton on 'task' view
* install instrastat modules, product harmonized system
* Update message subtypes for RFQ so that the author receives some additional
  notification

**Bugfixes**

* Fix base.action.rules for crm.lead transition not only for admin

**Build**

**Documentation**


10.0.9 (2017-03-23)
+++++++++++++++++++

**Features and Improvements**

**Bugfixes**

* Correct sale validation group names
* fix missing ACLs for hr.employee.status
* fix sale order validation workflow

**Build**

**Documentation**


10.0.8 (2017-03-17)
+++++++++++++++++++

**Features and Improvements**

* Add a second user on CRM leads
* Ghosts products and indicative sales quotes: have placeholder products on
  sale orders, and have an intermediate state on sales quotations.
* install sale_order_revision


10.0.7 (2017-03-10)
+++++++++++++++++++

**Features and Improvements**

* Add new fields in 'hr.employee' & 'hr.contracts'
* Update submodule hr
* Install 'hr_employee_phone_extension'
* Install hr_emergency_contact
* Install hr_contract_reference
* Install hr_employee_birth_name
* Install hr_experience
* Install hr_seniority
* Activate PO Double validation
* Add PO double validation view filters & security
* Add Check analytic account in PO validation
* Activate lots and serial number
* Change sequence for 'stock.production.lot'
* Add SN in PO report
* Install dropshipping
* Install FEDEX delivery
* Install sales layout and product set

**Bugfixes**

**Build**

**Documentation**


10.0.6 (2017-03-02)
+++++++++++++++++++

**Features and Improvements**

* Activate PO Double validation
* Add PO double validation view filters & security
* Add Check analytic account in PO validation
* Activate lots and serial number


10.0.5 (2017-02-21)
+++++++++++++++++++

**Features and Improvements**

* users with correct groups (taken from integration instance)
* install ``hr_maintenance`` and ``maintenance`` modules

**Bugfixes**

**Build**

**Documentation**


10.0.4 (2017-02-16)
+++++++++++++++++++

**Features and Improvements**

* Add product options on SO
* Configure margin on SO
* Install ``sale_order_revision``
* Install modules to manage margins on sale
* Install COA for Japan (Odoo fixed)
* Configure Base action rules, filters and server actions to be able to block
    or trigger actions when changing stage
* Manage option lines on sale orders


10.0.3 (2017-01-24)
+++++++++++++++++++

**Features and Improvements**

* import products


10.0.1 (2017-01-11)
+++++++++++++++++++

*Features and Improvements*

* initial setup
