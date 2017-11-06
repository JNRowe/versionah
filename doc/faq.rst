Frequently Asked Questions
--------------------------

.. contents::
   :local:

Isn’t this an overly elaborate solution for a simple problem?
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

Perhaps.  However, it Works For Me™.

You’re obviously free to use what works for you, be that manually updating the
information in your editor or using a simpler approach such as shtool_’s
``version`` applet.

.. _shtool: http://www.gnu.org/software/shtool/shtool.html

I give ``perl`` scripts the suffix ``.perl``, can I make type guessing work?
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

Yes.  The simplest way is to just create a symlink from |progref|’s
:file:`pl.jinja`` to
``${XDG_DATA_HOME:~/.local/share}/versionah/templates/perl.jinja``.

Do you accept template contributions?
'''''''''''''''''''''''''''''''''''''

Yes, if they are somewhat general.

Template contributions are also a great way to have me maintain template
compatibility for you, and protects you from breaking changes in a future
version.

Either open an issue_ or push them to a fork on GitHub_.

.. _issue: https://github.com/JNRowe/versionah/issues
.. _GitHub: https://github.com/JNRowe/versionah/

I don’t like your choice of template language
'''''''''''''''''''''''''''''''''''''''''''''

[It isn’t really a question, but it has come up a couple of times.]

The use of Jinja_ should only be an issue if you wish to :doc:`author your own
templates <templates>`, if you’re using the built-in templates you shouldn’t
notice Jinja_ at all.  That said…

The use of Jinja_ seems to be an unassailable barrier to entry for a couple of
people, but it isn’t going to change.  For the same — invariably pointless and
religious — reasons people prefer other templating engines *I* prefer Jinja_.

.. _Jinja: http://jinja.pocoo.org/

How do I add version data to my project’s :file:`README`?
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''

The way I manage it, using |progref|, is by having a :ref:`custom template
<template_naming-label>` for such a project.

The only templating requirement |progref| has is that ``{{ magic }}`` is
included *somewhere*.  This means you can use a custom template that includes
your full :file:`README` data, and generate the distributed :file:`README` from
that.  Consider it the :file:`README.in` approach you’ve probably used with GNU
autotools, and it makes perfect sense.

Will you support other version formats?
'''''''''''''''''''''''''''''''''''''''

If the patches you submit for other version formats aren’t too invasive then
they’ll probably be accepted.  If you’re going to propose such a patch open an
issue_ or drop me a mail_ first, so it can be discussed.

If the format you’re going to implement looks like the ``LooseVersion`` format
defined in :pep:`386` with support for random words or odd characters then the
answer is likely to be a resounding “no”.

Direct support for the full ``StrictVersion`` format defined in that PEP will,
however, likely be accepted with open arms.

.. _mail: jnrowe@gmail.com
