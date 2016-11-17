#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : urllib3
Version  : 1.19.1
Release  : 31
URL      : http://pypi.debian.net/urllib3/urllib3-1.19.1.tar.gz
Source0  : http://pypi.debian.net/urllib3/urllib3-1.19.1.tar.gz
Summary  : HTTP library with thread-safe connection pooling, file post, and more.
Group    : Development/Tools
License  : MIT
Requires: urllib3-python
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
BuildRequires : python-mock-python
BuildRequires : python3-dev
BuildRequires : setuptools
BuildRequires : six-python
BuildRequires : tornado-python

%description
urllib3
=======
.. image:: https://travis-ci.org/shazow/urllib3.png?branch=master
:alt: Build status on Travis
:target: https://travis-ci.org/shazow/urllib3

%package python
Summary: python components for the urllib3 package.
Group: Default
Requires: certifi-python
Requires: pyOpenSSL-python

%description python
python components for the urllib3 package.


%prep
%setup -q -n urllib3-1.19.1

%build
export LANG=C
python2 setup.py build -b py2

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
PYTHONPATH=%{buildroot}/usr/lib/python2.7/site-packages python2 setup.py test || :
%install
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot}

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*
