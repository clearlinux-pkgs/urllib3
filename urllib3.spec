#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : urllib3
Version  : 1.26.4
Release  : 106
URL      : https://files.pythonhosted.org/packages/cb/cf/871177f1fc795c6c10787bc0e1f27bb6cf7b81dbde399fd35860472cecbc/urllib3-1.26.4.tar.gz
Source0  : https://files.pythonhosted.org/packages/cb/cf/871177f1fc795c6c10787bc0e1f27bb6cf7b81dbde399fd35860472cecbc/urllib3-1.26.4.tar.gz
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
BuildRequires : nose
BuildRequires : pbr
BuildRequires : pip
BuildRequires : pyOpenSSL
BuildRequires : pyasn1
BuildRequires : pycparser
BuildRequires : setuptools
BuildRequires : six
BuildRequires : tornado

%description
urllib3 is a powerful, *user-friendly* HTTP client for Python. Much of the
        Python ecosystem already uses urllib3 and you should too.
        urllib3 brings many critical features that are missing from the Python

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
%setup -q -n urllib3-1.26.4
cd %{_builddir}/urllib3-1.26.4

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1615870406
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/urllib3
cp %{_builddir}/urllib3-1.26.4/LICENSE.txt %{buildroot}/usr/share/package-licenses/urllib3/fae7d86a68e1724238ed64674e4cd743a7dc6796
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
