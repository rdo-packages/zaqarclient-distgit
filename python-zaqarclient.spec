# Macros for py2/py3 compatibility
%if 0%{?fedora} || 0%{?rhel} > 7
%global pyver %{python3_pkgversion}
%else
%global pyver 2
%endif
%global pyver_bin python%{pyver}
%global pyver_sitelib %python%{pyver}_sitelib
%global pyver_install %py%{pyver}_install
%global pyver_build %py%{pyver}_build
# End of macros for py2/py3 compatibility
%{!?upstream_version: %global upstream_version %{version}%{?milestone}}

%global sname zaqarclient

%global common_desc \
Python client to Zaqar messaging service API v1

Name:           python-zaqarclient
Version:        1.11.0
Release:        1%{?dist}
Summary:        Client Library for OpenStack Zaqar Queueing API

License:        ASL 2.0
URL:            http://wiki.openstack.org/zaqar
Source0:        https://tarballs.openstack.org/%{name}/%{name}-%{upstream_version}.tar.gz
BuildArch:      noarch


%description
%{common_desc}

%package -n python%{pyver}-%{sname}
Summary:        Client Library for OpenStack Zaqar Queueing API
%{?python_provide:%python_provide python%{pyver}-%{sname}}
BuildRequires:  python%{pyver}-devel
BuildRequires:  python%{pyver}-pbr
BuildRequires:  python%{pyver}-setuptools
Requires:       python%{pyver}-keystoneauth1 >= 3.4.0
Requires:       python%{pyver}-osc-lib >= 1.10.0
Requires:       python%{pyver}-oslo-i18n >= 3.15.3
Requires:       python%{pyver}-oslo-log >= 3.36.0
Requires:       python%{pyver}-oslo-utils >= 3.33.0
Requires:       python%{pyver}-pbr
Requires:       python%{pyver}-requests >= 2.14.2
Requires:       python%{pyver}-six >= 1.10.0
Requires:       python%{pyver}-stevedore >= 1.20.0
Requires:       python%{pyver}-jsonschema

%description -n python%{pyver}-%{sname}
%{common_desc}

%prep
%setup -q -n %{name}-%{upstream_version}

# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%{pyver_build}

%install
%{pyver_install}


%files -n python%{pyver}-%{sname}
%doc README.rst ChangeLog examples
%license LICENSE
%{pyver_sitelib}/zaqarclient
%{pyver_sitelib}/python_zaqarclient-*-py?.?.egg-info

%changelog
* Tue Mar 12 2019 RDO <dev@lists.rdoproject.org> 1.11.0-1
- Update to 1.11.0

