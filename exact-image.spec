Summary:	A fast, modern and generic image processing library
Name:		exact-image
Version:	0.9.1
Release:	0
Group:		Graphics
License:	GPLv2 and BSD
Url:		https://exactcode.com/opensource/exactimage/
Source0:	https://dl.exactcode.de/oss/exact-image/%{name}-%{version}.tar.bz2
Patch0:		%{name}-0.9.1-configure.patch
Patch1:		%{name}-0.9.1-make.patch
Patch2:		%{name}-0.9.1-png.patch
Patch3:		%{name}-0.9.1-ungif.patch
Patch4:		%{name}-0.9.1-gfx.patch
Patch5:		%{name}-0.9.1-swig.patch
Patch6:		%{name}-0.9.1-bardecode.patch
Patch7:		%{name}-0.9.1-python3.patch
Patch8:		%{name}-0.9.1-lua.patch
Patch9:		%{name}-0.9.1-perl.patch
Patch10:	%{name}-0.9.1-php.patch
Patch11:	%{name}-0.9.1-ruby.patch
Patch100:	%{name}-0.9.1-c++11.patch

BuildRequires:	swig
BuildRequires:	xsltproc
BuildRequires:	giflib-devel
BuildRequires:	ungif-devel
BuildRequires:	jpeg-devel
BuildRequires:	perl-devel
BuildRequires:	php-devel
BuildRequires:	pkgconfig(expat)
BuildRequires:	pkgconfig(evas)
BuildRequires:	pkgconfig(freetype2)
BuildRequires:	pkgconfig(jasper)
BuildRequires:	pkgconfig(lcms)
BuildRequires:	pkgconfig(libagg)
BuildRequires:	pkgconfig(libpng)
BuildRequires:	pkgconfig(libtiff-4)
BuildRequires:	pkgconfig(libxml-2.0)
BuildRequires:	pkgconfig(lua)
BuildRequires:	pkgconfig(OpenEXR)
BuildRequires:	pkgconfig(python3)
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(xrender)


%description
# from the homepage
ExactImage is a fast, modern and generic image processing library.

It is intended to become a modern, generic (template) based C++ library,
as time permits. - Hopefully a viable alternative to ImageMagick.

%files
%{_bindir}/bardecode
%{_bindir}/e2mtiff
%{_bindir}/econvert
%{_bindir}/edentify
%{_bindir}/edisplay
%{_bindir}/empty-page
%{_bindir}/hocr2pdf
%{_bindir}/optimize2bw
%{py3_platsitedir}/ExactImage.py
%{py3_platsitedir}/_ExactImage.so
%{perl_vendorarch}/ExactImage.pm
%{perl_vendorarch}/ExactImage.so
#FIXME: is there a macro for standard arch lib path for lua?
/usr/lib/lua/*/ExactImage.so
#%{_libdir}/lua/*/ExactImage.so
%doc README
%doc TODO
%doc LICENSE

#-----------------------------------------------------------------

%prep
%setup -q

# Apply all patches
%patch0 -p1 -b .orig
%patch1 -p1 -b .orig
%patch2 -p1 -b .orig
%patch3 -p1 -b .orig
%patch4 -p1 -b .orig
%patch5 -p1 -b .orig
%patch6 -p1 -b .orig
%patch7 -p1 -b .python
%patch8 -p1 -b .lua
%patch9 -p1 -b .perl
%patch10 -p1 -b .php
%patch11 -p1 -b .ruby

%patch100 -p1 -b .orig

%build
%global optflags %{optflags} -Qunused-arguments
export CFLAGS="$(optflags) -Wall -O2"
export CXXFLAGS="${optflags} -Wall -O2 -Wno-sign-compare -std=c++11"

# verbose
#sed -i -e "s|Q = @|#Q = @|" build/bottom.make

# FIXME: swig 3.0.19 in not compatible with php7
%configure --without-php 
%make

%install
%global optflags %{optflags} -Qunused-arguments
export CFLAGS="$(optflags) -Wall -O2"
export CXXFLAGS="${optflags} -Wall -O2 -Wno-sign-compare -std=c++11"
%setup_compile_flags
%makeinstall_std

