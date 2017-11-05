Background
==========

I maintain a many projects, both my toy stuff on GitHub_ and more serious
things at the office.  While skipping around in my editor to increase a version
number I came to the blindingly obvious realisation that I shouldn’t be doing
this manually.

Bumping or querying version numbers should be a zero thought process.
I shouldn’t need to remember the :abbr:`regex (Regular Expression)` needed to
make my editor jump to the version identifier in any given file.  I shouldn’t
need to resort to various :kbd:`C-a` and :kbd:`C-x` contortions in vim_ or
formulating complicated lisp functions with ``number-to-string`` and
``string-to-number`` in emacs_.

Now |progref| is born, and I should be able to realise those dreams!

Version numbers
===============

This — for some — is a very complicated topic, but not for me.  Version numbers
are made of three components; major, minor and micro.  All three components are
natural numbers; no exceptions.

If you find version numbers like 0.6c11 acceptable then |progref| is not for
you.

.. note::

   If you like version numbers with two or four integer components then
   |progref| can be for you too.  Support was added in 0.6.0, but that doesn’t
   mean you have to use it!

PEP 386
~~~~~~~

The version numbering scheme supported by |progref| is a very small subset of
``LooseVersion`` defined in :pep:`386`.  It isn’t compliant with
``StrictVersion`` because of the 4 component support, but support for packages
in the wild is much more important to me.

Versioning policy
-----------------

Beyond the simple rule above you’re free to do as you wish, but consider this a
plea for a sane versioning policy.

.. blockdiag::

    diagram {
        group A {
            label = "Bug-fix releases";
            "0.1.0" -> "0.1.1";
            "0.1.1" -> "0.1.n" [style=dotted];
        }
        group B {
            label = "Bug-fix releases";
            "0.2.0" -> "0.2.n" [style=dotted];
            "0.2.0" [label = "0.2.0\nNew features"]
        }
        group C {
            label = "Bug-fix releases";
            "1.0.0" [label = "1.0.0\nFirst stable", color = "green"];
            "1.0.0" -> "1.0.n" [style=dotted];
        }
        "0.1.n" -> "0.2.0" [folded];
        "0.2.n" -> "1.0.0" [folded];
        "1.0.n" -> "2.0.0" [folded];
        "2.0.0" [label = "2.0.0\nIncompatible"];
    }

Major component
'''''''''''''''

Increment the major component for all backwards incompatible changes.

Minor component
'''''''''''''''

Increment the minor component for all backward compatible additions.

Micro component
'''''''''''''''

Increment the micro component for all bug-fix releases.

.. _GitHub: https://github.com/JNRowe/
.. _vim: http://www.vim.org/
.. _emacs: http://www.gnu.org/software/emacs/
