Interfacing Fortran and Python
##############################

Documentation:
==============

A nice reference for Python for Fortran programmers:

http://fortran90.org/src/rosetta.html


Fortran best practices (including interfacing with Python)

http://fortran90.org/src/best-practices.html

http://fortran90.org/src/best-practices.html#interfacing-with-python

Interfacing methods:
====================

There a a handful of ways to interface Fortran and Python:

f2py:
-----

http://docs.scipy.org/doc/numpy/user/c-info.python-as-glue.html#f2py

Been around a long time, and maintained (at least a little) as part of the numpy project -- but more useful with older fortran -- not up to modern fortran standards. Perhaps the best option for interfacing with old-style fortran.


fwrap:
--------

http://fwrap.sourceforge.net/

Very promising, but its development has stalled out -- so probably not a good bet unless you want to actually work on it yourself.


Cython and iso_c_binding:
---------------------------

http://fortran90.org/src/best-practices.html#interfacing-with-python

By using the iso_binding calls to extend a C interace to your fortran code, you can call it with Cython. And Cython is very useful for calling C, optimizing Python, and adding "thick" wrappers to either C or fortran.


An Example:
============

The following is an example of using Cython to call fortran from Python.

The problem at hand is an automatic gain control function function, expressed in fortran as::

      subroutine AGC(nAGC,npts,amp,ampAGC)
      real fmax,amp(npts),absamp(npts),ampAGC(npts)
      integer i,j,npts,nAGC,nAGC2

      do i=1,npts
         ampAGC(i)=0.
         absamp(i)=abs(amp(i))
      enddo

      nAGC2=nAGC/2

      do i=nAGC2+1,npts-nAGC2
         fmax=0.
         do j=i-nAGC2,i+nAGC2
            if (absamp(j).gt.fmax) fmax=absamp(j)
         enddo
         ampAGC(i)=amp(i)/fmax
      enddo

      return

      end

f2py:
-----

f2py is a command line utility that comes with numpy. You can build a default simple wrapper with the f2py command::

    f2py -m agc_subroutine agc_subroutine.f


This will result in the file `agc_subroutinemodule.c`, which is hte c source for a python extension module. Or you can have f2py build the module itself all at once::

    f2py -m -c agc_subroutine agc_subroutine.f

This will generate a compiled python extension named agc_subroutine that can be imported in python as::

    import agc_subroutine

f2p automatically generates a docstring for the function it created::

	agc - Function signature:
	  agc(nagc,amp,ampagc,[npts])
	Required arguments:
	  nagc : input int
	  amp : input rank-1 array('f') with bounds (npts)
	  ampagc : input rank-1 array('f') with bounds (npts)
	Optional arguments:
	  npts := len(amp) input int

So it can be called like so::

    agc_subroutine.agc(5, signal, filtered)

where `signal` and `filtered` are 1-d arrays of float32 values, both of the same length.

Giving f2py extra information:
..............................

f2py can build an interface to a fortran subroutine, but it can't do it all that well without some extra information. For instnce, note from the docstring that the argument `ampagc` is listed as an input argument, when it is really intended to be used for output.

To get f2py to generate an interface file use the -h option::

  f2py -h agc_subroutine.pyf -m agc_subroutine agc_subroutine.f

This command leaves the file agc_subroutine.pyf in the current directory, which contains::

  !    -*- f90 -*-
  ! Note: the context of this file is case sensitive.

   python module agc_subroutine ! in
      interface  ! in :agc_subroutine
         subroutine agc(nagc,npts,amp,ampagc) ! in :agc_subroutine:agc_subroutine.f
             integer :: nagc
             integer, optional,check(len(amp)>=npts),depend(amp) ::  npts=len(amp)
             real dimension(npts) :: amp
             real dimension(npts),depend(npts) :: ampagc
         end subroutine agc
     end interface
  end python module agc_subroutine

  ! This file was auto-generated with f2py (version:2).
  ! See http://cens.ioc.ee/projects/f2py2e/

You can then add to the interface file by placing intent directives and checking code. This will clean up the interface quite a bit so that the Python module method is both easier to use and more robust. This is the edited version::

  !    -*- f90 -*-
  ! Note: the context of this file is case sensitive.

   python module agc_subroutine ! in
      interface  ! in :agc_subroutine
         subroutine agc(nagc,npts,amp,ampagc) ! in :agc_subroutine:agc_subroutine.f
             integer :: nagc
             integer, optional,intent(hide),check(len(amp)>=npts),depend(amp) ::  npts=len(amp)
             real dimension(npts) :: amp
             real dimension(npts),intent(out),depend(npts) :: ampagc
         end subroutine agc
     end interface
  end python module agc_subroutine

  ! This file was auto-generated with f2py (version:2).
  ! Then hand edited for a better interface.
  ! See http://cens.ioc.ee/projects/f2py2e/


The intent directive, intent(out) is used to tell f2py that ampagc is an output variable and should be created by the interface before being passed to the underlying code. The intent(hide) directive tells f2py to not allow the user to specify the variable, npts, but instead to get it from the size of amp.

Inserting directives in the Fortran source
...........................................

Directives can alternatively be inserted in the fortran source as special comments::

	c
	c  Subrooutine to compute an automatic gain control filter.
	c
	c
	      subroutine AGC(nAGC,npts,amp,ampAGC)

	CF2PY INTENT(OUT) :: ampAGC
	CF2PY INTENT(HIDE) :: npts

	      real fmax,amp(npts),absamp(npts),ampAGC(npts)
	      integer i,j,npts,nAGC,nAGC2

This is probably an easier and clearer option if you maintaining the fortran source yourself.

Either way, you get a nicer, more pythonic and safer interface::

	agc - Function signature:
	  ampagc = agc(nagc,amp)
	Required arguments:
	  nagc : input int
	  amp : input rank-1 array('f') with bounds (npts)
	Return objects:
	  ampagc : rank-1 array('f') with bounds (npts)

called like so::

  filtered = agc_subroutine.agc(10, signal)

You can see that you don't need (and can't) specify the length of the array, and the output array is automatically created by the wrappers, and memory-managed by python.



















