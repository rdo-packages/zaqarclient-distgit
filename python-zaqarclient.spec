%{!?sources_gpg: %{!?dlrn:%global sources_gpg 1} }
%global sources_gpg_sign 0x4c29ff0e437f3351fd82bdf47c5a3bc787dc7035
%{!?upstream_version: %global upstream_version %{version}%{?milestone}}

%global sname zaqarclient

%global common_desc \
Python client to Zaqar messaging service API v1

Name:           python-zaqarclient
Version:        2.2.0
Release:        1%{?dist}
Summary:        Client Library for OpenStack Zaqar Queueing API

License:        ASL 2.0
URL:            http://wiki.openstack.org/zaqar
Source0:        https://tarballs.openstack.org/%{name}/%{name}-%{upstream_version}.tar.gz
# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
Source101:        https://tarballs.openstack.org/%{name}/%{name}-%{upstream_version}.tar.gz.asc
Source102:        https://releases.openstack.org/_static/%{sources_gpg_sign}.txt
%endif
BuildArch:      noarch

# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
BuildRequires:  /usr/bin/gpgv2
BuildRequires:  openstack-macros
%endif


%description
%{common_desc}

%package -n python3-%{sname}
Summary:        Client Library for OpenStack Zaqar Queueing API
%{?python_provide:%python_provide python3-%{sname}}
BuildRequires:  python3-devel
BuildRequires:  python3-pbr
BuildRequires:  python3-setuptools
Requires:       python3-keystoneauth1 >= 3.4.0
Requires:       python3-osc-lib >= 1.8.0
Requires:       python3-oslo-i18n >= 3.15.3
Requires:       python3-oslo-log >= 3.36.0
Requires:       python3-oslo-utils >= 3.33.0
Requires:       python3-pbr
Requires:       python3-requests >= 2.14.2
Requires:       python3-six >= 1.10.0
Requires:       python3-stevedore >= 1.20.0
Requires:       python3-jsonschema

%description -n python3-%{sname}
%{common_desc}

%prep
# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
%{gpgverify}  --keyring=%{SOURCE102} --signature=%{SOURCE101} --data=%{SOURCE0}
%endif
%setup -q -n %{name}-%{upstream_version}

# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%{py3_build}

%install
%{py3_install}


%files -n python3-%{sname}
%doc README.rst ChangeLog examples
%license LICENSE
%{python3_sitelib}/zaqarclient
%{python3_sitelib}/python_zaqarclient-*-py%{python3_version}.egg-info

%changelog
* Mon Sep 20 2021 RDO <dev@lists.rdoproject.org> 2.2.0-1
- Update to 2.2.0

# REMOVEME: error caused by commit https://opendev.org/openstack/python-zaqarclient/commit/e388947aae2c1440ffc8c635d9dc2f702dc2cb27
