Frequently Asked Questions
--------------------------

Isn't this an overly elaborate solution for a simple problem?
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

Perhaps.  However, it Works For Me™.

You're obviously free to use what works for you, be that manually updating the
information in your editor or using a simpler approach such as shtool_'s
``version`` applet.

.. _shtool: http://www.gnu.org/software/shtool/shtool.html

Do you accept template contributions?
'''''''''''''''''''''''''''''''''''''

Yes, if they are somewhat general.  And, it is a great way to have me maintain
template compatibility for you in case something changes in a future version.

Either open an issue_ or push them to a fork on GitHub_.

.. _issue: https://github.com/JNRowe/versionah/issues
.. _GitHub: https://github.com/JNRowe/versionah/

I don't like your choice of template language
'''''''''''''''''''''''''''''''''''''''''''''

How do I add version data to my project's :file:`README`?
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''

The way I manage it, using :mod:`versionah`, is by having a custom template for
such a project.

The only requirement :mod:`versionah` has is that ``{{ magic }}`` is included in
the template, so you can use a project specific template that includes your full
:file:`README` data and generate the distributed :file:`README` from that.
Consider it the ``README.in`` approach you've probably used with GNU autotools
and it makes perfect sense.

Will you support other version formats?
'''''''''''''''''''''''''''''''''''''''
