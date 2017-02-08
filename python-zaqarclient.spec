%{!?upstream_version: %global upstream_version %{version}%{?milestone}}

%global sname zaqarclient
%if 0%{?fedora}
%global with_python3 1
%endif

Name:           python-zaqarclient
Version:        XXX
Release:        XXX
Summary:        Client Library for OpenStack Zaqar Queueing API

License:        ASL 2.0
URL:            http://wiki.openstack.org/zaqar
Source0:        https://tarballs.openstack.org/%{name}/%{name}-%{upstream_version}.tar.gz
BuildArch:      noarch


%description
Python client to Zaqar messaging service API v1

%package -n python2-%{sname}
Summary:        Client Library for OpenStack Zaqar Queueing API
BuildRequires:  python2-devel
BuildRequires:  python-pbr
BuildRequires:  python-setuptools
Requires:       python-jsonschema
Requires:       python-keystoneauth1 >= 2.16.0
Requires:       python-keystoneclient >= 1:2.0.0
Requires:       python-osc-lib >= 1.2.0
Requires:       python-oslo-i18n >= 2.1.0
Requires:       python-oslo-log >= 3.11.0
Requires:       python-oslo-utils >= 3.18.0
Requires:       python-pbr
Requires:       python-requests >= 2.10.0
Requires:       python-six >= 1.9.0
Requires:       python-stevedore >= 1.17.1

%{?python_provide:%python_provide python2-%{sname}}

%description -n python2-%{sname}
Python client to Zaqar messaging service API v1


%if 0%{?with_python3}
%package -n python3-%{sname}
Summary:        Client Library for OpenStack Zaqar Queueing API
BuildRequires:  python3-devel
BuildRequires:  python3-pbr
BuildRequires:  python3-setuptools
Requires:       python3-jsonschema
Requires:       python3-keystoneauth1 >= 2.16.0
Requires:       python3-keystoneclient >= 1:2.0.0
Requires:       python3-osc-lib >= 1.2.0
Requires:       python3-oslo-i18n >= 2.1.0
Requires:       python3-oslo-log >= 3.11.0
Requires:       python3-oslo-utils >= 3.18.0
Requires:       python3-pbr
Requires:       python3-requests >= 2.10.0
Requires:       python3-six >= 1.9.0
Requires:       python3-stevedore >= 1.17.1

%{?python_provide:%python_provide python2-%{sname}}

%description -n python3-%{sname}
Python client to Zaqar messaging service API v1
%endif

%prep
%setup -q -n %{name}-%{upstream_version}

# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py2_build
%if 0%{?with_python3}
%py3_build
%endif


%install
%if 0%{?with_python3}
%py3_install
%endif

%py2_install


%files -n python2-%{sname}
%doc README.rst ChangeLog examples
%license LICENSE
%{python2_sitelib}/zaqarclient
%{python2_sitelib}/python_zaqarclient-*-py?.?.egg-info

%if 0%{?with_python3}
%files -n python3-%{sname}
%doc README.rst ChangeLog examples
%license LICENSE
%{python3_sitelib}/zaqarclient
%{python3_sitelib}/python_zaqarclient-*-py?.?.egg-info
%endif

%changelog
