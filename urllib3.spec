#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x70FE17F8A643E15B (lukasa@keybase.io)
#
Name     : urllib3
Version  : 1.22
Release  : 49
URL      : http://pypi.debian.net/urllib3/urllib3-1.22.tar.gz
Source0  : http://pypi.debian.net/urllib3/urllib3-1.22.tar.gz
Source99 : http://pypi.debian.net/urllib3/urllib3-1.22.tar.gz.asc
Summary  : HTTP library with thread-safe connection pooling, file post, and more.
Group    : Development/Tools
License  : MIT
Requires: urllib3-legacypython
Requires: urllib3-python3
Requires: urllib3-python
Requires: alabaster
Requires: certifi
Requires: cryptography
Requires: idna
Requires: ipaddress
Requires: pyOpenSSL
Requires: requests
BuildRequires : backports.ssl_match_hostname
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
BuildRequires : python3-dev
BuildRequires : setuptools
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


%package python
Summary: python components for the urllib3 package.
Group: Default
Requires: urllib3-legacypython
Requires: urllib3-python3

%description python
python components for the urllib3 package.


%package python3
Summary: python3 components for the urllib3 package.
Group: Default
Requires: python3-core

%description python3
python3 components for the urllib3 package.


%prep
%setup -q -n urllib3-1.22

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1507180260
python2 setup.py build -b py2
python3 setup.py build -b py3

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
PYTHONPATH=%{buildroot}/usr/lib/python3.6/site-packages python3 setup.py test || :
%install
export SOURCE_DATE_EPOCH=1507180260
rm -rf %{buildroot}
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

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
