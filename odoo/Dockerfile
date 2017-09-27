FROM camptocamp/odoo-project:10.0-2.4.0
MAINTAINER Camptocamp

COPY ./requirements.txt /opt/odoo

# Install additional debian and python packages if needed
RUN set -x; \
        apt-get update \
        && apt-get install -y --no-install-recommends \
        parallel \
        python-dev build-essential \
        && cd /opt/odoo \
        && find . -maxdepth 1 -name "*requirements.txt" ! -name src_requirements.txt ! -name base_requirements.txt -exec pip install -r {} \; \
        && apt-get remove -y build-essential python-dev \
        && apt-get clean \
        && rm -rf /var/lib/apt/lists/*

COPY ./before-migrate-entrypoint.d/* odoo/before-migrate-entrypoint.d/
COPY ./start-entrypoint.d/* odoo/start-entrypoint.d/
RUN chmod +x odoo/before-migrate-entrypoint.d/* \
    && chmod +x odoo/start-entrypoint.d/*

ENV ADDONS_PATH="/opt/odoo/external-src/enterprise, \
  /opt/odoo/src/addons, \
  /opt/odoo/external-src/server-tools, \
  /opt/odoo/external-src/odoo-cloud-platform, \
  /opt/odoo/external-src/hr, \
  /opt/odoo/external-src/sale-workflow, \
  /opt/odoo/external-src/hr-timesheet, \
  /opt/odoo/external-src/intrastat, \
  /opt/odoo/external-src/project, \
  /opt/odoo/external-src/account-analytic, \
  /opt/odoo/external-src/web, \
  /opt/odoo/external-src/odoo-prototype, \
  /opt/odoo/external-src/odoo-usability, \
  /opt/odoo/external-src/account-financial-tools, \
  /opt/odoo/local-src," \
  LIMIT_TIME_CPU=86400 \
  LIMIT_TIME_REAL=86400 \
  LIMIT_MEMORY_SOFT=1342177280 \
  LIMIT_MEMORY_HARD=1610612736
