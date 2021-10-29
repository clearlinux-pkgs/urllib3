#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : urllib3
Version  : 1.26.7
Release  : 116
URL      : https://files.pythonhosted.org/packages/80/be/3ee43b6c5757cabea19e75b8f46eaf05a2f5144107d7db48c7cf3a864f73/urllib3-1.26.7.tar.gz
Source0  : https://files.pythonhosted.org/packages/80/be/3ee43b6c5757cabea19e75b8f46eaf05a2f5144107d7db48c7cf3a864f73/urllib3-1.26.7.tar.gz
Summary  : HTTP library with thread-safe connection pooling, file post, and more.
Group    : Development/Tools
License  : MIT
Requires: urllib3-license = %{version}-%{release}
Requires: urllib3-python = %{version}-%{release}
Requires: urllib3-python3 = %{version}-%{release}
Requires: PySocks
Requires: brotlipy
Requires: certifi
Requires: cryptography
Requires: idna
Requires: pyOpenSSL
BuildRequires : PySocks
BuildRequires : backports.ssl_match_hostname
BuildRequires : brotlipy
BuildRequires : buildreq-distutils3
BuildRequires : certifi
BuildRequires : cffi
BuildRequires : cryptography
BuildRequires : idna
BuildRequires : mock
BuildRequires : ndg_httpsclient
BuildRequires : pbr
BuildRequires : pip
BuildRequires : pyOpenSSL
BuildRequires : pyasn1
BuildRequires : pycparser
BuildRequires : setuptools
BuildRequires : six
BuildRequires : tornado

%description
.. raw:: html
<p align="center">
<a href="https://github.com/urllib3/urllib3">
<img src="./docs/images/banner.svg" width="60%" alt="urllib3" />
</a>
</p>
<p align="center">
<a href="https://pypi.org/project/urllib3"><img alt="PyPI Version" src="https://img.shields.io/pypi/v/urllib3.svg?maxAge=86400" /></a>
<a href="https://pypi.org/project/urllib3"><img alt="Python Versions" src="https://img.shields.io/pypi/pyversions/urllib3.svg?maxAge=86400" /></a>
<a href="https://discord.gg/CHEgCZN"><img alt="Join our Discord" src="https://img.shields.io/discord/756342717725933608?color=%237289da&label=discord" /></a>
<a href="https://codecov.io/gh/urllib3/urllib3"><img alt="Coverage Status" src="https://img.shields.io/codecov/c/github/urllib3/urllib3.svg" /></a>
<a href="https://github.com/urllib3/urllib3/actions?query=workflow%3ACI"><img alt="Build Status on GitHub" src="https://github.com/urllib3/urllib3/workflows/CI/badge.svg" /></a>
<a href="https://travis-ci.org/urllib3/urllib3"><img alt="Build Status on Travis" src="https://travis-ci.org/urllib3/urllib3.svg?branch=master" /></a>
<a href="https://urllib3.readthedocs.io"><img alt="Documentation Status" src="https://readthedocs.org/projects/urllib3/badge/?version=latest" /></a>
</p>

%package license
Summary: license components for the urllib3 package.
Group: Default

%description license
license components for the urllib3 package.


%package python
Summary: python components for the urllib3 package.
Group: Default
Requires: urllib3-python3 = %{version}-%{release}

%description python
python components for the urllib3 package.


%package python3
Summary: python3 components for the urllib3 package.
Group: Default
Requires: python3-core
Provides: pypi(urllib3)

%description python3
python3 components for the urllib3 package.


%prep
%setup -q -n urllib3-1.26.7
cd %{_builddir}/urllib3-1.26.7

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1632343902
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
mkdir -p %{buildroot}/usr/share/package-licenses/urllib3
cp %{_builddir}/urllib3-1.26.7/LICENSE.txt %{buildroot}/usr/share/package-licenses/urllib3/fae7d86a68e1724238ed64674e4cd743a7dc6796
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/urllib3/fae7d86a68e1724238ed64674e4cd743a7dc6796

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
