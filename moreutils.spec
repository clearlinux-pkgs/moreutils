#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : moreutils
Version  : 0.62
Release  : 1
URL      : http://http.debian.net/debian/pool/main/m/moreutils/moreutils_0.62.orig.tar.xz
Source0  : http://http.debian.net/debian/pool/main/m/moreutils/moreutils_0.62.orig.tar.xz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0
Requires: moreutils-bin
Requires: moreutils-license
BuildRequires : docbook-xml
Patch1: noman.patch

%description
This is a collection of the unix tools that nobody thought to write
long ago, when unix was young. Currently it consists of these tools:

%package bin
Summary: bin components for the moreutils package.
Group: Binaries
Requires: moreutils-license

%description bin
bin components for the moreutils package.


%package license
Summary: license components for the moreutils package.
Group: Default

%description license
license components for the moreutils package.


%prep
%setup -q -n moreutils-0.62
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1528920883
make  %{?_smp_mflags}

%install
export SOURCE_DATE_EPOCH=1528920883
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/doc/moreutils
cp COPYING %{buildroot}/usr/share/doc/moreutils/COPYING
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/chronic
/usr/bin/combine
/usr/bin/errno
/usr/bin/ifdata
/usr/bin/ifne
/usr/bin/isutf8
/usr/bin/lckdo
/usr/bin/mispipe
/usr/bin/parallel
/usr/bin/pee
/usr/bin/sponge
/usr/bin/ts
/usr/bin/vidir
/usr/bin/vipe
/usr/bin/zrun

%files license
%defattr(-,root,root,-)
/usr/share/doc/moreutils/COPYING
