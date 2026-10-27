Start Here
==========

This documentation is organized around common tasks and the major Carfinity
systems:

* **Administration and authentication** covers account setup, permissions,
  group routing, and administrator workflows.
* **Vehicle care and maintenance** covers AutoCare, vehicle dashboards,
  maintenance records, and related user flows.
* **Inspections and assessments** describes inspection checklists, scoring,
  assessment workflows, and report generation.
* **Insurance and quotes** covers claims, risk assessment, repair costing,
  settlement, and parts-based quotes.
* **Technical reference** provides database, error-handling, and health
  monitoring material.
* **Project history** preserves implementation summaries and design analyses.

The source documents are historical Markdown files. Some describe planned or
past implementations rather than current behavior. Check the application
before using those documents as operational instructions.

.. note::

   The original Markdown documents are stored in ``CarfinityDocs/`` and remain
   the source of truth. A build script generates the Sphinx pages from them and
   removes horizontal rules that would otherwise break section parsing.

Build and deployment
--------------------

Install the dependencies and build the site locally from the ``Docs/``
directory::

   python -m pip install -r requirements.txt
   python scripts/create_guide_pages.py
   python -m sphinx -b html source build/html

Read the Docs installs the same dependencies and generates the guide pages
automatically before building the HTML site.
