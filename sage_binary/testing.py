r"""
Testing file for Sage binary
============================

This file is the main file of the package.

EXAMPLES::

sage: from sage.all import EllipticCurve
sage: EllipticCurve('11a1')
Elliptic Curve defined by y^2 + y = x^3 - x^2 - 10*x - 20 over Rational Field
"""

from sage.all import ZZ


def test():
    r"""
    Test that Sage is installed.

    EXAMPLES::

    sage: from sage.all import ZZ
    sage: ZZ(42)
    42
    """
    return ZZ(3)
