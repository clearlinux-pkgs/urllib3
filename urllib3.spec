#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x70FE17F8A643E15B (lukasa@keybase.io)
#
Name     : urllib3
Version  : 1.21
Release  : 38
URL      : http://pypi.debian.net/urllib3/urllib3-1.21.tar.gz
Source0  : http://pypi.debian.net/urllib3/urllib3-1.21.tar.gz
Source99 : http://pypi.debian.net/urllib3/urllib3-1.21.tar.gz.asc
Summary  : HTTP library with thread-safe connection pooling, file post, and more.
Group    : Development/Tools
License  : MIT
Requires: urllib3-python
Requires: Sphinx
Requires: alabaster
Requires: certifi
Requires: cryptography
Requires: idna
Requires: ipaddress
Requires: pyOpenSSL
BuildRequires : backports.ssl_match_hostname
BuildRequires : certifi-python
BuildRequires : cffi-python
BuildRequires : cryptography-python
BuildRequires : mock-python
BuildRequires : ndg_httpsclient-python
BuildRequires : nose-python
BuildRequires : pbr
BuildRequires : pip
BuildRequires : pyOpenSSL-python
BuildRequires : pyasn1-python
BuildRequires : pycparser-python
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools
BuildRequires : six-python
BuildRequires : tornado-python

%description
urllib3
=======
.. image:: https://travis-ci.org/shazow/urllib3.svg?branch=master
:alt: Build status on Travis
:target: https://travis-ci.org/shazow/urllib3

%package python
Summary: python components for the urllib3 package.
Group: Default

%description python
python components for the urllib3 package.


%prep
%setup -q -n urllib3-1.21

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1493208149
python2 setup.py build -b py2

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
PYTHONPATH=%{buildroot}/usr/lib/python3.6/site-packages python3 setup.py test || :
%install
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot}

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)
/usr/lib/python2*/*
