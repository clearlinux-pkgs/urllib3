#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : urllib3
Version  : 1.24.1
Release  : 68
URL      : https://files.pythonhosted.org/packages/b1/53/37d82ab391393565f2f831b8eedbffd57db5a718216f82f1a8b4d381a1c1/urllib3-1.24.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/b1/53/37d82ab391393565f2f831b8eedbffd57db5a718216f82f1a8b4d381a1c1/urllib3-1.24.1.tar.gz
Summary  : HTTP library with thread-safe connection pooling, file post, and more.
Group    : Development/Tools
License  : MIT
Requires: urllib3-license = %{version}-%{release}
Requires: urllib3-python = %{version}-%{release}
Requires: urllib3-python3 = %{version}-%{release}
Requires: alabaster
Requires: certifi
Requires: cryptography
Requires: idna
Requires: ipaddress
Requires: pyOpenSSL
Requires: requests
BuildRequires : backports.ssl_match_hostname
BuildRequires : buildreq-distutils23
BuildRequires : buildreq-distutils3
BuildRequires : certifi
BuildRequires : cffi
BuildRequires : cryptography
BuildRequires : mock
BuildRequires : ndg_httpsclient
BuildRequires : nose
BuildRequires : pbr
BuildRequires : pip
BuildRequires : pyOpenSSL
BuildRequires : pyasn1
BuildRequires : pycparser
BuildRequires : python-dev
BuildRequires : python-mock
BuildRequires : python3-dev
BuildRequires : setuptools
BuildRequires : setuptools-legacypython
BuildRequires : six
BuildRequires : tornado

%description
=======

%package legacypython
Summary: legacypython components for the urllib3 package.
Group: Default
Requires: python-core

%description legacypython
legacypython components for the urllib3 package.


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

%description python3
python3 components for the urllib3 package.


%prep
%setup -q -n urllib3-1.24.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1541196567
python2 setup.py build -b py2
python3 setup.py build -b py3

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
PYTHONPATH=%{buildroot}/usr/lib/python3.7/site-packages python3 setup.py test || :
%install
export SOURCE_DATE_EPOCH=1541196567
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/urllib3
cp LICENSE.txt %{buildroot}/usr/share/package-licenses/urllib3/LICENSE.txt
python2 -tt setup.py build -b py2 install --root=%{buildroot} --force
python3 -tt setup.py build -b py3 install --root=%{buildroot} --force
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files legacypython
%defattr(-,root,root,-)
/usr/lib/python2*/*

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/urllib3/LICENSE.txt

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
