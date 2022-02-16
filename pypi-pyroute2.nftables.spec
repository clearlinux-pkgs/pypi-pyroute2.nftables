#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-pyroute2.nftables
Version  : 0.6.6
Release  : 12
URL      : https://files.pythonhosted.org/packages/65/57/74800f222762259e5bdb33f838347bcb00f01b42f61fba16b41a901d4f95/pyroute2.nftables-0.6.6.tar.gz
Source0  : https://files.pythonhosted.org/packages/65/57/74800f222762259e5bdb33f838347bcb00f01b42f61fba16b41a901d4f95/pyroute2.nftables-0.6.6.tar.gz
Summary  : Python Netlink library: nftables
Group    : Development/Tools
License  : Apache-2.0 GPL-2.0 GPL-2.0+
Requires: pypi-pyroute2.nftables-license = %{version}-%{release}
Requires: pypi-pyroute2.nftables-python = %{version}-%{release}
Requires: pypi-pyroute2.nftables-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(pyroute2.core)

%description
pyroute2.nftables
=================
PyRoute2 is a pure Python **netlink** library.

%package license
Summary: license components for the pypi-pyroute2.nftables package.
Group: Default

%description license
license components for the pypi-pyroute2.nftables package.


%package python
Summary: python components for the pypi-pyroute2.nftables package.
Group: Default
Requires: pypi-pyroute2.nftables-python3 = %{version}-%{release}

%description python
python components for the pypi-pyroute2.nftables package.


%package python3
Summary: python3 components for the pypi-pyroute2.nftables package.
Group: Default
Requires: python3-core
Provides: pypi(pyroute2.nftables)
Requires: pypi(pyroute2.core)

%description python3
python3 components for the pypi-pyroute2.nftables package.


%prep
%setup -q -n pyroute2.nftables-0.6.6
cd %{_builddir}/pyroute2.nftables-0.6.6

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1645044132
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-pyroute2.nftables
cp %{_builddir}/pyroute2.nftables-0.6.6/LICENSE.Apache.v2 %{buildroot}/usr/share/package-licenses/pypi-pyroute2.nftables/cd9bad64b174708395f795bb92f7b4be7d996e8f
cp %{_builddir}/pyroute2.nftables-0.6.6/LICENSE.GPL.v2 %{buildroot}/usr/share/package-licenses/pypi-pyroute2.nftables/4cc77b90af91e615a64ae04893fdffa7939db84c
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-pyroute2.nftables/4cc77b90af91e615a64ae04893fdffa7939db84c
/usr/share/package-licenses/pypi-pyroute2.nftables/cd9bad64b174708395f795bb92f7b4be7d996e8f

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
