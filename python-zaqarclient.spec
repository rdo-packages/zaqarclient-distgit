%{!?upstream_version: %global upstream_version %{version}%{?milestone}}
Name:           python-zaqarclient
Version:        1.0.0
Release:        1%{?dist}
Summary:        Client Library for OpenStack Zaqar Queueing API

License:        ASL 2.0
URL:            http://wiki.openstack.org/zaqar
Source0:        https://pypi.python.org/packages/source/p/%{name}/%{name}-%{version}%{?milestone}.tar.gz
BuildArch:      noarch

BuildRequires:  python2-devel
BuildRequires:  python-pbr
BuildRequires:  python-setuptools
Requires:       python-jsonschema
Requires:       python-keystoneclient >= 1.6.0
Requires:       python-oslo-i18n >= 1.5.0
Requires:       python-pbr
Requires:       python-requests >= 2.5.2
Requires:       python-six >= 1.9.0
Requires:       python-stevedore >= 1.5.0

%description
Python client to Zaqar messaging service API v1

%prep
%setup -q -n %{name}-%{upstream_version}

# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%{__python2} setup.py build

%install
%{__python2} setup.py install --skip-build --root %{buildroot}

%files
%doc README.rst ChangeLog examples
%license LICENSE
%{python2_sitelib}/zaqarclient
%{python2_sitelib}/python_zaqarclient-*-py?.?.egg-info

%changelog
* Wed Mar 23 2016 RDO <rdo-list@redhat.com> 1.0.0-0.1
-  Rebuild for Mitaka 
